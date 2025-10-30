---
title: Hücrenin Zengin Metin Kısımlarına Erişim ve Güncelleme
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Rich Text Bölümlerine Erişme ve Güncelleme Yöntemlerini Aspose.Cells for Node.js via C++ API si ile öğrenin.
keywords: Hücrenin zengin metin bölümlerine erişme ve güncelleme, Hücrenin zengin metnini alma, Hücrenin zengin metnini düzenleme, Hücrenin zengin metnine erişme, Hücrenin zengin metnini güncelleme, Hücrenin zengin metnini değiştirme
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++, hücrenin rich text parçasına erişmenize ve güncellemenize izin verir. Bu amaçla, [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) ve [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) metodlarını kullanabilirsiniz. Bu metodlar, font adı, font rengi, kalınlık gibi çeşitli font özelliklerine erişmek ve güncellemek için kullanabileceğiniz [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) nesne dizisini döndürür ve kabul eder.

{{% /alert %}}

## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**

Aşağıdaki kod, sağlanan bağlantıdan indirebileceğiniz [kaynak excel dosyası](5112369.xlsx) kullanarak [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) ve [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) metodlarının kullanımını gösterir. Kaynak excel dosyasındaki A1 hücresinde rich text vardır. 3 bölümü vardır ve her bölüm farklı bir fonta sahiptir. Aşağıdaki kod parçacığı bu bölümlere erişir ve ilk kısmı yeni bir font ismiyle günceller. Son olarak, çalışma kitabını [çıkış excel dosyası](5112366.xlsx) olarak kaydeder. Açtığınızda, ilk bölümdeki yazı fontunun **"Arial"** olarak değiştirildiğini göreceksiniz.

### Hücrenin Rich Text bölümlerine erişim ve güncelleme için Node.js kodu

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

{{< app/cells/assistant language="nodejs-cpp" >}}
