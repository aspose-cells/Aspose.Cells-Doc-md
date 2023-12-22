---
title: Veri Filtreleme
type: docs
weight: 85
url: /tr/net/data-filtering/
description: Aspose.Cells for .NET API numaralı telefonu kullanarak veri filtresini nasıl ekleyeceğinizi öğrenin.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---
{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerini otomatik olarak filtrelemek için bazı iyi özellikler sağlar. Aspose.Cells, Microsoft Excel'in otomatik filtreleme özelliklerini tam olarak destekler. Bu makalede, Microsoft Excel'deki özelliklerin nasıl kullanılacağı ve bunların Aspose.Cells kullanılarak nasıl kodlanacağı açıklanmaktadır.

{{% /alert %}}

##  **Verileri Otomatik Filtrele**

Otomatik filtreleme, çalışma sayfasında yalnızca listede görüntülemek istediğiniz öğeleri seçmenin en hızlı yoludur. Otomatik filtreleme özelliği, kullanıcıların bir listedeki öğeleri belirlenen kriterlere göre filtrelemesine olanak tanır. Metne, sayılara veya tarihlere göre filtreleyin.

###  **Microsoft Excel'de otomatik filtreleme**

Microsoft Excel'de otomatik filtreleme özelliğini etkinleştirmek için:

1. Bir çalışma sayfasında başlık satırını tıklayın.
1.  itibaren**Veri** menü, seç**Filtre** ve ardından *Otomatik Filtre**.

Bir çalışma sayfasına otomatik filtre uyguladığınızda, sütun başlıklarının sağında filtre anahtarları (siyah oklar) görünür.

1. Filtre seçeneklerinin listesini görmek için bir filtre okunu tıklayın.

Otomatik filtre seçeneklerinden bazıları şunlardır:

|**Seçenekler**|**Tanım**|
| :- | :- |
|Tüm|Listedeki tüm öğeleri bir kez göster.|
|Gelenek|İçerir/içermez gibi filtre kriterlerini özelleştirin|
|Renge Göre Filtrele|Doldurulan renge göre filtreler|
|Tarih Filtreleri|Tarihe göre farklı ölçütlere göre satırları filtreler|
|Sayı Filtreleri|Karşılaştırma, ortalamalar ve İlk 10 gibi sayılara ilişkin farklı filtre türleri.|
|Metin Filtreleri|İle başlar, ile biter, içerir vb. gibi farklı filtreler,|
|Boşluklar/Boş Olmayanlar|Bu filtreler Boş Metin Filtresi aracılığıyla uygulanabilir|

Kullanıcılar bu seçenekleri kullanarak Microsoft Excel'deki çalışma sayfası verilerini manuel olarak filtrelerler.

###  **Aspose.Cells ile otomatik filtre**

Aspose.Cells, bir Excel dosyasını temsil eden Çalışma Kitabı adlı bir sınıf sağlar. Çalışma Kitabı sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir Çalışma Sayfaları koleksiyonu içerir.

Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Otomatik filtre oluşturmak için Worksheet sınıfının AutoFilter özelliğini kullanın. AutoFilter özelliği, bir başlık satırını oluşturan hücre aralığını belirtmek için Range özelliğini sağlayan AutoFilter sınıfının bir nesnesidir. Başlık satırı olan hücre aralığına otomatik filtre uygulanır.

Her çalışma sayfasında yalnızca bir filtre aralığı belirtebilirsiniz. Bu Microsoft Excel ile sınırlıdır. Özel veri filtreleme için AutoFilter.Custom yöntemini kullanın.

Aşağıda verilen örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz Otomatik Filtrenin aynısını Aspose.Cells kullanarak oluşturduk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

####  **Farklı Filtre türleri**

Aspose.Cells, Renk Filtresi, Tarih Filtresi, Sayı Filtresi, Metin Filtresi, Boş Filtreler ve Boş Olmayan Filtreler gibi farklı filtre türlerini uygulamak için birden fazla seçenek sunar.

#####  **Dolgu Rengi**

Aspose.Cells, hücrelerin dolgu rengi özelliğine göre verileri filtrelemek için AddFillColorFilter işlevini sağlar. Aşağıda verilen örnekte, renk filtreleme fonksiyonunu test etmek için sayfanın ilk sütununda farklı dolgu renklerine sahip bir şablon dosyası kullanılmıştır. Örnek dosyalar aşağıdaki bağlantılardan indirilebilir.

1. [Renkli Hücreler.xlsx](72417315.xlsx)
1. [FiltrelenmişRenkliHücreler.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

#####  **Tarih**

Ocak 2018'de tarihleri olan tüm satırları filtrelemek gibi farklı türde tarih filtreleri uygulanabilir. Aşağıdaki örnek kod, bu filtreyi AddDateFilter işlevini kullanarak gösterir. Örnek dosyalar aşağıda verilmiştir.

1. [Tarih.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

#####  **Dinamik Tarih**

Bazen, yıldan bağımsız olarak tüm hücrelerin Ocak ayında tarihlere sahip olması gibi, tarihe dayalı olarak dinamik filtreler gerekir. Bu durumda aşağıdaki örnek kodda verildiği gibi DynamicFilter fonksiyonu kullanılır. Örnek dosyalar aşağıda verilmiştir.

1. [Tarih.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

#####  **Sayı**

Belirli bir aralıkta sayıya sahip hücreleri seçmek gibi Aspose.Cells kullanılarak özel filtreler uygulanabilir. Aşağıdaki örnek, sayıları filtrelemek için Custom() işlevinin kullanımını göstermektedir. Örnek dosyalar aşağıda verilmiştir.

1. [Sayı.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

#####  **Metin**

Bir sütunda metin varsa ve belirli bir metni içeren hücreler seçilecekse, Filter() işlevi kullanılabilir. Aşağıdaki örnekte, şablon dosyası ülkelerin listesini içermektedir ve belirli bir ülke adını içeren satır seçilecektir. Aşağıdaki kod, metni filtrelemeyi gösterir. Örnek dosyalar aşağıda verilmiştir.

1. [Metin.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

#####  **Boşluklar**

Bir sütun, birkaç hücrenin boş olacağı şekilde metin içeriyorsa ve yalnızca boş hücrelerin bulunduğu satırları seçmek için filtre gerekiyorsa, MatchBlanks() işlevi aşağıda gösterildiği gibi kullanılabilir. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

#####  **Boşluksuz**

Herhangi bir metin içeren hücreler filtrelenecekse, aşağıda gösterildiği gibi MatchNonBlanks filtre işlevini kullanın. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

#####  **İçerir özelliğine sahip özel filtre**

Excel, bazı belirli dizeleri içeren filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda örnek dosyadaki adların filtrelenmesiyle gösterilmiştir. Örnek dosyalar aşağıda verilmiştir.

1. [kaynakÖrnekÜlkeAdları.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

#####  **NotContains ile özel filtre**

Excel, belirli bir dize içermeyen filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda verilen örnek dosyadaki isimler filtrelenerek aşağıda gösterilmiştir.

1. [kaynakÖrnekÜlkeAdları.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

#####  **BeginsWith ile özel filtre**

Excel, belirli bir dizeyle başlayan filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda verilen örnek dosyadaki isimler filtrelenerek aşağıda gösterilmiştir.

1. [kaynakÖrnekÜlkeAdları.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

#####  **EndsWith ile özel filtre**

Excel, belirli bir dizeyle biten filtre satırları gibi özel filtreler sağlar. Bu özellik Aspose.Cells'de mevcuttur ve aşağıda verilen örnek dosyadaki isimler filtrelenerek aşağıda gösterilmiştir.

1. [kaynakÖrnekÜlkeAdları.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

##  **İleri konular**
- [Karmaşık Kriterleri Karşılayan Kayıtları Görüntülemek için Microsoft Excel Gelişmiş Filtresini Uygulayın](/cells/tr/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Otomatik Filtreyi Yeniledikten Sonra Tüm Gizli Satır Dizinlerini Al](/cells/tr/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
