---
title: Php'de Sayfa Sonu Önizlemesi
type: docs
weight: 60
url: /tr/java/page-break-preview-in-php/
---
## **Aspose.Cells - Sayfa Sonu Önizlemesi**
 Çalışma sayfasını kullanarak sayfa sonu önizlemesini ayarlamak için**PHP için Aspose.Cells Java** , sadece çağırmak**PageBreakÖnizleme** modül.

**PHP Kodu**

{{< highlight "php" >}}

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
İndirmek**Sayfa Sonu Önizlemesi (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
