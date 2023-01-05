---
title: Entfernen von Arbeitsblättern unter Verwendung des Blattnamens in PHP
type: docs
weight: 40
url: /de/net/removing-worksheets-using-sheet-name-in-php/
---
## **Arbeitsblätter mit Blattnamen entfernen**
Arbeitsblätter mit Blattnamen entfernen

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
 Download**Arbeitsblätter mit Blattnamen entfernen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
