---
title: Få varningar för teckensnittsersättning vid rendering av Excel fil
type: docs
weight: 230
url: /sv/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

Ibland, när du renderar en Microsoft Excel-fil till PDF, ersätter Aspose.Cells teckensnitt. Aspose.Cells tillhandahåller en funktion som låter utvecklare veta vilket specifikt teckensnitt som har ersatts genom att utlösa en varning. Detta är en användbar funktion som kan hjälpa dig att identifiera varför en Aspose.Cells-renderad PDF ser annorlunda ut jämfört med den ursprungliga Microsoft Excel-filen, så att du kan vidta lämpliga åtgärder. Till exempel att installera de saknade teckensnitten så att renderingen ser likadan ut.

{{% /alert %}} 

För att få varningar för teckensnittsersättning vid rendering av Excel-filer till PDF ska du implementera gränssnittet IWarningCallback och ange egenskapen PdfSaveOptions.WarningCallback med ditt implementerade gränssnitt.

Skärmbilden nedan visar en käll-Excel-fil som vi kommer att använda i följande kod. Den har lite text i cellerna A6 och A7 med teckensnitt som inte renderas korrekt av Microsoft Excel.

|**Inte alla teckensnitt renderas korrekt**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells kommer att ersätta teckensnitten i cellerna A6 och A7 med lämpliga teckensnitt, som visas nedan.

|**Ersatta teckensnitt**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Hämta källfilen och output-PDF**
Du kan hämta den käll-Excel-filen och output-PDF från följande länkar

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **Kod**
Följande kod implementerar gränssnittet IWarningCallback och ställer PdfSaveOptions.WarningCallback-egendomen med det implementerade gränssnittet. Nu när teckensnitt kommer att ersättas i någon cell kommer Aspose.Cells att utlösa en varning inne i WarningCallback.Warning()-metoden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Output**
Efter att ha konverterat käll-Excel-filen till PDF kommer varningarna att skrivas ut till debuggkonsolen på detta sätt:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Om din kalkylblad innehåller formler är det bäst att anropa Workbook.CalculateFormula-metoden precis innan du renderar kalkylarket till PDF-format. På så sätt säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
