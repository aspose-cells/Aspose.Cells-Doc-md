---
title: Warnungen beim Laden der Excel Datei mit C++ erhalten
linktitle: Warnungen beim Laden einer Excel Datei erhalten
type: docs
weight: 110
url: /de/cpp/get-warnings-while-loading-excel-file/
description: Erfahren Sie, wie Sie Warnungen beim Laden von Excel Dateien mit Aspose.Cells for C++ erkennen und behandeln.
---

## **Mögliche Verwendungsszenarien**

Manchmal versucht der Benutzer, eine Arbeitsmappe zu laden, die einigermaßen beschädigt, aber dennoch ladbar ist. In solchen Fällen gibt Aspose.Cells Warnungen beim Laden der Arbeitsmappe aus. Sie können diese Warnungen abfangen, indem Sie die [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/)-Schnittstelle implementieren und die [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/)-Eigenschaft setzen.

## **Warnungen beim Laden von Excel-Dateien erhalten**

Der folgende Beispielcode erklärt, wie man Warnungen beim Laden einer Excel-Datei erhält. Der Code lädt die [Beispieldatei Excel](sampleDuplicateDefinedName.xlsx), die beim Laden eine [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/)-Warnung auslöst. Diese Warnung wird dann durch die [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/)-Methode abgefangen, die die Warnmeldungen in der Konsole ausgibt. Anschließend speichert der Code die Arbeitsmappe als [Ausgabedatei Excel](outputDuplicateDefinedName.xlsx). Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen, wird diese Warnung ebenfalls angezeigt, wie im untenstehenden Screenshot. Bitte überprüfen Sie auch die Konsolenausgabe des unten angegebenen Codes für ein besseres Verständnis.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Codes bei Ausführung mit der bereitgestellten [Beispiel-Excel-Datei](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
