---
title: PHP'de Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma
type: docs
weight: 30
url: /tr/net/removing-worksheets-using-sheet-index-in-php/
---
## **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**
Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma

**PHP Kodu**

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
## **Çalışan Kodu İndir**
 İndirmek**Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
