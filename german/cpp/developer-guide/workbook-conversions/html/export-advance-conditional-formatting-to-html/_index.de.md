---
title: Exportieren von DataBar, ColorScale und IconSet Bedingter Formatierung beim Excel zu HTML Konvertierung mit C++
linktitle: Bedingte Formatierung ins HTML exportieren
type: docs
weight: 30
url: /de/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Lernen, wie man DataBar, ColorScale und IconSet bedingte Formatierungen beim Konvertieren von Excel Dateien nach HTML mit Aspose.Cells for C++ exportiert.
---

{{% alert color="primary" %}} 

Sie können DataBar, ColorScale und IconSet bedingte Formatierungen beim Konvertieren Ihrer Excel-Datei in HTML exportieren. Diese Funktion wird von Microsoft Excel nur teilweise unterstützt, während Aspose.Cells for C++ sie vollständig unterstützt.

{{% /alert %}} 

## **Exportieren von DataBar, ColorScale und IconSet bedingter Formatierung beim Excel-zu-HTML-Konvertierung**
Das folgende Screenshot zeigt die [Beispiel-Excel-Datei](5115558.xlsx) mit DataBar, ColorScale und IconSet bedingter Formatierung. Sie können die [Beispiel-Excel-Datei](5115558.xlsx) über den bereitgestellten Link herunterladen.

![todo:image_alt_text](conversion_1.png)

Das folgende Screenshot zeigt die Aspose.Cells-Ausgabedatei in HTML mit DataBar, ColorScale und IconSet bedingter Formatierung. Wie Sie sehen können, sieht sie genau aus wie die [Beispiel-Excel-Datei](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Beispielcode**
Der folgende Beispielcode wandelt die Beispiel-Excel-Datei in HTML um, was nur eine normale [Excel-zu-HTML-Konvertierung](/cells/de/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml) ist.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
