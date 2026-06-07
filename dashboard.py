import pandas as pd
import plotly.express as px

data_path = "../backend/iot_data.csv"

df = pd.read_csv(data_path)

print("Toplam veri sayısı:", len(df))
print("Sensör sayısı:", df["device_id"].nunique())
print("Sensörler:", list(df["device_id"].unique()))

print("\nGenel Ortalama Değerler")
print("Ortalama sıcaklık:", round(df["temperature"].mean(), 2))
print("Ortalama nem:", round(df["humidity"].mean(), 2))
print("Ortalama hava kalitesi:", round(df["air_quality"].mean(), 2))
print("Ortalama trafik yoğunluğu:", round(df["traffic_density"].mean(), 2))

sensor_summary = df.groupby("device_id")[[
    "temperature",
    "humidity",
    "air_quality",
    "traffic_density"
]].mean().round(2)

print("\nSensör Bazlı Ortalama Değerler")
print(sensor_summary)

fig1 = px.line(
    df,
    x="timestamp",
    y="temperature",
    color="device_id",
    title="Sensörlere Göre Sıcaklık Değişimi"
)
fig1.show()

fig2 = px.line(
    df,
    x="timestamp",
    y="air_quality",
    color="device_id",
    title="Sensörlere Göre Hava Kalitesi Değişimi"
)
fig2.show()

fig3 = px.line(
    df,
    x="timestamp",
    y="traffic_density",
    color="device_id",
    title="Sensörlere Göre Trafik Yoğunluğu Değişimi"
)
fig3.show()

fig4 = px.bar(
    sensor_summary.reset_index(),
    x="device_id",
    y="air_quality",
    title="Sensör Bazlı Ortalama Hava Kalitesi"
)
fig4.show()