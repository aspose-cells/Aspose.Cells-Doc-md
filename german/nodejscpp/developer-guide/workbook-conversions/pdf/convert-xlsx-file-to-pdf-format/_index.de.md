---
title: XLSX Datei mit Node.js via C++ in PDF Format umwandeln
linktitle: XLSX Datei in PDF Format konvertieren
type: docs
weight: 30
url: /de/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Diese Anleitung erklärt, wie eine Excel Datei (XLSX) mit Aspose.Cells for Node.js via C++ in das PDF Format konvertiert wird. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der Software, Hardware und dem Betriebssystem, die zur Erstellung dieser Dokumente verwendet werden. Eine PDF-Datei kann Dokumente mit einer beliebigen Kombination von Text, Grafiken und Bildern in einer geräteunabhängigen und auflösungsunabhängigen Weise darstellen. PDF-Dateien werden oft komprimiert, so dass sie weniger Speicherplatz als die Originaldatei benötigen.

Manchmal müssen Sie eine Microsoft Excel-Datei in PDF umwandeln. Dafür benötigen Sie eine schnelle, sichere, präzise und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe erfüllen können. Sie müssen jedoch sicherstellen, dass das Layout des Original-Excel-Dokuments im Ausgabe-PDF erhalten bleibt. Bilder, Diagramme, Formen, Datenformatierungen, Schriftarten, Attribute, Farben, Seiteneinrichtungsoptionen, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise wiedergegeben werden. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) gewährleistet eine hochpräzise Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis dafür vermitteln, wie ein Microsoft Excel-Dokument (mit Bildern, Diagrammen, Formatierungen usw.) in PDF umgewandelt werden kann. Zu diesem Zweck wird gezeigt, wie man eine einfache Konsolenanwendung in Node.js erstellt, die eine Excel-Datei mit Aspose.Cells API in PDF konvertiert. Die Konvertierung erfolgt mit hoher Präzision und Genauigkeit.

{{% /alert %}}

## **Konvertierung von Excel nach PDF**

Dieses Beispiel verwendet eine Excel-Datei (SampleInput.xlsx) als Vorlage. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält verschiedene Typen von Formaten unter Verwendung von Schriftarten, Attributen, Farben, Schattierungseffekten und Rahmen. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

### **Die Vorlagen Excel-Datei**

Die Vorlage-Datei hat drei Arbeitsblätter, darunter Diagramme und Bilder als Medien. Das erste Arbeitsblatt enthält Diagramme und das letzte ein Bild, wie in den Screenshots gezeigt.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|

### **Konvertierungsprozess**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Falls die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle in PDF aufzurufen. So werden formelabhängige Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Files im Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabe-PDF-Datei beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|
{{< app/cells/assistant language="nodejs-cpp" >}}
