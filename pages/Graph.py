import streamlit as st
import numpy as np
import plotly.graph_objects as go
import sympy as sp

# Function to generate cartesian graph
def plot_cartesian(equation, x_range):
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = [eval(equation, {"x": x, "np": np}) for x in x_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=equation))
    fig.update_layout(title="Cartesian Graph", xaxis_title="X", yaxis_title="Y", grid=dict(visible=True))
    return fig

# Function to generate polar graph
def plot_polar(equation, theta_range):
    theta_vals = np.linspace(theta_range[0], theta_range[1], 400)
    r_vals = [eval(equation, {"theta": t, "np": np}) for t in theta_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=r_vals, theta=np.degrees(theta_vals), mode='lines', name=equation))
    fig.update_layout(title="Polar Graph")
    return fig

# Function to generate parametric graph
def plot_parametric(x_eq, y_eq, t_range):
    t_vals = np.linspace(t_range[0], t_range[1], 400)
    x_vals = [eval(x_eq, {"t": t, "np": np}) for t in t_vals]
    y_vals = [eval(y_eq, {"t": t, "np": np}) for t in t_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name="Parametric Curve"))
    fig.update_layout(title="Parametric Graph", xaxis_title="X", yaxis_title="Y")
    return fig

# Function to generate 3D graph
def plot_3d(equation, x_range, y_range):
    x_vals = np.linspace(x_range[0], x_range[1], 40)
    y_vals = np.linspace(y_range[0], y_range[1], 40)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.array([[eval(equation, {"x": x, "y": y, "np": np}) for x in x_vals] for y in y_vals])

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    fig.update_layout(title="3D Surface Plot", scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"))
    return fig

# Streamlit UI
st.title("Advanced Real-Time Graphing App 📈")

graph_type = st.selectbox("Select Graph Type:", ["Cartesian", "Polar", "Parametric", "3D Surface"])

if graph_type == "Cartesian":
    equation = st.text_input("Enter a function of x:", "np.sin(x)")
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_cartesian(equation, x_range))

elif graph_type == "Polar":
    equation = st.text_input("Enter a function of θ (theta):", "1 + np.sin(theta)")
    theta_range = st.slider("Select θ range (in radians):", 0, 6, (0, 6))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_polar(equation, theta_range))

elif graph_type == "Parametric":
    x_eq = st.text_input("Enter X equation in terms of t:", "np.sin(t)")
    y_eq = st.text_input("Enter Y equation in terms of t:", "np.cos(t)")
    t_range = st.slider("Select t range:", 0, 10, (0, 6))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_parametric(x_eq, y_eq, t_range))

elif graph_type == "3D Surface":
    equation = st.text_input("Enter a function of x and y:", "np.sin(np.sqrt(x**2 + y**2))")
    x_range = st.slider("Select X-axis range:", -10, 10, (-5, 5))
    y_range = st.slider("Select Y-axis range:", -10, 10, (-5, 5))
    if st.button("Plot Graph"):
        st.plotly_chart(plot_3d(equation, x_range, y_range))
