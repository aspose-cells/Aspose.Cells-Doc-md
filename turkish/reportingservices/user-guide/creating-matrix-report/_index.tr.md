---
title: Matrix Rapor Oluşturma
type: docs
weight: 10
url: /tr/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services, bir matrixi Microsoft Excel'de oluşturmanıza olanak tanır. 

{{% /alert %}} 
### **Matrix Şablonu**
Bir Aspose.Cells rapor şablonunda, matrix köşe, satır grupları, sütun grupları ve veri bölümlerinden oluşur. Bir örnek matrix aşağıda gösterilmiştir.

**Bir örnek matrix** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Matrix köşesi**: sol üst köşede bulunur, veya sağdan sola (RTL) düzenleri için sağ üst köşede. Bu alan, bir matrix veri bölgesine hem satır grupları hem de sütun grupları eklediğinizde otomatik olarak oluşturulur. Bu alanda, hücreleri gömülü metin kutusu rapor öğesini birleştirebilirsiniz.
- **Matrix sütun grupları alanı**: sağ üst köşede bulunur (RTL düzeni için sol üst köşe). Bu alan, bir sütun grubu eklediğinizde otomatik olarak oluşturulur. Bu alandaki hücreler, sütun gruplarının hiyerarşisini temsil eder ve sütun grup örneği değerlerini gösterir. Şekilde, OrderYear'ı gösteren hücreler, iç içe geçmiş bir sütun grubu ve OrderQtr'ı gösteren hücre, bitişik bir sütun grubudur.
- **Matrix satır grupları alanı**: sol alt köşede bulunur (RTL düzeni için sağ alt köşe). Bu alan, bir satır grubu eklediğinizde otomatik olarak oluşturulur. Bu alandaki hücreler, satır gruplarının hiyerarşisini temsil eder ve satır grup örneği değerlerini gösterir. Şekilde, bu hücreler iç içe geçmiş satır gruplarını temsil eder.
- **Matrix veri alanı**: sağ alt köşede bulunur (RTL düzeni için sol alt köşe). Matrix verisi, detay ve gruplanmış veriyi gösterir. Bu örnekte yalnızca toplanmış veri kullanılır. Bir grup satır veya sütundaki hücreler, gruplamayı içermeyen basit ifadeleri içeriyorsa, varsayılan olarak hücreler, gruptaki ilk değere eşit olacak şekilde değerlendirilir. Şekilde, hücreler satış siparişlerinin satır toplamları için toplam toplamları gösterir.
#### **Matrix Şablonu Oluşturma**
Bir matrix raporu oluşturmadan önce, önceden oluşturulmuş veri kaynakları, veri kümeleri ve rapor parametreleri (isteğe bağlı) oluşturun. (Yardıma ihtiyacınız varsa [Veri Kaynakları ve Sorgular](/cells/tr/reportingservices/data-sources-and-queries/) bölümündeki talimatları izleyin.) Örnekte, SQL Server Reporting Services 2008 ile birlikte gönderilen AdventureWorks örnek veritabanını kullanıyoruz.

Yeni bir matrix oluşturmak için:

1. Microsoft Excel'i açın.
1. Veri kaynakları, veri kümeleri ve rapor parametrelerini içeren önceden oluşturulmuş bir RDL Rapor dosyasını açmak için **Rapor Aç**'a tıklayın.
   Dosya başarıyla açıldıktan sonra tüm bilgileri kullanabilir durumda olacak, örneğin veri kümeleri **Veri Seti** listesinde listelenir.
1. Bir Microsoft Excel çalışma sayfasını açın ve bir veri kümesi seçin. 

![todo:image_alt_text](creating-matrix-report_2.png)




1. **Grup Ayarla** aracılığıyla satır grupları ve sütun grupları belirleyin. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Hücreleri birleştirerek matris köşesini ayarlayın.

![todo:image_alt_text](creating-matrix-report_4.png)




1. Bir formül ekleyerek matris köşesini ayarlayın. 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. Matris özniteliğini ayarlamak için **Öznitelik Ayarla**'yı tıklayın. 

![todo:image_alt_text](creating-matrix-report_7.png)



Ad, aralık, grup ve sıra olarak oluşur.

1. Değiştirmek için özniteliğe tıklama, güncel çalışma sayfasının tüm matris özniteliklerini kontrol eder ve değiştirir.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Raporu kaydedin, yayınlayın ve inceleyin.
