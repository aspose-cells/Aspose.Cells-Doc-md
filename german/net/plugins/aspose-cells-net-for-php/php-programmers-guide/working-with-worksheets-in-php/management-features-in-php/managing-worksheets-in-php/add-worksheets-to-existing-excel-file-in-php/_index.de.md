---
title: Arbeitsblätter zu vorhandener Excel Datei in PHP hinzufügen
type: docs
weight: 10
url: /de/net/add-worksheets-to-existing-excel-file-in-php/
---

Arbeitsblätter zu vorhandener Excel-Datei hinzufügen

Arbeitsblätter zu vorhandener Excel-Datei hinzufügen

**PHP-Code**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $worksheet_index = $ptr->Call($worksheets,"Add_2",array());

        $worksheet = $ptr->Get($worksheets,"Item",array($worksheet_index));

        $ptr->Set($worksheet,"Name","My Worksheet",array());

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

        print "Completed." . PHP_EOL;

{{< /highlight >}}
## **Laufenden Code herunterladen**
**Arbeitsblätter zu vorhandener Excel-Datei hinzufügen (Aspose.Cells)** von einer der unten genannten sozialen Coding-Websites herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/AddWorksheetsToExistingExcelFile.php)
