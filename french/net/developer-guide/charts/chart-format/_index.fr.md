---
title: Définition de l'apparence du graphique
description: Découvrez comment configurer l'apparence des graphiques dans Aspose.Cells for .NET. Notre guide vous montrera comment modifier la disposition, les couleurs, les polices et les effets des graphiques pour obtenir le style visuel souhaité et améliorer vos feuilles de calcul.
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: Format du graphique
type: docs
weight: 20
url: /fr/net/setting-chart-appearance/
---
##  **Définition de l'apparence du graphique**
Dans Comment créer un graphique, nous avons donné une brève introduction aux types de graphiques et d'objets graphiques proposés par Aspose.Cells, et avons décrit comment en créer un. Cet article explique comment personnaliser l'apparence des graphiques en définissant leurs propriétés :

- Définition de la zone graphique.
- Définition des lignes du graphique.
- Application de thèmes.
- Définition des titres des graphiques et des axes.
- Travailler avec un quadrillage.
###  **Zone de réglage du graphique**
Il existe différents types de zones dans un graphique et Aspose.Cells offre la possibilité de modifier l'apparence de chaque zone. Les développeurs peuvent appliquer différents paramètres de formatage sur une zone en modifiant sa couleur de premier plan, sa couleur d'arrière-plan, son format de remplissage, etc.

Dans l'exemple ci-dessous, nous avons appliqué différents paramètres de formatage sur différents types de zones d'un graphique. Ces domaines comprennent :

- Superficie du terrain
- Zone graphique
- Zone CollectionSéries
- Aire d'un point unique dans une SeriesCollection

L'extrait de code suivant montre comment définir la zone de graphique.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **Définition des lignes du graphique**
 Les développeurs peuvent également appliquer différents types de styles sur les lignes ou les marqueurs de données du[SérieCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). L'extrait de code suivant montre comment définir les lignes d'un graphique à l'aide de Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **Application des thèmes Excel Microsoft 2007/2010 aux graphiques**
 Les développeurs peuvent appliquer différents thèmes/couleurs Excel Microsoft à[SérieCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)ou d'autres objets graphiques, comme indiqué ci-dessous dans l'exemple.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **Définition des titres des graphiques ou des axes**
 Vous pouvez utiliser Microsoft Excel pour définir les titres d'un graphique et ses axes dans un environnement WYSIWYG. Aspose.Cells permet également aux développeurs de définir les titres d'un graphique et ses axes au moment de l'exécution. Tous les graphiques et leurs axes contiennent un[Titre](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)propriété qui peut être utilisée pour définir leurs titres comme indiqué ci-dessous dans un exemple.

L'extrait de code suivant montre comment définir des titres pour les graphiques et les axes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **Travailler avec les principaux quadrillages**
Il est possible de personnaliser l’apparence des principaux quadrillages. Masquez ou affichez le quadrillage, ou définissez leur couleur et d'autres paramètres. Ci-dessous, nous montrons comment masquer le quadrillage et comment changer leur couleur.
####  **Masquage du quadrillage principal**
 Les développeurs peuvent contrôler la visibilité des principaux quadrillages en définissant le[Est visible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) propriété du[Doubler](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) s'opposer à**vrai** ou fausse**.

L'extrait de code suivant montre comment masquer les principaux quadrillages. Après avoir masqué le quadrillage principal, un histogramme sera ajouté à la feuille de calcul sans quadrillage.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **Modification des principaux paramètres du quadrillage**
Les développeurs peuvent non seulement contrôler la visibilité du quadrillage principal, mais également d'autres propriétés, notamment sa couleur, etc.

L'extrait de code suivant montre comment modifier la couleur du quadrillage principal. Après avoir défini la couleur du quadrillage principal, un histogramme sera ajouté à la feuille de calcul avec le quadrillage modifié.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **Sujets avancés**
- [Définir le code de format des valeurs de la série de graphiques](/cells/fr/net/set-the-values-format-code-of-chart-series/)
- [Définir l'image comme arrière-plan Remplissez le graphique](/cells/fr/net/set-picture-as-background-fill-in-the-chart/)
