---
title: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylbladsfiler, vilket stöder kontroll av anpassade nummers formateringar vid formatering. Denna artikel visar hur du använder Aspose.Cells biblioteket för att kontrollera anpassade nummers formateringar för att säkerställa att formateringen är korrekt.
keywords: Aspose.Cells, Python bibliotek, kalkylblad, formatering, anpassad nummers formatering, kontroll, validering
type: docs
weight: 170
url: /sv/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ett ogiltigt anpassat nummerformat till [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)-egenskapen, kastar inte Aspose.Cells något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ då in [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/)-egenskapen till **true**.

## **Kontrollera anpassad nummerformatering vid inställning av Style.Custom-egenskap**

Följande kodprov tilldelar ett ogiltigt anpassat nummerformat till [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)-egenskapen. Eftersom vi redan har ställt in [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/)-egenskapen till **true**, kastar det därför ett undantag, t.ex. Ogiltigt nummerformat. Läs kommentarerna i koden för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

