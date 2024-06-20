---
title: Rasterspalten in PHP anzeigen oder ausblenden
type: docs
weight: 10
url: /de/java/display-or-hide-gridlines-in-php/
---

## **Aspose.Cells - Rasterspalten anzeigen oder ausblenden**
### **Rasterspalten ausblenden**
Um ein Arbeitsblatt unter Verwendung von **Aspose.Cells Java für PHP** auszublenden, rufen Sie das Modul **displayhidegridlines** auf.

**PHP-Code**

{{< highlight php >}}

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
## **Laufenden Code herunterladen**
Laden Sie **Anzeigen oder Ausblenden von Gitternetzlinien (Aspose.Cells)** von einer der unten aufgeführten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
