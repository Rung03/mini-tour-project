from flask import Flask, render_template
import folium

app = Flask(__name__)

places = [
    {
        "name": "จุดเริ่มต้น : กรุงเทพ",
        "lat": 13.762563149770429,
        "lon": 100.49782640288294,
        "type": "🚗 จุดเริ่มต้น",
        "description": "เริ่มต้นการเดินทางจากกรุงเทพมหานคร เมืองหลวงที่เต็มไปด้วยเสน่ห์ ก่อนออกเดินทางสู่ One Day Trip",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAGIO40YVpj2OgN0ZRIiwtM32QwLusfWV0zZIDFBTXucA4xBj5vS3a-he4hQGBgxqNqGhsnpeelVoFIbnqi_KIoZSRVWiwHCI0Z_yqqboLJE8Cl-d9dwBsEwchwB73z7S4I-2eTg=w408-h272-k-no",
    },
    {
        "name": "วิลเลจจิโอ รังสิต คลอง 3",
        "lat": 13.966418124364987,
        "lon": 100.66727666606947,
        "type": "🏡 ที่พัก",
        "description": "บ้านพักบรรยากาศอบอุ่น ใช้เป็นจุดรวมตัวก่อนออกเดินทาง",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlHLz4-GZ_MnqVa8uBBbaNsLlZkrnMZQJ0vhSR9VkUng03c1fEu4C6NqdeoqDO92scvamQVnZU4iM5U9Ro8cg2A2IFJbsRh541Vhf_lfSG8AfBf0fEBerV7cmpK9cqFPqPAqRyS=w426-h240-k-no",
    },
    {
        "name": "หมู่บ้านวรางกูล รังสิตคลอง 3",
        "lat": 13.978770158375152,
        "lon": 100.6688220310735,
        "type": "🏠 บ้านเพื่อน",
        "description": "แวะเยี่ยมเพื่อน พูดคุยและพักผ่อนในบรรยากาศเป็นกันเอง",
        "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
    },
    {
        "name": "ดรีมเวิลด์",
        "lat": 13.988801737195503,
        "lon": 100.67685719513622,
        "type": "💦 เล่นน้ำ",
        "description": "สวนสนุกชื่อดังของประเทศไทย สนุกกับเครื่องเล่นและสวนน้ำ",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAEwhfDuFimXab_kA9Nxr_CbOt1AQDtL1IYQ665iGCYNdDLYXDTEZiRI0xEG2OveureoU03JmnJiAmgUnlxCPXhkCDgPRKgnHBsjP52zZK_4CPvm1V3Z4M8FqDAvKs67ksQBu_0Y=w408-h306-k-no",
    },
    {
        "name": "มิสเตอร์บีนชาบู ลำลูกกา",
        "lat": 13.961670357339512,
        "lon": 100.68143872974426,
        "type": "🍲 ตลาดเย็น",
        "description": "ปิดท้ายวันด้วยชาบูบุฟเฟต์และอาหารเย็นแสนอร่อย",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAEH5nmLW1P_87HcQnhEswGW4MOjfwn-iRJpEmYS8N_BAAXoq1BvGb_qjFutfG_Jt43XZ6BbscZAH3TNq1KGqVuo-CPecCGRBIflB7SYmchRxHCiNmy_frAukywNwEvYefcAMh24yG-cybQ=w408-h612-k-no",
    }
]


@app.route("/")
def index():

    m = folium.Map(
        location=[14.5,100.2],
        zoom_start=7,
        tiles="CartoDB positron"
    )

    points=[]

    for p in places:

        folium.Marker(
            [p["lat"],p["lon"]],
            popup=f"<b>{p['name']}</b>",
            tooltip=p["name"],
            icon=folium.Icon(color="darkred",icon="star")
        ).add_to(m)

        points.append([p["lat"],p["lon"]])

    folium.PolyLine(
        points,
        color="#8B4513",
        weight=5
    ).add_to(m)

    map_html=m._repr_html_()

    return render_template(
        "index.html",
        places=places,
        map_html=map_html
    )


if __name__=="__main__":
    app.run(debug=True)