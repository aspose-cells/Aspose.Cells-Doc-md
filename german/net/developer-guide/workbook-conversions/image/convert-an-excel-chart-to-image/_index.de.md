---
title: Konvertieren Sie ein Excel-Diagramm in ein Bild
type: docs
weight: 20
url: /de/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

Diagramme sind optisch ansprechend und machen es Benutzern leicht, Vergleiche, Muster und Trends in Daten zu erkennen. Anstatt beispielsweise Spalten mit Arbeitsblattzahlen zu analysieren, zeigt ein Diagramm auf einen Blick, ob die Umsätze sinken oder steigen oder wie die tatsächlichen Umsätze im Vergleich zu den prognostizierten Umsätzen abschneiden. Menschen werden häufig gebeten, statistische und grafische Informationen auf leicht verständliche und leicht zu pflegende Weise darzustellen. Ein Bild hilft.

Manchmal werden Diagramme in einer Anwendung oder auf Webseiten benötigt. Oder es wird für ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder eine andere Anwendung benötigt. In jedem Fall möchten Sie das Diagramm als Bild rendern, damit Sie es an anderer Stelle verwenden können.

{{% /alert %}}

## **Konvertieren von Diagrammen in Bilder**

In den Beispielen hier werden ein Tortendiagramm und ein Säulendiagramm in Bilder umgewandelt.

### **Konvertieren eines Kreisdiagramms in eine Bilddatei**

Erstellen Sie zunächst ein Kreisdiagramm in Microsoft Excel und konvertieren Sie es dann in eine Bilddatei mit Aspose.Cells. Der Code in diesem Beispiel erstellt ein EMF-Bild basierend auf dem Kreisdiagramm in der Vorlage Microsoft Excel-Datei.

|**Ausgabe: Kreisdiagrammbild**|
|:- |
|![todo: Bild_alt_Text](convert-an-excel-chart-to-image_1.png)|

1. Erstellen Sie ein Kreisdiagramm in Microsoft Excel:
 1. Öffnete eine neue Arbeitsmappe in Microsoft Excel.
 1. Geben Sie einige Daten in ein Arbeitsblatt ein.
 1. Erstellt ein Tortendiagramm basierend auf den Daten.
 1. Speichern Sie die Datei.

|**Die Eingabedatei.**|
|:- |
|![todo: Bild_alt_Text](convert-an-excel-chart-to-image_2.png)|

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Herunterladen Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Installieren Sie es auf Ihrem Entwicklungscomputer.

 Alle[Aspose](http://www.aspose.com/) Komponenten arbeiten bei der Erstinstallation im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in Ausgabedokumente ein.

1. Erstellen Sie ein Projekt:
 1. Starten Sie Visual Studio.Net.
 1. Erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.
 1. Fügen Sie eine Referenz hinzu. Dieses Projekt verwendet Aspose.Cells, fügen Sie also einen Verweis auf Aspose.Cells hinzu, zum Beispiel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Schreiben Sie den Code, der das Diagramm findet und konvertiert. Unten ist der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Es werden nur sehr wenige Codezeilen verwendet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Konvertieren eines Säulendiagramms in eine Bilddatei**

Erstellen Sie zunächst ein Säulendiagramm in Microsoft Excel und konvertieren Sie es wie oben in eine Bilddatei. Nach dem Ausführen des Beispielcodes wird basierend auf dem Säulendiagramm in der Excel-Vorlagendatei eine JPEG-Datei erstellt.

|**Ausgabedatei: ein Säulendiagrammbild.**|
|:- |
|![todo: Bild_alt_Text](convert-an-excel-chart-to-image_3.png)|

1. Erstellen Sie ein Säulendiagramm in Microsoft Excel:
 1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
 1. Geben Sie einige Daten in ein Arbeitsblatt ein.
 1. Erstellen Sie basierend auf den Daten ein Säulendiagramm.
 1. Speichern Sie die Datei.

|**Eingabedatei.**|
|:- |
|![todo: Bild_alt_Text](convert-an-excel-chart-to-image_4.png)|

1. Richten Sie wie oben beschrieben ein Projekt mit Referenzen ein.
1. Konvertieren Sie das Diagramm dynamisch in ein Bild. Es folgt der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Der Code ähnelt dem vorherigen:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
