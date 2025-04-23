---
title: Paramétrer l apparence du graphique
description: Apprenez comment configurer l apparence des graphiques dans Aspose.Cells pour Python via .NET. Notre guide vous montrera comment modifier la disposition du graphique, les couleurs, les polices et les effets pour obtenir le style visuel désiré et améliorer vos feuilles de calcul.
keywords: Aspose.Cells pour Python via .NET, création de graphiques, apparence, dispositions, couleurs, polices, effets, feuilles de calcul.
linktitle: Format de graphique
type: docs
weight: 20
url: /fr/python-net/setting-chart-appearance/
---

## **Réglage de l’apparence du graphique**
Dans 'Comment créer un graphique', nous avons donné une brève introduction aux types de graphiques et aux objets de graphique proposés par Aspose.Cells pour Python via .NET, et décrit comment en créer un. Cet article explique comment personnaliser l'apparence des graphiques en réglant leurs propriétés :

- Définir la zone du graphique.
- Définition des lignes du graphique.
- Application de thèmes.
- Définition des titres des graphiques et des axes.
- Travailler avec des lignes de repère.
### **Définition de la zone du graphique**
Il existe différents types de zones dans un graphique et Aspose.Cells pour Python via .NET offre la flexibilité pour modifier l'apparence de chaque zone. Les développeurs peuvent appliquer différents réglages de mise en forme en changeant leur couleur de premier plan, leur couleur d'arrière-plan et leur format de remplissage, etc.

Dans l'exemple ci-dessous, nous avons appliqué différents paramètres de mise en forme sur différents types de zones d'un graphique. Ces zones comprennent :

- Zone de traçage
- Zone du graphique
Zone de SeriesCollection
- Zone d'un point unique dans une SeriesCollection

Le code suivant montre comment définir la zone du graphique.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **Définition des lignes du graphique**
Les développeurs peuvent également appliquer différents styles aux lignes ou aux marqueurs de données de la [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection). Le code suivant illustre comment définir les lignes du graphique en utilisant l'API Aspose.Cells pour Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Application des thèmes Microsoft Excel 2007/2010 aux graphiques**
Les développeurs peuvent appliquer différents thèmes/couleurs Microsoft Excel à la [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) ou à d'autres objets de graphique, comme illustré dans l'exemple ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **Configuration des titres des graphiques ou des axes**
Vous pouvez utiliser Microsoft Excel pour définir les titres d'un graphique et de ses axes dans un environnement WYSIWYG. Aspose.Cells pour Python via .NET permet également aux développeurs de définir les titres d'un graphique et de ses axes en temps réel. Tous les graphiques et leurs axes contiennent une propriété [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title) qui peut être utilisée pour définir leurs titres comme dans l'exemple ci-dessous.

Le snippet de code suivant démontre comment définir des titres pour les graphiques et les axes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **Travailler avec les grandes lignes de la grille**
Il est possible de personnaliser l'apparence des grandes lignes de la grille. Masquer ou afficher les lignes de la grille, ou définir leur couleur et d'autres paramètres. Ci-dessous, nous montrons comment masquer les lignes de la grille et comment changer leur couleur.

#### **Masquer les grandes lignes de la grille**
Les développeurs peuvent contrôler la visibilité des lignes de grille principales en réglant la propriété [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) de l'objet [Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line) sur **true** ou **false**.

Le code suivant montre comment masquer les grandes lignes de la grille. Après avoir masqué les grandes lignes de la grille, un graphique en colonnes sera ajouté à la feuille de calcul sans lignes de grille.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **Changer les paramètres des grandes lignes de la grille**
Les développeurs peuvent non seulement contrôler la visibilité des grandes lignes de la grille, mais aussi d'autres propriétés comme sa couleur, etc.

Le code suivant montre comment changer la couleur des grandes lignes de la grille. Après avoir défini la couleur des grandes lignes de la grille, un graphique en colonnes sera ajouté à la feuille de calcul avec des lignes de grille modifiées.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **Sujets avancés**
- [Définir le code de format des valeurs de la série du graphique](/cells/fr/python-net/set-the-values-format-code-of-chart-series/)
- [Définir une image comme remplissage d'arrière-plan dans le graphique](/cells/fr/python-net/set-picture-as-background-fill-in-the-chart/)
