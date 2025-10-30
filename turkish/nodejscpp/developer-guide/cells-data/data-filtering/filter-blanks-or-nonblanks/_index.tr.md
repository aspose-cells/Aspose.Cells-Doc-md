---
title: Boş veya Boş olmayanları Filtreleme
type: docs
weight: 85
url: /tr/nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for Node.js via C++ API sini kullanarak Boş ve Boş Olmayanları Filtrelemeyi Öğrenin.
keywords: Boşları Filtrele, Boş Olmayanları Filtrele, Çalışma sayfasında Boşları Filtrele, Çalışma sayfasında Boş Olmayanları Filtrele, Excel de Boşları Filtrele, Excel de Boş Olmayanları Filtrele, Excel de Boşları ve Boş Olmayanları Filtreleme
---

## **Olası Kullanım Senaryoları**
Excel'de veri filtreleme, kullanıcıların kriterlerine dayalı olarak belirli veri alt kümelerine odaklanmalarını sağlayarak veri analizini, keşfini ve sunumunu geliştiren değerli bir araçtır, bu da genel veri işleme ve yorum sürecini daha verimli ve etkili hale getirir.

## **Excel'de Boş veya Boş Olmayanları Filtreleme**
Excel'de, filtreleme seçeneklerini kullanarak kolayca boş veya boş olmayanları filtreleyebilirsiniz. Bunu nasıl yapabileceğinizi aşağıda bulabilirsiniz:

### **Excel'de Boşları Filtreleme**
1. Aralığı Seçin: Tüm sütunu seçmek için sütun başlığının harfine tıklayın veya boşları filtrelemek istediğiniz aralığı seçin.
1. Filtre Menüsünü Açın: Kurdeledeki "Veri" sekmesine gidin.
<br>
<image src="1.png" width="70%" />
1. Filtre Seçenekleri: "Filtre" düğmesine tıklayın. Bu, seçilen aralığa filtre oklarını ekleyecektir.
1. Boşları Filtrele: Boşları filtrelemek istediğiniz sütundaki filtre okuna tıklayın. "Boşlar" hariç tüm seçenekleri seçmeyin ve Tamam'a tıklayın. Bu, o sütundaki yalnızca boş hücreleri gösterecektir.
<br>
<image src="2.png" width="70%" />
1. Sonuç aşağıdaki gibidir:
<br>
<image src="3.png" width="70%" />

### **Excel'de Boş Olmayanları Filtreleme**
1. Aralığı Seçin: Tüm sütunu seçmek için sütun başlığının harfine tıklayın veya boş olmayanları filtrelemek istediğiniz aralığı seçin.
1. Filtre Menüsünü Açın: Kurdeledeki "Veri" sekmesine gidin.
<br>
<image src="1.png" width="70%" />
1. Filtre Seçenekleri: "Filtre" düğmesine tıklayın. Bu, seçilen aralığa filtre oklarını ekleyecektir.
1. Boş Olmayanları Filtrele: Boş olmayanları filtrelemek istediğiniz sütundaki filtre okuna tıklayın. "Boş olmayanlar" veya "Özel" dışındaki tüm seçenekleri kaldırın ve koşulları ayarlayın. Tamam'a tıklayın. Bu, o sütundaki yalnızca boş olmayan hücreleri gösterecektir.
<br>
<image src="4.png" width="70%" />
1. Sonuç aşağıdaki gibidir:
<br>
<image src="5.png" width="70%" />

## **Aspose.Cells for Node.js via C++ kullanarak Boşlukları Nasıl Filtreleriz**
Bir sütunda çok az hücre boş ise ve sadece boş hücrelerin olduğu satırları seçmek gerekiyorsa, [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) ve [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) fonksiyonları aşağıda gösterildiği gibi kullanılabilir. 

Lütfen aşağıdaki örnek kodu inceleyin, bu örnek Excel dosyasından (örnek.xlsx) bazı sahte veriler içeren dosyayı yükler. Örnek kod, boşları filtrelemek için üç yöntem kullanır. Daha sonra çalışma kitabını [çıktı Excel dosyası](FiltrelenmişBoşlar.xlsx) olarak kaydeder. 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}


## **Aspose.Cells for Node.js via C++ kullanarak Boş Olmayanları Nasıl Filtreleriz**

Lütfen aşağıdaki örnek kodu inceleyin; bu kod, bazı sahte veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Dosyayı yükledikten sonra, boş olmayan verileri filtrelemek için [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) fonksiyonunu çağırın ve sonunda çalışma kitabını [çıktı Excel dosyasıyla](FilteredNonBlanks.xlsx) kaydedin. 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
