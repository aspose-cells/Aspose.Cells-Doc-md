---
title: Ein Excel Diagramm in ein Bild umwandeln
type: docs
weight: 20
url: /de/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

Diagramme sind optisch ansprechend und erleichtern es den Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen. Anstelle von Spalten von Arbeitsblattnummern zu analysieren, zeigt ein Diagramm auf einen Blick, ob die Verkäufe sinken oder steigen oder wie die tatsächlichen Verkäufe im Vergleich zu den prognostizierten Verkäufen stehen. Menschen werden häufig gebeten, statistische und graphische Informationen in einem leicht verständlichen und leicht zu pflegenden Format zu präsentieren. Ein Bild hilft.

Manchmal werden Diagramme in einer Anwendung oder auf Webseiten benötigt. Oder sie werden für ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder eine andere Anwendung benötigt. In jedem Fall möchten Sie das Diagramm als Bild rendern, damit Sie es anderswo verwenden können.

{{% /alert %}}

## **Das Umwandeln von Diagrammen in Bilder**

In den hier gezeigten Beispielen werden ein Tortendiagramm und ein Säulendiagramm in Bilder umgewandelt.

### **Umwandeln eines Tortendiagramms in eine Bilddatei**

Erstellen Sie zuerst ein Tortendiagramm in Microsoft Excel und wandeln Sie es dann in eine Bilddatei mit Aspose.Cells um. Der Code in diesem Beispiel erstellt ein EMF-Bild basierend auf dem Tortendiagramm in der Vorlage der Microsoft Excel-Datei.

|**Ausgabe: Bild des Tortendiagramms**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Erstellen Sie ein Tortendiagramm in Microsoft Excel :
   1. Öffnete eine neue Arbeitsmappe in Microsoft Excel.
   1. Geben Sie einige Daten in ein Arbeitsblatt ein.
   1. Erstellte ein Tortendiagramm basierend auf den Daten.
   1. Speichern Sie die Datei.

|**Die Eingabedatei.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Laden Sie Aspose.Cells for .NET herunter](https://downloads.aspose.com/cells/net).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.

Alle [Aspose](http://www.aspose.com/) Komponenten arbeiten im Evaluierungsmodus, wenn sie zuerst installiert werden. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in Ausgabedokumente ein.

1. Ein Projekt erstellen:
   1. Starten Sie Visual Studio.Net.
   1. Erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.
   1. Fügen Sie eine Referenz hinzu. Dieses Projekt verwendet Aspose.Cells, fügen Sie also eine Referenz zu Aspose.Cells hinzu, zum Beispiel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
   1. Schreiben Sie den Code, der das Diagramm findet und konvertiert. Unten ist der vom Komponenten verwendete Code, um die Aufgabe zu erledigen. Sehr wenige Zeilen Code werden verwendet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Ein Säulendiagramm in eine Bilddatei konvertieren**

Erstellen Sie zunächst ein Säulendiagramm in Microsoft Excel und konvertieren Sie es in eine Bilddatei, wie oben. Nach Ausführung des Beispielscodes wird eine JPEG-Datei auf Basis des Säulendiagramms in der Vorlagen-Excel-Datei erstellt.

|**Ausgabedatei: ein Säulendiagrammbild.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Erstellen Sie ein Säulendiagramm in Microsoft Excel:
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
   1. Geben Sie einige Daten in ein Arbeitsblatt ein.
   1. Erstellen Sie ein Säulendiagramm basierend auf den Daten.
   1. Speichern Sie die Datei.

|**Eingabedatei.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Richten Sie ein Projekt mit den oben beschriebenen Referenzen ein.
1. Konvertieren Sie das Diagramm dynamisch in ein Bild. Im Folgenden ist der vom Komponenten verwendete Code, um die Aufgabe zu erledigen. Der Code ist ähnlich zu dem vorherigen:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
