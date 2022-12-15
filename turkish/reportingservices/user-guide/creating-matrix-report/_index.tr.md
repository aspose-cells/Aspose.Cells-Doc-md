---
title: Matris Raporu Oluşturma
type: docs
weight: 10
url: /tr/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services, Microsoft Excel'de bir matris tasarlamanızı sağlar.

{{% /alert %}} 
### **Matris Şablonu**
Aspose.Cells rapor şablonunda, bir matris köşe, satır grupları, sütun grupları ve veri bölümlerinden oluşur. Örnek bir matris aşağıda gösterilmiştir.

**Örnek bir matris** 

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_1.png)

- **matris köşesi**sol üst köşede veya sağdan sola (RTL) düzenler için sağ üst köşede bulunur. Bu alan, bir matris veri bölgesine hem satır gruplarını hem de sütun gruplarını eklediğinizde otomatik olarak oluşturulur. Bu alanda, gömülü metin kutusu rapor öğesi hücreleri birleştirebilirsiniz.
- **Matris sütun grupları alanı**: sağ üst köşede bulunur (RTL düzeni için sol üst köşe). Bu alan, bir sütun grubu eklediğinizde otomatik olarak oluşturulur. Bu alandaki hücreler, sütun grupları hiyerarşisinin üyelerini temsil eder ve sütun grubu örnek değerlerini görüntüler. Şekilde, OrderYear'ı görüntüleyen hücreler iç içe bir sütun grubudur ve OrderQtr'yi görüntüleyen hücre bitişik bir sütun grubudur.
- **Matris satır grupları alanı**: sol alt köşede bulunur (RTL düzeni için sağ alt). Bu alan, bir satır grubu eklediğinizde otomatik olarak oluşturulur. Bu alandaki hücreler, satır grupları hiyerarşisinin üyelerini temsil eder ve satır grubu örnek değerlerini görüntüler. Şekilde bu hücreler iç içe satır gruplarıdır.
- **Matris veri alanı**: sağ alt köşede bulunur (RTL düzeni için sol alt). Matris verileri, ayrıntılı ve gruplandırılmış verileri görüntüler. Bu örnekte, yalnızca birleştirilmiş veriler kullanılmıştır. Varsayılan olarak, bir toplama işlevi içermeyen basit ifadeler içeren bir grup satırındaki veya sütunundaki hücreler, gruptaki ilk değer olarak değerlendirilir. Şekilde hücreler, tüm satış siparişleri için satır toplamları için toplamları görüntüler.
#### **Matris Şablonu Oluşturma**
 Bir matris raporu oluşturmadan önce veri kaynaklarını, veri kümelerini ve rapor parametrelerini (isteğe bağlı) oluşturun. (içindeki talimatları izleyin.[Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) yardıma ihtiyacınız varsa.) Örnekte, SQL Server Reporting Services 2008 ile birlikte gelen AdventureWorks örnek veritabanını kullanıyoruz.

Yeni bir matris oluşturmak için:

1. Microsoft Excel'i açın.
1.  Tıklamak**Raporu Aç** önceden oluşturulmuş veri kaynaklarını, veri kümelerini ve rapor parametrelerini içeren bir RDL Rapor dosyasını açmak için.
Dosya başarılı bir şekilde açıldıktan sonra, tüm bilgileri kullanılabilir hale gelir; örneğin, veri kümeleri**Veri Kümesi** liste.
1.  Bir Microsoft Excel çalışma sayfası açın ve bir veri kümesi seçin.

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_2.png)




1.  Satır gruplarını ve sütun gruplarını şu şekilde ayarlayın:**Grubu Ayarla**. 

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_3.png)




1. Matris köşesini ayarlamak için hücreleri birleştirin.

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_4.png)




1.  Bir formül ekleyerek matris köşesini ayarlayın.

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_5.png)




![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_6.png)




1.  Tıklamak**Özniteliği Ayarla** matris özniteliğini ayarlamak için.

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_7.png)



Ad, aralık, grup ve düzenden oluşur.

1. Özniteliği değiştir'i tıklatmak, geçerli çalışma sayfasının tüm matris özniteliklerini kontrol eder ve değiştirir.

![yapılacaklar:resim_alternatif_Metin](creating-matrix-report_8.png)




1. Raporu kaydedin, yayınlayın ve inceleyin.
