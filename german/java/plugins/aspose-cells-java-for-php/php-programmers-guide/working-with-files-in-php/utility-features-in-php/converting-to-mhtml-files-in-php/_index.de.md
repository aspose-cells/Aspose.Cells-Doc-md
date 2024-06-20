---
title: Konvertierung in MHTML Dateien in PHP
type: docs
weight: 40
url: /de/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - Konvertierung in MHTML-Dateien**
Um ein Arbeitsblatt in eine MHTML-Datei mit Aspose.Cells for Java in PHP umzuwandeln, rufen Sie einfach die worksheet_to_mhtml() Methode des Converter-Moduls auf.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Konvertierung in MHTML-Dateien (Aspose.Cells)** von einer der unten aufgeführten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
