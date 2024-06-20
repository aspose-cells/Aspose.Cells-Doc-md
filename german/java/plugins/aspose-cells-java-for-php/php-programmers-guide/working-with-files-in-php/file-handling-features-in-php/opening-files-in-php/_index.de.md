---
title: Öffnen von Dateien in PHP
type: docs
weight: 10
url: /de/java/opening-files-in-php/
---

## **Aspose.Cells - Einfache Möglichkeiten zum Öffnen von Excel-Dateien**
### **Öffnen durch Pfad**
Öffnen Sie einfach eine Microsoft Excel-Datei, indem Sie auf den Dateipfad verweisen

**PHP-Code**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Öffnen durch Stream**
Manchmal wird die Excel-Datei, die Sie öffnen möchten, als Stream gespeichert. Verwenden Sie in diesem Fall eine überladene Version der Open-Methode, die das Stream-Objekt enthält, das die Excel-Datei enthält, um die Datei zu öffnen.

**PHP-Code**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Öffnen von Dateien (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
