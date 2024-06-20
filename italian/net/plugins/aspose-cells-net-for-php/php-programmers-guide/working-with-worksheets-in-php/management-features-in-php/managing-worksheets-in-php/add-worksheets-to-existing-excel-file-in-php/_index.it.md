---
title: Aggiungere Fogli di Lavoro a un File Excel Esistente in PHP
type: docs
weight: 10
url: /it/net/add-worksheets-to-existing-excel-file-in-php/
---

Aggiungi Fogli di Lavoro a un File Excel Esistente

Aggiungi Fogli di Lavoro a un File Excel Esistente

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Aggiungi Fogli di Lavoro a un File Excel Esistente (Aspose.Cells)** da uno qualsiasi dei siti di codifica sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/AddWorksheetsToExistingExcelFile.php)
