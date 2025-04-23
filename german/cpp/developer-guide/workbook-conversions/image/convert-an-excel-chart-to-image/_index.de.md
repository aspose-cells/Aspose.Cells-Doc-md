---
title: Konvertieren Sie ein Excel Diagramm in ein Bild mit C++
linktitle: Ein Excel Diagramm in ein Bild umwandeln
type: docs
weight: 20
url: /de/cpp/convert-an-excel-chart-to-image/
description: Lernen Sie, wie man Excel Diagramme mit Aspose.Cells in Bilder mit C++ umwandelt.
---

{{% alert color="primary" %}}

 Diagramme sind optisch ansprechend und erleichtern es den Nutzern, Vergleiche, Muster und Trends in Daten zu erkennen. Statt Tabellenzahlen zu analysieren, zeigt ein Diagramm auf einen Blick, ob die Verkaufszahlen fallen oder steigen oder wie die tatsächlichen Verkäufe im Vergleich zu den prognostizierten Verkäufen sind. Menschen werden häufig gebeten, statistische und grafische Informationen auf eine leicht verständliche und wartbare Weise darzustellen. Ein Bild hilft dabei.

 Manchmal werden Diagramme in einer Anwendung oder auf Webseiten benötigt. Oder sie könnten für ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder eine andere Anwendung gebraucht werden. In jedem Fall möchten Sie das Diagramm als Bild rendern, um es anderswo verwenden zu können.

{{% /alert %}}

## **Das Umwandeln von Diagrammen in Bilder**

In den Beispielen hier werden ein Kreisdiagramm und ein Säulendiagramm in Bilder umgewandelt.

### **Umwandeln eines Tortendiagramms in eine Bilddatei**

Erstellen Sie zuerst ein Tortendiagramm in Microsoft Excel und wandeln Sie es dann in eine Bilddatei mit Aspose.Cells um. Der Code in diesem Beispiel erstellt ein EMF-Bild basierend auf dem Tortendiagramm in der Vorlage der Microsoft Excel-Datei.

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
    1. [Laden Sie Aspose.Cells for C++ herunter](https://downloads.aspose.com/cells/cpp).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.

Alle [Aspose](http://www.aspose.com/) Komponenten arbeiten im Evaluierungsmodus, wenn sie zuerst installiert werden. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in Ausgabedokumente ein.

1. Ein Projekt erstellen:
    1. Starten Sie Ihre C++-Entwicklungsumgebung (z.B. Visual Studio).
   1. Erstellen Sie eine neue Konsolenanwendung.
    1. Fügen Sie eine Referenz zu Aspose.Cells hinzu. Dieses Projekt verwendet Aspose.Cells, also fügen Sie eine Referenz zur Aspose.Cells-Bibliothek hinzu.
   1. Schreiben Sie den Code, der das Diagramm findet und konvertiert. Unten ist der vom Komponenten verwendete Code, um die Aufgabe zu erledigen. Sehr wenige Zeilen Code werden verwendet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
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

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
