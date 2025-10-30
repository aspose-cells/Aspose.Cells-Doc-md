---
title: Få varningar för fontsubstitution vid rendering av Excel fil med Golang via C++
linktitle: Få varningar för fontersättning
type: docs
weight: 230
url: /sv/go-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Lär dig hur du får varningar för fontsubstitution när du renderar Excel filer till PDF med Aspose.Cells med Golang via C++.
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsForFontSubstitutionWhileRenderingExcelFile.go" >}}
## **Output**
Efter att ha konverterat käll-Excel-filen till PDF kommer varningarna att skrivas ut till debuggkonsolen på detta sätt:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att anropa `Workbook.CalculateFormula`-metoden precis innan du renderar kalkylbladet till PDF-format. Detta säkerställer att de formelberoende värdena omräknas och att de rätta värdena visas i PDF:en.

{{% /alert %}}
