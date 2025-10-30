---
title: C++ kullanarak araç ipucu ile Excel yi HTML ye dönüştürme
linktitle: Excel i HTML e dönüştür ve açıklama metni ekleyin
type: docs
weight: 200
url: /tr/go-cpp/convert-excel-to-html-with-tooltip/
description: Aspose.Cells kullanarak C++ ile araç ipucu ekleyerek Excel yi HTML ye dönüştürme.
---

## **Excel'i HTML'e dönüştür ve açıklama metni ekleyin**

Oluşturulan HTML'de metin kesildiği durumlar olabilir ve üzerine geldiğinizde tam metni araç ipucu olarak göstermek isteyebilirsiniz. Aspose.Cells bu durumu [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) özelliği ile destekler. [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) özelliğini **true** olarak ayarlamak, tam metni araç ipucu olarak ekler.

Aşağıdaki resim, oluşturulan HTML dosyasındaki açıklama metnini göstermektedir.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Aşağıdaki kod örneği, [kaynak excel dosyasını](98107416.xlsx) yükler ve [çıktı HTML dosyasını](98107417.zip) araç ipucu ile oluşturur.

Örnek Kod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
