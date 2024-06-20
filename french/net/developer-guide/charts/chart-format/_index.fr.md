---
title: Paramétrer l apparence du graphique
description: Apprenez à configurer l apparence des graphiques dans Aspose.Cells for .NET. Notre guide vous montrera comment modifier les agencements, couleurs, polices et effets des graphiques pour obtenir le style visuel désiré et améliorer vos feuilles de calcul.
keywords: Aspose.Cells for .NET, tracé, apparence de tracé, agencements, couleurs, polices, effets, feuilles de calcul.
linktitle: Format de graphique
type: docs
weight: 20
url: /fr/net/setting-chart-appearance/
---

## **Réglage de l’apparence du graphique**
Dans Comment créer un graphique, nous avons présenté brièvement les types de graphiques et d'objets de graphiques offerts par Aspose.Cells, et décrit comment en créer un. Cet article discute comment personnaliser l'apparence des graphiques en définissant leurs propriétés :

- Définir la zone du graphique.
- Définition des lignes du graphique.
- Application de thèmes.
- Définition des titres des graphiques et des axes.
- Travailler avec des lignes de repère.
### **Définition de la zone du graphique**
Il existe différents types de zones dans un graphique et Aspose.Cells offre la flexibilité de modifier l'apparence de chaque zone. Les développeurs peuvent appliquer différents paramètres de mise en forme à une zone en changeant sa couleur avant-plan, sa couleur d'arrière-plan et son format de remplissage, etc.

Dans l'exemple ci-dessous, nous avons appliqué différents paramètres de mise en forme sur différents types de zones d'un graphique. Ces zones comprennent :

- Zone de traçage
- Zone du graphique
Zone de SeriesCollection
- Zone d'un point unique dans une SeriesCollection

Le code suivant montre comment définir la zone du graphique.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Définition des lignes du graphique**
Les développeurs peuvent également appliquer différents types de styles sur les lignes ou les marqueurs de données de la [SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Le code suivant montre comment définir les lignes du graphique à l'aide de l'API Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Application des thèmes Microsoft Excel 2007/2010 aux graphiques**
Les développeurs peuvent appliquer différents thèmes/couleurs de Microsoft Excel à [SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) ou à d'autres objets de graphique comme indiqué ci-dessous dans l'exemple.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Configuration des titres des graphiques ou des axes**
Vous pouvez utiliser Microsoft Excel pour définir les titres d'un graphique et de ses axes dans un environnement WYSIWYG. Aspose.Cells permet également aux développeurs de définir les titres d'un graphique et de ses axes à l'exécution. Tous les graphiques et leurs axes contiennent une propriété [Titre](https://reference.aspose.com/cells/net/aspose.cells.charts/graphique/propriétés/titre) qui peut être utilisée pour définir leurs titres comme illustré ci-dessous dans un exemple.

Le snippet de code suivant démontre comment définir des titres pour les graphiques et les axes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Travailler avec les grandes lignes de la grille**
Il est possible de personnaliser l'apparence des grandes lignes de la grille. Masquer ou afficher les lignes de la grille, ou définir leur couleur et d'autres paramètres. Ci-dessous, nous montrons comment masquer les lignes de la grille et comment changer leur couleur.
#### **Masquer les grandes lignes de la grille**
Les développeurs peuvent contrôler la visibilité des grandes lignes de la grille en définissant la propriété [IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) de l'objet [Line](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) à **true** ou **false**.

Le code suivant montre comment masquer les grandes lignes de la grille. Après avoir masqué les grandes lignes de la grille, un graphique en colonnes sera ajouté à la feuille de calcul sans lignes de grille.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Changer les paramètres des grandes lignes de la grille**
Les développeurs peuvent non seulement contrôler la visibilité des grandes lignes de la grille, mais aussi d'autres propriétés comme sa couleur, etc.

Le code suivant montre comment changer la couleur des grandes lignes de la grille. Après avoir défini la couleur des grandes lignes de la grille, un graphique en colonnes sera ajouté à la feuille de calcul avec des lignes de grille modifiées.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Sujets avancés**
- [Définir le code de format des valeurs de la série du graphique](/cells/fr/net/set-the-values-format-code-of-chart-series/)
- [Définir une image comme remplissage d'arrière-plan dans le graphique](/cells/fr/net/set-picture-as-background-fill-in-the-chart/)
