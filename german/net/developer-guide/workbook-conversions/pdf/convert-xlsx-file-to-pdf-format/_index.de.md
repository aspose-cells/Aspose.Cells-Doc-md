---
title: XLSX Datei in PDF Format konvertieren
type: docs
weight: 30
url: /de/net/convert-xlsx-file-to-pdf-format/
---

{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der Software, Hardware und dem Betriebssystem, die zur Erstellung dieser Dokumente verwendet werden. Eine PDF-Datei kann Dokumente mit einer beliebigen Kombination von Text, Grafiken und Bildern in einer geräteunabhängigen und auflösungsunabhängigen Weise darstellen. PDF-Dateien werden oft komprimiert, so dass sie weniger Speicherplatz als die Originaldatei benötigen.

Manchmal müssen Sie eine Microsoft Excel-Datei in ein PDF konvertieren. Dafür benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, die es Ihnen ermöglicht, PDF-Dokumente weltweit zu verbreiten. Es gibt zahlreiche Konvertierungswerkzeuge, die diese Aufgabe ausführen können. Aber Sie müssen sicherstellen, dass das Layout des ursprünglichen Excel-Dokuments in der Ausgabepdf-Datei erhalten bleibt. Bilder, Diagramme, Formate, Schriftarten, Attribute, Farben, Seiteneinrichtungseinstellungen, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise gerendert werden. [Aspose.Cells](https://products.aspose.com/cells/net/) sorgt für eine hochwertige Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis dafür vermitteln, wie eine Microsoft Excel-Datei (mit Bildern, Diagrammen, Formatierungen usw.) in PDF konvertiert werden kann. Zu diesem Zweck zeigt es, wie man eine einfache Konsolenanwendung in Visual Studio.Net erstellt, die mithilfe der Aspose.Cells-API eine Excel-Datei in PDF konvertiert. Die Konvertierung wird mit hoher Genauigkeit und Präzision durchgeführt.

{{% /alert %}}

## **Konvertierung von Excel nach PDF**

In diesem Beispiel wird eine Excel-Datei (SampleInput.xlsx) als Vorlage verwendet. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält unterschiedliche Arten von Formaten, die Schriftarten, Attribute, Farben, Schattierungseffekte und Rahmen verwenden. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

### **Die Vorlagen Excel-Datei**

Die Vorlagendatei hat drei Arbeitsblätter, darunter Diagramme und ein Bild als Media. Das erste Arbeitsblatt enthält Diagramme und das letzte Arbeitsblatt ein Bild, wie unten in den Screenshots zu sehen ist.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|

### **Konvertierungsprozess**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, kurz vor dem Rendern der Tabelle in PDF die Methode [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Files im Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabe-PDF-Datei beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|
{{< app/cells/assistant language="csharp" >}}
