---
title: Détection de feuilles de calcul vides
type: docs
weight: 410
url: /fr/net/detecting-empty-worksheets/
description: Cet article vous montre un code expliquant comment détecter programmatoirement les feuilles de calcul vides des classeurs Excel en utilisant l API C# avec la bibliothèque .NET.
keywords: détecter la feuille de calcul vide c#, trouver la feuille de calcul Excel vide c#
---

## **Vérifier les cellules peuplées**

Les feuilles de calcul peuvent avoir une ou plusieurs cellules peuplées de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans ce cas, il est facile de détecter si une feuille de calcul donnée est vide ou non. Il suffit de vérifier les propriétés [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) ou [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn). Si les propriétés mentionnées retournent zéro ou des valeurs positives, cela signifie qu'une ou plusieurs cellules ont été peuplées, cependant, si l'une de ces propriétés retourne -1, cela indique que aucune des cellules n'a été peuplée dans la feuille de calcul donnée.

{{% alert color="primary" %}}

Les collections de lignes et de colonnes ont un index à base zéro, donc une cellule à la ligne 0 et à la colonne 0 signifie la première cellule dans la feuille de calcul, qui est A1.

{{% /alert %}}

## **Vérifier les cellules initialisées vides**

Toutes les cellules qui ont des valeurs sont automatiquement initialisées, cependant, il est possible qu'une feuille de calcul ait des cellules avec seulement une mise en forme appliquée. Dans un tel scénario, les propriétés [**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow) ou [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) retourneront -1 indiquant l'absence de valeurs peuplées mais des cellules initialisées en raison de la mise en forme des cellules ne peuvent pas être détectées en utilisant cette approche. Afin de vérifier si une feuille de calcul a des cellules initialisées vides, il est conseillé d'utiliser la méthode IEnumerator.MoveNext sur l'énumérateur acquis à partir de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Si la méthode IEnumerator.MoveNext retourne **true**, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille de calcul donnée.

## **Vérifier les formes**

Il est possible qu'une feuille de calcul donnée n'ait pas de cellules peuplées, cependant, elle pourrait contenir des formes et des objets tels que des contrôles, des graphiques, des images, etc. Si nous devons vérifier si une feuille de calcul contient une forme, nous pouvons le faire en inspectant la propriété [**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection). Toute valeur positive indique la présence de forme(s) dans la feuille de calcul.

## **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
