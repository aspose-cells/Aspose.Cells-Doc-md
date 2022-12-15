---
title: Gitternetzlinien in Php anzeigen oder ausblenden
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells – Rasterlinien anzeigen oder ausblenden**
### **Ausblenden von Gitternetzlinien**
 Arbeitsblatt ausblenden mit**Aspose.Cells Java for PHP** , Anruf**Rasterlinien ausblenden** Modul.

**PHP-Code**

{{< highlight "php" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Laufcode herunterladen**
Download**Rasterlinien ein- oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
