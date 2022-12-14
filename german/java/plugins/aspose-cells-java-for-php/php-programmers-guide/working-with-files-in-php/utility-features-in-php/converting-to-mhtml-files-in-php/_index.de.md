---
title: Konvertieren in MHTML-Dateien in PHP
type: docs
weight: 40
url: /de/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells – Konvertieren in MHTML-Dateien**
Um Worksheet in eine MHTML-Datei mit Aspose.Cells for Java in PHP zu konvertieren, rufen Sie einfach worksheet auf_zu_mhtml()-Methode des Converter-Moduls.

**PHP-Code**

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
## **Laufcode herunterladen**
Download**Konvertieren in MHTML-Dateien (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
