---
title: Mostra o nascondi le linee della griglia in Php
type: docs
weight: 10
url: /it/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells - Visualizza o nascondi griglia**
### **Nascondere le linee della griglia**
 Per nascondere il foglio di lavoro utilizzando**Aspose.Cells Java for PHP** , chiamata**displayhidegridlines** modulo.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scaricamento**Mostra o nascondi griglia (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
