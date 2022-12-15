---
title: Speichern von Dateien in PHP
type: docs
weight: 20
url: /de/java/saving-files-in-php/
---
## **Aspose.Cells – Speichern von Dateien**
### **Datei an einem Ort speichern**
 Wenn Entwickler ihre Dateien mit speichern müssen**Aspose.Cells Java for PHP** zu einem Speicherort, dann können sie einfach den Dateinamen (mit vollständigem Speicherpfad) und das gewünschte Dateiformat (mithilfe der**Dateiformattyp**Aufzählung) beim Aufrufen der**sparen**Methode von**Arbeitsmappe**Objekt.

**PHP-Code**

{{< highlight "php" >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Dateien speichern (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
