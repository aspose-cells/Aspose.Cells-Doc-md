---
title: Veri Filtreleme
type: docs
weight: 60
url: /tr/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerini otomatik olarak filtrelemek için bazı iyi özellikler sağlar. Aspose.Cells, Microsoft Excel'in otomatik filtreleme özelliklerini tam olarak destekler. Bu makalede, Microsoft Excel'deki özelliklerin nasıl kullanılacağı ve bunların Aspose.Cells kullanılarak nasıl kodlanacağı açıklanmaktadır.

{{% /alert %}}

## **Verileri Otomatik Filtrele**

Otomatik filtreleme, çalışma sayfasından yalnızca bir listede görüntülemek istediğiniz öğeleri seçmenin en hızlı yoludur. Otomatik filtreleme özelliği, kullanıcıların bir listedeki öğeleri belirli bir kritere göre filtrelemesine olanak tanır. Metne, sayılara veya tarihlere göre filtreleyin.

### **Microsoft Excel'de otomatik filtreleme**

Microsoft Excel'de otomatik filtreleme özelliğini etkinleştirmek için:

1. Bir çalışma sayfasındaki başlık satırını tıklayın.
1. itibaren**Veri**menü, seç**filtre**ve daha sonra**Otomatik filtre**.

Bir çalışma sayfasına otomatik filtre uyguladığınızda, sütun başlıklarının sağında filtre anahtarları (siyah oklar) görünür.

1. Filtre seçeneklerinin listesini görmek için bir filtre okuna tıklayın.

Otomatik filtreleme seçeneklerinden bazıları şunlardır:

|**Seçenekler**|**Tanım**|
|:- |:- |
|Herşey|Listedeki tüm öğeleri bir kez göster.|
|Gelenek|İçerir/içermez gibi filtre kriterlerini özelleştirin|
|Renge Göre Filtrele|Doldurulmuş renge göre filtreler|
|Tarih Filtreleri|Tarihteki farklı ölçütlere göre satırları filtreler|
|Sayı Filtreleri|Karşılaştırma, ortalamalar ve İlk 10 gibi sayılar üzerinde farklı türde filtreler.|
|Metin Filtreleri|Şununla başlar, şununla biter, içerir vb. gibi farklı filtreler:|
|Boşluklar/Boş Olmayanlar|Bu filtreler Boş Metin Filtresi aracılığıyla uygulanabilir|
Kullanıcılar, bu seçenekleri kullanarak çalışma sayfası verilerini Microsoft Excel'de manuel olarak filtreler.

### **Aspose.Cells ile otomatik filtre**

Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar.

Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bir otomatik filtre oluşturmak için,[**Otomatik filtre**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)mülkiyeti[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)sınıf. bu[**Otomatik filtre**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)özellik bir nesnedir[**Otomatik filtre**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)sağlayan sınıf,[**Menzil**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)başlık satırını oluşturan hücre aralığını belirleme özelliği. Başlık satırı olan hücre aralığına bir otomatik filtre uygulanır.

Her çalışma sayfasında yalnızca bir filtre aralığı belirtebilirsiniz. Bu, Microsoft Excel ile sınırlıdır. Özel veri filtreleme için,[**Otomatik Filtre. Özel**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) yöntem.

Aşağıda verilen örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz aynı AutoFilter'ı Aspose.Cells kullanarak oluşturduk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Farklı Filtre türleri**

Aspose.Cells, Renk Filtresi, Tarih Filtresi, Sayı Filtresi, Metin Filtresi, Boş Filtreler ve Boş Filtre Yok gibi farklı filtre türlerini uygulamak için birden fazla seçenek sunar.

##### **Dolgu Rengi**

Aspose.Cells bir işlev sağlar[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)hücrelerin dolgu rengi özelliğine göre verileri filtrelemek için. Aşağıda verilen örnekte, renk filtreleme işlevini test etmek için sayfanın ilk sütununda farklı dolgu renkleri olan bir şablon dosyası kullanılmıştır. İşlevselliği kontrol etmek için aşağıdaki dosyalar indirilebilir.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Tarih**

Ocak 2018'de tarihleri olan tüm satırları filtrelemek gibi farklı türde tarih filtreleri uygulanabilir. Aşağıdaki örnek kod, bu filtreyi kullanarak gösterir.[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) işlev. Bu işlevselliği test etmek için aşağıdaki dosyalar kullanılabilir.

1. [Tarih.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dinamik Tarih**

Bazen, yıldan bağımsız olarak Ocak ayındaki tüm hücreler gibi bir tarihe göre dinamik filtreler gerekir. Bu durumda,[**Dinamik Filtre**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) fonksiyonu aşağıdaki örnek kodda verildiği gibi kullanılır. Test için aşağıdaki dosyalar kullanılabilir.

1. [Tarih.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Sayı**

Belirli bir aralık arasında sayıya sahip hücrelerin seçilmesi gibi Aspose.Cells kullanılarak özel filtreler uygulanabilir. Aşağıdaki örnek, kullanımını göstermektedir[**gelenek()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) sayıları filtreleme işlevi. Örnek dosyalar aşağıdaki linklerden indirilebilir.

1. [Sayı.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Metin**

Bir sütun metin içeriyorsa ve belirli bir metni içeren hücreler seçilecekse,[**filtre()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) fonksiyonu kullanılabilir. Aşağıdaki örnekte, şablon dosyası bir ülke listesi içermektedir ve belirli bir ülke adını içeren satır seçilecektir. Aşağıdaki kod, aşağıdaki örnek dosyaları kullanarak metnin filtrelenmesini gösterir.

1. [Metin.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Boşluklar**

Bir sütun, birkaç hücre boş olacak şekilde metin içeriyorsa ve yalnızca boş hücrelerin bulunduğu satırları seçmek için filtre gerekiyorsa,[**maçBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) işlevi aşağıda gösterildiği gibi kullanılabilir. Örnek dosyalar aşağıdaki linklerden indirilebilir.

1. [Boş.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Boşluksuz**

Herhangi bir metne sahip hücreler filtreleneceği zaman şunu kullanın:[**Boş Olmayanları Eşleştir**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) aşağıda gösterildiği gibi filtre işlevi. Örnek dosyalar aşağıdaki linklerden indirilebilir.

1. [Boş.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **İçeriği olan özel filtre**

Excel, bazı belirli dizeleri içeren filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda örnek dosyadaki adların filtrelenmesiyle gösterilmektedir. Örnek dosyalar aşağıdaki linklerden indirilebilir.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **NotContains ile özel filtre**

Excel, belirli bir dize içermeyen filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda verilen örnek dosyadaki adlar filtrelenerek aşağıda gösterilmiştir.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **BeginsWith ile özel filtre**

Excel, belirli bir dizeyle başlayan filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda verilen örnek dosyadaki adlar filtrelenerek aşağıda gösterilmiştir.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **EndsWith ile özel filtre**

Excel, belirli bir dizeyle biten filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda verilen örnek dosyadaki adlar filtrelenerek aşağıda gösterilmiştir.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **ileri konular**
- [Karmaşık Kriterleri Karşılayan Kayıtları Görüntülemek için Microsoft Excel'in Gelişmiş Filtresini Uygulayın](/cells/tr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [AutoFilter'ı Yeniledikten Sonra Tüm Gizli Satır Dizinlerini Alın](/cells/tr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

