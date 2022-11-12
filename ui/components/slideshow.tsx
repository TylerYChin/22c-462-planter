import React from "react";
import { Grid, Theme, useTheme } from "@mui/material";
import { Slide } from "react-slideshow-image";
import "react-slideshow-image/dist/styles.css";
import { Subscription } from "rxjs";
import { photoData, store } from "../models/store";

let photoDataSubscription: Subscription | null = null;

const Slideshow = () => {
  const theme = useTheme<Theme>();
  const [photoData, setphotoData] = React.useState(store.photoData.value);
  React.useEffect(() => {
    if (!photoDataSubscription) {
      photoDataSubscription = store.photoData.subscribe((data) => {
        setphotoData(data);
      });
    }
  });
  return (
    <div
      className="slide-container"
      style={{ width: `${photoData[0].width}px` }}
    >
      <Slide>
        {photoData.map((slideImage, index) => (
          <div className="each-slide" key={index}>
            <div
              style={{
                backgroundImage: `url(${slideImage.filepath})`,
                height: `${slideImage.height}px`,
                backgroundRepeat: "no-repeat",
                backgroundSize: "cover",
              }}
            >
              {/* <span>{slideImage.caption}</span> */}
            </div>
          </div>
        ))}
      </Slide>
    </div>
  );
};
export default Slideshow;