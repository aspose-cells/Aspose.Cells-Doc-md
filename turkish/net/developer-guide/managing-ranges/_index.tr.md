---
title: Aralıkları Yönetme
linktitle: Aralıklar
type: docs
weight: 105
url: /tr/net/managing-ranges/
---

## **Giriş**

Excel'de fare kutu seçimi ile birden fazla hücre seçebilirsiniz, seçilen hücrelerin setine "Aralık" denir.

Örneğin, Excel'in "A1" hücresine sol fare düğmesiyle tıklayıp ardından "C4" hücresine sürükleyebilirsiniz. Seçtiğiniz dikdörtgen alanı, Aspose.Cells kullanarak kolayca bir nesne olarak da oluşturulabilir.

Aralık oluşturma, değer koyma, stil ayarlama ve "Aralık" nesnesine daha fazla işlem yapmanın yolları.

## **Aspose.Cells kullanarak Aralıkları Yönetme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışsayfa [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu sağlar.

### **Aralık Oluştur**

A1:C4 üzerine uzanan bir dikdörtgen alan oluşturmak istediğinizde aşağıdaki kodu kullanabilirsiniz:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Aralık Hücrelerine Değer Atama**

Örneğin, A1:C4'e uzanan bir hücre aralığınız var. Matris, 4 * 3 = 12 hücre oluşturur. Aralık hücreleri sıralı bir şekilde düzenlenir: Aralık[0,0], Aralık[0,1], Aralık[0,2], Aralık[1,0], Aralık[1,1], Aralık[1,2], Aralık[2,0], Aralık[2,1], Aralık[2,2], Aralık[3,0], Aralık[3,1], Aralık[3,2].

Aşağıdaki örnek, Aralık hücrelerine bazı değerleri girme işlemini göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Aralık Hücrelerinin Stilini Belirleme**

Aşağıdaki örnek, Aralığın hücrelerinin stilini ayarlamanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Aralık 'ın Mevcut Bölgesini Al**

CurrentRegion, mevcut bir bölgeyi temsil eden bir Aralık nesnesi döndüren bir özelliktir. 

Mevcut bölge, herhangi bir kombinasyonla sınırlandırılmış bir aralıktır. Salt okunur.

Excel'de, CurrentRegion alanını şu şekilde alabilirsiniz:
1. Fare kutusu ile bir alan (range1) seçin.
2. "Ana Sayfa - Düzenleme - Bul & Seç - Özel Git - Gelen bölge" yi tıklayın veya "Ctrl+Shift+*" kullanarak, excel otomatik olarak bir bölge (range2) seçmenize yardımcı olacaktır, şimdi başardınız, range2 range1'in CurrentRegion'ıdır.

Aspose.Cells kullanarak aynı işlemi yapmak için "Range.CurrentRegion" özelliğini kullanabilirsiniz.

Lütfen aşağıdaki test dosyasını indirin, excel'de açın, bir alanı seçmek için fare kutusunu kullanın "A1:D7", sonra "Ctrl+Shift+*" tıklayın, "A1:C3" alanının seçildiğini göreceksiniz.

[current_region.xlsx](current_region.xlsx)

Şimdi lütfen aşağıdaki örneği çalıştırın, Aspose.Cells içinde nasıl çalıştığını görün:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Gelişmiş Konular**
- [Excel dosyasının Otomatik Doldurması](/cells/tr/net/autofill-ranges/)
- [Excel'in Aralıklarını Kopyala](/cells/tr/net/copy-ranges-of-Excel/)
- [Yalnızca Aralık Verisini Kopyala](/cells/tr/net/copy-range-data-only/)
- [Yalnızca Aralık Verisiyle Kopyala](/cells/tr/net/copy-range-data-with-style/)
- [Yalnızca Aralık Stiliyle Kopyala](/cells/tr/net/copy-range-style-only/)
- [Birleşik Aralık Oluştur](/cells/tr/net/create-union-range/)
- [Aralığı Kes ve Yapıştır](/cells/tr/net/cut-and-paste-cells/)
- [Aralıkları Sil](/cells/tr/net/delete-ranges-from-Excel/)
- [Aralığın Adresini, Hücre Sayısını ve Konumunu, Tüm Sütunu ve Tüm Satırı Al](/cells/tr/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Aralık Ekle](/cells/tr/net/insert-ranges-to-Excel/)
- [Hücreleri Birleştir veya Birleşikliği Kaldır](/cells/tr/net/merge-or-unmerge-range-of-cells/)
- [Çalışma Sayfasında Hücre Aralığını Taşıma](/cells/tr/net/move-range-of-cells-in-a-worksheet/)
- [Çalışma Kitabı ve Çalışma Sayfası Kapsamlı Adlandırılan Aralıkları Oluştur](/cells/tr/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Aralıktaki Veriyi Arama ve Değiştirme](/cells/tr/net/search-and-replace-data-in-a-range/)
