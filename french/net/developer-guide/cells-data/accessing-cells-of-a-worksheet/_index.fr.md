---
title: Accéder au Cells d'une feuille de calcul
type: docs
weight: 10
url: /fr/net/accessing-cells-of-a-worksheet/
description: Cet article montre comment obtenir la plage d'affichage maximale de la feuille de calcul et des cellules d'accès via le Aspose.Cells for .NET API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (qui composent une feuille de calcul). Une cellule est un élément de base d'une feuille de calcul utilisée pour construire l'ensemble de la feuille de calcul sous la forme d'une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous devons accéder à ses cellules. Ainsi, dans cette rubrique, nous aborderons quelques approches de base pour accéder aux cellules d'une feuille de calcul au moment de l'exécution à l'aide de Aspose.Cells.

{{% /alert %}}

##  **Comment accéder au Cells**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contient un[**Collection de feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection qui représente toutes les cellules de la feuille de calcul.

 On peut utiliser[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection pour accéder aux cellules d’une feuille de calcul. Aspose.Cells propose trois approches de base pour accéder aux cellules d'une feuille de calcul :

1. En utilisant le nom de la cellule.
1. Utilisation de l'index de ligne et de colonne d'une cellule.
1.  Utiliser un index de cellule dans le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection

**IMPORTANT:**Nous avons mentionné que la 3ème approche est la plus rapide et la 1ère approche est la plus lente. La différence de performances entre les approches est très faible, ne vous inquiétez donc pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

###  **Comment obtenir un objet Cell par nom Cell**

 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant son nom de cellule au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collecte des[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe comme index.

 Si vous créez une feuille de calcul vierge au début, le nombre de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)la collecte est nulle. Lorsque vous utilisez cette approche pour accéder à une cellule, il vérifiera si cette cellule existe ou non dans la collection. Si oui, il renvoie l'objet cellule dans la collection sinon, il crée un nouveau[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objet, ajoute l'objet à l'objet[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection puis renvoie l'objet. Cette approche est le moyen le plus simple d'accéder à la cellule si vous êtes familier avec Excel Microsoft, mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **Comment obtenir l'objet Cell par index de ligne et de colonne du Cell**

 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant les indices de sa ligne et de sa colonne au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collecte des[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

Cette approche fonctionne de la même manière que celle de la première approche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **Comment obtenir l'objet Cell par l'index Cell dans la collection Cells**

 Une cellule est également accessible en transmettant l'index numérique de la cellule au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection.

Si vous utilisez cette approche pour accéder aux cellules, une exception peut être levée si l'index numérique de la cellule est hors plage. Cette approche est la plus rapide pour accéder aux cellules, mais il est important de savoir que si vous utilisez cette approche pour accéder à un objet cellule, l'index numérique peut changer après l'ajout de nouvelles cellules au fichier.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. Les objets cellules dans le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Les collections sont triées en interne par indices de ligne et de colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **Comment obtenir la plage d'affichage maximale de la feuille de calcul**

Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale (la plage de cellules entre la première et la dernière cellule contenant du contenu) est utile lorsque vous devez copier, sélectionner ou afficher l'intégralité du contenu d'une feuille de calcul dans une image.

Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul en utilisant[**Feuille de calcul.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . L'exemple de code suivant illustre comment accéder au[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
