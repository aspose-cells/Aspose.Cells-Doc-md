---
title: Créer un graphique boursier Open High Low Close (OHLC)
description: Apprenez comment créer un graphique boursier ouverture haut bas fermeture en utilisant Aspose.Cells pour Python via .NET. Notre guide montrera comment tracer des données de marché boursier, y compris les prix d ouverture, haut, bas et de clôture, pour une meilleure analyse et visualisation.
keywords: Aspose.Cells pour Python via .NET, Graphique boursier Ouverture Haut Bas Fermeture, Données de marché boursier, Analyse, Visualisation.
type: docs
weight: 182
url: /fr/python-net/create-open-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le graphique Open-High-Low-Close (OHLC) utilise cinq colonnes de données, dans l'ordre : catégorie, ouverture, haut, bas et clôture. La plage de prix dans chaque catégorie est à nouveau indiquée par une ligne verticale, tandis que la plage entre l'ouverture et la clôture est donnée par une barre flottante plus large ; si le prix augmente dans la catégorie (la clôture est supérieure à l'ouverture), la barre est remplie d'une couleur, tandis que si le prix diminue, la barre est remplie d'une autre couleur. Ce type de graphique est souvent appelé un graphique en chandelier.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Améliorations de la visibilité dans le graphique**
Nous utilisons souvent des couleurs plutôt que du noir et blanc pour indiquer les prix croissants et décroissants. Dans le premier ensemble de chandeliers ci-dessous, le rouge montre les prix croissants et le vert les prix décroissants.

![todo:image_alt_text](sample2.png)

## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Open-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-open-high-low-close-stock-chart.py" >}}
