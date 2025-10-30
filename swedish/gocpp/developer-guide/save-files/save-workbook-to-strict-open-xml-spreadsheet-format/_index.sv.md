---
title: Spara arbetsboken i strikt Open XML Spreadsheet format med Golang via C++
linktitle: Spara arbetsbok till strikt öppet XML kalkylbladsformat
type: docs
weight: 150
url: /sv/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Lär dig hur du sparar en arbetsbok i Strict Open XML Spreadsheet format med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter att du sparar arbetsboken i *Strict Open XML Spreadsheet* format. För detta ändamål tillhandahåller det egenskapen [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/). Om du ställer in dess värde till [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), kommer den ifrågavarande Excel-filen att sparas i Strict Open XML Spreadsheet-format.

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**

Följande exempel skapar en arbetsbok och ställer in värdet av egenskapen [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) till [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) och sparar den som [utdata Excel-fil](67338272.xlsx). Om du öppnar den genererade Excel-filen i Microsoft Excel och öppnar Spara Som... dialogrutan, kommer du att se dess format som *Strict Open XML Kalkylblad* som visas i denna skärmbild.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}
