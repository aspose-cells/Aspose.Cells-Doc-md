---
title: Wie man mit C++ ein dynamisches scrollendes Diagramm erstellt
linktitle: Dynamisches scrollendes Diagramm erstellen
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ ein dynamisches scrollendes Diagramm erstellen. Unser Schritt für Schritt Leitfaden zeigt, wie man glatte Datenübergänge und automatisches Scrollen in Ihrem Diagramm implementiert für eine kontinuierliche und aktualisierte Anzeige.
keywords: Aspose.Cells for C++, Dynamisches scrollendes Diagramm, Datenübergänge, sanftes Scrollen, kontinuierliche Anzeige, aktualisierte Visualisierung.
type: docs
weight: 75
url: /de/cpp/create-dynamic-scrolling-chart/
---

## **Mögliche Verwendungsszenarien**
Das dynamische Bildlaufdiagramm ist eine Art grafische Darstellung, die verwendet wird, um Daten anzuzeigen, die sich im Laufe der Zeit ändern. Es ist darauf ausgelegt, einen Echtzeit-Blick auf Daten zu bieten, der es Benutzern ermöglicht, kontinuierliche Aktualisierungen und Trends zu verfolgen. Das Diagramm aktualisiert sich kontinuierlich, wenn neue Daten hinzugefügt werden, und scrollt automatisch, um die neuesten Informationen anzuzeigen.

Dynamische Bildlaufdiagramme werden in verschiedenen Branchen wie Finanzen, Börsenanalyse, Wetterverfolgung und sozialen Medienanalysen häufig eingesetzt. Sie ermöglichen es Benutzern, Datenmuster zu visualisieren und zu analysieren und auf Echtzeitinformationen basierende fundierte Entscheidungen zu treffen.

Diese Diagramme sind normalerweise interaktiv und ermöglichen es dem Benutzer, herein- oder herauszuzoomen, durch historische Daten zu scrollen und Zeitintervalle anzupassen. Sie unterstützen oft mehrere Datenreihen, die einen umfassenden Überblick über verschiedene Metriken und ihre Korrelationen bieten.

Insgesamt sind dynamische Bildlaufdiagramme wertvolle Werkzeuge zur Überwachung und Analyse von zeitbezogenen Daten, zur Unterstützung von Echtzeit-Entscheidungsfindung und zur Verbesserung der Datenvisualisierungsfähigkeiten.

## **Verwenden Sie Aspose Cells, um ein dynamisches scrollendes Diagramm zu erstellen**
Im folgenden zeigen wir Ihnen, wie Sie mit Aspose.Cells ein dynamisches scrollendes Diagramm erstellen. Wir präsentieren den Code für das Beispiel sowie die Excel-Datei, die mit diesem Code erstellt wurde.

## **Beispielcode**
Der folgende Beispielcode generiert die [Dynamische Bildlaufdiagramm-Datei](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Anmerkungen**
In der generierten Datei können Sie auf die Bildlaufleiste zugreifen, während das Diagramm dynamisch die neuesten 10 Datensätze zählt. Dies wird mithilfe der "OFFSET"-Formel im Beispielcode durchgeführt:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Sie können versuchen, die Zahl "10" in "15" in der Zelle "Sheet1!$H$20" zu ändern, und das dynamische Diagramm wird die neuesten 15 Datensätze zählen. Jetzt haben wir erfolgreich ein dynamisches Bildlaufdiagramm mit Aspose.Cells erstellt.
