# """ flask_example.py

#     Required packages:
#     - flask
#     - folium

#     Usage:

#     Start the flask server by running:

#         $ python flask_example.py

#     And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

# """

# import folium
# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def index():
#     locations = [
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (51.340632, 12.374733),
#         (34.053691, -118.242766),
#         (34.053691, -118.242766),
#         (34.053691, -118.242766),
#         (37.779026, -122.419906),
#         (37.779026, -122.419906),
#         (38.581021, -121.4939328),
#         (38.581021, -121.4939328),
#         (38.581021, -121.4939328),
#         (39.101454, -84.51246),
#     ]

#     # draw a line between the locations
#     line = folium.PolyLine(locations=locations, weight=5)

#     # bounding box
#     bb = line.get_bounds()

#     # create the map and make the full bounding box visible
#     m = folium.Map()
#     m.fit_bounds(bb)

#     # add the line to the map
#     m.add_child(line)

#     # add points to the map
#     for location in locations:
#         folium.Marker(location).add_to(m)

#     return m._repr_html_()


# if __name__ == "__main__":
#     app.run(debug=True)
