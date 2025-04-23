---
title: Détection de feuilles de calcul vides
type: docs
weight: 710
url: /fr/java/detecting-empty-worksheets/
---

## **Vérifier les cellules peuplées**
Les feuilles de calcul peuvent avoir une ou plusieurs cellules peuplées de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans un tel cas, il est facile de détecter si une feuille de calcul donnée est vide ou non. Il suffit de vérifier les propriétés [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) ou [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn). Si les propriétés mentionnées ci-dessus renvoient des valeurs zéro ou positives, cela signifie qu'une ou plusieurs cellules ont été peuplées, cependant, si l'une de ces propriétés renvoie -1, cela indique que aucune des cellules n'a été peuplée dans la feuille de calcul donnée.

{{% alert color="primary" %}} 

Les collections de lignes et de colonnes ont un index à base zéro, par conséquent, une cellule à la ligne 0 et à la colonne 0 signifie la première cellule de la feuille de calcul, c'est-à-dire A1.

{{% /alert %}} 
## **Vérifier les cellules initialisées vides**
Toutes les cellules qui ont des valeurs sont automatiquement initialisées, cependant, il est possible qu'une feuille de calcul ait des cellules avec seulement une mise en forme appliquée. Dans un tel scénario, les propriétés [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) ou [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) renverront -1 indiquant l'absence de valeurs peuplées mais des cellules initialisées en raison de la mise en forme de la cellule ne peuvent pas être détectées en utilisant cette méthode. Afin de vérifier si une feuille de calcul a des cellules initialisées vides, il est conseillé d'utiliser la méthode *Iterator.hasNext* sur l'itérateur acquis à partir de la collection de cellules. Si la méthode *iterator.hasNext* renvoie true, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille de calcul donnée.

{{% alert color="primary" %}} 

Il existe plusieurs façons d'acquérir l'énumérateur de cellules comme détaillé dans [Comment et où utiliser les itérateurs](/cells/fr/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Vérifier les formes**
Il est possible qu'une feuille de calcul donnée n'ait pas de cellules peuplées, cependant, elle pourrait contenir des formes et des objets tels que des contrôles, des graphiques, des images, etc. Si nous devons vérifier si une feuille de calcul contient une forme, nous pouvons le faire en inspectant la propriété [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count). Toute valeur positive indique la présence de forme(s) dans la feuille de calcul.
## **Exemple de programmation**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
