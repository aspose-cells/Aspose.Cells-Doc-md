---
title: Rimozione Fogli di Lavoro Usando il Nome del Foglio in PHP
type: docs
weight: 40
url: /it/net/removing-worksheets-using-sheet-name-in-php/
---

## **Rimozione Fogli di Lavoro Usando il Nome del Foglio**
Rimozione Fogli di Lavoro Usando il Nome del Foglio

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Rimozione Fogli di Lavoro Usando il Nome del Foglio (Aspose.Cells)** da uno qualsiasi dei siti di codifica sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
