---
title: Anteprima di interruzioni di pagina in Php
type: docs
weight: 60
url: /it/java/page-break-preview-in-php/
---

## **Aspose.Cells - Anteprima interruz. pagina**
Per impostare il foglio di lavoro in anteprima delle interruzioni di pagina usando **Aspose.Cells Java per PHP**, invoca semplicemente il modulo **PageBreakPreview**.

**Codice PHP**

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
## **Scarica il codice in esecuzione**
Scarica **Anteprima interruzioni di pagina (Aspose.Cells)** da uno qualsiasi dei siti di codici sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
