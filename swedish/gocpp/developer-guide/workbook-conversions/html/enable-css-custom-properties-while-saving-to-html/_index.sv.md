---
title: Aktivera CSS Custom Properties medan du sparar till HTML med Golang via C++
linktitle: Aktivera CSS Anpassade Egenskaper under sparande till HTML
type: docs
weight: 320
url: /sv/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: Lär dig hur du aktiverar CSS anpassade egenskaper när du sparar Excel filer till HTML med Aspose.Cells for C++. Förbättra prestanda genom att minska redundanta bilddata.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, i scenariot att det finns flera förekomster av en base64-bild, behöver bilddata endast sparas en gång tack vare en anpassad egenskap, vilket kan förbättra prestandan hos den genererade HTML-filen. Använd [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/)-egenskapen och ställ in den till **true** när du sparar till HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Aktivera CSS Anpassade Egenskaper under sparande till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/)-egenskapen. Skärmbilden visar effekten av denna egenskap när den inte är inställd på **true**. Ladda ner [dokumentnamnet Excel-fil](50528260.xlsx) som används i detta exempel och den [genererade HTML-filen](50528261.zip) för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}
