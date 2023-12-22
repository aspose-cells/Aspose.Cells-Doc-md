---
title: Kontrollera Custom Number Format när du ställer in Style.Custom Property
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylarksfiler, som stöder kontroll av anpassade talformat vid styling. Den här artikeln visar hur du använder Aspose.Cells-biblioteket för att kontrollera anpassade nummerformat för att säkerställa att stilen är korrekt.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /sv/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Möjliga användningsscenarier**

 Om du tilldelar ogiltigt anpassat nummerformat till[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) egenskap, då kommer Aspose.Cells inte att ge något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ in[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) egendom till *sant**.

##  **Kontrollera Custom Number Format när du ställer in Style.Custom-egenskapen**

 Följande exempelkod tilldelar ett ogiltigt anpassat nummerformat till[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) fast egendom. Sedan har vi redan satt[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) egenskapen till *true**, därför ger den undantag t.ex. Ogiltigt talformat. Läs kommentarerna i koden för mer hjälp.

##  **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
