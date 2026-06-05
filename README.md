# The Credit Score Nobody Understands
### Canadian Credit Score Platform Transparency Analysis

I checked my credit score for the first time recently. It was different on every platform I checked. Equifax showed one number. Borrowell showed another. My bank showed a third. I spent an hour trying to figure out which one was real. I never fully did.

That made me want to understand the problem properly. Not just why it happened to me but what the system actually looks like when you map it out.

---

## What this is

A business analysis of how five major Canadian credit score platforms present information to consumers and where the experience breaks down. 500 synthetic consumers modelled with scores from all five platforms. A nine-step user journey mapped from deciding to check a score to giving up. Ten requirements written for what a genuinely clear credit information experience would look like. A business case for who benefits and what the three highest-impact changes are.

---

## Live app

[Launch the Credit Score Transparency Dashboard](https://canadian-credit-card-optimizer-20262.streamlit.app/)

---

## What the analysis found

The average variance between the highest and lowest score shown to the same consumer across platforms is 45.3 points. Nearly 35% of consumers see a 50-point gap or more. 58% of consumers check more than one platform. Of those nearly half walk away more confused than when they started.

The three reasons scores differ are not obvious or explained anywhere. Different bureaus collect different information. Different platforms use different scoring models even with the same bureau. And Credit Karma uses a different scale entirely — 300 to 850 — while every other Canadian platform uses 300 to 900.

The most painful moment in the consumer journey is not seeing a low score. It is seeing a different score on a second platform and finding no explanation anywhere in the system.

None of the five platforms currently meet four of the six Must Have requirements identified in this analysis.

---

## What the five tabs cover

The Problem tab shows the score variance distribution across 500 consumers, the box plot comparing score distributions by platform, and the age group breakdown showing younger consumers experience higher variance.

The Platform Breakdown tab compares all five platforms on consumer confusion rating, features available, and the key gap for each one.

The Consumer Journey tab maps all nine steps with a pain level chart and a step by step breakdown of what goes wrong and what the opportunity is at each stage.

What Better Looks Like shows the full requirements register with priority, acceptance criteria, and which platforms currently meet each requirement.

The Business Case tab covers who benefits, who is responsible for making changes, and the three specific changes with the highest impact.

---

## Files in this repo

| File | What it is |
|------|-----------|
| app.py | Streamlit analytics and requirements dashboard |
| platform-comparison.csv | Feature and transparency comparison across 5 platforms |
| consumer-score-data.csv | 500 synthetic consumers with scores from all 5 platforms |
| user-journey.csv | 9-step user journey with pain levels and opportunities |
| requirements-register.csv | 10 requirements with priority, acceptance criteria, and current status |
| key-findings.json | Headline findings |
| ba-report.pdf | Full business analysis report |
| generate-data.py | Python script that built all structured data |
| requirements.txt | Package dependencies |

---

## Skills this project demonstrates

Current state gap analysis. User journey mapping. Requirements elicitation with acceptance criteria. Platform benchmarking. Consumer pain point identification. Business case development. Python for data generation and analysis. Streamlit dashboard design and deployment. Fintech and consumer finance domain knowledge.

---

## About this project

Part of a portfolio series built while job searching in Canada after graduating from the University of Waterloo.

Prepared by Simran Saran. Targeting business analyst, product analyst, and fintech roles across Canada.

Platform comparison data based on publicly available information as of May 2026. Consumer score variance modelled on documented methodology differences between Equifax and TransUnion scoring systems.
