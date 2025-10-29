---  
title: Comment utiliser la palette de couleurs
linktitle: Comment utiliser la palette de couleurs  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/excel-color-palette/  
description: Code Node.js pour ajouter des couleurs personnalisées à la palette et utiliser la palette de couleurs Excel avec Aspose.Cells for Node.js via C++.  
keywords: node.js ajouter des couleurs personnalisées à la palette, palette de couleurs Excel par programmation sous node.js, comment utiliser la palette de couleurs dans un classeur par programmation, comment utiliser la palette de couleurs dans excel avec node.js  
---  

## **Couleurs et palette**  

Une palette est le nombre de couleurs disponibles pour créer une image. L'utilisation d'une palette normalisée dans une présentation permet à l'utilisateur de créer un aspect cohérent. Chaque fichier Microsoft Excel (97-2003) possède une palette de 56 couleurs qui peuvent être appliquées aux cellules, polices, quadrillages, objets graphiques, remplissages et lignes dans un graphique.  

Avec Aspose.Cells for Node.js via C++, il est possible non seulement d'utiliser les couleurs existantes de la palette, mais aussi des couleurs personnalisées. Avant d'utiliser une couleur personnalisée, ajoutez-la d'abord à la palette.  

Ce sujet traite de l'ajout de couleurs personnalisées à la palette.  

## **Ajouter des couleurs personnalisées à la palette**  

Aspose.Cells prend en charge la palette de 56 couleurs de Microsoft Excel. Pour utiliser une couleur personnalisée qui n'est pas définie dans la palette, ajoutez la couleur à la palette.  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) fournit une méthode [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) qui prend les paramètres suivants pour ajouter une couleur personnalisée afin de modifier la palette :  

- Couleur personnalisée, la couleur personnalisée à ajouter.  
- Index, l'index de la couleur dans la palette que la couleur personnalisée remplacera. Doit être compris entre 0 et 55.  

L'exemple ci-dessous ajoute une couleur personnalisée (Orchid) à la palette avant de l'appliquer sur une police.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

La palette ne contient que 56 couleurs. Lorsque vous ajoutez une couleur personnalisée à la palette, la palette est modifiée et tout élément dans le fichier formaté avec la couleur précédente est modifié. Ainsi, lorsque vous modifiez la palette, veuillez être très prudent. De plus, il s'agit d'une limitation du format de fichier XLS (Excel 97 - 2003) uniquement car il n'y a pas de telle limitation pour les formats de fichier XLSX ou d'autres formats avancés de MS Excel (2007/2010 ou 2013).  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
