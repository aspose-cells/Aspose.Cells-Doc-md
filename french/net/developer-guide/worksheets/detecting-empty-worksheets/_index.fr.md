---
title: Détection des feuilles de calcul vides
type: docs
weight: 410
url: /fr/net/detecting-empty-worksheets/
---
## **Vérifier le Cells peuplé**

Les feuilles de calcul peuvent avoir une ou plusieurs cellules remplies de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans un tel cas, il est facile de détecter si une feuille de calcul donnée est vide ou non. Il ne nous reste plus qu'à vérifier[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) ou alors[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)Propriétés. Si les propriétés susmentionnées renvoient des valeurs nulles ou positives, cela signifie qu'une ou plusieurs cellules ont été remplies, cependant, si l'une de ces propriétés renvoie -1, cela indique qu'aucune des cellules n'a été remplie dans la feuille de calcul donnée.

{{% alert color="primary" %}}

Les collections de lignes et de colonnes ont un index de base zéro. Par conséquent, une cellule à la ligne 0 et à la colonne 0 signifie la première cellule de la feuille de calcul, qui est A1.

{{% /alert %}}

## **Vérifier vide initialisé Cells**

 Toutes les cellules contenant des valeurs sont automatiquement initialisées, cependant, il est possible qu'une feuille de calcul contienne des cellules auxquelles seule la mise en forme est appliquée. Dans un tel scénario, le[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)ou alors[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) properties renverra -1 indiquant l'absence de toute valeur peuplée, mais les cellules initialisées en raison du formatage des cellules ne peuvent pas être détectées à l'aide de cette approche. Afin de vérifier si une feuille de calcul contient des cellules initialisées vides, il est conseillé d'utiliser la méthode IEnumerator.MoveNext sur l'énumérateur acquis à partir de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. Si la méthode IEnumerator.MoveNext renvoie**vrai** cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille de calcul donnée.

## **Vérifier les formes**

 Il est possible qu'une feuille de calcul donnée n'ait pas de cellules remplies, cependant, elle peut contenir des formes et des objets tels que des contrôles, des graphiques, des images, etc. Si nous devons vérifier si une feuille de calcul contient une forme, nous pouvons le faire en inspectant le[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)la propriété. Toute valeur positive indique la présence de forme(s) dans la feuille de calcul.

## **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
