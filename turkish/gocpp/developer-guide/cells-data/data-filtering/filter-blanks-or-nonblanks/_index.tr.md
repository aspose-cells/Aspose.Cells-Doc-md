---
title: Golang ve C++ kullanarak Boş veya Dolu Hücreleri Filtreleme
linktitle: Boş veya Boş olmayanları Filtreleme
type: docs
weight: 85
url: /tr/go-cpp/how-to-filter-blanks-and-non-blanks/
description: Boş ve boş olmayan verileri filtrelemek için Aspose.Cells for C++ API kullanımı hakkında bilgi edinin.
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

## **Aspose.Cells ile Boşları Filtreleme**
Bir sütunda az sayıda boş hücre varsa ve yalnızca boş hücreler bulunan satırların seçilmesi gerekiyorsa, [AutoFilter.MatchBlanks(int fieldIndex)] ve [AutoFilter.AddFilter(int fieldIndex, string criteria)] fonksiyonları aşağıda gösterildiği gibi kullanılabilir. 

Lütfen aşağıdaki örnek kodu inceleyin, bu örnek Excel dosyasından (örnek.xlsx) bazı sahte veriler içeren dosyayı yükler. Örnek kod, boşları filtrelemek için üç yöntem kullanır. Daha sonra çalışma kitabını [çıktı Excel dosyası](FiltrelenmişBoşlar.xlsx) olarak kaydeder. 

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterBlanksOrNonblanks.go" >}}
## **Aspose.Cells Kullanarak Boş Olmayanları Filtreleme**

Aşağıdaki örnek kodu inceleyin, bu kod bazı rastgele veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Dosya yüklendikten sonra, [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) fonksiyonunu çağırarak boş olmayan verileri filtreler ve sonunda çalışma kitabını [çıkış Excel dosyası](FilteredNonBlanks.xlsx) olarak kaydeder. 

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterBlanksOrNonblanks-1.go" >}}

