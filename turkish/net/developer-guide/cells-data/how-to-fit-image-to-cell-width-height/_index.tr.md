---
title: Resmi Hücre Genişliğine ve Yüksekliğine Sığdırma Yöntemi
type: docs
weight: 130
url: /tr/net/how-to-fit-image-to-cell-width-height/
description: Aspose.Cells kullanarak hücre genişliğine resmi nasıl sığdıracağınızı öğrenin.
keywords: Resmi Hücre Genişliğine Sığdırma, Resmi Hücre Genişliğine Sığdırma, Resmi Hücre Genişliği ve Yüksekliği ile Sığdırma, Resmi Yükseğe Sığdırma.
---


## ** Neden Resmi Hücre Genişliği ve Yüksekliğine Sığdırıyoruz**
Bir resmi belirli bir hücrenin genişlik ve yüksekliğine sığdırmak sadece estetikle ilgili değil. Temelde hassasiyet, otomasyon ve veri organizasyonu ile ilgilidir.

1. Profesyonel Sunum ve Okunabilirlik İçin: Bir gösterge paneli oluştururken, verilerle mükemmel hizalanması gereken ikonlar, bayraklar veya ürün görsellerine ihtiyacınız olur. Hizalamamış bir görüntü düzensiz ve profesyonelsiz görünür. Başkalarının kullanması için şablon tasarlıyorsanız (örneğin, ürün kataloğu, çalışan dizini), görsellerin otomatik olarak belirlenen alanlara uymasını istersiniz, böylece her şablon kullanıldığında tutarlılık sağlanır. Hücreleri aşan görseller, yazdırırken beklenmedik sayfa kırılmaları ve biçimlendirme sorunlarına neden olabilir. Uygun şekilde yerleştirilmiş bir görsel, yazdırılan sayfada tutarlı davranır.

2. Veri Düzenleme ve Yapılandırma İçin: En kritik fonksiyonel sebeptir. Excel, veri için bir ızgaradır. Bir görsel "hücreye yerleştirildiği" zaman, "sığıntı" (fitted) değilse sorunlar ortaya çıkar. Serbestçe yüzeyde duran görselin sorunları: Hücrelerle hareket etmez: Sıralama, filtreleme veya satır ekleme/silme yaparsanız, görsel sayfada mutlak konumunu korur ve temsil etmesi gereken veriden kopar. Yeniden boyutlandırılmaz: Satır yüksekliği veya sütun genişliği değiştirilirse, serbest yüzeyde duran görsel aynı boyutta kalır, düzeni bozar. Hücreye uyarlamanın avantajı: Hücre "Kapsayıcı" olur: Bir görsel, hücreye uygun hale getirildiğinde, konumu ve boyutu hücrenin ızgara koordinatlarıyla belirlenir. Veriyi taşırsanız (örneğin, tabloyu sıralarsanız), görsel, karşılık gelen satırla birlikte hareket eder. Gerçek bir Resim-Veri Çifti Oluşur: Bu, görseli ilgili satırdaki verilerin görsel özelliği olarak kullanmanıza olanak tanır, bu otomasyon için önemlidir.

3. Otomasyon ve Gelişmiş İşlevsellik İçin: Bu noktada görselleri hücreye sığdırmak adeta bir güçtür. Görselleri Dinamik Bağlama: Bir formül kullanarak görüntü yolunu bir hücreden çekebilir ve ardından bir makro (VBA) ile otomatik olarak boyutlandırıp yan hücreye ekleyebilirsiniz. Bu şekilde, ürün kimliği değiştikçe otomatik olarak ürün adı, fiyat ve görsel güncellenen dinamik bir ürün katalogu oluşturulur. Veritabanı Entegrasyonu: Veri dışa aktarırken veya Excel ile veritabanına bağlanırken, görsellerin belirli hücrelerde bulunması, tüm veri setini ve görsellerini daha yapılandırılmış ve taşınabilir kılar.

## **Excel'de Görseli Hücre Genişliği ve Yüksekliğine Sığdırma**
Aşağıdaki iki yöntemle görseli Excel'de hücre genişliği ve yüksekliğine sığdırabilirsiniz.

