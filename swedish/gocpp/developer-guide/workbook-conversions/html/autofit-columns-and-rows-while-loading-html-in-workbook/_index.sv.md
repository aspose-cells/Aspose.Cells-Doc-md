---
title: Automatisk justering av kolumner och rader när HTML laddas i arbetsbok med Golang via C++
linktitle: Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken
type: docs
weight: 120
url: /sv/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Lär dig hur man autofit kolumner och rader när du laddar HTML i en arbetsbok med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan autofita kolumner och rader medan du laddar in din HTML-fil i Arbetsbokobjektet. Ställ in egenskapen [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) till **true** för detta ändamål.

## **Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken**

Följande exempelkod läser först in exemplet HTML i Arbetsboken utan några laddningsalternativ och sparar den i XLSX-format. Sedan laddar den igen exemplet HTML i Arbetsboken men denna gång, laddar HTML efter att ha ställt in egenskapen [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) till **true** och sparar den i XLSX-format. Vänligen ladda ner båda de resulterande excelfilerna dvs. [Resultat Excel-fil utan AutofitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) och [Resultat Excel-fil med AutofitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Följande skärmbild visar effekten av [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) egenskapen på båda utdata-excelfilerna.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}
