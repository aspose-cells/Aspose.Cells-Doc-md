---
title: Comment utiliser la palette de couleurs
type: docs
weight: 80
url: /fr/net/excel-color-palette/
description: Code C# pour ajouter des couleurs personnalisées à la palette et utiliser la palette de couleurs Excel avec Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **Couleurs et palette**

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette standardisée dans une présentation permet à l'utilisateur de créer une apparence cohérente. Chaque fichier Excel Microsoft (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes d'un graphique.

Avec le Aspose.Cells, il est possible d'utiliser non seulement les couleurs existantes de la palette mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.

Cette rubrique explique comment ajouter des couleurs personnalisées à la palette.

##  **Ajouter des couleurs personnalisées à la palette**

Aspose.Cells prend en charge la palette de 56 couleurs d'Excel Microsoft. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , cela représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe fournit un[**Changer la palette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) méthode qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :

- Couleur personnalisée, la couleur personnalisée à ajouter.
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.

L'exemple ci-dessous ajoute une couleur personnalisée (Orchidée) à la palette avant de l'appliquer sur une police.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément du fichier formaté avec la couleur précédente est modifié. Donc, lorsque vous changez de palette, soyez très prudent. De plus, il s'agit de la limitation du format de fichier XLS (Excel 97 - 2003) uniquement, car il n'existe pas de limitation de ce type pour XLSX ou d'autres formats de fichiers MS Excel avancés (2007/2010 ou 2013).

{{% /alert %}}