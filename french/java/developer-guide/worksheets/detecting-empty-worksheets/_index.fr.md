---
title: Détection des feuilles de calcul vides
type: docs
weight: 710
url: /fr/java/detecting-empty-worksheets/
---
## **Vérifier le Cells peuplé**
Les feuilles de calcul peuvent avoir une ou plusieurs cellules remplies de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans un tel cas, il est facile de détecter si une feuille de calcul donnée est vide ou non. Il ne nous reste plus qu'à vérifier[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) ou[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)Propriétés. Si les propriétés susmentionnées renvoient des valeurs nulles ou positives, cela signifie qu'une ou plusieurs cellules ont été remplies, cependant, si l'une de ces propriétés renvoie -1, cela indique qu'aucune des cellules n'a été remplie dans la feuille de calcul donnée.

{{% alert color="primary" %}} 

Les collections de lignes et de colonnes ont un index de base zéro, par conséquent, une cellule à la ligne 0 et à la colonne 0 signifie la première cellule de la feuille de calcul, qui est A1.

{{% /alert %}} 
## **Vérifier vide initialisé Cells**
 Toutes les cellules contenant des valeurs sont automatiquement initialisées, cependant, il est possible qu'une feuille de calcul contienne des cellules auxquelles seule la mise en forme est appliquée. Dans un tel scénario, le[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) ou[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)properties renverra -1 indiquant l'absence de toute valeur peuplée, mais les cellules initialisées en raison du formatage des cellules ne peuvent pas être détectées à l'aide de cette approche. Afin de vérifier si une feuille de calcul contient des cellules initialisées vides, il est conseillé d'utiliser la fonction*Iterator.hasNext* méthode sur l'itérateur acquis de la collection Cells. Si la*iterator.hasNext*La méthode renvoie true, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille de calcul donnée.

{{% alert color="primary" %}} 

 Il existe plusieurs façons d'acquérir l'énumérateur de cellules, comme indiqué dans[Comment et où utiliser les itérateurs](/cells/fr/java/how-and-where-to-use-iterators/).

{{% /alert %}} 
## **Vérifier les formes**
 Il est possible qu'une feuille de calcul donnée n'ait pas de cellules remplies, cependant, elle peut contenir des formes et des objets tels que des contrôles, des graphiques, des images, etc. Si nous devons vérifier si une feuille de calcul contient une forme, nous pouvons le faire en inspectant le[ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count)propriété. Toute valeur positive indique la présence de forme(s) dans la feuille de calcul.
## **Exemple de programmation**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
