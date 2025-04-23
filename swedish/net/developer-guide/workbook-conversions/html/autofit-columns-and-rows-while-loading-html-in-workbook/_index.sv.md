---
title: Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken
type: docs
weight: 120
url: /sv/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Möjliga användningsscenario**

Du kan autofita kolumner och rader medan du laddar in din HTML-fil i Arbetsbokobjektet. Ställ in egenskapen [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) till **true** för detta ändamål.

## **Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken**

Följande exempelkod läser först in exemplet HTML i Arbetsboken utan några laddningsalternativ och sparar den i XLSX-format. Sedan laddar den igen exemplet HTML i Arbetsboken men denna gång, laddar HTML efter att ha ställt in egenskapen [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) till **true** och sparar den i XLSX-format. Vänligen ladda ner båda de resulterande excelfilerna dvs. [Resultat Excel-fil utan AutofitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och [Resultat Excel-fil med AutofitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Följande skärmbild visar effekten av [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) egenskapen på båda utdata-excelfilerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
