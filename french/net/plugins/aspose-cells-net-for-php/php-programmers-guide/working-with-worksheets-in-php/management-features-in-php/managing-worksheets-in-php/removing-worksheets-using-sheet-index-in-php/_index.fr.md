---
title: Suppression de feuilles de calcul à l'aide de l'index de feuilles en PHP
type: docs
weight: 30
url: /fr/net/removing-worksheets-using-sheet-index-in-php/
---
## **Suppression de feuilles de calcul à l'aide de l'index des feuilles**
Suppression de feuilles de calcul à l'aide de l'index des feuilles

**Code PHP**

{{< highlight "php" >}}

         $dataDir = '';

        / Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $ptr->Call($worksheets,"RemoveAt",array(0));

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Suppression de feuilles de calcul à l'aide de l'index des feuilles (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
