---
title: Spara arbetsbok till strikt öppet XML kalkylbladsformat
type: docs
weight: 150
url: /sv/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET låter dig spara arbetsboken i *Strict Open XML Spreadsheet* format. För det ändamålet tillhandahåller den egenskapen [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance). Om du ställer in dess värde till [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) kommer den utgående Excel-filen att sparas i Strict Open XML Spreadsheet-format.

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**

Följande exempelkod skapar en arbetsbok och ställer in värdet för [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) egenskapen som [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance)och sparar den som [utdata Excel-fil](67338272.xlsx). Om du öppnar utdata Excel-filen i Microsoft Excel och öppnar dialogrutan Spara som..., kommer du att se dess format som *Strikt Öppet XML Kalkylblad*, vilket visas på denna skärmbild.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

{{< app/cells/assistant language="python-net" >}}
