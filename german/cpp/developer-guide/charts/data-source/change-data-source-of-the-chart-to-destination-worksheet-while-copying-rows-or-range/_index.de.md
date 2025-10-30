---  
title: Ändern Sie die Datenquelle des Diagramms in das Zielarbeitsblatt beim Kopieren von Zeilen oder Bereichen mit C++  
description: Erfahren Sie, wie Sie die Datenquelle eines Diagramms beim Kopieren von Zeilen oder einem Bereich in Aspose.Cells for C++ auf ein Zielarbeitsblatt ändern. Unser Leitfaden zeigt, wie Sie den Datenbereich des Diagramms aktualisieren und mit dem Zielarbeitsblatt verknüpfen, sodass die kopierten Zeilen oder der Bereich im Diagramm genau widerspiegelt werden.  
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenquelle, Zielarbeitsblatt, Zeilen, Bereich, Kopieren, Aktualisieren, Datenbereich, Verknüpfung.  
type: docs  
weight: 440  
url: /de/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Mögliche Verwendungsszenarien**

Wenn Sie Zeilen oder Bereiche mit Diagrammen in ein neues Arbeitsblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Beispiel: Wenn die Datenquelle des Diagramms =Sheet1!$A$1:$B$4 ist, bleibt sie nach dem Kopieren in ein neues Arbeitsblatt gleich, also =Sheet1!$A$1:$B$4. Sie verweist weiterhin auf das alte Arbeitsblatt, also Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Möchten Sie, dass sie auf das neue Zielarbeitsblatt verweist, verwenden Sie bitte die [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/)-Eigenschaft und setzen diese beim Aufruf der [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/)-Methode auf **true**. Wenn Ihr Zielarbeitsblatt beispielsweise DestSheet heißt, ändert sich die Datenquelle Ihres Diagramms von =Sheet1!$A$1:$B$4 zu =DestSheet!$A$1:$B$4.

## **Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen**

Der folgende Beispielcode erläutert die Verwendung der [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/)-Eigenschaft beim Kopieren von Zeilen oder Bereichen mit Diagrammen in ein neues Arbeitsblatt. Der Code nutzt die [Beispieldatei](5113699.xlsx) und erzeugt die [Ausgabedatei](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
