import plotly.graph_objects as go


# Start
x_start = 1
x_funnel_start = 4
x_funnel_stop  = 7
x_end = 10

y_start_range = 260
y_start_top = y_start_range + 10
y_start_range = 260

y_funnel_range = 150
y_funnel_top   = (y_start_top - (y_start_range/2.0)) + (y_funnel_range/2.0)


y_end_range = 150
y_end_top = (y_start_top - (y_start_range/2.0)) + (y_end_range/2.0)




channels = [
    {"label": "Device", "size": 100, 'color': 'red', "priority": 0},
    {"label": "Stream", "size": 100, 'color': 'blue', "priority": 0},
    {"label": "App A", "size": 25, 'color': 'green', "priority": 0},
    {"label": "App B", "size": 5, 'color': 'brown', "priority": 0},
    {"label": "App C", "size": 30, 'color': 'purple', "priority": 0},
]

fig = go.Figure()

# Create scatter trace of text labels
# fig.add_trace(go.Scatter(
#     x=[2, 1, 8, 8],
#     y=[0.25, 9, 2, 6],
#     text=["Filled Triangle",
#           "Filled Polygon",
#           "Quadratic Bezier Curves",
#           "Cubic Bezier Curves"],
#     mode="text",
# ))

#Update axes properties
fig.update_xaxes(
    range=[0, x_end + 1],
    zeroline=False,
    showgrid=False,
    showticklabels=False,
)

fig.update_yaxes(
    range=[0, y_start_top + 10],
    zeroline=False,
    showgrid=False,
    showticklabels=False,
)




def bow_tie_shapes(fig, channels):
    # path=" M 0,10 L0,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z",
    total_size = sum([a['size'] for a in channels])
    print(total_size)
    y_start_scale = y_start_range/total_size
    y_end_scale = y_end_range/total_size
    y_funnel_scale = y_funnel_range/total_size

    chan_shape = []
    text_x = []
    text_y = []
    text_text = []
    text_pos = []

    y_start = y_start_top
    y_end = y_end_top
    y_funnel = y_funnel_top

    for chan in channels:
        path_str = "M "
        points = []
        x1 = x_start
        y1 = y_start
        path_str += f"{x1},{y1} "
        points.append((x1,y1))
        x2 = x_funnel_start
        y2 = y_funnel
        path_str += f"L{x2},{y2} "
        points.append((x2,y2))
        x3 = x_funnel_stop
        y3 = y_funnel
        path_str += f"L{x3},{y3} "
        points.append((x3,y3))
        x4 = x_end
        y4 = y_end
        path_str += f"L{x4},{y4} "
        points.append((x4,y4))
        x5 = x_end
        y5 = y_end - (y_end_scale * chan['size'])
        path_str += f"L{x5},{y5} "
        points.append((x5,y5))
        x6 = x_funnel_stop
        if chan['priority'] != 1:
            y6 = y_funnel - (y_funnel_scale * chan['size'])
        else:
            y6 = y_funnel - (y_start_scale * chan['size'])
        path_str += f"L{x6},{y6} "
        points.append((x6,y6))
        x7 = x_funnel_start
        if chan['priority'] != 1:
            y7 = y_funnel - (y_funnel_scale * chan['size'])
        else:
            y7 = y_funnel - (y_start_scale * chan['size'])
        path_str += f"L{x7},{y7} "
        points.append((x7,y7))
        x8 = x_start
        y8 = y_start - (y_start_scale * chan['size'])
        path_str += f"L{x8},{y8} Z"
        points.append((x8,y7))

        the_shape = dict(
            type="path",
            path=path_str,
            line_color=chan['color'],
            fillcolor=chan['color'],
            layer="below",
        )

        text_x.append(x1 - (x1/2.0))
        text_y.append(y1 - ((y1-y8)/2.0))
        text_text.append(chan['label'] + " " + str(chan['size']))
        text_pos.append("middle left")

        # textposition=["top center", "middle left", "top center", "bottom center",
        #           "top right",
        #           "middle left", "bottom right", "bottom left", "top right",
        #           "top right"]

        chan_shape.append(the_shape)

        y_start = y_start - (y_start_scale * chan['size'])
        if chan['priority'] != 1:
            y_funnel = y_funnel - (y_funnel_scale * chan['size'])
        else:
            y_funnel = y_funnel - (y_start_scale * chan['size'])
        y_end = y_end - (y_end_scale * chan['size'])

    fig.update_layout(
        shapes=chan_shape
    )

    fig.add_trace(go.Scatter(
    x=text_x,
    y=text_y,
    text=text_text,
    mode="text",
    textposition=text_pos,
))

    





bow_tie_shapes(fig, channels)




"""
# Add shapes
fig.update_layout(
    shapes=[
        # Quadratic Bezier Curves
        dict(
            type="path",
            path="M 4,4 Q 6,0 8,4",
            line_color="RoyalBlue",
        ),
        # Cubic Bezier Curves
        dict(
            type="path",
            path="M 1,4 C 2,8 6,4 8,8",
            line_color="MediumPurple",
        ),
        # filled Triangle
        dict(
            type="path",
            path=" M 1 1 L 1 3 L 4 1 Z",
            fillcolor="LightPink",
            line_color="Crimson",
        ),
        # filled Polygon
        dict(
            type="path",
            path=" M 3,7 L2,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z",
            fillcolor="PaleTurquoise",
            line_color="LightSeaGreen",
        ),
        # filled Polygon

        

        dict(
            type="path",
            path=" M 0,10 L0,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z",
            fillcolor="red",
            line_color="red",
        ),
    ]
)
"""

fig.show()
