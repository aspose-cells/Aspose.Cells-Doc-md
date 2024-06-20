---
title: Veri Filtreleme
type: docs
weight: 60
url: /tr/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel, elektronik tablo verilerini otomatik filtreleme özellikleri sağlar. Aspose.Cells, Microsoft Excel'in otomatik filtreleme özelliklerini tamamen destekler. Bu makale, Microsoft Excel'deki özellikleri nasıl kullanabileceğinizi ve onları Aspose.Cells kullanarak nasıl kodlayabileceğinizi açıklar.

{{% /alert %}}

## **Veriye Otomatik Filtreleme Uygulama**

Otomatik filtreleme, listede görüntülemek istediğiniz yalnızca öğeleri seçmenin en hızlı yoludur. Otomatik filtreleme özelliği, kullanıcılara belirli bir kriterlere göre listedeki öğeleri filtreleme olanağı sağlar. Metne, sayılara veya tarih bilgilerine göre filtreleme yapın.

### **Microsoft Excel'de Otomatik Filtreleme**

Microsoft Excel'de otomatik filtreleme özelliğini etkinleştirmek için:

1. Bir çalışma sayfasında başlık satırına tıklayın.
1. **Veri** menüsünden **Filtre** seçin ve ardından **Otomatik Filtre**'yi seçin.

Bir çalışma sayfasına otomatik filtre uyguladığınızda, filtre anahtarları (siyah oklar) sütun başlıklarının sağında görünür.

1. Bir filtre okuna tıklayarak filtre seçeneklerinin listesini görüntüleyin.

Otomatik filtre seçeneklerinden bazıları:

|**Seçenekler**|**Açıklama**|
| :- | :- |
|All|Listedeki tüm öğeleri bir kez gösterir.
|Custom|İçerir/içermez gibi özel filtre kriterleri
|Filter by Color|Dolgu rengine göre filtreleme
|Date Filters|Tarihe göre farklı kriterlere dayalı filtreleme
|Number Filters|Kıyaslama, ortalamalar ve En İyi 10 vb. gibi sayılara dayalı farklı türde filtreler|
|Text Filters|Başlangıç, son, içerir vb. gibi farklı filtreler
|Blanks/Non Blanks|Bu filtreler Metin Filtre Boş üzerinden uygulanabilir
Kullanıcılar, Microsoft Excel'de bu seçenekleri kullanarak çalışma sayfalarındaki verileri manuel olarak filtreler.

### **Aspose.Cells ile Autofilter**

Aspose.Cells, Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir otomatik filtre oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) özelliğini kullanın. [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) özelliği, başlık satırını oluşturan hücre aralığının belirlenmesi için [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) sınıfından bir nesnedir ve [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) özelliğini sağlar. Otomatik filtre, başlık satırını oluşturan hücre aralığına uygulanır.

Her bir çalışma sayfasında, yalnızca bir filtre aralığı belirtebilirsiniz. Bu, Microsoft Excel tarafından sınırlıdır. Özel veri filtrelemesi için [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) yöntemini kullanın.

Aşağıdaki örnekte, Yukarıdaki bölümde Microsoft Excel kullanarak oluşturulan AutoFilter'ı Aspose.Cells kullanarak oluşturduk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Farklı Türlerde Filtre**

Aspose.Cells, Renk Filtresi, Tarih Filtresi, Sayı Filtresi, Metin Filtresi, Boş Filtreler ve Dolu Filtreler gibi farklı filtre türleri uygulamak için birden fazla seçenek sağlar.

##### **Dolgu Rengi**

Aspose.Cells, hücrelerin dolgu rengi özelliğine göre verileri filtrelemek için [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)) işlevini sağlar. Aşağıdaki örnekte, sayfanın ilk sütununda farklı dolgu renkleri olan bir şablon dosya, renk filtresi işlevini test etmek için kullanılır. İşlevselliği kontrol etmek için aşağıdaki dosyalar indirilebilir.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Tarih**

Filtrelenecek Ocak 2018 tarihlerine sahip tüm satırları filtrelemek gibi farklı türde tarih filtreleri uygulanabilir. Aşağıdaki örnek kod, bu filtrelemeyi [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) işlevini kullanarak göstermektedir. Bu işlevselliği test etmek için aşağıdaki dosyalar kullanılabilir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dinamik Tarih**

Bazen tarihe dayalı dinamik filtreler, yıl gözetmeksizin, örneğin Ocak ayında tüm hücrelerin gerekliliği olabilir. Bu durumda, aşağıdaki örnek kodda verildiği gibi [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) işlevi kullanılır. Bu işlevselliği test etmek için aşağıdaki dosyalar kullanılabilir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Sayı**

Aspose.Cells ile sayılar arasında belirli bir aralıkta hücreleri seçerek özel filtreler uygulanabilir. Aşağıdaki örnek, sayıları filtrelemek için [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) işlevinin kullanımını göstermektedir. İşlevin işlevselliğini kontrol etmek için örnek dosyalar aşağıdaki bağlantılardan indirilebilir.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Metin**

Bir sütun metin içeriyorsa ve belirli metni içeren hücrelerin seçilmesi gerekiyorsa, aşağıdaki örnek dosyada belirli ülke adını içeren bir satır bulunan bir şablon dosya kullanılarak [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) işlevi kullanılabilir. Aşağıdaki örnek kod, aşağıdaki örnek dosyalar kullanılarak metin filtrelemesini göstermektedir.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Boşluklar**

Bir sütun öyle metin içeriyor ki, bazı hücreler boş ise ve yalnızca boş hücrelerin bulunduğu satırların seçilmesi gerekiyorsa, aşağıdaki örnek kodda gösterildiği gibi [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) işlevi kullanılabilir. İşlevin işlevselliğini kontrol etmek için örnek dosyalar aşağıdaki bağlantılardan indirilebilir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBos.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Boş Olmayanlar**

Herhangi bir metni içeren hücrelerin filtrelenmesi gerektiğinde, aşağıdaki bağlantılardan örnek dosyalar kullanılarak [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) filtre işlevini kullanın.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBosOlmayan.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Contains ile Özel filtre**

Excel, belirli bir dize içeren satırları filtrelemek gibi özel filtreler sağlar. Bu özellik Aspose.Cells içinde kullanılabilir ve aşağıdaki örnek dosyada isimleri filtreleyerek gösterilmektedir. İşlevselliği kontrol etmek için aşağıdaki dosyalar indirilebilir.

1. [sourseOrnekUlkeIsimleri.xlsx](sourseOrnekUlkeIsimleri.xlsx)
1. [dışörnekÜlkeAdları.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Contains Kullanmadan Özel filtre**

Excel, belirli bir dizeyi içermeyen satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Belirli bir dizeyle Başlayan Özel Filtre**

Excel, belirli bir dizeyle başlayan satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Belirli Bir Dize ile Biten Özel Filtre**

Excel, Aspose.Cells'de mevcut olan ve aşağıdaki örnek dosyadaki isimleri filtreleyerek aşağıda gösterildiği gibi belirli bir dizeyle biten satırları filtreleyen özel filtreler sağlar.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Gelişmiş Konular**
- [Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın](/cells/tr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın](/cells/tr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

