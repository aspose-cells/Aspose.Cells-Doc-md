---
title: Conversione in file MHTML in PHP
type: docs
weight: 40
url: /it/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - Conversione in file MHTML**
Per convertire il foglio di lavoro nel file MHTML utilizzando Aspose.Cells for Java in PHP, è sufficiente richiamare il foglio di lavoro_a_mhtml() del modulo Converter.

**Codice PHP**

{{< highlight "php" >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Conversione in file MHTML (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
