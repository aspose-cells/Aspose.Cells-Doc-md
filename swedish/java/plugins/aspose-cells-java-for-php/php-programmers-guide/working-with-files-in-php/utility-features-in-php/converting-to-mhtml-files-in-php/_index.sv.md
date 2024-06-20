---
title: Konvertera till MHTML filer i PHP
type: docs
weight: 40
url: /sv/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - Konvertering till MHTML-filer**
För att konvertera arbetsblad till MHTML-fil med Aspose.Cells for Java i PHP, helt enkelt anropa worksheet_to_mhtml() metoden i konverteringsmodulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ned **Konvertera till MHTML-filer (Aspose.Cells)** från någon av nedanstående sociala kodningssajter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
