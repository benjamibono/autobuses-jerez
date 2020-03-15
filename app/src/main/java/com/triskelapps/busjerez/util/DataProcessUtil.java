package com.triskelapps.busjerez.util;

import android.content.Context;
import android.text.TextUtils;
import android.util.Log;

import com.google.gson.Gson;
import com.triskelapps.busjerez.App;
import com.triskelapps.busjerez.model.BusLine;
import com.triskelapps.busjerez.model.BusStop;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class DataProcessUtil {

    private static final String TAG = "DataProcessUtil";
    private final Context context;

    private DataProcessUtil(Context context) {
        this.context = context;
    }

    public static DataProcessUtil with(Context context) {
        return new DataProcessUtil(context);
    }


    public void processData() {


        List<BusLine> busLines = new ArrayList<>();

        for (int lineNumber = 1; lineNumber <= App.BUS_LINES_COUNT; lineNumber++) {

            try {
                String jsonStr = Util.getStringFromAssets(context, String.format("geojson/linea%d.geojson", lineNumber)); // A string containing GeoJSON

                JSONObject jsonObject = new JSONObject(jsonStr);
                JSONArray jsonArray = jsonObject.getJSONArray("features");

                BusLine busLine = new BusLine();
                List<BusStop> busStops = new ArrayList<>();

                for (int i = 0; i < jsonArray.length(); i++) {
                    JSONObject jsonFeature = jsonArray.getJSONObject(i);
                    JSONObject jsonGeometry = jsonFeature.getJSONObject("geometry");
                    String type = jsonGeometry.getString("type");
                    switch (type) {
                        case "Point":

                            BusStop busStop = new BusStop();

                            JSONObject jsonPropertiesBusStop = jsonFeature.getJSONObject("properties");
                            String nameLine1 = jsonPropertiesBusStop.getString("name");
                            busStop.setName(nameLine1);

                            try {
                                if (jsonPropertiesBusStop.has("COD")) {
                                    busStop.setCode((int) jsonPropertiesBusStop.getDouble("COD"));
                                } else if (jsonPropertiesBusStop.has("COD. PARADA")) {
                                    busStop.setCode((int) jsonPropertiesBusStop.getDouble("COD. PARADA"));
                                } else {
                                    busStop.setCode((int) jsonPropertiesBusStop.getDouble("COD.PARADA"));
                                }
                            } catch (Exception e) {
                                // Some lines have no field COD. PARADA
                            }

                            busStop.setLineId(lineNumber);

                            busStop.setTransfer(jsonPropertiesBusStop.getString("TRANSBORDO"));
                            busStop.setDirection(jsonPropertiesBusStop.getString("SENTIDO"));

                            JSONArray coords = jsonGeometry.getJSONArray("coordinates");

                            List<Double> coordinates = new ArrayList<>();
                            coordinates.add(coords.getDouble(1));
                            coordinates.add(coords.getDouble(0));

                            busStop.setCoordinates(coordinates);
                            busStops.add(busStop);

                            busLine.setBusStops(busStops);
                            break;

                        case "LineString":

                            String nameLine = jsonFeature.getJSONObject("properties").getString("name");
                            busLine.setName(nameLine);
//                            busLine.setId(Integer.parseInt(nameLine.replace("Línea", "").trim()));
                            busLine.setId(lineNumber);

                            if (jsonFeature.getJSONObject("properties").has("description")) {
                                String descriptionLine = jsonFeature.getJSONObject("properties").getString("description");
                                busLine.setDescription(descriptionLine);
                            }


                            JSONArray coordinatesList = jsonGeometry.getJSONArray("coordinates");

                            for (int j = 0; j < coordinatesList.length(); j++) {
                                JSONArray latLngCoords = coordinatesList.getJSONArray(j);
                                busLine.addCoordsToPath(latLngCoords.getDouble(1), latLngCoords.getDouble(0));
                            }

                            break;
                    }
                }

                if (TextUtils.isEmpty(busLine.getDescription())) {
                    throw new RuntimeException("No description field for " + busLine.getName());
                }

                busLines.add(busLine);
            } catch (JSONException e) {
                Log.e(TAG, "processData: error in bus line: " + lineNumber);
                throw new RuntimeException(e);
            }
        }


        String busLinesData = new Gson().toJson(busLines);
        Log.i(TAG, "processData: BusLines data: " + busLinesData);
    }
}
