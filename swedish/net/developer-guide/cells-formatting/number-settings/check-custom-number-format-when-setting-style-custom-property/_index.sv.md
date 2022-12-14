---
title: Kontrollera Custom Number Format när du ställer in Style.Custom Property
type: docs
weight: 170
url: /sv/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Möjliga användningsscenarier**

 Om du tilldelar ogiltigt anpassat nummerformat till[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)egenskap, då kommer Aspose.Cells inte att ge något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ in[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) egendom till**Sann**.

## **Kontrollera Custom Number Format när du ställer in Style.Custom-egenskapen**

 Följande exempelkod tilldelar ett ogiltigt anpassat nummerformat till[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) fast egendom. Sedan har vi redan satt[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) egendom till**Sann**, därför ger den undantag t.ex. Ogiltigt talformat. Läs kommentarerna i koden för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
