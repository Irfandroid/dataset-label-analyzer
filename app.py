import streamlit as st
import pandas as pd
import plotly.express as px
from rapidfuzz import fuzz

st.title("Dataset Label Analyzer")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    try:
        # Baca CSV
        df = pd.read_csv(uploaded_file)

        st.subheader("Preview Data")
        st.dataframe(df.head())

        # Cek apakah kolom label ada
        if "label" not in df.columns:
            st.error(
                "Kolom 'label' tidak ditemukan. "
                "Pastikan CSV memiliki kolom bernama 'label'."
            )
            st.write("Kolom yang tersedia:")
            st.write(df.columns.tolist())
            st.stop()

        # Hapus nilai kosong dan ubah ke string
        df["label"] = df["label"].astype(str)

        # =========================
        # DATASET SUMMARY
        # =========================
        st.subheader("Dataset Summary")

        total_rows = len(df)
        unique_labels = df["label"].nunique()

        st.write(f"Total Data: {total_rows}")
        st.write(f"Unique Labels: {unique_labels}")

        # =========================
        # LABEL DISTRIBUTION
        # =========================
        label_counts = df["label"].value_counts()

        st.subheader("Label Distribution")
        st.dataframe(label_counts)

        fig = px.bar(
            x=label_counts.index,
            y=label_counts.values,
            labels={
                "x": "Label",
                "y": "Count"
            },
            title="Label Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =========================
        # INCONSISTENT LABEL CHECK
        # =========================
        labels = (
            df["label"]
            .dropna()
            .astype(str)
            .unique()
        )

        st.subheader("Possible Inconsistent Labels")

        found = False

        for i in range(len(labels)):
            for j in range(i + 1, len(labels)):

                score = fuzz.ratio(
                    labels[i].lower(),
                    labels[j].lower()
                )

                if score > 80:
                    found = True

                    st.write(
                        f"🔍 {labels[i]} ↔ {labels[j]} "
                        f"({score:.0f}%)"
                    )

        if not found:
            st.success(
                "Tidak ditemukan label yang mirip."
            )

    except Exception as e:
        st.error(f"Terjadi error: {e}")