---
title: Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken
type: docs
weight: 120
url: /sv/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Detta ämne visar hur du Autofitar kolumner och rader medan du laddar HTML i Arbetsbok med hjälp av Aspose.Cells för Python via NET.
keywords: Autofit kolumner och rader medan du laddar HTML i Arbetsbok, Autofit kolumner och rader för laddning av HTML.
---

## **Möjliga användningsscenario**

Du kan autofita kolumner och rader medan du laddar in din HTML-fil i Arbetsbokobjektet. Ställ in egenskapen [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) till **true** för detta ändamål.

## **Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken**

Följande exempelkod läser först in exemplet HTML i Arbetsboken utan några laddningsalternativ och sparar den i XLSX-format. Sedan laddar den igen exemplet HTML i Arbetsboken men denna gång, laddar HTML efter att ha ställt in egenskapen [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) till **true** och sparar den i XLSX-format. Vänligen ladda ner båda de resulterande excelfilerna dvs. [Resultat Excel-fil utan AutofitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och [Resultat Excel-fil med AutofitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Följande skärmbild visar effekten av [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) egenskapen på båda utdata-excelfilerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

