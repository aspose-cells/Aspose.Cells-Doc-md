---
title: Mostra o nascondi le linee della griglia in Php
type: docs
weight: 10
url: /it/java/display-or-hide-gridlines-in-php/
---

## **Aspose.Cells - Mostra o Nascondi le linee della griglia**
### **Nascondere le Linee della Griglia**
Per nascondere il foglio di lavoro utilizzando **Aspose.Cells Java per PHP**, chiamare il modulo **displayhidegridlines**.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Mostra o Nascondi le linee della griglia (Aspose.Cells)** da uno dei siti di codice sociale di seguito elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
