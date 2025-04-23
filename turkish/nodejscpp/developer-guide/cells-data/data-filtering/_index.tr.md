---
title: Veri Filtreleme
type: docs
weight: 85
url: /tr/nodejs-cpp/data-filtering/
description: Aspose.Cells for Node.js via C++ API sini kullanarak veri filtresi eklemeyi öğrenin.
keywords: Renk ile Filtre Ekle Node.js ve C++ kullanımı, Tarih Filtresi Ekle Node.js ve C++ kullanımı, Sayı Filtreleri Ekle Node.js ve C++ kullanımı, Dinamik Filtre Ekle Node.js ve C++ kullanımı, Metin Filtreleri Ekle Node.js ve C++ kullanımı, İçerdiği gibi özel filtre ekleme Node.js ve C++ kullanımı, İçermemesi gibi özel filtre ekleme Node.js ve C++ kullanımı, Başlangıca Göre özel filtre ekleme Node.js ve C++ kullanımı, Bitişe Göre özel filtre ekleme Node.js ve C++ kullanımı
---

{{% alert color="primary" %}}
Microsoft Excel, çalışma sayfası verileri otomatik filtreleme için bazı iyi özellikler sunar. Aspose.Cells, Microsoft Excel'in otomatik filtreleme özelliklerini tam destekler. Bu makale, bu özelliklerin Microsoft Excel'de nasıl kullanılacağını ve Aspose.Cells for Node.js via C++ kullanılarak nasıl kodlanacağını açıklar.
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

### **Aspose.Cells for Node.js via C++ ile Otomatik Filtre**

Aspose.Cells, Excel dosyasını temsil eden Bir Excel dosyasını temsil eden Workbook sınıfını sağlar. Workbook sınıfı, her bir çalışma sayfasına erişime izin veren Worksheets koleksiyonunu içerir.

Bir çalışma sayfası Worksheet sınıfı ile temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir otomatik filtre oluşturmak için AutoFilter sınıfının Worksheet sınıfının AutoFilter özelliğini kullanın. AutoFilter özelliği, başlık satırını oluşturan hücre aralığını belirtmek için Range özelliğini sağlar. Bir otomatik filtre, başlık satırını oluşturan hücre aralığına uygulanır.

Her çalışma sayfasında yalnızca bir filtre aralığı belirleyebilirsiniz. Bu, Microsoft Excel tarafından sınırlıdır. Özel veri filtrelemesi için AutoFilter.Custom yöntemini kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanılarak oluşturulan aynı Otomatik Filtre Aspose.Cells for Node.js via C++ kullanılarak oluşturuldu.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **Farklı Türlerde Filtre**

Aspose.Cells, Renk Filtresi, Tarih Filtresi, Sayı Filtresi, Metin Filtresi, Boş Filtreler ve Dolu Filtreler gibi farklı filtre türleri uygulamak için birden fazla seçenek sağlar.

##### **Dolgu Rengi**

Aspose.Cells, hücrelerin dolum rengi özelliğine göre verileri filtrelemek için AddFillColorFilter fonksiyonunu sağlar. Aşağıdaki örnekte, sayfanın ilk sütununda farklı dolgu renklerine sahip bir şablon dosyası, renk filtreleme işlevini test etmek için kullanılmaktadır. Örnek dosyalar aşağıdaki bağlantılardan indirilebilir.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **Tarih**

Farklı tarih filtreleri uygulanabilir, örneğin, Ocak 2018 tarihleri olan tüm satırları filtreleme. Aşağıdaki örnek kod bu filtreyi AddDateFilter fonksiyonu kullanarak gösterir. Örnek dosyalar aşağıda verilmiştir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **Dinamik Tarih**

Zaman zaman yıla bağlı olmaksızın, örneğin Ocak ayında tüm hücrelerin tarih temelli dinamik filtrelemelere ihtiyaç duyulabilir. Bu durumda DynamicFilter işlevi aşağıdaki örnek kodda olduğu gibi kullanılır. Örnek dosyalar aşağıdaki verilmiştir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **Sayı**

Aspose.Cells ile Özel filtreler, belirli bir aralıktaki sayıları seçmek gibi uygulanabilir. Aşağıdaki örnek, sayıları filtreleme işlevini göstermek için Custom() fonksiyonunun kullanımını göstermektedir. Örnek dosyalar aşağıda verilmiştir.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **Metin**

Bir sütun metin içeriyorsa ve belirli bir metin içeren hücreler seçilecekse, Filter() fonksiyonu kullanılabilir. Aşağıdaki örnekte, şablon dosyası bir ülke listesi içerir ve satır belirli bir ülke adı içeriyorsa seçilir. Aşağıdaki kod, metin filtrelemeyi gösterir. Örnek dosyalar aşağıda verilmiştir.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **Boşluklar**

Eğer bir sütun metin içeriyorsa ve bazı hücreler boşsa ve yalnızca boş hücrelerin bulunduğu satırları seçmek gerekiyorsa, MatchBlanks() işlevi aşağıda gösterildiği gibi kullanılabilir. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBos.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **Boş Olmayanlar**

Herhangi bir metin içeren hücrelerin filtrelenmesi gerektiğinde, aşağıda gösterildiği gibi MatchNonBlanks filtre işlevi kullanılır. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBosOlmayan.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **Contains ile Özel filtre**

Excel, bazı belirli dizeleri içeren satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir. Örnek dosyalar aşağıda verilmiştir

1. [sourseOrnekUlkeIsimleri.xlsx](sourseOrnekUlkeIsimleri.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **Contains Kullanmadan Özel filtre**

Excel, belirli bir dizge içermeyen satırları filtrelemek gibi özelleştirilmiş filtreler sağlar. Bu özellik Aspose.Cells'ta mevcuttur ve aşağıdaki örnek, verilen örnek dosyadaki isimleri filtreleyerek gösterir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **Belirli bir dizeyle Başlayan Özel Filtre**

Excel, belirli bir dizge ile başlayan satırları filtreleme gibi özelleştirilmiş filtreler sağlar. Bu özellik Aspose.Cells'ta mevcuttur ve aşağıdaki örnek, verilen örnek dosyadaki isimleri filtreleyerek gösterir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **Belirli Bir Dize ile Biten Özel Filtre**

Excel, Aspose.Cells'de mevcut olan ve aşağıdaki örnek dosyadaki isimleri filtreleyerek aşağıda gösterildiği gibi belirli bir dizeyle biten satırları filtreleyen özel filtreler sağlar.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **Gelişmiş Konular**
- [Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın](/cells/tr/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın](/cells/tr/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
