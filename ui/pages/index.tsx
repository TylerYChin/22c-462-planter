import { once } from "lodash";
import Head from "next/head";
import MoistureSensors from "../components/moistureSensors";
import Slideshow from "../components/slideshow";
import { WaterConsumption } from "../components/waterConsumption";
import { api } from "../models/api";
import { randomSensorData, store } from "../models/store";
import styles from "../styles/Home.module.css";

let getLatestPhotos = once(() => {
  api.photos.getLatestPhotos().then((photos) => {
    store.photoData.next(photos);
  });
});

export default function Home() {
  getLatestPhotos();
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <MoistureSensors />
      <WaterConsumption />
      <Slideshow />
    </div>
  );
}