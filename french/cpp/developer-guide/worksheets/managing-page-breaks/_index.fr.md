---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et où la page suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page est terminée et toutes les données restantes après le saut de page sont imprimées sur la page suivante lors de l'impression. En d'autres termes, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul à l'exécution à l'aide d'Aspose.Cells. Aspose.Cells permet aux développeurs d'ajouter deux types de saut de page :

- Saut de page horizontal
- Saut de page vertical

Dans le reste de la discussion, nous décrirons comment ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul à l'aide d'Aspose.Cells.

{{% /alert %}} 
## **Sauts de page**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) qui représente un fichier Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) permettant d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une large gamme de méthodes utilisées pour gérer une feuille de calcul. Pour ajouter les sauts de page, utilisez la méthode [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
### **Ajout de sauts de page**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
