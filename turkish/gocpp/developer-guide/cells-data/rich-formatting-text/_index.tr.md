---
title: Golang aracılığıyla C++ ile hücrenin Zengin Metin Kısımlarına Erişin ve Güncelleyin
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for C++ API kullanarak Hücrenin Zengin Metin bölümlerine Erişim ve Güncelleme nasıl yapılır öğrenin.
keywords: Hücrenin zengin metin bölümlerine erişme ve güncelleme, Hücrenin zengin metnini alma, Hücrenin zengin metnini düzenleme, Hücrenin zengin metnine erişme, Hücrenin zengin metnini güncelleme, Hücrenin zengin metnini değiştirme
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin zengin metin bölümlerine erişmenize ve güncellemenize izin verir. Bu amaçla, [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) ve [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) yöntemlerini kullanabilirsiniz. Bu yöntemler, font adı, font rengi, kalın olma gibi çeşitli özelliklere erişmek ve bunları güncellemek için kullanabileceğiniz [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) nesnesi dizisini döndürecek ve kabul edecektir.

{{% /alert %}}

## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**

Aşağıdaki kod, [kaynak excel dosyası](5112369.xlsx) kullanılarak [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) ve [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) metodlarının kullanımını gösterir. Kaynak excel dosyasında, hücre A1’de 3 bölümden oluşan ve her biri farklı bir fonta sahip zengin metin vardır. Kod bu bölümlere erişir ve ilk bölümün fontunu **"Arial"** olarak günceller. Değiştirilen çalışma kitabı [çıkış excel dosyasına](5112366.xlsx) kaydedilir.

### C++ ile zengin metin bölümlerine erişim ve güncelleme kodu

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### Örnek kod tarafından oluşturulan konsol çıktısı

İşte [kaynak excel dosyası](5112369.xlsx) kullanıldığında konsol çıktısı:

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
