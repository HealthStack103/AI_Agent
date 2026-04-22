// this file is set for prometeus metrics collection. 

import express from "express";
import client from "prom-client";

export function startMetricsServer() {
  const app = express();
  const register = new client.Registry();

  client.collectDefaultMetrics({ register });

  app.get("/metrics", async (req, res) => {
    res.set("Content-Type", register.contentType);
    res.end(await register.metrics());
  });

  app.listen(8080, "0.0.0.0", () => {
    console.log("📊 Metrics server running on port 8080");
  });
}