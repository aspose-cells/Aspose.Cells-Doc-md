---
title: Başlık ve Altbilgileri Ayarlama
type: docs
weight: 30
url: /tr/python-net/setting-headers-and-footers/
description: Bu makale, Aspose.Cells for Python via .NET API kullanarak Excel çalışma sayfalarının üst ve altbilgisinde görsel eklemenin programatik yolunu açıklamaktadır.
keywords: Python Excel Kütüphanesi, Python ile Excel üstbilgi ve altbilgiye görsel ekleme, Python kullanarak Excel üstbilgi ve altbilgi komutlarını ayarlama.
---

{{% alert color="primary" %}}

Başlık ve altbilgiler, üst kenar boşluğunun altında veya alt kenar boşluğunun üstünde gösterilen metin satırlarıdır. Çalışma sayfalarına da başlık ve altbilgi eklemek mümkündür. Başlıklar ve altbilgiler, sayfa numarası, yazar adı, konu adı veya tarih ve saat gibi yararlı bilgileri göstermek için kullanılabilir. Başlıklar ve altbilgiler, sayfa düzeni ayarları kullanılarak yönetilir.

{{% /alert %}}

## **Başlık ve Altbilgileri Ayarlama**

Aspose.Cells for Python via .NET, çalışma sayfalarına çalışma zamanı sırasında üstbilgi ve altbilgi eklemenize olanak tanır, ancak yazdırma işlemi için önceden tasarlanmış bir dosyada manuel olarak üstbilgi ve altbilgi ayarlamanız önerilir. Microsoft Excel GUI aracını kullanarak üstbilgi ve altbilgileri ayarlayabilir, böylece çaba ve geliştirme süresinden tasarruf edebilirsiniz. Aspose.Cells for Python via .NET, dosyayı içeri aktarabilir ve ayarları kaydedebilir.

Çalışma zamanı üstbilgi ve altbilgi eklemek için, Aspose.Cells for Python via .NET özel API çağrıları ve script komutları sağlar.

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

### **Başlık ve Altbilgi Ayarları Nasıl Yapılır**

 [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfı, çalışma sayfasına başlık ve altbilgi eklemek için kullanılan [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) ve [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str) adlı iki yöntem sağlar. Bu yöntemler yalnızca iki parametre alır:

- **Bölüm** – başlığın veya altbilginin yerleştirileceği bölüm. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Betik** – başlık veya altbilgi için kullanılacak betik. Bu betik, başlıkları veya altbilgileri biçimlendirmek için betik komutları içerir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **Bir Başlığa veya Alt Bilgiye Görsel Nasıl Eklersiniz**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfı, başlığa ve altbilgiye resim eklemek için kullanılan [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) ve [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes) adlı iki ek yönteme sahiptir. Bu yöntemlerle şu parametreler alınır:

- **Bölüm** – resmin yerleştirileceği başlık veya altbilgi bölümü. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Bayt dizisi** – görsel veri (ikili veri bir byte dizisinin tamponuna yazılmalıdır).

Aşağıdaki kodu çalıştırdıktan sonra dosyayı açarak, çalışma sayfasının üstbilgisini kontrol edin:

1. **Dosya** menüsünde **Sayfa Düzeni**'ni seçin. Bir iletişim kutusu görüntülenecektir.
1. **Üst Bilgi/Alt Bilgi** sekmesini seçin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
