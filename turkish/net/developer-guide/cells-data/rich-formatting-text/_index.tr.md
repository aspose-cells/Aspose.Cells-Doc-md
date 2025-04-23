---
title: Hücrenin Zengin Metin Kısımlarına Erişim ve Güncelleme
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Hücrenin zengin metin bölümlerine erişme ve güncelleme ve Aspose.Cells for .NET API si üzerinden nasıl yapıldığını öğrenin.
keywords: Hücrenin zengin metin bölümlerine erişme ve güncelleme, Hücrenin zengin metnini alma, Hücrenin zengin metnini düzenleme, Hücrenin zengin metnine erişme, Hücrenin zengin metnini güncelleme, Hücrenin zengin metnini değiştirme
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin zengin metin bölümlerine erişmenize ve güncellemenize izin verir. Bu amaçla, [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) ve [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemlerini kullanabilirsiniz. Bu yöntemler, font adı, font rengi, kalın olma gibi çeşitli özelliklere erişmek ve bunları güncellemek için kullanabileceğiniz [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) nesnesi dizisini döndürecek ve kabul edecektir.

{{% /alert %}}

## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**

Aşağıdaki kod, [kaynak excel dosyası](5112369.xlsx) kullanarak [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) ve [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemlerinin kullanımını göstermektedir. Kaynak excel dosyasında hücre A1'de zengin metin bulunmaktadır. 3 bölümü vardır ve her bölümün farklı bir fontu bulunmaktadır. Aşağıdaki kod parçacığı, bu bölümlere erişir ve ilk bölümü yeni bir font adı ile günceller. Son olarak, workbook'u [çıktı excel dosyası](5112366.xlsx) olarak kaydeder. Açtığınızda, metnin ilk bölümünün fontunun **"Arial"** olarak değiştiğini göreceksiniz.

### Hücrenin Zengin Metin Kısımlarına Erişme ve Güncelleme için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

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

{{< app/cells/assistant language="csharp" >}}
