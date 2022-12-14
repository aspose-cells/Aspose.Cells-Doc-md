---
title: Üst Bilgileri ve Alt Bilgileri Ayarlama
type: docs
weight: 30
url: /tr/net/setting-headers-and-footers/
---
{{% alert color="primary" %}}

Üstbilgiler ve altbilgiler, sırasıyla üst kenar boşluğunun altında veya alt kenar boşluğunun üzerinde görüntülenen metin satırlarıdır. Çalışma sayfalarına üstbilgi ve altbilgi eklemek de mümkündür. Üstbilgiler ve altbilgiler, sayfa numarası, yazar adı, konu adı veya tarih ve saat gibi faydalı bilgileri görüntülemek için kullanılabilir. Üstbilgiler ve altbilgiler, sayfa yapısı ayarları kullanılarak yönetilir.

{{% /alert %}}

## **Üst Bilgileri ve Alt Bilgileri Ayarlama**

Aspose.Cells, çalışma zamanında çalışma sayfalarına üst bilgiler ve alt bilgiler eklemenize olanak tanır, ancak üst bilgileri ve alt bilgileri yazdırmak için önceden tasarlanmış bir dosyada manuel olarak ayarlamanızı öneririz. Microsoft Excel'i, emekten ve geliştirme süresinden tasarruf etmek amacıyla üst bilgileri ve alt bilgileri ayarlamak için bir GUI aracı olarak kullanabilirsiniz. Aspose.Cells dosyayı içe aktarabilir ve ayarları kaydedebilir.

Çalışma zamanında üst bilgiler ve alt bilgiler eklemek için Aspose.Cells, üst bilgileri ve alt bilgileri biçimlendirmek için özel API çağrıları ve komut dosyası komutları sağlar.

### **Komut Dosyası Komutları**

Komut dosyası komutları, üst bilgi ve alt bilgi biçimlendirmesini ayarlamanıza izin veren özel komutlardır.

|**Komut Dosyası Komutları**|**Tanım**|
|:- |:- |
|&P|geçerli sayfa numarası|
|&G|Bir resim|
|&N|toplam sayfa sayısı|
|&D|Geçerli tarih|
|&T|şimdiki zaman|
|&A|çalışma sayfası adı|
|&F|Yolu olmayan dosya adı|
|&"\<FontName>"|Bir yazı tipi adını temsil eder. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Yazı tipi adını stil ile temsil eder. Örneğin: &"Arial,Kalın"|
|&\<FontSize>|Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak bu komutun ardından başlıkta yazdırılacak düz bir sayı geliyorsa bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Üstbilgileri ve Altbilgileri Ayarlama**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf iki yöntem sağlar,[**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) ve[**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), çalışma sayfasına üst bilgi ve alt bilgi eklemek için kullanılır. Bu yöntemler yalnızca iki parametre alır:

- **Bölüm** – üstbilgi veya altbilginin yerleştirilmesi gereken bölüm. Üç bölüm vardır: sırasıyla 0, 1 ve 2 ile temsil edilen sol, orta ve sağ.
- **Senaryo** – üst bilgi veya alt bilgi için kullanılacak komut dosyası. Bu komut dosyası, üst bilgileri veya alt bilgileri biçimlendirmek için komut dosyası komutları içerir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Üstbilgiye veya Altbilgiye Görüntü Ekleme**

 bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfın iki ek yöntemi vardır,[**Başlık Resmini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) ve[**Altbilgi Resmini Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), üstbilgiye ve altbilgiye resim eklemek için kullanılır. Bu yöntemler parametreleri alır:

- **Bölüm**– resmin yerleştirileceği üstbilgi veya altbilgi bölümü. Sırasıyla 0, 1 ve 2 değerleri ile temsil edilen sol, orta ve sağ olmak üzere üç bölüm vardır.
- **Bayt dizisi** – grafiksel veriler (ikili veriler bir bayt dizisinin arabelleğine yazılmalıdır).

Aşağıdaki kodu çalıştırdıktan ve dosyayı açtıktan sonra, çalışma sayfasının başlığını şu şekilde kontrol edin:

1.  Üzerinde**Dosya** menü, seç**Sayfa ayarı**. Bir diyalog görüntülenecektir.
1.  seçin**Üstbilgi Altbilgi** sekme.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
