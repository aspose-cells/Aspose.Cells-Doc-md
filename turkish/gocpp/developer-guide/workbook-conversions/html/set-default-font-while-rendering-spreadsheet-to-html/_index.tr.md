---
title: Varsayılan Yazı Tipini ayarlayın, Golang ve C++ kullanarak Excel dosyasını HTML ye dönüştürürken
linktitle: Elektronik tabloyu HTML e dönüştürürken varsayılan yazı tipini ayarlayın
type: docs
weight: 370
url: /tr/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Aspose.Cells for C++ kullanarak elektronik tabloyu HTML’ye dönüştürürken varsayılan yazı tipini nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, elektronik tabloyu HTML’ye dönüştürürken varsayılan yazı tipini ayarlamanıza olanak tanır. Lütfen bu amaçla [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/)'ı kullanın. Bu özellik, bir elektronik tabloda geçersiz veya mevcut olmayan yazı tiplerine sahip hücreler varsa faydalıdır. Bu hücreler, [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) özelliği ile belirtilen yazı tipinde görüntülenir.

{{% /alert %}}

## Elektronik tabloyu HTML'e dönüştürürken varsayılan yazı tipini ayarlayın

Aşağıdaki örnek kod bir çalışma kitabı oluşturur, ilk çalışma sayfasının B4 hücresine bir metin ekler ve yazı tipini bilinmeyen/bulunmayan bir yazı tipine ayarlar. Daha sonra, çalışma kitabını farklı varsayılan yazı tipi adları olarak Courier New, Arial, Times New Roman vb. ayarlayarak HTML olarak kaydeder.

Ekran görüntüsü, farklı varsayılan yazı tipi adlarını [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) özelliği aracılığıyla ayarlamanın etkisini gösterir.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Kod, [Courier New ile](5115516), [Arial ile](5115518) ve [Times New Roman ile](5115517) çıktı HTML dosyasını oluşturur.

## Örnek Kod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
