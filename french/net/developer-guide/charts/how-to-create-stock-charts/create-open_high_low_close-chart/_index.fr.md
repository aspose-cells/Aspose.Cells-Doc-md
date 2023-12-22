---
title: Créer un graphique boursier ouvert-haut-bas-fermeture (OHLC)
description: Apprenez à créer un graphique boursier d'ouverture-haut-bas-clôture en utilisant le Aspose.Cells for .NET. Notre guide vous montrera comment tracer les données boursières, y compris les prix d'ouverture, haut, bas et de clôture, sur un graphique pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for .NET, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /fr/net/create-open-high-low-close-stock-chart/
---
##  **Scénarios d'utilisation possibles**
Le graphique OHLC (Open-High-Low-Close) utilise cinq colonnes de données, dans l'ordre : catégorie, ouverture, haut, bas et clôture. La fourchette de prix dans chaque catégorie est à nouveau indiquée par une ligne verticale, tandis que la fourchette entre l'ouverture et la clôture est indiquée par une barre flottante plus large ; si le prix augmente dans la catégorie (la clôture est supérieure à l'ouverture), la barre est remplie d'une couleur, tandis que si le prix diminue, la barre est remplie d'une autre. Ce type de graphique est souvent appelé graphique en chandeliers.

![tâche : image_alt_text](data.png)

![tâche : image_alt_text](sample.png)
##  **Améliorations de la visibilité dans le graphique**
Nous utilisons souvent des couleurs plutôt que le noir et blanc pour indiquer les prix croissants et décroissants. Dans la première série de chandeliers ci-dessous, le rouge montre les prix en hausse et le vert en baisse.

![tâche : image_alt_text](sample2.png)
##  **Exemple de code**
 L'exemple de code suivant charge le[exemple de fichier Excel](Open-High-Low-Close.xlsx) et génère le[sortie du fichier Excel](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
