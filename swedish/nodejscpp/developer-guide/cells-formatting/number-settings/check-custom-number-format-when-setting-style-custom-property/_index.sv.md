---
title: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
linktitle: Kontrollera anpassad nummerformatering vid inställning av Style.Custom egenskap
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler, vilket stöder kontroll av anpassade nummerformat vid styling. Den här artikeln visar hur du använder Aspose.Cells biblioteket för att kontrollera anpassade nummerformat för att säkerställa att stilen är korrekt.
keywords: Aspose.Cells, Node.js bibliotek, kalkylblad, styling, anpassad nummerformatiering, kontroll, validering
type: docs
weight: 170
url: /sv/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ett ogiltigt anpassat nummerformat till [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) metoden, kommer Aspose.Cells for Node.js via C++ inte kasta några undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ då in [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) metoden till **true**.

## ** Kontrollera anpassat nummerformat vid inställning av Style.setCustom(string) metod**

Följande kodexempel tilldelar ett ogiltigt anpassat nummerformat till [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) metoden. Eftersom vi redan har ställt in [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) metoden till **true**, kastar den ett undantag, t.ex. Ogiltigt nummerformat. Läs kommentarerna i koden för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

