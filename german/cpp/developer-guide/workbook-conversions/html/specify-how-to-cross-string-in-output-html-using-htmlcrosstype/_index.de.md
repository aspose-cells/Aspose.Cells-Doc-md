---
title: Geben Sie an, wie Strings im Ausgab HTML über HtmlCrossType mit C++ quergelesen werden sollen
linktitle: Geben Sie HtmlCrossType im Ausgabe HTML an
type: docs
weight: 140
url: /de/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Lernen Sie, wie Sie den Textüberlauf in HTML Ausgaben mit Aspose.Cells for C++ und HtmlCrossType kontrollieren.
---

## **Mögliche Verwendungsszenarien**

 Wenn eine Zelle Text oder einen String enthält, der größer ist als die Breite der Zelle, läuft der Text über, wenn die nächste Zelle in der nächsten Spalte null oder leer ist. Beim Speichern Ihrer Excel-Datei als HTML können Sie diesen Überlauf steuern, indem Sie den Quertyp mit [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) festlegen. Er hat folgende Werte:

- **HtmlCrossType.Default**: Zeigen Sie es wie MS Excel an, abhängig von der nächsten Zelle. Wenn die nächste Zelle leer ist, wird der String durchgestrichen oder abgeschnitten.

- **HtmlCrossType.MSExport**: Zeigen Sie den String wie MS Excel, der HTML exportiert.

- **HtmlCrossType.Cross**: Zeigen Sie den HTML-Durchkreuzungsstring an. Die Leistung bei der Erstellung großer HTML-Dateien ist mehr als zehnmal schneller als das Setzen des Werts auf Standard oder FitToCell.

- **HtmlCrossType.FitToCell**: Nur innerhalb der Breite der Zelle anzeigen.

## **Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740732.xlsx) und speichert sie im HTML-Format, indem verschiedene [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/) angegeben werden. Bitte laden Sie die [Ausgabedateien HTML](51740734.zip) herunter, die mit diesem Code generiert wurden. Die Beispiel-Excel-Datei enthält das Bild mit rotem Rahmen, wie in diesem Screenshot gezeigt, der die Wirkung der [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)-Werte auf das Ausgabe-HTML zeigt.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
