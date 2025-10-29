---
title: Comment créer des graphiques boursiers avec Node.js via C++
linktitle: Comment créer des graphiques boursiers
description: Apprenez à créer différents types de graphiques boursiers, y compris HLC, OHLC, VHLC, et VOHLC en utilisant Aspose.Cells APIs pour Node.js via C++. 
keywords: Créer des graphiques boursiers Node.js via C++, Aspose.Cells, Visualisation des données de marché, Analyse du marché boursier, Guide étape par étape.
type: docs
weight: 71
url: /fr/nodejs-cpp/how-to-create-stock-charts/
---

{{% alert color="primary" %}}

Ce paragraphe vous expliquera comment créer un graphique boursier, qui comprend quatre types :
- **HLC** – Haut-Bas-Clôture.
- **OHLC** – Ouverture-Haut-Bas-Clôture.
- **VHLC** – Volume-Haut-Bas-Clôture.
- **VOHLC** – Volume-Ouverture-Haut-Bas-Clôture.

{{% /alert %}}

## **Qu’est-ce qu’un graphique boursier ?**

Les graphiques boursiers sont des graphiques spécifiques utilisés pour suivre l'évolution du prix des actifs négociés tels que les matières premières, les actions, et les cryptomonnaies. Ils permettent de voir les valeurs élevées et basses dans le temps, ainsi que les valeurs d'ouverture et de clôture en un seul graphique. Aspose.Cells for Node.js via C++ offre quatre graphiques boursiers, et pour les utiliser, vous devez disposer des bons jeux de données, et sélectionner les colonnes dans le bon ordre.

L'ensemble de données suivant montre les informations de trading quotidiennes d’une action. Nous utiliserons ces données pour créer quatre types de graphiques boursiers : graphique High-Low-Close (HLC), graphique Open-High-Low-Close (OHLC), graphique Volume-High-Low-Close (VHLC), et graphique Volume-Open-High-Low-Close (VOHLC).

![todo:image_alt_text](stock.chart.data.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
