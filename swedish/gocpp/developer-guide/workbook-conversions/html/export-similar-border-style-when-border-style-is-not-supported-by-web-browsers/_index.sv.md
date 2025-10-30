---
title: Exportera liknande kantstils när kantstilen inte stöds av webbläsare med Golang via C++
linktitle: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare
type: docs
weight: 70
url: /sv/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Lär dig hur man exporterar liknande kantstilar när de inte stöds av webbläsare med Aspose.Cells med Golang via C++.
---

## **Möjliga användningsscenario**

Microsoft Excel stöder vissa typer av streckade kanter som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells tas dessa kanter bort. Men Aspose.Cells kan även visa sådana kanter med [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)-egenskapen. Sätt dess värde till **true** så exporteras även de stödda kanterna till HTML-filen.

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**

Följande exempel kod laddar [exempel-Excel-filen](64716806.xlsx) som innehåller vissa stödfria kanter, som visas i följande skärmbild. Skärmbilden visar ytterligare effekten av [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)-egenskapen i [utdata-HTML](64716804.zip).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
