---
title: Предварительный просмотр разрыва страницы в Php
type: docs
weight: 60
url: /ru/java/page-break-preview-in-php/
---

## **Aspose.Cells - Предварительный просмотр разрыва страницы**
Чтобы установить лист на предварительный просмотр разрыва страницы с помощью **Aspose.Cells Java для PHP**, просто вызовите модуль **PageBreakPreview**.

**PHP-код**

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
## **Скачать работающий код**
Скачайте **Предварительный просмотр разрыва страницы (Aspose.Cells)** с любого из нижеуказанных сайтов для социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
