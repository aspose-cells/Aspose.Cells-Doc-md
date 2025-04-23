---
title: Spara arbetsbok till strikt öppet XML kalkylbladsformat
type: docs
weight: 150
url: /sv/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig spara arbetsboken i *Strikt Öppet XML Kalkylblad* format. För detta ändamål tillhandahåller den [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) egenskapen. Om du ställer in dess värde som [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance), kommer den resulterande Excel-filen att sparas i Strikt Öppet XML Kalkylblad format.

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**

Följande exempelkod skapar en arbetsbok och ställer in värdet för [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) egenskapen som [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)och sparar den som [utdata Excel-fil](67338272.xlsx). Om du öppnar utdata Excel-filen i Microsoft Excel och öppnar dialogrutan Spara som..., kommer du att se dess format som *Strikt Öppet XML Kalkylblad*, vilket visas på denna skärmbild.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
