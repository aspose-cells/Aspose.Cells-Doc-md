---
title: Başlık ve Altbilgileri Ayarlama
type: docs
weight: 30
url: /tr/net/setting-headers-and-footers/
description: Bu makale, C# API veya .NET Kitaplığını kullanarak betik komutlarıyla Excel çalışma sayfalarının üstbilgi ve altbilgisine resim programlı olarak nasıl ekleyeceğinizi açıklar.
keywords: excel başlık altbilgi c# da resim ekle, excel başlık altbilgi betik komutları c# ayarla
---

{{% alert color="primary" %}}

Başlık ve altbilgiler, üst kenar boşluğunun altında veya alt kenar boşluğunun üstünde gösterilen metin satırlarıdır. Çalışma sayfalarına da başlık ve altbilgi eklemek mümkündür. Başlıklar ve altbilgiler, sayfa numarası, yazar adı, konu adı veya tarih ve saat gibi yararlı bilgileri göstermek için kullanılabilir. Başlıklar ve altbilgiler, sayfa düzeni ayarları kullanılarak yönetilir.

{{% /alert %}}

## **Başlık ve Altbilgileri Ayarlama**

Aspose.Cells, çalışma sayfalarına çalışma zamanında başlıklar ve altbilgiler eklemenize olanak tanır, ancak yazdırma için önceden tasarlanmış bir dosyada başlık ve altbilgileri manuel olarak ayarlamanızı öneririz. Çaba ve geliştirme zamanı tasarrufu yapmak için Microsoft Excel'i başlık ve altbilgileri ayarlamak için bir GUI aracı olarak kullanabilirsiniz. Aspose.Cells, dosyayı içe aktarabilir ve ayarlamaları kaydedebilir.

Çalışma zamanında başlık ve altbilgiler eklemek için Aspose.Cells, özel API çağrıları ve betik komutları sağlar.

### **Betik Komutları**

Betik komutları, başlık ve altbilgi biçimlendirmesini ayarlamanıza olanak tanıyan özel komutlardır.

|**Betik Komutları**|**Açıklama**|
| :- | :- |
|&P| Geçerli sayfa numarası
|&G| Bir resim
|&N| Toplam sayfa sayısı
|&D| Geçerli tarih
|&T| Geçerli saat
|&A| Çalışma sayfası adı
|&F| Dosya adı ve yolu olmadan
|&"\<FontName>"| Yazı tipi adını temsil eder. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"| Stil ile yazı tipi adını temsil eder. Örneğin: &"Arial,Kalın"|
|&\<FontSize>| Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak, bu komuttan sonra başlığa yazdırılacak düz bir sayı izlenecekse, bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Başlık ve Altbilgileri Ayarlama**

 [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfı, çalışma sayfasına başlık ve altbilgi eklemek için kullanılan [**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) ve [**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter) adlı iki yöntem sağlar. Bu yöntemler yalnızca iki parametre alır:

- **Bölüm** – başlığın veya altbilginin yerleştirileceği bölüm. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Betik** – başlık veya altbilgi için kullanılacak betik. Bu betik, başlıkları veya altbilgileri biçimlendirmek için betik komutları içerir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Bir Resmi Başlık veya Altbilgiye Ekleyin**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfı, başlığa ve altbilgiye resim eklemek için kullanılan [**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) ve [**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture) adlı iki ek yönteme sahiptir. Bu yöntemlerle şu parametreler alınır:

- **Bölüm** – resmin yerleştirileceği başlık veya altbilgi bölümü. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Bayt dizisi** – görsel veri (ikili veri bir byte dizisinin tamponuna yazılmalıdır).

Aşağıdaki kodu çalıştırdıktan sonra dosyayı açarak, çalışma sayfasının üstbilgisini kontrol edin:

1. **Dosya** menüsünde **Sayfa Düzeni**'ni seçin. Bir iletişim kutusu görüntülenecektir.
1. **Üst Bilgi/Alt Bilgi** sekmesini seçin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
