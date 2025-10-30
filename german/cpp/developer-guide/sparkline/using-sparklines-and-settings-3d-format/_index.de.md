---
title: Verwendung von Sparklines und Einstellungen 3D Format in C++
linktitle: Verwenden von Sparklines und Einstellungen 3D Format
type: docs
weight: 40
url: /de/cpp/using-sparklines-and-settings-3d-format/
description: Erfahren Sie, wie man Sparklines verwendet und 3D Formatierung in Excel Dateien mit Aspose.Cells in C++ anwendet.
---

## **Verwendung von Sparklines**
Microsoft Excel 2010 kann Informationen auf vielfältige Weise analysieren. Es ermöglicht Benutzern, wichtige Datentrends mit neuen Datenanalyse- und Visualisierungstools nachzuverfolgen und hervorzuheben. Sparklines sind Mini-Diagramme, die Sie innerhalb von Zellen platzieren können, um Daten und Diagramme in derselben Tabelle anzuzeigen. Wenn Sparklines richtig verwendet werden, ist die Datenanalyse schneller und präziser. Sie bieten auch einen einfachen Überblick über Informationen, vermeiden überfüllte Arbeitsblätter mit vielen belebten Diagrammen.

Aspose.Cells bietet eine API zur Manipulation von Sparklines in Tabellenkalkulationen.
### **Sparklines in Microsoft Excel**
Um Sparklines in Microsoft Excel 2010 einzufügen:

1. Wählen Sie die Zellen aus, in denen die Sparklines erscheinen sollen. Um sie leicht zu sehen, wählen Sie Zellen neben den Daten aus.
1. Klicken Sie auf **Einfügen** im Menüband und wählen Sie dann **Spalte** in der Gruppe **Sparklines** aus.
1. Wählen Sie den Bereich der Zellen im Arbeitsblatt aus oder geben Sie ihn ein, der die Quelldaten enthält. Die Diagramme werden angezeigt.

Sparklines helfen Ihnen, Trends zu erkennen, beispielsweise die Gewinn- oder Verlustbilanz für eine Softball-Liga. Sparklines können sogar die gesamte Saison jedes Teams in der Liga zusammenfassen.
### **Sparklines mit Aspose.Cells verwenden**
Entwickler können Sparklines (im Vorlage-Datei) mit der API von Aspose.Cells erstellen, löschen oder lesen. Die Klassen, die Sparklines verwalten, befinden sich im [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) Namespace, daher müssen Sie diesen Namespace importieren, bevor Sie diese Funktionen verwenden.

Durch das ​​Hinzufügen benutzerdefinierter Grafiken für einen bestimmten Datenbereich haben Entwickler die Freiheit, verschiedene Arten von Mini-Diagrammen in ausgewählten Zellbereichen hinzuzufügen.

Das folgende Beispiel zeigt die Sparklines-Funktion. Das Beispiel zeigt, wie man:

1. Eine einfache Vorlagendatei öffnen.
1. Sparklines-Informationen für ein Arbeitsblatt lesen.
1. Neue Sparklines für einen bestimmten Datenbereich zu einem Zellbereich hinzufügen.
1. Speichern Sie die Excel-Datei auf der Festplatte.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Einstellung des 3D-Formats**
Möglicherweise benötigen Sie 3D-Diagrammstile, um die Ergebnisse für Ihr Szenario zu erhalten. Aspose.Cells bietet die relevante API zur Anwendung von Microsoft Excel 2007 3D-Formatierung.

Ein vollständiges Beispiel finden Sie unten, um zu demonstrieren, wie man ein Diagramm erstellt und Microsoft Excel 2007 3D-Formatierung anwendet. Nach Ausführung des Beispielcodes wird ein Spaltendiagramm (mit 3D-Effekten) zum Arbeitsblatt hinzugefügt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
