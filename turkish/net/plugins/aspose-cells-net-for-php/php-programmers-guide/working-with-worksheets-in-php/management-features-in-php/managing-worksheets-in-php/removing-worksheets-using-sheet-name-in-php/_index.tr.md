---
title: PHP de Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma
type: docs
weight: 40
url: /tr/net/removing-worksheets-using-sheet-name-in-php/
---

## **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**
Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma

PHP Kodu

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
## **Çalışan Kodu İndir**
Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma (Aspose.Cells) kılavuzunu aşağıdaki sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
