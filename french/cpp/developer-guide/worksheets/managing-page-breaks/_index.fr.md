---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et la suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page se termine et tout le reste des données après le saut de page est imprimé sur la page suivante lors de l'impression. En termes simples, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul lors de l'exécution à l'aide de Aspose.Cells. Aspose.Cells permet aux développeurs d'ajouter deux types de sauts de page :

- Saut de page horizontal
- Saut de page vertical

Dans le reste de la discussion, nous décrirons comment ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul en utilisant Aspose.Cells.

{{% /alert %}} 
## **Sauts de page**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)fournit un large éventail de méthodes utilisées pour gérer une feuille de calcul. Pour ajouter des sauts de page, utilisez le[Ajouter des sauts de page](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) méthode de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe.
### **Ajouter des sauts de page**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
