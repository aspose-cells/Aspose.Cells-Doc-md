---
title: Gérer les feuilles de calcul
type: docs
weight: 20
url: /fr/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans des fichiers Microsoft Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Ce sujet décrit les approches pour ajouter et supprimer des feuilles de calcul dans des fichiers Microsoft Excel.

{{% /alert %}} 

Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) . La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une large gamme de méthodes pour la gestion des feuilles de calcul.
## **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour créer un nouveau fichier Excel de manière programmatique:

1. Créez un objet de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
1. Appelez la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) de la collection [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/). Une feuille de calcul vide est ajoutée au fichier Excel automatiquement. Elle peut être référencée en passant l'indice de la nouvelle feuille de calcul à la collection [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
1. Obtenez une référence de feuille de calcul.
1. Travaillez sur les feuilles de calcul.
1. Enregistrez le nouveau fichier Excel avec de nouvelles feuilles de calcul en appelant la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de la classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Accès aux feuilles de calcul à l'aide de l'indice de la feuille**
Le code d'exemple suivant montre comment accéder à une feuille de calcul ou en obtenir une en spécifiant son indice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**
La suppression des feuilles de calcul par nom fonctionne bien lorsque le nom de la feuille de calcul est connu. Si vous ne connaissez pas le nom de la feuille de calcul, utilisez une version surchargée de la méthode [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) prenant l'indice de la feuille de calcul au lieu de son nom.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
