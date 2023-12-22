---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et la suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page est terminée et toutes les autres données après le saut de page sont imprimées sur la page suivante lors de l'impression. En termes simples, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul lors de l'exécution à l'aide de Aspose.Cells. Aspose.Cells permet aux développeurs d'ajouter deux types de sauts de page :

- Saut de page horizontal
- Saut de page vertical

Dans la suite de la discussion, nous décrirons comment ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul à l'aide du Aspose.Cells.

{{% /alert %}} 
##  **Sauts de page**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) qui représente un fichier Excel. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)collection qui permet d’accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La classe fournit un large éventail de méthodes utilisées pour gérer une feuille de calcul. Pour ajouter les sauts de page, utilisez le[Ajouter des sauts de page](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) méthode du[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe.
###  **Ajout de sauts de page**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
