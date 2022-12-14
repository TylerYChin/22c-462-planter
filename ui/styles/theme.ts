import { createTheme, CustomThemeOptions } from "@mui/material/styles";

// Create a theme instance.
const theme = createTheme({
  palette: {
    primary: {
      main: "#357960",
    },
    secondary: {
      main: "#3993DD",
    },
    tertiary: {
      main: "#6A3E37",
    },
    light: {
      main: "#F4F3EE",
    },
    dark: {
      main: "#051923",
    },
    background: {
      default: "#051923",
      paper: "#0b364c",
    },

    mode: "dark",
    borderColor: "#131313",
  },
  background: {
    default: "#020202",
    paper: "#24292F",
  },
} as CustomThemeOptions);

export default theme;
