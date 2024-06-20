---
title: Dateien in PHP speichern
type: docs
weight: 20
url: /de/java/saving-files-in-php/
---

## **Aspose.Cells - Dateien speichern**
### **Datei an einem Ort speichern**
Wenn Entwickler ihre Dateien unter Verwendung von **Aspose.Cells Java für PHP** an einem Speicherort speichern müssen, können sie einfach den Dateinamen (mit seinem vollständigen Speicherpfad) und das gewünschte Dateiformat (unter Verwendung der Enumeration **FileFormatType**) beim Aufrufen der **save**-Methode des **Workbook**-Objekts angeben.

**PHP-Code**

{{< highlight php >}}

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
## **Laufenden Code herunterladen**
Herunterladen von **Speichern von Dateien (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
