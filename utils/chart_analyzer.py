import cv2
import numpy as np

def analyze_chart(image):
    edges = cv2.Canny(image, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    chart_type = "Unknown"
    if lines is not None:
        chart_type = "Line Chart / Bar Chart detected"

    insights = {
        "chart_type": chart_type,
        "trend": "Upward trend detected" if lines is not None else "No clear trend"
    }
    return insights
