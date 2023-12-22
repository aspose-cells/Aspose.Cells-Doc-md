---
title: Konvertieren Sie die Datei XLSX in das Format PDF
type: docs
weight: 30
url: /de/python-net/convert-xlsx-file-to-pdf-format/
description: Erfahren Sie, wie Sie eine XLSX-Datei in das PDF-Format mit Aspose.Cells for Python via .NET API konvertieren.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

PDF (Portable Document Format) stellt Dokumente unabhängig von der Software, Hardware und dem Betriebssystem dar, die zum Erstellen dieser Dokumente verwendet wurden. Eine PDF-Datei kann geräte- und auflösungsunabhängig Dokumente mit einer beliebigen Kombination aus Text, Grafiken und Bildern sein. PDF-Dateien werden oft komprimiert, sodass sie weniger Platz beanspruchen als die Originaldatei.

 Manchmal müssen Sie eine Microsoft-Excel-Datei in PDF konvertieren. Dafür benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe übernehmen können. Sie müssen jedoch darauf achten, dass das Layout des ursprünglichen Excel-Dokuments in der Ausgabedatei PDF erhalten bleibt. Bilder, Diagramme, Formen, Datenformatierungen, Schriftarten, Attribute, Farben, Seiteneinrichtungseinstellungen, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise wiedergegeben werden.[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) sorgt für eine High-Fidelity-Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis dafür vermitteln, wie ein Microsoft-Excel-Dokument (mit Bildern, Diagrammen, Formatierungen usw.) in PDF konvertiert werden kann. Zu diesem Zweck wird gezeigt, wie eine einfache Konsolenanwendung in Visual Studio.Net erstellt wird, die konvertiert eine Excel-Datei in PDF mithilfe von Aspose.Cells for Python via .NET API. Die Konvertierung erfolgt mit einem hohen Maß an Präzision und Genauigkeit.

{{% /alert %}}

##  **Konvertieren von Excel in PDF**

In diesem Beispiel wird eine Excel-Datei (SampleInput.xlsx) als Vorlage verwendet. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält verschiedene Arten von Formaten mit Schriftarten, Attributen, Farben, Schattierungseffekten und Rahmen. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

###  **Die Excel-Vorlagendatei**

Die Vorlagendatei enthält drei Arbeitsblätter, einschließlich Diagrammen und Bildern als Medien. Das erste Arbeitsblatt enthält Diagramme und das letzte Arbeitsblatt enthält ein Bild, wie unten in den Screenshots gezeigt.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| Das erste Arbeitsblatt**(Verkaufsprognose)**| Das zweite Arbeitsblatt**(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Das dritte Arbeitsblatt**(Dateneingabe)**| Das letzte Arbeitsblatt**(Bild)**|

###  **Umwandlungsprozess**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) Methode direkt vor dem Rendern der Tabelle in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte in PDF gerendert werden.

{{% /alert %}}

###  **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine Datei PDF im Ordner „Dateien“ in Ihrem Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der Ausgabedatei PDF beibehalten werden.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| Das erste Arbeitsblatt**(Verkaufsprognose)**| Das zweite Arbeitsblatt**(Verkaufsbericht)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Das dritte Arbeitsblatt**(Dateneingabe)**| Das letzte Arbeitsblatt**(Bild)**|
