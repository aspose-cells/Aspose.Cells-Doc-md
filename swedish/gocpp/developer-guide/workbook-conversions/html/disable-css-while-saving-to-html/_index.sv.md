---
title: Inaktivera CSS medan du sparar till HTML med Golang via C++
linktitle: Inaktivera CSS vid sparning till HTML
type: docs
weight: 320
url: /sv/go-cpp/disable-css-while-saving-to-html/
description: Lär dig hur du inaktiverar CSS vid sparning av Excel filer till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till en HTML som en enda sida, kommer CSS-elementen vanligtvis att vara inbäddade i HTML-filen och ligga i HEAD-sektionen. Om du bifogar denna fil som innehåll/kropp i ett email, kommer CSS-elementen att tas bort av de flesta email-klienter, vilket resulterar i felaktig rendering. Version 24.12 av Aspose.Cells introducerar ett alternativ som tillåter dig att inaktivera CSS, så att stilar kan tillämpas direkt inom HTML-elementen själva. Om du vill använda HTML som innehåll/kropp i emailet, använd [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/)-egenskapen och ställ in den på **true**.

## **Inaktivera CSS vid sparning till HTML**

Följande exempel kod visar användningen av [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/)-egenskapen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
