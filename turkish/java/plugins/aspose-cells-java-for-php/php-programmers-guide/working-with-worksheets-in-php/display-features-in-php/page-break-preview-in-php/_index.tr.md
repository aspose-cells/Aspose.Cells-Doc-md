---
title: Php de Sayfa Aralığı Önizleme
type: docs
weight: 60
url: /tr/java/page-break-preview-in-php/
---

## **Aspose.Cells - Sayfa Kesme Önizlemesi**
**Aspose.Cells Java for PHP** kullanarak çalışma sayfasını sayfa aralığı önizlemesi olarak ayarlamak için **PageBreakPreview** modülünü çağırın.

PHP Kodu

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview

$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirin **Sayfa Kesme Önizlemesi (Aspose.Cells)**	any of the aşağıda bahsedilen sosyal kodlama sitelerinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
