import React from "react";
import DonutProgress from "./DonutProgress";

const ResultCard = ({ result }) => {
  if (!result) return null;

  // Handle error state
  if (result.error) {
    return (
      <div className="space-y-4">
        <h3 className="text-xl font-bold text-red-600">Analysis Error</h3>
        <p className="text-base text-slate-600">{result.error}</p>
      </div>
    );
  }

  // Determine risk level color based on CRITICAL, HIGH, MEDIUM, LOW, MINIMAL
  const getRiskLevelColor = (riskLevel) => {
    const level = riskLevel?.toUpperCase() || "";
    if (level === "CRITICAL") return "text-red-700";
    if (level === "HIGH") return "text-orange-700";
    if (level === "MEDIUM") return "text-yellow-700";
    if (level === "LOW") return "text-lime-700";
    if (level === "MINIMAL") return "text-green-700";
    return "text-slate-600";
  };

  const getRiskLevelBgColor = (riskLevel) => {
    const level = riskLevel?.toUpperCase() || "";
    if (level === "CRITICAL") return "bg-red-200 border-red-500 shadow-lg shadow-red-200";
    if (level === "HIGH") return "bg-orange-200 border-orange-500 shadow-lg shadow-orange-200";
    if (level === "MEDIUM") return "bg-yellow-200 border-yellow-500 shadow-lg shadow-yellow-200";
    if (level === "LOW") return "bg-lime-200 border-lime-500 shadow-lg shadow-lime-200";
    if (level === "MINIMAL") return "bg-green-200 border-green-500 shadow-lg shadow-green-200";
    return "bg-slate-100 border-slate-300";
  };

  return (
    <div className="space-y-8">
      {/* Header with Risk Level */}
      <div className="space-y-4">
        <p className="text-xs font-bold uppercase tracking-[0.25em] text-indigo-600 sm:text-sm">
          Step 2
        </p>
        <h3 className="text-2xl font-bold tracking-tight text-slate-900 sm:text-[26px]">
          Analysis Results
        </h3>
      </div>

      {/* Overall Score and Risk Level */}
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {/* Overall Score */}
        <div className="rounded-2xl border border-slate-200 bg-slate-50 p-6">
          <p className="mb-4 text-sm font-semibold text-slate-600">Overall Score</p>
          <div className="flex items-center justify-center">
            <DonutProgress score={result.overall_score ?? 0} />
          </div>
          <p className="mt-4 text-center text-xs text-slate-500">
            {result.overall_score ?? 0} / 100
          </p>
        </div>

        {/* Risk Level */}
        <div className={`rounded-2xl border-2 p-6 ${getRiskLevelBgColor(result.risk_level)}`}>
          <p className="mb-4 text-sm font-semibold text-slate-600">Risk Level</p>
          <p className={`text-center text-2xl font-bold ${getRiskLevelColor(result.risk_level)}`}>
            {result.risk_level ?? "Unknown"}
          </p>
          <p className="mt-4 text-center text-xs text-slate-500">
            {result.risk_level?.toUpperCase() === "CRITICAL"
              ? "Danger: Very likely to be phishing"
              : result.risk_level?.toUpperCase() === "HIGH"
              ? "Warning: Likely to be phishing"
              : result.risk_level?.toUpperCase() === "MEDIUM"
              ? "Caution: Some suspicious indicators"
              : result.risk_level?.toUpperCase() === "LOW"
              ? "Safe: Few suspicious indicators"
              : "Very Safe: Email appears legitimate"}
          </p>
        </div>

        {/* Originating IP */}
        <div className="rounded-2xl border border-slate-200 bg-slate-50 p-6">
          <p className="mb-4 text-sm font-semibold text-slate-600">Originating IP</p>
          <p className="text-center font-mono text-sm text-slate-900">
            {result.originating_ip ?? "Unknown"}
          </p>
          <p className="mt-4 text-center text-xs text-slate-500">IP Address</p>
        </div>
      </div>

      {/* Authentication Checks */}
      <div className="space-y-3">
        <p className="text-sm font-semibold text-slate-700">Authentication Checks</p>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
          {["spf", "dmarc", "dkim"].map((auth) => {
            const authValue = String(result[auth] ?? "Unknown").toLowerCase();
            return (
              <div
                key={auth}
                className="flex items-center justify-between rounded-lg border border-slate-200 bg-slate-50 px-4 py-3"
              >
                <span className="font-semibold text-slate-700">{auth.toUpperCase()}</span>
                <span
                  className={`font-semibold ${
                    authValue === "pass"
                      ? "text-green-600"
                      : authValue === "fail"
                      ? "text-red-600"
                      : "text-slate-600"
                  }`}
                >
                  {result[auth] ?? "Unknown"}
                </span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Email Details */}
      <div className="space-y-3">
        <p className="text-sm font-semibold text-slate-700">Email Information</p>
        <div className="space-y-2 rounded-lg border border-slate-200 bg-slate-50 p-4">
          <div className="flex flex-col sm:flex-row sm:justify-between">
            <span className="font-semibold text-slate-600">From:</span>
            <span className="truncate text-slate-900">{result.from_address ?? "Unknown"}</span>
          </div>
          <div className="flex flex-col sm:flex-row sm:justify-between">
            <span className="font-semibold text-slate-600">To:</span>
            <span className="truncate text-slate-900">{result.to_address ?? "Unknown"}</span>
          </div>
        </div>
      </div>

      {/* Component Scores */}
      {result.component_scores && (
        <div className="space-y-3">
          <p className="text-sm font-semibold text-slate-700">Component Analysis Scores</p>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {result.component_scores &&
              Object.entries(result.component_scores).map(([component, score]) => (
                <div key={component} className="rounded-lg border border-slate-200 bg-slate-50 p-4">
                  <p className="mb-2 text-sm font-semibold text-slate-600 capitalize">
                    {component.replace(/_/g, " ")}
                  </p>
                  <div className="flex items-end justify-between">
                    <span className="text-xl font-bold text-slate-900">{score ?? 0}</span>
                    <span className="text-xs text-slate-500">/100</span>
                  </div>
                  <div className="mt-3 h-2 w-full rounded-full bg-slate-200">
                    <div
                      className={`h-full rounded-full ${
                        score >= 75
                          ? "bg-red-500"
                          : score >= 50
                          ? "bg-yellow-500"
                          : "bg-green-500"
                      }`}
                      style={{ width: `${score ?? 0}%` }}
                    ></div>
                  </div>
                </div>
              ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ResultCard;
