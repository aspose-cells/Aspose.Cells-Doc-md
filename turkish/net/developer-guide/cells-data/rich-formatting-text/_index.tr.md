---
title: Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells, hücrenin zengin metin bölümlerine erişmenizi ve bunları güncellemenizi sağlar. Bu amaçla kullanabileceğiniz[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) ve[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemler. Bu yöntemler diziyi döndürür ve kabul eder.[**Yazı Tipi Ayarı**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi çeşitli yazı tipi özelliklerine erişmek ve bunları güncellemek için kullanabileceğiniz nesneler.

{{% /alert %}}

## **Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin**

 Aşağıdaki kod, kullanımını gösterir[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) ve[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemini kullanarak[kaynak excel dosyası](5112369.xlsx)verilen bağlantıdan indirebilirsiniz. Kaynak excel dosyasının A1 hücresinde zengin bir metin var. 3 bölümden oluşur ve her bölümün yazı tipi farklıdır. Aşağıdaki kod parçacığı bu bölümlere erişir ve ilk bölümü yeni bir yazı tipi adıyla günceller. Son olarak, çalışma kitabını şu şekilde kaydeder:[çıktı excel dosyası](5112366.xlsx) . Açtığınızda, metnin ilk bölümünün yazı tipinin şu şekilde değiştiğini göreceksiniz:**"Arial"**.

### C# kodu, Cell Zengin Metin bölümlerine erişmek ve bunları güncellemek için

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Örnek kod tarafından oluşturulan konsol çıktısı

 İşte yukarıdaki örnek kodun konsol çıktısı[kaynak excel dosyası](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

