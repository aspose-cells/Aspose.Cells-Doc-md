---
title: Konvertera till MHTML-filer i PHP
type: docs
weight: 40
url: /sv/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - Konvertering till MHTML-filer**
För att konvertera kalkylblad till MHTML-fil med Aspose.Cells för Java i PHP, anropa kalkylblad_till_mhtml()-metoden för konverteringsmodulen.

**PHP-kod**

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
## **Ladda ner Running Code**
Ladda ner**Konvertera till MHTML-filer (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
