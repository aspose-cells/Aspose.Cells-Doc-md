---
title: Ein Excel Diagramm in ein Bild umwandeln
type: docs
weight: 20
url: /de/python-net/convert-an-excel-chart-to-image/
description: Konvertieren Sie ein Excel Diagramm in ein Bild mithilfe von Aspose.Cells für Python via .NET API.
keywords: Python Konvertieren Sie ein Excel Diagramm in ein Bild, Exportieren Sie ein Excel Diagramm in ein Bild in Python via NET, Python Speichern Sie ein Excel Diagramm in ein Bild.
---

{{% alert color="primary" %}}

Diagramme sind optisch ansprechend und erleichtern es den Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen. Anstelle von Spalten von Arbeitsblattnummern zu analysieren, zeigt ein Diagramm auf einen Blick, ob die Verkäufe sinken oder steigen oder wie die tatsächlichen Verkäufe im Vergleich zu den prognostizierten Verkäufen stehen. Menschen werden häufig gebeten, statistische und graphische Informationen in einem leicht verständlichen und leicht zu pflegenden Format zu präsentieren. Ein Bild hilft.

Manchmal werden Diagramme in einer Anwendung oder auf Webseiten benötigt. Oder sie werden für ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder eine andere Anwendung benötigt. In jedem Fall möchten Sie das Diagramm als Bild rendern, damit Sie es anderswo verwenden können.

{{% /alert %}}

## **Das Umwandeln von Diagrammen in Bilder**

In den hier gezeigten Beispielen werden ein Tortendiagramm und ein Säulendiagramm in Bilder umgewandelt.

### **Umwandeln eines Tortendiagramms in eine Bilddatei**

Erstellen Sie zunächst ein Kreisdiagramm in Microsoft Excel und wandeln Sie es dann mithilfe von Aspose.Cells für Python via .NET in eine Bilddatei um. Der Code in diesem Beispiel erstellt ein EMF-Bild basierend auf dem Kreisdiagramm in der Vorlage der Microsoft Excel-Datei.

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

Wir hosten unsere Python-Pakete in PyPi-Repositorys.

Installieren Sie Aspose.Cells für Python aus pypi. Verwenden Sie den Befehl: $ pip install aspose-cells-python.

Und Sie können auch den schrittweisen Anweisungen folgen, wie Sie "Aspose.Cells für Python via .NET" in Ihre Entwicklerumgebung installieren.
1. Laden Sie Aspose.Cells für Python via .NET herunter und installieren Sie es:
   1. Installieren Sie Aspose.Cells für Python via .NET von [pypi](https://pypi.org/project/aspose-cells-python/) mit dem Befehl: $ pip install aspose-cells-python.
   1. Sie können auch den [schrittweisen Anweisungen](https://docs.aspose.com/cells/python-net/getting-started/) folgen, wie Sie "Aspose.Cells für Python via .NET" in Ihre Entwicklerumgebung installieren.

Alle [Aspose](http://www.aspose.com/) Komponenten arbeiten im Evaluierungsmodus, wenn sie zuerst installiert werden. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in Ausgabedokumente ein.

1. Ein Projekt erstellen:
   1. Starten Sie Visual Studio.
   1. Fügen Sie Ihrem Python-Projekt einen Bibliotheksverweis hinzu (importieren Sie die Bibliothek).
   1. Schreiben Sie den Code, der das Diagramm findet und konvertiert. Unten ist der vom Komponenten verwendete Code, um die Aufgabe zu erledigen. Sehr wenige Zeilen Code werden verwendet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingPieChartToImageFile-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ConvertingColumnChartToImage-1.py" >}}
