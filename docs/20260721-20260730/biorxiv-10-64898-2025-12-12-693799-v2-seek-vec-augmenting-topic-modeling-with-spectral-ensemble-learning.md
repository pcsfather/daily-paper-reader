---
title: "SEEK-VEC: Augmenting topic modeling with spectral ensemble learning"
title_zh: SEEK-VEC：利用谱集成学习增强主题建模
authors: "Danning, R., Ke, Z. T., Ma, R., Lin, X."
date: 2026-07-21
pdf: "https://www.biorxiv.org/content/10.64898/2025.12.12.693799v2.full.pdf"
tags: ["query:wo"]
score: 7.0
evidence: 集成主题建模从计数数据中发现潜在产品分组
tldr: 面对计数数据中潜在模式检测问题，标准主题模型易受假设限制、噪声和主题数误设影响。提出 SEEK-VEC 框架，通过谱集成方法融合多个候选主题模型，生成包含优先级评分和分组评分的元结构矩阵，以支持词汇分类与交互式模式发现。仿真表明，即便信号弱，该方法也能增强标准主题模型的词汇识别与关系理解能力；在统计摘要数据集上的应用验证了其在模型诊断与结果解释方面的价值。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2025-12-12-693799-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1679, \"height\": 872, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2025-12-12-693799-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1632, \"height\": 1648, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2025-12-12-693799-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 866, \"height\": 606, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2025-12-12-693799-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1626, \"height\": 1278, \"label\": \"Figure\"}]"
motivation: 标准主题模型假设严格、易受噪声干扰且对主题数设定敏感，需增强其稳健性与可解释性。
method: 提出 SEEK-VEC 谱集成框架，综合多候选模型生成评分矩阵用于词汇嵌入与分类。
result: 仿真显示 SEEK-VEC 在弱信号下仍能提升重要词汇识别与关系发现性能，并在 MADStat 数据集上验证了模型诊断能力。
conclusion: SEEK-VEC 作为一种谱集成学习方法，有效增强了主题建模的可靠性和洞察力。
---

## 摘要
计数数据在许多应用中普遍存在，而理解其中的潜在模式一直是人们关注的重点。主题建模是检测计数数据中潜在结构的强大工具。然而，标准主题建模方法往往受限于其严格的假设，容易受到噪声干扰，并对主题数目的错误设定十分敏感。本文提出SEEK-VEC（主题模型的谱集成方法，利用特征评分实现K未知情况下的词汇嵌入与分类），这是一种集成主题建模框架，通过谱集成过程整合多个候选主题模型的见解。SEEK-VEC生成一个元结构矩阵，其中包含优先级评分和分组评分，能够用于变量分类、交互式模式发现和模型诊断。通过模拟实验，我们证明SEEK-VEC增强了标准主题模型在识别重要词汇和理解它们之间关系方面的性能，尤其是在信号强度较弱的情况下。我们将SEEK-VEC应用于统计摘要的MADStat数据集，并展示了其在评估主题模型所提出的解释方面的实用性。

## 速览
**TLDR**：计数数据广泛存在于多领域，理解其潜在模式至关重要，但标准主题建模方法受限于严格假设、噪声敏感与主题数误设问题。为此，提出SEEK-VEC框架，通过谱集成学习整合多候选模型，生成优先化与分组分数，支持变量分类与交互发现。仿真证实，尤其在弱信号下，能显著提升重要词汇识别及关系捕捉性能；在MADStat统计摘要数据集的应用展示了其模型诊断与解释评估的实用价值，为复杂计数数据中的稳健主题发现提供了可扩展方案。 \
**Motivation**：计数数据的潜在模式挖掘受限于标准主题模型的严格假设、噪声敏感与主题数误设。 \
**Method**：提出SEEK-VEC框架，利用谱集成学习整合多候选模型，生成优先化与分组分数构造元矩阵。 \
**Result**：仿真弱信号下词汇识别与关系捕捉性能提升，MADStat数据集验证了模型解释评估效用。 \
**Conclusion**：SEEK-VEC增强了主题建模鲁棒性，为复杂计数数据提供可解释的集成方案。

---

## Abstract
Count data are ubiquitous across many applications in which understanding latent patterns is of interest. Topic modeling is a powerful tool for detecting latent structure in count data. However, standard topic modeling methods are often constrained by their restrictive assumptions, susceptible to noise, and sensitive to misspecification of the number of topics. Here, we introduce SEEK-VEC (Spectral Ensembling of topic models with Eigenscore for K-agnostic Vocabulary Embedding and Classification), an ensemble topic modeling framework that integrates insights from multiple candidate topic models through a spectral ensembling procedure. SEEK-VEC produces a meta-structure matrix containing prioritization scores and grouping scores that enable variable classification, interactive pattern discovery, and model diagnostics. Through simulations, we demonstrate that SEEK-VEC augments the performance of standard topic models for identifying important vocabulary words and understanding the relationships among them, particularly when signal strength is weak. We apply SEEK-VEC to the MADStat dataset of statistical abstracts and demonstrate its utility for evaluating the proposed interpretation of a topic model.