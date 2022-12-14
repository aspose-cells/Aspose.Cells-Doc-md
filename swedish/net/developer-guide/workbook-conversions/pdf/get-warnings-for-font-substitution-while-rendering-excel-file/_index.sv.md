---
title: Få varningar för teckensnittsersättning när du renderar Excel-fil
type: docs
weight: 230
url: /sv/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

Ibland, när du renderar en Microsoft Excel-fil till PDF, ersätter Aspose.Cells teckensnitt. Aspose.Cells tillhandahåller en funktion som låter utvecklare veta vilket typsnitt som har ersatts av en varning. Det här är en användbar funktion som kan hjälpa dig att identifiera varför en Aspose.Cells-renderad PDF ser annorlunda ut än den ursprungliga Microsoft Excel-filen så att du kan vidta lämpliga åtgärder. Till exempel att installera de saknade typsnitten så att renderingsresultaten ser likadana ut.

{{% /alert %}} 

För att få varningar för teckensnittsersättning när du renderar Excel-filer till PDF, implementera IWarningCallback-gränssnittet och ställ in egenskapen PdfSaveOptions.WarningCallback med ditt implementerade gränssnitt.

Skärmdumpen nedan visar en Excel-källfil som vi kommer att använda i följande kod. Den har en del text i cellerna A6 och A7 i typsnitt som inte renderas bra av Microsoft Excel.

|**Alla teckensnitt renderas inte korrekt**|
|:- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells kommer att ersätta typsnitten i cellerna A6 och A7 med lämpliga typsnitt som visas nedan.

|**Ersatta typsnitt**|
|:- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Ladda ner källfil och utdata-PDF**
Du kan ladda ner källfilen för Excel och PDF-filen från följande länkar

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Koda**
Följande kod implementerar IWarningCallback och ställer in egenskapen PdfSaveOptions.WarningCallback med det implementerade gränssnittet. Nu, närhelst ett teckensnitt kommer att ersättas i en cell, kommer Aspose.Cells att avge en varning i metoden WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Produktion**
Efter att ha konverterat källfilen i Excel till PDF matas varningarna ut till felsökningskonsolen så här:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler är det bäst att anropa Workbook.CalculateFormula-metoden precis innan du renderar kalkylarket till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
