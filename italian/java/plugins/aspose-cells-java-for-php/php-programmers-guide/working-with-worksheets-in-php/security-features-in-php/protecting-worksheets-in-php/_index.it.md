---
title: Protezione dei fogli di lavoro in Php
type: docs
weight: 10
url: /it/java/protecting-worksheets-in-php/
---

## **Aspose.Cells - Protezione dei fogli di lavoro**
Per proteggere il foglio di lavoro utilizzando **Aspose.Cells Java per PHP**, chiamare il metodo **protect_worksheet** del modulo **protection**.

**Codice PHP**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");  

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Protezione dei fogli di lavoro (Aspose.Cells)** da uno dei siti di codice sociale di seguito indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
