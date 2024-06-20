---
title: Arbeitsblätter anhand des Blattnamens in PHP entfernen
type: docs
weight: 40
url: /de/net/removing-worksheets-using-sheet-name-in-php/
---

## **Arbeitsblätter anhand des Blattnamens entfernen**
Arbeitsblätter anhand des Blattnamens entfernen

**PHP-Code**

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
## **Laufenden Code herunterladen**
**Arbeitsblätter anhand des Blattnamens entfernen (Aspose.Cells)** von einer der unten genannten sozialen Coding-Websites herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
