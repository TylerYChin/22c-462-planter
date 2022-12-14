import { useTheme } from "@mui/material";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { Subscription } from "rxjs";
import { Dispatch, RootState, store } from "../models/store";

export function LightSensor() {
  const theme = useTheme();

  const light = useSelector((state: RootState) => state.hub.dashboard.light);
  const dispatch = useDispatch<Dispatch>();
  return (
    <div>
      <h1>Luminosity</h1>
      <h2>{light.luminosity}</h2>
    </div>
  );
}
