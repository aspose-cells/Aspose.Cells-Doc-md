---
title: Удаление листов с использованием индекса листа в PHP
type: docs
weight: 30
url: /ru/net/removing-worksheets-using-sheet-index-in-php/
---

## **Удаление листов с использованием индекса листа**
Удаление листов с использованием индекса листа

**PHP-код**

{{< highlight php >}}

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
## **Скачать работающий код**
Скачайте **Удаление листов по индексу (Aspose.Cells)** с любого из нижеперечисленных сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
