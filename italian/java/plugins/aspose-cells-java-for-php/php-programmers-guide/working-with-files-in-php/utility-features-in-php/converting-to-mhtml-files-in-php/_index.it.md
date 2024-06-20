---
title: Conversione in file MHTML in PHP
type: docs
weight: 40
url: /it/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - Conversione in file MHTML**
Per convertire il foglio di lavoro in un file MHTML usando Aspose.Cells for Java in PHP, basta invocare il metodo worksheet_to_mhtml() del modulo Converter.

**Codice PHP**

{{< highlight php >}}

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
Scarica **Conversione in file MHTML (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale sotto elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
