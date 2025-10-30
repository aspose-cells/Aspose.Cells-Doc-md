---
title: Hücrenin Zengin Metin Kısımlarına Erişim ve Güncelleme
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for Python via .NET API si aracılığıyla Hücrenin Zengin Metin Kısımlarına Erişmeyi ve Güncellemeyi Nasıl Öğrenirsiniz.
keywords: Python Excel Kütüphanesi, Python Hücrenin Zengin Metin Kısımlarına Erişme ve Güncelleme, Python Zengin Metin Alma, Python Hücresinin Zengin Metnini Düzenleme, Python Hücrenin Zengin Metnine Erişme, Python Zengin Metin Kısmını Güncelleme, Python Hücrenin Zengin Metnini Değiştirme.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, hücrenin zengin metin kısımlarına erişmenizi ve güncellemenizi sağlar. Bu amaçla [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) ve [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) yöntemlerini kullanabilirsiniz. Bu yöntemler, font adı, font rengi, kalınlık vb. gibi fontun çeşitli özelliklerine erişmek ve bunları güncellemek için kullanabileceğiniz [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) nesneleri dizisini döndürecek ve kabul edecektir.

{{% /alert %}}

## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**

Aşağıdaki kod, [kaynak excel dosyası](5112369.xlsx) üzerinde [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) ve [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) yöntemlerinin kullanımını gösterir. Kaynak excel dosyasında bir hücrede zengin metin bulunmaktadır. 3 bölümü bulunmakta ve her bir bölüm farklı bir yazı tipine sahiptir. Aşağıdaki kod parçası, bu bölümlere erişir ve ilk bölümü yeni bir yazı tipiyle günceller. Son olarak, çalışma kitabını [çıktı excel dosyası](5112366.xlsx) olarak kaydeder. Açtığınızda, metnin ilk bölümünün yazı tipinin **"Arial"** olarak değişmiş olduğunu göreceksiniz.

### Hücrenin Zengin Metin Kısımlarına Erişme ve Güncelleme için C# kodu

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

### Örnek kod tarafından oluşturulan konsol çıktısı

Yukarıdaki örnek kodun [kaynak excel dosyası](5112369.xlsx) kullanılarak oluşturulan konsol çıktısı aşağıda verilmiştir.

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
