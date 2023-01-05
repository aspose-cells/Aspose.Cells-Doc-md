---
title: Seitenumbruch-Vorschau in Php
type: docs
weight: 60
url: /de/java/page-break-preview-in-php/
---
## **Aspose.Cells - Seitenumbruchvorschau**
 So stellen Sie das Arbeitsblatt auf Seitenumbruchvorschau ein**Aspose.Cells Java for PHP** , einfach aufrufen**Seitenumbruchvorschau** Modul.

**PHP-Code**

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
## **Laufcode herunterladen**
Download**Seitenumbruch-Vorschau (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
