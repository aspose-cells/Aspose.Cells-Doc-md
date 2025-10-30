---
title: Få varningar för fontersättning vid rendering av Excel fil med C++
linktitle: Få varningar för fontersättning
type: docs
weight: 230
url: /sv/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Lär dig hur man får varningar för fontersättning vid rendering av Excel filer till PDF med Aspose.Cells i C++.
---

{{% alert color="primary" %}}

Ibland, när du renderar en Microsoft Excel-fil till PDF, ersätter Aspose.Cells teckensnitt. Aspose.Cells tillhandahåller en funktion som låter utvecklare veta vilket specifikt teckensnitt som har ersatts genom att utlösa en varning. Detta är en användbar funktion som kan hjälpa dig att identifiera varför en Aspose.Cells-renderad PDF ser annorlunda ut jämfört med den ursprungliga Microsoft Excel-filen, så att du kan vidta lämpliga åtgärder. Till exempel att installera de saknade teckensnitten så att renderingen ser likadan ut.

{{% /alert %}}

För att få varningar för teckensubstitution när du renderar Excel-filer till PDF, implementera `IWarningCallback`-gränssnittet och ställ in egenskapen `PdfSaveOptions.WarningCallback` med ditt implementerade gränssnitt.

Skärmbilden nedan visar en käll-Excel-fil som vi kommer att använda i följande kod. Den har lite text i cellerna A6 och A7 med teckensnitt som inte renderas korrekt av Microsoft Excel.

|**Inte alla teckensnitt renderas korrekt**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells kommer att ersätta teckensnitten i cellerna A6 och A7 med lämpliga teckensnitt, som visas nedan.

|**Ersatta teckensnitt**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Hämta källfilen och output-PDF**
Du kan ladda ner den användarstyrda Excel-filen och den genererade PDF:en från följande länkar:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Kod**
Följande kod implementerar `IWarningCallback` och ställer in egenskapen `PdfSaveOptions.WarningCallback` med den implementerade gränssnittet. Nu, när vilken teckensubstitution som helst sker i vilken cell som helst, kommer Aspose.Cells att utlösa en varning inuti `WarningCallback.Warning()`-metoden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output**
Efter att ha konverterat käll-Excel-filen till PDF kommer varningarna att skrivas ut till debuggkonsolen på detta sätt:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att anropa `Workbook.CalculateFormula`-metoden precis innan du renderar kalkylbladet till PDF-format. Detta säkerställer att de formelberoende värdena omräknas och att de rätta värdena visas i PDF:en.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
