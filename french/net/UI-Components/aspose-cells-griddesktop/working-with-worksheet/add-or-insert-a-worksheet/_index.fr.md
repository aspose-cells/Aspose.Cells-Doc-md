---
title: Ajouter ou insérer une feuille de calcul
type: docs
weight: 20
url: /fr/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

Dans cette rubrique, nous aborderons les techniques pour ajouter ou insérer des feuilles de calcul dans un fichier Excel à l'aide de Aspose.Cells.GridDesktop. La différence entre l'ajout et l'insertion de feuilles de calcul est qu'en plus, une feuille de calcul est simplement ajoutée à la fin de la collection de feuilles de calcul du fichier Excel, mais l'insertion signifie l'ajout d'une feuille de calcul à une position spécifique dans la collection de feuilles de calcul.

{{% /alert %}} 
## **Ajout d'une feuille de calcul**
Pour ajouter une feuille de calcul à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridDesktop à un formulaire.
1. Appelez la méthode Add de la collection Worksheet dans le contrôle GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


De nombreuses versions surchargées de la méthode Add sont disponibles. En utilisant la version surchargée ci-dessus, par exemple, une feuille de calcul est ajoutée au fichier Excel avec un nom de feuille par défaut. En utilisant d'autres versions surchargées de la méthode Add, il est possible de définir le nom comme indiqué ci-dessous dans l'exemple.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Insertion d'une feuille de calcul**
Pour insérer une feuille de calcul à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridDesktop à un formulaire.
1. Appelez la méthode Insert de la collection Worksheets dans le contrôle GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Microsoft Excel (97-2003 XLS) prend en charge les feuilles Excel comportant jusqu'à 65 536 lignes et 256 colonnes. Aspose.Cells.GridDesktop suit les mêmes normes. Dans le contrôle Aspose.Cells.GridDesktop, les développeurs peuvent ajouter ou insérer des feuilles de calcul avec plus de lignes et de colonnes que la limite standard, mais lorsqu'ils essaient d'enregistrer les données de la grille dans un fichier Excel, une exception est levée. Cela signifie que seules les données contenues dans les 65 536 lignes et 256 colonnes peuvent être enregistrées dans un fichier Excel XLS à l'aide de Aspose.Cells.GridDesktop, si vous utilisez le format de fichier XLSX (MS Excel 2007/2010), il n'y a cependant pas une telle limitation.

{{% /alert %}}
