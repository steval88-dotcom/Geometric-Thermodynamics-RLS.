# LLM Complexity Benchmark: Tutto sa l'AI? (Nature Methods Submission)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](requirements.txt)
[![Reproducible](https://img.shields.io/badge/reproducible-100%25-green.svg)](validate_results.py)
[![AI Transparent](https://img.shields.io/badge/AI_Disclosure-Full-blueviolet)](#ai-tools-disclosure)

Codice completo per **"Tutto sa l'AI? Valutazione delle performance di Large Language Models su problemi di complessità computazionale"**.

## 🧠 AI Tools Disclosure (Nature Methods 2026 Compliant)

**Sviluppato con tutti i principali LLM del 2025 - Full Transparency:**

| AI Model | Provider | Contribution | Human Validation Method |
|----------|----------|--------------|-------------------------|
| **Gemini 1.5 Pro** | Google | Dataset SAT generation (n=150 verified) | SAT solver + manual check |
| **Perplexity AI** | Perplexity | P vs NP literature synthesis (47 refs) | Scopus/PubMed cross-check |
| **Grok-2** | xAI | Code optimization (28% runtime ↓) | CPU/GPU timing benchmarks |
| **Llama 4 70B** | Meta | ROC curves & confusion matrices | Matplotlib re-rendered |

**Human Validation Protocol:**

# Geometric-Thermodynamics-RLS.
# Riemannian Langevin Solver (RLS) & The Valente Benchmark (VB-250)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14624795.svg)](https://doi.org/10.5281/zenodo.14624795)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

The **Riemannian Langevin Solver (RLS)** is a novel computational framework designed to predict protein folding kinetics with a **10,000x speedup** over traditional all-atom Molecular Dynamics (MD). 

By leveraging **Geometric Thermodynamics**, RLS maps the amino acid sequence onto a Riemannian manifold. Instead of brute-forcing physical simulations, the solver identifies the conformational flow along geodesics of a sequence-encoded metric tensor ($g_{ij}$).

### Key Features:
* **Unprecedented Speed:** Fold a WW domain in **52 seconds** on a standard CPU (vs ~14 hours in OpenMM).
* **High Accuracy:** Validated with an **$R^2 = 0.89$** on the Valente Benchmark (VB-250).
* **Predictive Power:** Identifies **Topological Risk Factors (TRF)** for neurodegenerative misfolding (e.g., Hopf Bifurcations in $\alpha$-synuclein).

---

## The Valente Benchmark (VB-250)

The **VB-250** is a curated dataset of 250 proteins with experimentally verified folding rates ($\ln k_f$). It serves as a gold standard for validating geometric and topological descriptors in protein kinetics.

**Dataset Status:**
* **Zenodo:** [https://doi.org/10.5281/zenodo.14624795](https://doi.org/10.5281/zenodo.14624795)
* **Local:** Check the `/data` folder in this repository for the `.csv` file.

---

## Scientific Background

Traditional models often ignore the non-Euclidean nature of the protein configuration space. RLS uses **Karplus-Schulz propensities** to derive local metric properties, allowing the detection of **Poincaré-Andronov-Hopf bifurcations**. This mathematical framework explains the transition from stable native states to amyloid attractors in proteopathic disorders.

---

## Clinical Impact

Led by **Stefano Valente, MD**, this project bridges the gap between Clinical Psychiatry and Computational Biophysics. We provide open-access tools for early diagnostic biomarkers in Alzheimer’s and Parkinson’s disease.

## Contact

**Stefano Valente, MD** [ResearchGate Profile](https://www.researchgate.net/profile/Stefano-Valente-2)
Commercial Use: For proprietary integration or private R&D use, a commercial license is required. Contact: steval88@icloud.com

