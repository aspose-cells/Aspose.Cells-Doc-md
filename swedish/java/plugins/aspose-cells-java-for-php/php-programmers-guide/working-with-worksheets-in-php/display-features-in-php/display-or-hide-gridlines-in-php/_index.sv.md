---
title: Visa eller dölj rutsnät i PHP
type: docs
weight: 10
url: /sv/java/display-or-hide-gridlines-in-php/
---

## **Aspose.Cells - Visa eller dölj rutnät**
### **Gömmer rutnätslinjer**
För att dölja arbetsblad med **Aspose.Cells Java för PHP**, anropa **displayhidegridlines** modulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Visa eller Dölj rutnät (Aspose.Cells)** från någon av de sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
