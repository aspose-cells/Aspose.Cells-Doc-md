---
title: Einfrieren von Fenstern in Php
type: docs
weight: 40
url: /de/java/freeze-panes-in-php/
---
## **Aspose.Cells - Fenster einfrieren**
 So frieren Sie Fenster im Tabellenkalkulationsdokument ein**Aspose.Cells Java for PHP** , einfach aufrufen**FreezePanes** Modul.

**PHP-Code**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Fenster einfrieren (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
