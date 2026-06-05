import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path

st.set_page_config(
    page_title="Canadian Credit Score Transparency",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container{padding:1.5rem 2rem}
    .kpi{background:white;border-radius:12px;padding:16px 20px;border:1px solid #E8E8E8;box-shadow:0 1px 4px rgba(0,0,0,0.05);margin-bottom:8px}
    .kpi-label{font-size:11px;color:#888;margin-bottom:4px;font-weight:500;text-transform:uppercase;letter-spacing:.04em}
    .kpi-value{font-size:26px;font-weight:700;color:#111;line-height:1.1}
    .kpi-note{font-size:11px;color:#888;margin-top:3px}
    .kpi-red .kpi-value{color:#C0392B}
    .kpi-green .kpi-value{color:#0A7540}
    .kpi-amber .kpi-value{color:#B7791F}
    .kpi-blue .kpi-value{color:#0C447C}
    .finding{background:#F0FBF6;border-left:3px solid #27AE60;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#1A5C35;margin:10px 0;line-height:1.6}
    .alert{background:#FDF2F2;border-left:3px solid #C0392B;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7B1818;margin:10px 0;line-height:1.6}
    .warning{background:#FEF9EC;border-left:3px solid #F39C12;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7D5A00;margin:10px 0;line-height:1.6}
    .insight{background:#EEF3FB;border-left:3px solid #1A56DB;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#0C2A6E;margin:10px 0;line-height:1.6}
    .section-title{font-size:15px;font-weight:600;color:#111;margin:18px 0 10px 0;padding-bottom:6px;border-bottom:1.5px solid #EBEBEB}
    .journey-step{background:white;border-radius:10px;padding:14px 18px;border:1px solid #E8E8E8;margin:8px 0}
    .journey-step-high{border-left:4px solid #C0392B}
    .journey-step-med{border-left:4px solid #F59E0B}
    .journey-step-low{border-left:4px solid #27AE60}
    footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    base = Path(__file__).parent
    platforms = pd.read_csv(base / "platform-comparison.csv")
    consumers = pd.read_csv(base / "consumer-score-data.csv")
    journey   = pd.read_csv(base / "user-journey.csv")
    reqs      = pd.read_csv(base / "requirements-register.csv")
    with open(base / "key-findings.json") as f:
        findings = json.load(f)
    return platforms, consumers, journey, reqs, findings

platforms, consumers, journey, reqs, findings = load()

PAIN_COLORS = {1: "#27AE60", 2: "#52BE80", 3: "#F59E0B", 4: "#E67E22", 5: "#C0392B"}

st.markdown("## Canadian Credit Score Transparency Analysis")
st.markdown("**5 platforms assessed** &nbsp;|&nbsp; **500 synthetic consumers modelled** &nbsp;|&nbsp; **9-step user journey mapped** &nbsp;|&nbsp; **10 requirements written**")
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "  The Problem  ",
    "  Platform Breakdown  ",
    "  The Consumer Journey  ",
    "  What Better Looks Like  ",
    "  The Business Case  ",
])

# ── TAB 1: THE PROBLEM ────────────────────────────────────────────────────────
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Avg score variance across platforms</div>
            <div class="kpi-value">{findings['avg_score_variance_points']} pts</div>
            <div class="kpi-note">Same person, different platforms</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Consumers with 50+ point gap</div>
            <div class="kpi-value">{findings['consumers_with_50_plus_variance_pct']}%</div>
            <div class="kpi-note">Across their platform scores</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="kpi kpi-amber">
            <div class="kpi-label">Check more than one platform</div>
            <div class="kpi-value">{findings['consumers_checking_multiple_platforms_pct']}%</div>
            <div class="kpi-note">Of consumers surveyed</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Left confused by differences</div>
            <div class="kpi-value">{findings['consumers_confused_by_differences_pct']}%</div>
            <div class="kpi-note">Who checked multiple platforms</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="alert"><strong>The core problem:</strong> None of the five major Canadian credit platforms use the same bureau, the same scoring model, or the same scale. A consumer checking their score on Credit Karma and then on Equifax.ca will see two different numbers with no explanation of why. Nearly half of consumers who check multiple platforms walk away more confused than when they started.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Score variance distribution — how far apart are scores for the same person</div>', unsafe_allow_html=True)
        fig_var = px.histogram(
            consumers, x="Score Variance", nbins=40,
            color_discrete_sequence=["#4285F4"],
        )
        fig_var.add_vline(x=findings['avg_score_variance_points'], line_dash="dash",
            line_color="#C0392B", annotation_text=f"Average: {findings['avg_score_variance_points']} pts")
        fig_var.update_layout(height=300, plot_bgcolor="white",
            xaxis=dict(title="Score variance (highest minus lowest across platforms)", gridcolor="#F1F1F1"),
            yaxis=dict(title="Number of consumers", gridcolor="#F1F1F1"),
            margin=dict(t=10, b=20))
        st.plotly_chart(fig_var, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Score distribution by platform — same consumers, five different answers</div>', unsafe_allow_html=True)
        score_cols = ["Equifax Score", "TransUnion Score", "Borrowell Score", "Credit Karma Score", "Mogo Score"]
        fig_box = go.Figure()
        colors = ["#E1306C", "#4285F4", "#27AE60", "#F59E0B", "#8B5CF6"]
        for col, color in zip(score_cols, colors):
            fig_box.add_trace(go.Box(
                y=consumers[col], name=col.replace(" Score", ""),
                marker_color=color, boxmean=True,
            ))
        fig_box.update_layout(height=300, plot_bgcolor="white",
            yaxis=dict(title="Credit Score", gridcolor="#F1F1F1"),
            xaxis=dict(title=""),
            showlegend=False,
            margin=dict(t=10, b=20))
        st.plotly_chart(fig_box, use_container_width=True)

    st.markdown('<div class="section-title">Consumer score variance by age group</div>', unsafe_allow_html=True)
    age_var = consumers.groupby("Age Group")["Score Variance"].mean().reset_index()
    age_order = ["18 to 24", "25 to 34", "35 to 44", "45 to 54", "55 plus"]
    age_var["Age Group"] = pd.Categorical(age_var["Age Group"], categories=age_order, ordered=True)
    age_var = age_var.sort_values("Age Group")
    fig_age = px.bar(age_var, x="Age Group", y="Score Variance",
        color="Score Variance", color_continuous_scale=["#27AE60","#F59E0B","#C0392B"],
        text="Score Variance")
    fig_age.update_traces(texttemplate="%{text:.1f} pts", textposition="outside")
    fig_age.update_layout(height=280, plot_bgcolor="white",
        yaxis=dict(title="Avg Score Variance (pts)", gridcolor="#F1F1F1"),
        xaxis=dict(title=""),
        coloraxis_showscale=False,
        margin=dict(t=10, b=20))
    st.plotly_chart(fig_age, use_container_width=True)
    st.markdown('<div class="insight">Younger consumers aged 18 to 34 show higher score variance on average. This group is also most likely to be checking their score for the first time, making the confusion most harmful when financial decisions like first credit cards, student loans, and first apartments are being made.</div>', unsafe_allow_html=True)

# ── TAB 2: PLATFORM BREAKDOWN ─────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">How each platform compares on what actually matters to consumers</div>', unsafe_allow_html=True)
    st.markdown('<div class="warning">Every platform uses a different bureau, a different scoring model, and a different scale. Credit Karma uses a 300 to 850 range while every other Canadian platform uses 300 to 900. That single difference means a score of 820 on Credit Karma and 820 on Equifax are not the same thing at all — but nothing on either platform tells you that.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Consumer confusion rating by platform (5 is most confusing)</div>', unsafe_allow_html=True)
        conf_data = platforms[["Platform", "Consumer Confusion Rating (1 to 5, 5 is most confusing)"]].copy()
        conf_data.columns = ["Platform", "Confusion Rating"]
        fig_conf = go.Figure(go.Bar(
            x=conf_data["Platform"],
            y=conf_data["Confusion Rating"],
            marker_color=["#C0392B","#C0392B","#F59E0B","#27AE60","#F59E0B"],
            text=conf_data["Confusion Rating"],
            textposition="outside",
        ))
        fig_conf.update_layout(height=300, plot_bgcolor="white",
            yaxis=dict(title="Confusion Rating", gridcolor="#F1F1F1", range=[0,6]),
            xaxis=dict(title="", tickangle=15, tickfont=dict(size=10)),
            margin=dict(t=10, b=60))
        st.plotly_chart(fig_conf, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Features available by platform</div>', unsafe_allow_html=True)
        feature_cols = ["Platform", "Cost to Access", "Factors Explained in Plain Language",
                       "Shows Score History", "Dispute Process Available", "Plain Language Summary"]
        feature_disp = platforms[feature_cols].copy()
        st.dataframe(feature_disp, use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">The key gap for each platform</div>', unsafe_allow_html=True)
    for _, row in platforms.iterrows():
        conf = row["Consumer Confusion Rating (1 to 5, 5 is most confusing)"]
        box_class = "alert" if conf >= 4 else "warning" if conf == 3 else "finding"
        st.markdown(f"""<div class="{box_class}">
            <strong>{row['Platform']}</strong> — Uses {row['Bureau Used']}, {row['Score Model']}, range {row['Score Range']}<br>
            {row['Key Gap']}
        </div>""", unsafe_allow_html=True)

# ── TAB 3: USER JOURNEY ───────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">The journey a consumer takes from deciding to check their score to giving up</div>', unsafe_allow_html=True)
    st.markdown('<div class="alert">The consumer journey has nine steps. Five of them have a pain level of 4 or 5 out of 5. The highest pain moment is not when they see a low score — it is when they see a different score on a second platform and have nowhere to turn for an explanation.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        fig_journey = px.line(
            journey, x="Step", y="Pain Level (1 to 5)",
            markers=True, color_discrete_sequence=["#C0392B"],
        )
        fig_journey.add_hline(y=4, line_dash="dot", line_color="#F59E0B",
            annotation_text="High pain threshold")
        for _, row in journey.iterrows():
            color = PAIN_COLORS.get(row["Pain Level (1 to 5)"], "#888")
            fig_journey.add_scatter(
                x=[row["Step"]], y=[row["Pain Level (1 to 5)"]],
                mode="markers", marker=dict(size=14, color=color),
                showlegend=False,
            )
        fig_journey.update_layout(height=320, plot_bgcolor="white",
            yaxis=dict(title="Pain Level (1 to 5)", gridcolor="#F1F1F1", range=[0, 6]),
            xaxis=dict(title="Step in journey", tickmode="linear", dtick=1),
            margin=dict(t=10, b=20))
        st.plotly_chart(fig_journey, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Pain level key</div>', unsafe_allow_html=True)
        for level, color_name in [(1,"Low"), (2,"Low-Medium"), (3,"Medium"), (4,"High"), (5,"Critical")]:
            color = PAIN_COLORS[level]
            st.markdown(f"<div style='background:{color};color:white;padding:6px 10px;border-radius:6px;margin:4px 0;font-size:12px;font-weight:600'>{level} — {color_name}</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Step by step breakdown</div>', unsafe_allow_html=True)
    for _, step in journey.iterrows():
        pain = step["Pain Level (1 to 5)"]
        box_class = "journey-step journey-step-high" if pain >= 4 else "journey-step journey-step-med" if pain == 3 else "journey-step journey-step-low"
        st.markdown(f"""<div class="{box_class}">
            <strong>Step {int(step['Step'])} — {step['Stage']}: {step['Action']}</strong><br>
            <span style="font-size:12px;color:#888">How the consumer feels: {step['Emotion']} &nbsp;|&nbsp; Pain level: {pain}/5</span><br><br>
            <span style="font-size:13px;color:#C0392B"><strong>What goes wrong:</strong> {step['What Goes Wrong']}</span><br>
            <span style="font-size:13px;color:#0A7540"><strong>The opportunity:</strong> {step['Opportunity']}</span>
        </div>""", unsafe_allow_html=True)

# ── TAB 4: REQUIREMENTS ───────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">What a better credit information experience needs to do</div>', unsafe_allow_html=True)
    st.markdown('<div class="finding">10 requirements across disclosure, plain language, dispute access, and consumer education. 4 of the 6 Must Have requirements are currently met by none of the five platforms assessed. The simplest and highest impact change is also the one nobody has done: telling consumers which bureau the platform uses before they create an account.</div>', unsafe_allow_html=True)

    priority_filter = st.multiselect(
        "Filter by priority",
        ["Must Have", "Should Have", "Could Have"],
        default=["Must Have", "Should Have", "Could Have"],
        key="req_filter"
    )

    filtered_reqs = reqs[reqs["Priority"].isin(priority_filter)]

    col1, col2, col3 = st.columns(3)
    with col1:
        mh = len(reqs[reqs["Priority"]=="Must Have"])
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Must Have requirements</div>
            <div class="kpi-value">{mh}</div>
            <div class="kpi-note">Foundation of any meaningful improvement</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        none_met = len(reqs[reqs["Currently Met By"]=="None of the 5 platforms"])
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Met by no platform</div>
            <div class="kpi-value">{none_met} of {len(reqs)}</div>
            <div class="kpi-note">Requirements currently unmet across all 5 platforms</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="kpi kpi-green">
            <div class="kpi-label">Most transparent platform</div>
            <div class="kpi-value" style="font-size:16px">Credit Karma</div>
            <div class="kpi-note">Meets the most requirements of any platform assessed</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    for _, req in filtered_reqs.iterrows():
        box_class = "alert" if req["Priority"] == "Must Have" else "warning" if req["Priority"] == "Should Have" else "insight"
        st.markdown(f"""<div class="{box_class}">
            <strong>{req['Req ID']} ({req['Priority']}) — {req['Requirement']}</strong><br>
            <strong>Why this matters:</strong> {req['Why This Matters']}<br>
            <strong>Currently met by:</strong> {req['Currently Met By']}
        </div>""", unsafe_allow_html=True)

# ── TAB 5: BUSINESS CASE ──────────────────────────────────────────────────────
with tab5:
    st.markdown('<div class="section-title">Who benefits and what it would take to fix this</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Why banks and fintechs should care</div>', unsafe_allow_html=True)
        st.markdown("""<div class="finding">
            A consumer who understands their credit score is more likely to take action to improve it.
            A consumer who improves their score is more likely to qualify for better financial products.
            A bank that helps a consumer understand their score earns trust that translates directly into
            product uptake — credit cards, mortgages, lines of credit. The investment in better credit
            education pays back in higher-quality customer relationships.
        </div>""", unsafe_allow_html=True)
        st.markdown("""<div class="insight">
            Neobanks like Koho and Neo Financial are already competing on financial wellness features.
            A traditional Canadian bank that builds a genuinely clear and useful credit score dashboard
            has a differentiation opportunity that most of its competitors have ignored.
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-title">Who is responsible for making this better</div>', unsafe_allow_html=True)
        stakeholders = [
            {"Stakeholder": "Credit Bureaus (Equifax, TransUnion)", "Role": "Must disclose scoring model clearly and standardise consumer-facing language"},
            {"Stakeholder": "Free Score Platforms (Borrowell, Credit Karma, Mogo)", "Role": "Must explain bureau and model used before account creation. Must link to dispute process."},
            {"Stakeholder": "Canadian Banks", "Role": "Opportunity to build best-in-class credit education tool and earn consumer trust"},
            {"Stakeholder": "Financial Consumer Agency of Canada", "Role": "Can mandate disclosure standards for any platform showing consumers a credit score"},
            {"Stakeholder": "Canadian Consumers", "Role": "Benefit from standardised, plain language credit information to make better financial decisions"},
        ]
        st.dataframe(pd.DataFrame(stakeholders), use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">The three changes with the most impact</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="kpi kpi-blue">
            <div class="kpi-label">Change 1</div>
            <div class="kpi-value" style="font-size:16px">Disclose the bureau</div>
            <div class="kpi-note">Show which bureau and model is used before account creation. Zero cost to implement. Eliminates the biggest source of confusion immediately.</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="kpi kpi-blue">
            <div class="kpi-label">Change 2</div>
            <div class="kpi-value" style="font-size:16px">Plain language factors</div>
            <div class="kpi-note">Explain every factor in one plain language sentence with one specific action. Converts a confusing number into something a consumer can actually do something about.</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="kpi kpi-blue">
            <div class="kpi-label">Change 3</div>
            <div class="kpi-value" style="font-size:16px">Explain the variance</div>
            <div class="kpi-note">Show consumers why their score differs across platforms before they discover it themselves. Proactive explanation builds trust. Leaving them to figure it out destroys it.</div>
        </div>""", unsafe_allow_html=True)

st.divider()
st.markdown(
    "**Data note:** Consumer score data is synthetic and generated for portfolio purposes. "
    "Platform information is based on publicly available data as of May 2026. "
    "Score variance modelled on documented differences between Equifax and TransUnion scoring methodologies. "
    "Prepared by Simran Saran as part of The Case Files portfolio series."
)
