---
title: Veri Filtreleme
type: docs
weight: 85
url: /tr/python-net/data-filtering/
description: Aspose.Cells for Python via .NET API sını kullanarak veri filtresi eklemenin nasıl yapıldığını öğrenin.
keywords: Python Excel Kütüphanesi, Python Renk Filtresi Ekle, Python Tarih Filtreleri Ekle, Python Sayı Filtreleri Ekle, Python Dinamik Filtre Ekle, Python Metin Filtreleri Ekle, Python İçeren Özel Filtre Ekle, Python İçermeyen Özel Filtre Ekle, Python İle Başlayan Özel Filtre Ekle, Python İle Biten Özel Filtre Ekle, Python Özel Filtre Ekleyin
---

{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerine otomatik filtreleme yapmak için bazı iyi özellikler sunar. Aspose.Cells for Python via .NET, Microsoft Excel'in otomatik filtreleme özelliklerini tamamen destekler. Bu makale, özelliklerin Microsoft Excel'de nasıl kullanılacağını ve bunların Aspose.Cells for Python via .NET kullanılarak nasıl kodlanacağını açıklar.

{{% /alert %}}

## **Veriye Otomatik Filtreleme Uygulama**

Otomatik filtreleme, listede görüntülemek istediğiniz yalnızca öğeleri seçmenin en hızlı yoludur. Otomatik filtreleme özelliği, kullanıcılara belirli bir kriterlere göre listedeki öğeleri filtreleme olanağı sağlar. Metne, sayılara veya tarih bilgilerine göre filtreleme yapın.

### **Microsoft Excel'de Otomatik Filtreleme**

Microsoft Excel'de otomatik filtreleme özelliğini etkinleştirmek için:

1. Bir çalışma sayfasında başlık satırına tıklayın.
1. **Veri** menüsünden **Filtre** seçin ve ardından **Otomatik Filtre**'yi seçin.

Bir çalışma sayfasına otomatik filtre uyguladığınızda, filtre anahtarları (siyah oklar) sütun başlıklarının sağında görünür.

1. Bir filtre okuna tıklayarak filtre seçeneklerinin listesini görüntüleyin.

Otomatik filtre seçeneklerinden bazıları:

|**Seçenekler**|**Açıklama**|
| :- | :- |
|All|Listedeki tüm öğeleri bir kez gösterir.
|Custom|İçerir/içermez gibi özel filtre kriterleri
|Filter by Color|Dolgu rengine göre filtreleme
|Date Filters|Tarihe göre farklı kriterlere dayalı filtreleme
|Number Filters|Karşılaştırma, ortalama ve En Üst 10 vb. gibi sayılar üzerinde farklı filtre türleri.
|Text Filters|Başlangıç, son, içerir vb. gibi farklı filtreler
|Blanks/Non Blanks|Bu filtreler Metin Filtre Boş üzerinden uygulanabilir

Kullanıcılar, Microsoft Excel'de bu seçenekleri kullanarak çalışma sayfalarındaki verileri manuel olarak filtreler.

### **Aspose.Cells for Python Excel Kütüphanesi ile Otomatik Filtrele**

Aspose.Cells for Python via .NET, bir Excel dosyasını temsil eden Workbook adında bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan Worksheets koleksiyonunu içerir.

Bir çalışma sayfası Worksheet sınıfı ile temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir otomatik filtre oluşturmak için AutoFilter sınıfının Worksheet sınıfının AutoFilter özelliğini kullanın. AutoFilter özelliği, başlık satırını oluşturan hücre aralığını belirtmek için Range özelliğini sağlar. Bir otomatik filtre, başlık satırını oluşturan hücre aralığına uygulanır.

Her çalışma sayfasında yalnızca bir filtre aralığı belirleyebilirsiniz. Bu, Microsoft Excel tarafından sınırlıdır. Özel veri filtrelemesi için AutoFilter.Custom yöntemini kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuz gibi Aspose.Cells for Python via .NET kullanarak aynı Otomatik Filtreyi oluşturduk.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Farklı Türlerde Filtre**

Aspose.Cells for Python via .NET, Renk Filtresi, Tarih Filtresi, Sayı Filtresi, Metin Filtresi, Boş Filtreler ve Boş Olmayan Filtreler gibi farklı filtre türleri uygulamak için birden fazla seçenek sunar.

##### **Dolgu Rengi**

Aspose.Cells for Python via .NET, hücrelerin dolgu rengi özelliğine göre verileri filtrelemek için AddFillColorFilter işlevini sağlar. Aşağıdaki örnekte, sayfaın ilk sütununda farklı dolgu renklerine sahip bir şablon dosyası, renk filtreleme işlevini test etmek için kullanılır. Örnek dosyalar aşağıdaki bağlantılardan indirilebilir.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Tarih**

Ocak 2018 tarihine sahip tüm satırları filtrelemek gibi farklı tarih filtreleri uygulanabilir. Aşağıdaki örnek kod, AddDateFilter işlevini kullanarak bu filtrelemeyi göstermektedir. Örnek dosyalar aşağıda verilmiştir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Dinamik Tarih**

Zaman zaman yıla bağlı olmaksızın, örneğin Ocak ayında tüm hücrelerin tarih temelli dinamik filtrelemelere ihtiyaç duyulabilir. Bu durumda DynamicFilter işlevi aşağıdaki örnek kodda olduğu gibi kullanılır. Örnek dosyalar aşağıdaki verilmiştir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Sayı**

Aspose.Cells for Python via .NET ile bir Custom() işlevi kullanarak özel filtreler uygulanabilir. Aşağıdaki örnek, sayıları filtrelemek için Custom() işlevinin kullanımını göstermektedir. Örnek dosyalar aşağıda verilmiştir.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Metin**

Eğer bir sütun metin içeriyorsa ve belirli metni içeren hücreler seçilmek isteniyorsa, Filter() işlevi kullanılabilir. Aşağıdaki örnekte, şablon dosyası ülkelerin listesini içerir ve belirli bir ülke adını içeren satır seçilmelidir. Aşağıdaki kod, metni filtrelemeyi göstermektedir. Örnek dosyalar aşağıda verilmiştir.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Boşluklar**

Eğer bir sütun metin içeriyorsa ve bazı hücreler boşsa ve yalnızca boş hücrelerin bulunduğu satırları seçmek gerekiyorsa, MatchBlanks() işlevi aşağıda gösterildiği gibi kullanılabilir. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBos.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **Boş Olmayanlar**

Herhangi bir metin içeren hücrelerin filtrelenmesi gerektiğinde, aşağıda gösterildiği gibi MatchNonBlanks filtre işlevi kullanılır. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBosOlmayan.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Contains ile Özel filtre**

Excel, belirli bir dize içeren satırları filtrelemek gibi özel filtreler sağlar. Bu özellik, Aspose.Cells for Python via .NET'de mevcuttur ve örnek dosyadaki isimleri filtreleyerek aşağıda gösterilmiştir. Örnek dosyalar aşağıda verilmiştir.

1. [sourseOrnekUlkeIsimleri.xlsx](sourseOrnekUlkeIsimleri.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Contains Kullanmadan Özel filtre**

Excel, belirli bir dize içermeyen satırları filtrelemek gibi özel filtreler sağlar. Bu özellik, Aspose.Cells for Python via .NET'de mevcuttur ve örnek dosyadaki isimleri filtreleyerek aşağıda gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Belirli bir dizeyle Başlayan Özel Filtre**

Excel, belirli bir dize ile başlayan satırları filtrelemek gibi özel filtreler sağlar. Bu özellik, Aspose.Cells for Python via .NET'de mevcuttur ve örnek dosyadaki isimleri filtreleyerek aşağıda gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Belirli Bir Dize ile Biten Özel Filtre**

Excel, belirli bir dize ile biten satırları filtrelemek gibi özel filtreler sağlar. Bu özellik, Aspose.Cells for Python via .NET'de mevcuttur ve örnek dosyadaki isimleri filtreleyerek aşağıda gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Gelişmiş Konular**
- [Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın](/cells/tr/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın](/cells/tr/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
