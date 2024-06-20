---
title: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
description: Aspose.Cells är ett .NET bibliotek för att arbeta med kalkylbladsfiler, vilket stöder att kontrollera anpassade nummerformat vid formatering. Den här artikeln kommer att visa hur man använder Aspose.Cells biblioteket för att kontrollera anpassade nummerformat för att säkerställa att formateringen är korrekt.
keywords: Aspose.Cells, .NET bibliotek, kalkylblad, formatering av anpassade nummer, kontroll, validering
type: docs
weight: 170
url: /sv/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ett ogiltigt anpassat nummerformat till [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)-egenskapen, kastar inte Aspose.Cells något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ då in [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)-egenskapen till **true**.

## **Kontrollera anpassad nummerformatering vid inställning av Style.Custom-egenskap**

Följande kodprov tilldelar ett ogiltigt anpassat nummerformat till [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)-egenskapen. Eftersom vi redan har ställt in [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)-egenskapen till **true**, kastar det därför ett undantag, t.ex. Ogiltigt nummerformat. Läs kommentarerna i koden för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
