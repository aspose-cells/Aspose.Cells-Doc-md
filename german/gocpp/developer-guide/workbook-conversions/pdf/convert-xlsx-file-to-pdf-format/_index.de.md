---
title: XLSX Datei mit Golang via C++ in PDF Format konvertieren
linktitle: XLSX Datei in PDF Format konvertieren
type: docs
weight: 30
url: /de/go-cpp/convert-xlsx-file-to-pdf-format/
description: Erfahren Sie, wie Sie Excel Dateien mit Aspose.Cells for C++ in hoher Präzision und Genauigkeit in PDF Format konvertieren.
---

{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der verwendeten Software, Hardware und dem Betriebssystem, um diese Dokumente zu erstellen. Eine PDF-Datei kann beliebige Kombinationen aus Text, Grafiken und Bildern in einer geräte- und auflösungsunabhängigen Weise enthalten. PDF-Dateien werden häufig komprimiert, sodass sie weniger Platz als die Originaldatei benötigen.

Manchmal müssen Sie eine Microsoft Excel-Datei in PDF umwandeln. Dafür benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe erfüllen können. Sie müssen jedoch sicherstellen, dass das Layout des Original-Excel-Dokuments im Ausgabedatei-PDF erhalten bleibt. Bilder, Diagramme, Formen, Datenformatierung, Schriftarten, Attribute, Farben, Seiteneinstellungen, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise dargestellt werden. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) gewährleistet eine hochpräzise Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis darüber vermitteln, wie ein Microsoft Excel-Dokument (mit Bildern, Diagrammen, Formatierungen usw.) in PDF umgewandelt werden kann. Dazu wird gezeigt, wie man eine einfache Konsolenanwendung in C++ erstellt, die eine Excel-Datei mit Aspose.Cells API in PDF umwandelt. Die Konvertierung erfolgt mit hohem Präzisions- und Genauigkeitsgrad.

{{% /alert %}}

## **Konvertierung von Excel nach PDF**

Dieses Beispiel verwendet eine Excel-Datei (SampleInput.xlsx) als Vorlage. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält verschiedene Typen von Formaten unter Verwendung von Schriftarten, Attributen, Farben, Schattierungseffekten und Rahmen. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

### **Die Vorlagen Excel-Datei**

Die Vorlage-Datei verfügt über drei Arbeitsblätter, darunter Diagramme und Bilder als Medien. Das erste Arbeitsblatt enthält Diagramme, und das letzte Arbeitsblatt ein Bild, wie in den Bildschirmaufnahmen gezeigt.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|

### **Konvertierungsprozess**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) kurz vor der Konvertierung der Tabelle in PDF aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die korrekten Werte im PDF dargestellt werden.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Files im Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabe-PDF-Datei beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|
