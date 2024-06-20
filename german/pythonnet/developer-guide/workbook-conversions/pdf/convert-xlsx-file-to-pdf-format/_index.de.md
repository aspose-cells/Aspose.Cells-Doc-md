---
title: XLSX Datei in PDF Format konvertieren
type: docs
weight: 30
url: /de/python-net/convert-xlsx-file-to-pdf-format/
description: Erfahren Sie, wie Sie eine XLSX Datei in das PDF Format mit der Aspose.Cells for Python via .NET API konvertieren.
keywords: Python Konvertieren Sie eine XLSX Datei in das PDF Format, Konvertieren Sie xlsx in pdf mit Python, Python xlsx in pdf, Speichern Sie xlsx in pdf in Python, Xlsx in pdf Format in Python
---

{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der Software, Hardware und dem Betriebssystem, die zur Erstellung dieser Dokumente verwendet werden. Eine PDF-Datei kann Dokumente mit einer beliebigen Kombination von Text, Grafiken und Bildern in einer geräteunabhängigen und auflösungsunabhängigen Weise darstellen. PDF-Dateien werden oft komprimiert, so dass sie weniger Speicherplatz als die Originaldatei benötigen.

Manchmal müssen Sie eine Microsoft Excel-Datei in PDF konvertieren. Dafür benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe ausführen können. Sie müssen jedoch sicherstellen, dass das Layout des ursprünglichen Excel-Dokuments in der Ausgabedatei PDF beibehalten wird. Bilder, Diagramme, Formate, Schriften, Attribute, Farben, Seiteneinrichtungseinstellungen, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise wiedergegeben werden. [Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) gewährleistet eine hochwertige Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis dafür vermitteln, wie ein Microsoft Excel-Dokument (das Bilder, Diagramme, Formatierungen usw. enthält) in ein PDF konvertiert werden kann. Zu diesem Zweck zeigt es, wie Sie eine einfache Konsolenanwendung in Visual Studio.Net erstellen, die eine Excel-Datei unter Verwendung der Aspose.Cells for Python via .NET-API in PDF konvertiert. Die Konvertierung erfolgt mit einem hohen Maß an Präzision und Genauigkeit.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

Wenn die Tabellenkalkulation Formeln enthält, ist es am besten, kurz vor dem Rendern der Tabellenkalkulation in PDF die [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)-Methode aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die korrekten Werte im PDF wiedergegeben werden.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Files im Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabe-PDF-Datei beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Das erste Arbeitsblatt **(Umsatzprognose)**|Das zweite Arbeitsblatt **(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Das dritte Arbeitsblatt **(Dateneingabe)**|Das letzte Arbeitsblatt **(Bild)**|