### **Görseli Hücre Genişliği ve Yüksekliğine Sığdırmak için Hücrede Konumlandırma Kullanma**
Excel'de bir hücreye resim eklemek için şu adımları izleyin:

1. Ekle sekmesine gidin ve Resimler seçeneğine tıklayın.
2. **Hücreye Yerleştir**'i seçin. **Resim Ekleme Yerinden** açılır menüsünden aşağıdaki kaynaklardan birini seçin (**Bu Cihaz**, **Stok Resimler** ve **Çevrimiçi Resimler**). Bu Cihaz, cihazınızdan resim eklemek için. Stok Resimler, stok resimlerden resim eklemek için. Çevrimiçi Resimler, webden resim eklemek için.
<br>
<img src="1.png" width=60% />
3. Resmi seçin ve bir hücreye resim ekleyin.
<br>
<img src="8.png" width=60% />

### **Görseli Hücre Genişliği ve Yüksekliğine Sığdırmak için Hücreler Üzerinde Konumlandırma Kullanma**
Excel'de hücrelerin üzerine resim eklemek için şu adımları izleyin:

1. Ekle sekmesine gidin ve Resimler seçeneğine tıklayın.
2. **Hücrelerin Üzerine Yerleştir**'i seçin. **Resim Ekleme Yerinden** açılır menüsünden aşağıdaki kaynaklardan birini seçin (**Bu Cihaz**, **Stok Resimler** ve **Çevrimiçi Resimler**). Bu Cihaz, cihazınızdan resim eklemek için. Stok Resimler, stok resimlerden resim eklemek için. Çevrimiçi Resimler, webden resim eklemek için.
<br>
<img src="2.png" width=60% />
3. Resmi seçin ve hücrelerin üzerine resim ekleyin.
<br>
<img src="3.png" width=60% />
4. Görselin genişliğini ve yüksekliğini hücrelerle eşleştirecek şekilde manuel olarak ayarlayın.
<br>
<img src="6.png" width=60% />

## **Aspose.Cells Kullanarak Görseli Hücre Genişliği ve Yüksekliğine Sığdırma**
Diller ve görüntü oranlarına göre satır ve sütunların genişlik ve yüksekliğindeki farklılıklar nedeniyle, bir görselin genişlik ve yüksekliğini ayarlamak bazı küçük farklara yol açabilir ve bazen hücrelerle tamamen tutarlı olmayabilir. Aspose.Cells'te aşağıdaki iki yöntemle görseli hücreye sığdırabilirsiniz.

### **Görseli Hücre Genişliği ve Yüksekliğine Sığdırmak için Hücrede Konumlandırma Kullanma**
Aspose.Cells kullanarak hücreye resim ekleme. Lütfen aşağıdaki örnek kodu görün. Örnek kodu yürüttükten sonra, bir resim hücreye eklenecektir.
1. Bir Workbook nesnesi oluşturun. 
2. Resmi yerleştirmek istediğiniz hücreyi alın.
3. Cell.EmbeddedImage özelliğini ayarlayın. 
4. Son olarak, çalışma kitabını [çıktı XLSX](out.xlsx) formatında kaydeder. 

### **Hücrede Konumlandırma İçin Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-in-cell.cs" >}}
{{< app/cells/assistant language="csharp" >}}

### **Görseli Hücre Genişliği ve Yüksekliğine Sığdırmak için Hücreler Üzerinde Konumlandırma Kullanma**
Bir elektron mikroskobuna resim eklemek çok kolaydır. Sadece birkaç satır kod gerektirir:
Sadece [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nesnesinin [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) koleksiyonunun [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodunu çağırın. Ardından, hücrelerin genişlik ve yüksekliğine göre görselin genişliğini ve yüksekliğini ayarlayın. Son olarak, dosyayı [çıktı XLSX](out_net.xlsx) biçiminde kaydedin. [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) yöntemi aşağıdaki parametreleri alır:

- **Sol üst satır dizini**, sol üst sütunun dizini.
- **Sol üst sütun dizini**, sol üst sütunun dizini.
- **Resim dosya adı**, yol bilgisi ile birlikte resim dosyasının adı.


### **Hücrelere Konumlandırma için Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-over-cells-fit-cell-width-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
