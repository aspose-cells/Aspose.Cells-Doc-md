---
title: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare
type: docs
weight: 70
url: /sv/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Möjliga användningsscenario**

Microsoft Excel stöder vissa typer av streckade ramar som inte är stödda av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells för Python via .NET tas dessa ramar bort. Dock kan Aspose.Cells för Python via .NET också stödja att visa dessa ramar med [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style)-egenskapen. Ställ in dess värde till **true** och de icke-stödda ramarna kommer att exporteras till HTML-filen.

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**

Följande exempelkod laddar [exempel Excel-filen](64716806.xlsx) som innehåller några icke-stödda ramar enligt följande skärmbild. Skärmbilden illustrerar hur [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) egenskapen påverkar den [utdata-HTML-filen](64716804.zip).

![todo:image_alt_text](1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
