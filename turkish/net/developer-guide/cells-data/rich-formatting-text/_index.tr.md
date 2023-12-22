---
title: Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Cell ile Aspose.Cells for .NET API arasındaki Zengin Metin Bölümlerine nasıl erişeceğinizi ve bunları güncelleyeceğinizi öğrenin.
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---
{{% alert color="primary" %}}

 Aspose.Cells, hücrenin zengin metninin bölümlerine erişmenizi ve bunları güncellemenizi sağlar. Bu amaçla kullanabilirsiniz[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) Ve[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemler. Bu yöntemler geri dönecek ve diziyi kabul edecektir.[**Yazı Tipi Ayarı**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)yazı tipi adı, yazı tipi rengi, kalınlık vb. gibi yazı tipinin çeşitli özelliklerine erişmek ve bunları güncellemek için kullanabileceğiniz nesneler.

{{% /alert %}}

##  **Cell Zengin Metin Bölümlerine Erişin ve Güncelleyin**

 Aşağıdaki kod kullanımını gösterir[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) Ve[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) yöntemini kullanarak[kaynak excel dosyası](5112369.xlsx) verilen bağlantıdan indirebilirsiniz. Kaynak excel dosyasının A1 hücresinde zengin bir metin var. 3 bölümden oluşur ve her bölüm farklı bir yazı tipine sahiptir. Aşağıdaki kod parçacığı bu bölümlere erişir ve ilk bölümü yeni bir yazı tipi adıyla günceller. Son olarak çalışma kitabını şu şekilde kaydeder:[excel dosyasının çıktısını almak](5112366.xlsx). Açtığınızda metnin ilk kısmının yazı tipinin *"Arial"** olarak değiştiğini göreceksiniz.

###  Cell Zengin Metin bölümlerine erişmek ve bunları güncellemek için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Örnek kod tarafından oluşturulan konsol çıktısı

 Yukarıdaki örnek kodun konsol çıktısı şu şekildedir:[kaynak excel dosyası](5112369.xlsx).

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

