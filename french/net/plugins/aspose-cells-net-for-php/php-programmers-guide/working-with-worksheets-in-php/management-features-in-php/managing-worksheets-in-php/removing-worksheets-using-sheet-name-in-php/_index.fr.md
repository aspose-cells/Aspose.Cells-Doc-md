---
title: Suppression des feuilles de calcul en utilisant le nom de la feuille en PHP
type: docs
weight: 40
url: /fr/net/removing-worksheets-using-sheet-name-in-php/
---

## **Suppression des feuilles de calcul en utilisant le nom de la feuille**
Suppression des feuilles de calcul en utilisant le nom de la feuille

**Code PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $ptr->Call($worksheets,"RemoveAt_2",array("Sheet1"));

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

        print "Completed." . PHP_EOL;

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Suppression des feuilles de calcul en utilisant le nom de la feuille (Aspose.Cells)** de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
