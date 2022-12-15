---
title: Anteprima dell'interruzione di pagina in Php
type: docs
weight: 60
url: /it/java/page-break-preview-in-php/
---
## **Aspose.Cells - Anteprima interruzione di pagina**
 Per impostare il foglio di lavoro sull'anteprima dell'interruzione di pagina utilizzando**Aspose.Cells Giava for PHP** , semplicemente invocare**Anteprima interruzione di pagina** modulo.

**Codice PHP**

{{< highlight "php" >}}

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
Scarica**Anteprima interruzione di pagina (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
