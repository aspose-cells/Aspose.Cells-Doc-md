---
title: Få varningar för teckensnittsersättning vid rendering av Excel fil
type: docs
weight: 120
url: /sv/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

Ibland, när man renderar Microsoft Excel-filer till PDF, gör Aspose.Cells teckensnittsersättningar. Aspose.Cells tillhandahåller en funktion som låter utvecklare veta att ett visst teckensnitt har ersatts genom att avfyra en varning. Detta är en användbar funktion som kan hjälpa dig att identifiera varför Aspose.Cells renderade PDF är annorlunda än den faktiska Excel-filen och du kan sedan vidta lämpliga åtgärder. Till exempel kan du installera de saknade teckensnitten så att renderingresultaten ser likadana ut.

Om du vill få varningar för teckensnittsersättning vid rendering av en Excel-fil till PDF implementerar du IWarningCallback-gränssnittet och anger PdfSaveOptions.setWarningCallback() metoden med ditt implementerade gränssnitt.

{{% /alert %}}

Skärmdumpen nedan visar den källa Excel-fil som används i följande kod. Den har lite text i cellerna A6 och A7 i teckensnitt som inte renderas väl av Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells kommer att ersätta teckensnitten i cellerna A6 och A7 med lämpliga teckensnitt, som visas nedan.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Hämta källfilen och output-PDF**

Du kan hämta den käll-Excel-filen och output-PDF från följande länkar

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

Följande kod implementerar [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) och ställer in [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) metoden med det implementerade gränssnittet. Nu, när något teckensnitt kommer att ersättas i någon cell, kommer Aspose.Cells att avfyra en varning inuti WarningCallback.warning() metoden.

{{< highlight java >}}

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

## **Varningsutdata**

Efter att ha konverterat källfilen, utdata följande varningar till felsökningskonsolen:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Om din kalkylblad innehåller formler är det bäst att kalla Workbook.calculateFormula metoden strax före rendering av kalkylbladet till PDF-format. Genom att göra det säkerställs att formla beroende värden omberäknas och de korrekta värdena renderas i PDF. 

{{% /alert %}}
