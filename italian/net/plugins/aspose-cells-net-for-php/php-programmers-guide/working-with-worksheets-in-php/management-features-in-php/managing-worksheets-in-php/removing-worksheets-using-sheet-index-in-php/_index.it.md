---
title: Rimozione di fogli di lavoro utilizzando l'indice dei fogli in PHP
type: docs
weight: 30
url: /it/net/removing-worksheets-using-sheet-index-in-php/
---
## **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**
Rimozione di fogli di lavoro utilizzando l'indice dei fogli

**Codice PHP**

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
## **Scarica il codice in esecuzione**
 Scarica**Rimozione di fogli di lavoro utilizzando l'indice dei fogli (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
