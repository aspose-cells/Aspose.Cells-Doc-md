---
title: Spara arbetsbok till strikt öppet XML kalkylbladsformat
type: docs
weight: 100
url: /sv/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att spara arbetsboken i formatet *Strict Open XML Spreadsheet*. För detta ändamål tillhandahåller den egenskapen [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance). Om du anger dess värde som [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO_29500_2008_STRICT), kommer den resulterande Excel-filen att sparas i *Strict Open XML Spreadsheet*-format.

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**

Följande kodexempel skapar en arbetsbok och anger värdet för egenskapen [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance) till [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO_29500_2008_STRICT) och sparar den som [utdata Excel-fil](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx). Om du öppnar utdata Excel-filen i Microsoft Excel och öppnar dialogrutan *Spara som...* kommer du att se dess format som *Strict Open XML Spreadsheet* som visas på skärmbilden.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
