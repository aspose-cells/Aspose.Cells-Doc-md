---
title: Konvertieren Sie eine XLS-Datei in das PDF-Format
type: docs
weight: 30
url: /de/net/convert-an-xls-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) repräsentiert Dokumente unabhängig von der Software, Hardware und dem Betriebssystem, die zum Erstellen dieser Dokumente verwendet werden. Eine PDF-Datei kann geräte- und auflösungsunabhängig ein Dokument mit beliebiger Kombination aus Text, Grafiken und Bildern sein. PDF-Dateien werden häufig komprimiert, sodass sie weniger Speicherplatz beanspruchen als die Originaldatei.

Manchmal müssen Sie eine Microsoft Excel-Datei in PDF konvertieren. Dazu benötigen Sie eine schnelle, sichere, genaue und zuverlässige Lösung, mit der Sie PDF-Dokumente weltweit verteilen können. Es gibt zahlreiche Konvertierungstools, die diese Aufgabe übernehmen können. Sie müssen jedoch darauf achten, dass das Layout des ursprünglichen Excel-Dokuments in der ausgegebenen PDF-Datei erhalten bleibt. Bilder, Datenformatierung, Schriftarten, Attribute, Farben, Seiteneinrichtungseinstellungen, Textausrichtung, Rahmen, Diagramme usw. sollten genau und präzise gerendert werden.[Aspose.Cells](https://products.aspose.com/cells/net/) gewährleistet eine High-Fidelity-Konvertierung.

Dieses Dokument soll ein umfassendes Verständnis dafür vermitteln, wie ein Microsoft Excel-Dokument (mit Bildern, Diagrammen, Formatierungen usw.) in PDF konvertiert werden kann. Zu diesem Zweck wird gezeigt, wie Sie eine einfache Konsolenanwendung in Visual Studio.Net erstellen, die eine Excel-Datei mit Aspose.Cells API in PDF konvertiert. Die Konvertierung wird mit einem hohen Maß an Präzision und Genauigkeit durchgeführt.

{{% /alert %}}

## **Konvertieren von Excel in PDF**

Dieses Beispiel verwendet eine Excel-Datei (SampleInput.xlsx) als Vorlage. Die Arbeitsmappe enthält Arbeitsblätter mit Diagrammen und Bildern. Jedes Arbeitsblatt enthält verschiedene Arten von Formaten mit Schriftarten, Attributen, Farben, Schattierungseffekten und Rahmen. Auf dem ersten Arbeitsblatt befindet sich ein Säulendiagramm und auf dem letzten ein Bild.

### **Die Excel-Vorlagendatei**

Die Vorlagendatei enthält drei Arbeitsblätter, darunter Diagramme und Bilder als Medien. Das erste Arbeitsblatt hat Diagramme und das letzte Arbeitsblatt hat ein Bild, wie unten in den Screenshots gezeigt.

|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
|:- |:- |
| Das erste Arbeitsblatt**(Verkaufsprognose)**| Das zweite Arbeitsblatt**(Verkaufsbericht)**|
|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| Das dritte Arbeitsblatt**(Dateneingabe)**| Das letzte Arbeitsblatt**(Bild)**|

### **Umwandlungsprozess**

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
 1. Laden Sie Aspose.Cells for .NET herunter.
 1. Installieren Sie es auf Ihrem Entwicklungscomputer.
1. Erstellen Sie ein Projekt und fügen Sie Referenzen hinzu:
 1. Starten Sie Visual Studio.Net.
 1. Erstellen Sie eine neue Konsolenanwendung.
 1. Fügen Sie einen Verweis auf …\Programme\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu
1. Fügen Sie dem Projekt den Konvertierungscode hinzu:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, Workbook.CalculateFormula() direkt vor dem Rendern der Tabelle in PDF aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die richtigen Werte im PDF wiedergegeben werden.

{{% /alert %}}

### **Ergebnis**

Wenn der obige Code ausgeführt wurde, wird eine PDF-Datei im Ordner Dateien in Ihrem Anwendungsverzeichnis erstellt.
Die folgenden Screenshots zeigen die PDF-Seiten. Beachten Sie, dass Kopf- und Fußzeilen auch in der ausgegebenen PDF-Datei erhalten bleiben.

|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Converted2.png)|
|:- |:- |
| Das erste Arbeitsblatt**(Verkaufsprognose)**| Das zweite Arbeitsblatt**(Verkaufsbericht)**|
|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo: Bild_alt_Text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| Das dritte Arbeitsblatt**(Dateneingabe)**| Das letzte Arbeitsblatt**(Bild)**|
