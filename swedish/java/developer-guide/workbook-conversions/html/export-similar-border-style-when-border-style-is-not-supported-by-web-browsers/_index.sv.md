---
title: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare
type: docs
weight: 70
url: /sv/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Möjliga användningsscenario**

Microsoft Excel stöder vissa typer av punkterade kanter som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med hjälp av Aspose.Cells tas sådana kanter bort. Men Aspose.Cells kan också stödja att visa liknande kanter med [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) egenskapen. Ställ in dess värde som **sant** och de oaccepterade kanterna kommer också att exporteras till HTML-filen.

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**

Följande provkod laddar den [provexelfilen](64716832.xlsx) som innehåller några oaccepterade kanter enligt följande skärmbild. Skärmbilden illustrerar ytterligare effekten av [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) egenskapen i [utdata-HTML](64716831.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
{{< app/cells/assistant language="java" >}}
