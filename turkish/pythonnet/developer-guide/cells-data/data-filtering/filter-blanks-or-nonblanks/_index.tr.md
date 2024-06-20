---
title: Boş veya Boş olmayanları Filtreleme
type: docs
weight: 85
url: /tr/python-net/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for Python via .NET API kullanarak Boş ve boş olmayanları filtreleme nasıl yapılır öğrenin.
keywords: Python Excel Kütüphanesi, Python Boşlukları Filtrele, Python Boş Olmayanları Filtrele, Python Çalışma sayfasında Boşlukları Filtrele, Python Çalışma sayfasında Boş Olmayanları Filtrele, Python Excel de Boşlukları Filtrele, Python Excel de Boş Olmayanları Filtrele, Python Excel de Boşlukları ve Boş Olmayanları Filtrele
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

## **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Boşlukları Filtreleme**
Eğer bir sütun metin içeriyorsa ve bazı hücreler boşsa, boş hücreleri seçmek için [AutoFilter.match_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_blanks/#int) ve [AutoFilter.add_filter(field_index, criteria)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/add_filter/#int) metodları aşağıda gösterildiği gibi kullanılabilir. 

Lütfen aşağıdaki örnek kodu inceleyin, bu örnek Excel dosyasından (örnek.xlsx) bazı sahte veriler içeren dosyayı yükler. Örnek kod, boşları filtrelemek için üç yöntem kullanır. Daha sonra çalışma kitabını [çıktı Excel dosyası](FiltrelenmişBoşlar.xlsx) olarak kaydeder. 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-blanks.py" >}}

## **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Boş Olmayanları Filtreleme**

[Örnek Excel dosyasını](sample.xlsx) yükledikten sonra, boş olmayan verileri filtrelemek için [AutoFilter.match_non_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_non_blanks/#int) fonksiyonunu çağırın ve son olarak çalışma kitabını [çıktı Excel dosyası](FilteredNonBlanks.xlsx) olarak kaydedin. 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-non-blanks.py" >}}

