---
title: Få varningar för teckensnittsersättning när du renderar Excel-fil
type: docs
weight: 120
url: /sv/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

Ibland, när du renderar Microsoft Excel-filer till PDF, ersätter Aspose.Cells teckensnitt. Aspose.Cells tillhandahåller en funktion som låter utvecklare veta att ett visst teckensnitt har ersatts med en varning. Detta är en användbar funktion som kan hjälpa dig att identifiera varför Aspose.Cells renderad PDF är annorlunda än den faktiska Excel-filen och du kan sedan vidta lämpliga åtgärder. Du kan till exempel installera de saknade typsnitten så att renderingsresultaten kan se likadana ut.

Om du vill få varningarna för teckensnittsersättning medan du renderar en Excel-fil till PDF, implementera IWarningCallback-gränssnittet och ställ in metoden PdfSaveOptions.setWarningCallback() med ditt implementerade gränssnitt.

{{% /alert %}}

Skärmdumpen nedan visar källfilen för Excel som används i följande kod. Den har en del text i cellerna A6 och A7 i teckensnitt som inte renderas bra av Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells kommer att ersätta typsnitten i cellerna A6 och A7 med lämpliga typsnitt som visas nedan.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Ladda ner källfil och utdata PDF**

Du kan ladda ner källfilen för Excel och utgången PDF från följande länkar

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

 Följande kod implementerar[**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) och ställ in[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) metod med det implementerade gränssnittet. Nu, när ett teckensnitt kommer att ersättas i en cell, kommer Aspose.Cells att avge en varning i metoden WarningCallback.warning().

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Utmatning av varningar**

Efter konvertering av källfilen matas följande varningar till felsökningskonsolen:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att anropa Workbook.calculateFormula-metoden precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
