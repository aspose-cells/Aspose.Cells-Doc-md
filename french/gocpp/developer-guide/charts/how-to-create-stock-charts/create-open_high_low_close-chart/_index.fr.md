---
title: Créer un graphique boursier Open High Low Close (OHLC) avec Golang via C++
description: Apprenez comment créer un graphique bourse ouverture haut bas fermeture avec Aspose.Cells for C++. Notre guide montrera comment tracer les données du marché boursier, y compris les prix d ouverture, haut, bas et fermeture, pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for C++, Graphique bourse Ouverture Haut Bas Fermeture, Données du marché boursier, Analyse, Visualisation.
type: docs
weight: 182
url: /fr/go-cpp/create-open-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le graphique Open-High-Low-Close (OHLC) utilise cinq colonnes de données, dans l'ordre : catégorie, ouverture, haut, bas et clôture. La plage de prix dans chaque catégorie est à nouveau indiquée par une ligne verticale, tandis que la plage entre l'ouverture et la clôture est donnée par une barre flottante plus large ; si le prix augmente dans la catégorie (la clôture est supérieure à l'ouverture), la barre est remplie d'une couleur, tandis que si le prix diminue, la barre est remplie d'une autre couleur. Ce type de graphique est souvent appelé un graphique en chandelier.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Améliorations de la visibilité dans le graphique**
Nous utilisons souvent des couleurs plutôt que du noir et blanc pour indiquer l'augmentation ou la diminution des prix. Dans le premier ensemble de chandeliers ci-dessous, le rouge montre une augmentation et le vert une diminution des prix.

![todo:image_alt_text](sample2.png)

## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Open-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
