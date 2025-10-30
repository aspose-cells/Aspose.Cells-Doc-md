---
title: Kontrollera anpassad talformat när du ställer in style.Custom egenskapen med Golang via C++
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylblad, vilket stöder att kontrollera anpassade nummerformat vid formatering. Denna artikel visar hur man använder Aspose.Cells biblioteket för att kontrollera anpassade nummerformat för att säkerställa att formateringen är korrekt.
keywords: Aspose.Cells, C++ bibliotek, kalkylblad, formatering, anpassad nummerformat, kontroll, validering
type: docs
weight: 170
url: /sv/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ett ogiltigt anpassat nummerformat till [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)-egenskapen kommer Aspose.Cells inte att ge något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ då in [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-egenskapen till **true**.

## **Kontrollera anpassad nummerformatering vid inställning av Style.Custom-egenskap**

Följande kodexempel tilldelar ett ogiltigt anpassat nummerformat till [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)-egenskapen. Eftersom vi redan har ställt in [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-egenskapen till **true**, kastar den ett undantag, t.ex. ogiltigt nummerformat. Läs kommentarerna i koden för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
