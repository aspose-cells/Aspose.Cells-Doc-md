---
title: Sidbrytning i förhandsgranskning i Php
type: docs
weight: 60
url: /sv/java/page-break-preview-in-php/
---

## **Aspose.Cells - Sidbrytningsgranskning**
För att ställa in arbetsblad till sidobrytningsförhandsgranskning med **Aspose.Cells Java for PHP**, helt enkelt anropa **PageBreakPreview**-modulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Sidbrytningsgranskning (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
