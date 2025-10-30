---
title: Verfolgen Sie den Umwandlungsfortschritt von Excel nach TIFF mit C++
linktitle: Konvertierungsvorgang von Excel nach TIFF verfolgen
type: docs
weight: 190
url: /de/cpp/track-conversion-progress-of-excel-to-tiff/
description: Lernen Sie, wie Sie den Fortschritt bei der Umwandlung von Excel Dateien in TIFF mit Aspose.Cells for C++ verfolgen können.
---

## **Mögliche Verwendungsszenarien**

 Das Konvertieren großer Excel-Dateien kann manchmal einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie vielleicht den Fortschritt der Dokumenten-Konvertierung anzeigen, anstatt nur einen Ladebildschirm, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Fortschritts bei der Dokumenten-Konvertierung durch die Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)-Schnittstelle bietet [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) und [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/)-Methoden, die Sie in Ihrer eigenen Klasse implementieren können. Außerdem können Sie steuern, welche Seiten gerendert werden, wie im benutzerdefinierten *TestPageSavingCallback*-Klasse demonstriert.

## **Konvertierungsvorgang von Excel nach TIFF verfolgen**

Das folgende Codebeispiel lädt die [Quelle Excel-Datei](95584311.xlsx) und zeigt den Fortschritt der Konvertierung in der Konsole durch die Verwendung der benutzerdefinierten Klasse *TestPageSavingCallback*, die das [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)-Schnittstelle implementiert. Die generierte Ausgabedatei ist zu Ihrer Referenz angehängt.

[Output File](95584312.tiff)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestTiffPageSavingCallback : public IPageSavingCallback {
public:
    void PageStartSaving(PageStartSavingArgs& args) override {
        // Implement page start saving logic here
    }

    void PageEndSaving(PageEndSavingArgs& args) override {
        // Implement page end saving logic here
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    ImageOrPrintOptions opts;
    opts.SetPageSavingCallback(new TestTiffPageSavingCallback());
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Tiff);

    WorkbookRender wr(workbook, opts);
    wr.ToImage(outDir + u"DocumentConversionProgressForTiff_out.tiff");

    std::cout << "Document converted to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Der folgende Code zeigt die *TestTiffPageSavingCallback*-benutzerdefinierte Klasse.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestTiffPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages before page index 2.
        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages after page index 8.
        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **Konsolenausgabe**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
