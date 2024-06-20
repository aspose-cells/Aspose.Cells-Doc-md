---
title: Dölj eller Visa ett kalkyldokument i Php
type: docs
weight: 50
url: /sv/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - Dölj eller visa en arbetsbok**
### **Dölja ett arbetsblad**
För att dölja arbetsblad med Aspose.Cells Java for PHP, anropa **hideunhideworksheet**-modulen.

**PHP-kod**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Dölj eller visa arbetsblad (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
