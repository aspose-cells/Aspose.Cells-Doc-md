---
title: Créer un graphique boursier Open High Low Close (OHLC)
description: Apprenez à créer un graphique boursier open high low close en utilisant Aspose.Cells for .NET. Notre guide vous montrera comment tracer des données du marché boursier, y compris les prix d ouverture, élevés, bas et de clôture, sur un graphique pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for .NET, Graphique boursier Open High Low Close, Données du marché boursier, Analyse, Visualisation.
type: docs
weight: 182
url: /fr/net/create-open-high-low-close-stock-chart/
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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
