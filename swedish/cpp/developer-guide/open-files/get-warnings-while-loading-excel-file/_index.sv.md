---
title: Få varningar vid laddning av Excel fil med C++
linktitle: Få varningar när Excel filen laddas
type: docs
weight: 110
url: /sv/cpp/get-warnings-while-loading-excel-file/
description: Lär dig hur du fångar och hanterar varningar vid laddning av Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland försöker användaren ladda en arbetsbok som är något korrupt men fortfarande kan laddas. I sådana fall ger Aspose.Cells varningar vid inläsning av arbetsboken. Du kan fånga dessa varningar genom att implementera gränssnittet [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) och ställa in egenskapen [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/).

## **Få varningar vid inläsning av Excel-fil**

Följande exempel förklarar hur man får varningar vid inläsning av en Excel-fil. Koden laddar den [exempel-Excel-filen](sampleDuplicateDefinedName.xlsx), vilken ger en [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) varning vid inläsning. Denna varning fångas sedan av metoden [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/), som skriver ut varningsmeddelandena i konsolen. Koden sparar sedan arbetsboken som en [utgångs Excel-fil](outputDuplicateDefinedName.xlsx). Om du öppnar den exempel-Excel-fil i Microsoft Excel visas denna varning också, som visas i skärmslädret nedan. Kontrollera även kodens konsolutgång nedan för ytterligare förståelse.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Exempelkod**

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

## **Konsoloutput**

Här är konsolens utdata för ovanstående kod när den körs med den medföljande [exempelfilen](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
