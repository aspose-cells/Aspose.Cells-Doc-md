---  
title: Excel Diagramm in Bild mit Node.js über C++ konvertieren  
linktitle: Ein Excel Diagramm in ein Bild umwandeln  
type: docs  
weight: 20  
url: /de/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Erfahren Sie, wie Sie Excel Diagramme mit Aspose.Cells for Node.js via C++ in Bilder umwandeln.  
---  

{{% alert color="primary" %}}  

Diagramme sind optisch ansprechend und erleichtern es den Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen. Anstelle von Spalten von Arbeitsblattnummern zu analysieren, zeigt ein Diagramm auf einen Blick, ob die Verkäufe sinken oder steigen oder wie die tatsächlichen Verkäufe im Vergleich zu den prognostizierten Verkäufen stehen. Menschen werden häufig gebeten, statistische und graphische Informationen in einem leicht verständlichen und leicht zu pflegenden Format zu präsentieren. Ein Bild hilft.  

Manchmal werden Diagramme in Anwendungen oder Webseiten benötigt. Oder es ist für ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder eine andere Anwendung erforderlich. In jedem Fall möchten Sie das Diagramm als Bild rendern, um es anderweitig zu verwenden.  

{{% /alert %}}  

## **Das Umwandeln von Diagrammen in Bilder**  

In den Beispielen hier werden ein Kreisdiagramm und ein Säulendiagramm in Bilder umgewandelt.  

### **Umwandeln eines Tortendiagramms in eine Bilddatei**  

Erstellen Sie zuerst ein Kreisdiagramm in Microsoft Excel und konvertieren Sie es dann in eine Bilddatei mit Aspose.Cells for Node.js via C++. Der Code in diesem Beispiel erstellt ein EMF-Bild basierend auf dem Kreisdiagramm in der Vorlage Microsoft Excel-Datei.  

|**Ausgabe: Bild des Tortendiagramms**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Erstellen Sie ein Kreisdiagramm in Microsoft Excel:  
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.  
   1. Geben Sie einige Daten in ein Arbeitsblatt ein.  
   1. Erstellen Sie ein Kreisdiagramm basierend auf den Daten.  
   1. Speichern Sie die Datei.  

|**Die Eingabedatei.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Laden Sie Aspose.Cells herunter und installieren Sie es:  
   1. [Laden Sie Aspose.Cells for Node.js via C++ herunter](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.  

Alle [Aspose](http://www.aspose.com/) Komponenten arbeiten im Evaluierungsmodus, wenn sie zuerst installiert werden. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in Ausgabedokumente ein.  

1. Ein Projekt erstellen:  
   1. Starten Sie Ihre bevorzugte IDE.  
   1. Erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine Node.js-Anwendung, Sie können es jedoch mit jeder JavaScript-Laufzeitumgebung erstellen.  
   1. Fügen Sie eine Referenz hinzu. Dieses Projekt verwendet Aspose.Cells, also fügen Sie eine Referenz zu Aspose.Cells for Node.js via C++ hinzu.  
   1. Schreiben Sie den Code, der das Diagramm findet und konvertiert. Unten ist der vom Komponenten verwendete Code, um die Aufgabe zu erledigen. Sehr wenige Zeilen Code werden verwendet.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **Ein Säulendiagramm in eine Bilddatei konvertieren**  

Erstellen Sie zuerst ein Säulendiagramm in Microsoft Excel und konvertieren Sie es in eine Bilddatei, wie oben beschrieben. Nach der Ausführung des Beispielcodes wird eine JPEG-Datei basierend auf dem Säulendiagramm in der Vorlage Excel-Datei erstellt.  

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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
