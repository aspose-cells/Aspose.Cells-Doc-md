---
title: Aralıkları Yönetme
linktitle: Aralıklar
type: docs
weight: 75
url: /tr/java/managing-ranges/
---
## **Giriş**

Excel'de, fare kutusu seçimiyle birden çok hücre seçebilirsiniz, seçilen hücreler kümesine "Aralık" adı verilir.

Örneğin, Excel'in Cell "A1" satırında farenin sol düğmesine tıklayıp ardından "C4" hücresine sürükleyebilirsiniz. Seçtiğiniz dikdörtgen alanı Aspose.Cells kullanarak da kolayca bir nesne olarak oluşturabilirsiniz.

Aralık oluşturma, değer koyma, stil ayarlama ve "Range" nesnesine daha fazla işlem yapma burada anlatılmaktadır.

## **Aspose.Cells Kullanarak Aralıkları Yönetme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak.

### **Aralık Oluştur**

A1:C4'ün üzerine uzanan dikdörtgen bir alan oluşturmak istediğinizde aşağıdaki kodu kullanabilirsiniz:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Aralığın Cells'ine değer koyun**

A1:C4'ün üzerinde uzanan bir hücre aralığınız olduğunu varsayalım. Matris 4 * 3 = 12 hücre yapar. Ayrı aralık hücreleri sırayla düzenlenir: Aralık[0,0], Aralık[0,1], Aralık[0,2], Aralık[1,0], Aralık[1,1], Aralık[1,2], Menzil[2,0], Menzil[2,1], Menzil[2,2], Menzil[3,0], Menzil[3,1], Menzil[3,2].

Aşağıdaki örnek, Aralık hücrelerine bazı değerlerin nasıl girileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Serinin Cells stilini ayarlayın**

Aşağıdaki örnek, Aralık hücrelerinin stilinin nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

### **Aralığın Geçerli Bölgesini Alın**

 CurrentRegion, geçerli bölgeyi temsil eden bir Range nesnesi döndüren bir özelliktir.

Geçerli bölge, boş satırların ve boş sütunların herhangi bir kombinasyonuyla sınırlanan bir aralıktır. Sadece oku.

Excel'de CurrentRegion alanını şu şekilde alabilirsiniz:
1. Fare kutusuyla bir alan(aralık1) seçin.
2. "Giriş - Düzenleme - Bul ve Seç - Özele Git - Geçerli bölge"ye tıklayın veya "Ctrl+Shift+*" kullanın, excel'in otomatik olarak bir alan (aralık2) seçmenize yardımcı olduğunu göreceksiniz, şimdi yaptınız, aralık2 aralık1'in Geçerli Bölgesi.

Aspose.Cells ile "Range.CurrentRegion" özelliğini kullanarak aynı işlevi gerçekleştirebilirsiniz.

Lütfen aşağıdaki test dosyasını indirin, excel'de açın, "A1:D7" alanını seçmek için fare kutusunu kullanın, ardından "Ctrl+Shift+*"ye tıklayın, "A1:C3" alanının seçili olduğunu göreceksiniz.

[geçerli_bölge.xlsx](current_region.xlsx)

Şimdi lütfen aşağıdaki örneği çalıştırın, Aspose.Cells'de nasıl çalıştığını görün:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **ileri konular**
- [Excel dosyasının Otomatik Doldurma aralığı](/cells/tr/java/autofill-ranges/)
- [Satırları veya Aralığı Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirin](/cells/tr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Excel Aralıklarını Kopyala](/cells/tr/java/copy-ranges-of-Excel/)
- [Yalnızca Aralık Verilerini Kopyala](/cells/tr/java/copy-range-data-only/)
- [Aralık Verilerini Tarzla Kopyala](/cells/tr/java/copy-range-data-with-style/)
- [Yalnızca Aralık Stilini Kopyala](/cells/tr/java/copy-range-style-only/)
- [Kaynak Aralığının Satır Yüksekliklerini Hedef Aralığa Kopyala](/cells/tr/java/copy-row-heights-of-source-range-to-destination-range/)
- [Birlik Aralığı Oluştur](/cells/tr/java/create-union-range/)
- [Kesme ve Yapıştırma Aralıkları](/cells/tr/java/cut-and-paste-cells/)
- [Aralıkları Sil](/cells/tr/java/delete-ranges-from-Excel/)
- [Çalışma Sayfasında Birleştirilmiş Cells'i Algıla](/cells/tr/java/detect-merged-cells-in-a-worksheet/)
- [Al Adresi Cell Sayı Aralığının Tüm Sütununu ve Tüm Satırını Uzaklaştır](/cells/tr/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Harici Bağlantılarla Menzil Alın](/cells/tr/java/get-range-with-external-links/)
- [Sıralı Olmayan Aralıkları Uygulama](/cells/tr/java/implementing-non-sequential-ranges/)
- [Aralık Ekle](/cells/tr/java/insert-ranges-to-Excel/)
- [Cells aralığını birleştir veya ayır](/cells/tr/java/merge-or-unmerge-range-of-cells/)
- [Bir Çalışma Sayfasında Cells Aralığını Taşı](/cells/tr/java/move-range-of-cells-in-a-worksheet/)
- [Adlandırılmış Aralıklar](/cells/tr/java/named-ranges/)
- [Bir Aralıktaki Verileri Arayın ve Değiştirin](/cells/tr/java/search-and-replace-data-in-a-range/)

