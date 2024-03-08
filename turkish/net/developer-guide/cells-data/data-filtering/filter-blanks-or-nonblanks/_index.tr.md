---
title: Boşlukları veya Boş Olmayanları Filtreleme
type: docs
weight: 85
url: /tr/net/how-to-filter-blanks-and-non-blanks/
description: Aspose.Cells for .NET API'i kullanarak Boşlukları ve boşluk olmayanları nasıl filtreleyeceğinizi öğrenin.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **Olası Kullanım Senaryoları**
Excel'de verileri filtrelemek, kullanıcıların kendi kriterlerine göre belirli veri alt kümelerine odaklanmasını sağlayarak veri analizini, keşfini ve sunumunu geliştiren, genel veri işleme ve yorumlama sürecini daha verimli ve etkili hale getiren değerli bir araçtır.

##  **Excel'de Boşlukları veya Boş Olmayanları Filtreleme**
Excel'de filtreleme seçeneklerini kullanarak boşlukları veya boşluk olmayanları kolayca filtreleyebilirsiniz. Bunu nasıl yapabileceğiniz aşağıda açıklanmıştır:

###  **Excel'de Boşlukları Filtreleme**
1. Aralığı Seçin: Tüm sütunu seçmek için sütun başlığının harfine tıklayın veya boşlukları filtrelemek istediğiniz aralığı seçin.
1. Filtre Menüsünü açın: Şeritteki "Veri" sekmesine gidin.
<br>
<image src="1.png" width="70%" />
1. Filtre Seçenekleri: "Filtrele" butonuna tıklayın. Bu, seçilen aralığa filtre okları ekleyecektir.
1. Boşlukları Filtrele: Boşlukları filtrelemek istediğiniz sütundaki filtre okuna tıklayın. "Boşluklar" dışındaki tüm seçeneklerin seçimini kaldırın ve Tamam'a tıklayın. Bu, yalnızca o sütundaki boş hücreleri gösterecektir.
<br>
<image src="2.png" width="70%" />
1. Sonuç şu şekilde:
<br>
<image src="3.png" width="70%" />

###  **Excel'de Boş Olmayanları Filtreleme**
1. Aralığı Seçin: Tüm sütunu seçmek için sütun başlığının harfine tıklayın veya boşluk olmayanları filtrelemek istediğiniz aralığı seçin.
1. Filtre Menüsünü açın: Şeritteki "Veri" sekmesine gidin.
<br>
<image src="1.png" width="70%" />
1. Filtre Seçenekleri: "Filtrele" butonuna tıklayın. Bu, seçilen aralığa filtre okları ekleyecektir.
1. Boş Olmayanları Filtrele: Boş olmayanları filtrelemek istediğiniz sütundaki filtre okuna tıklayın. "Boş olmayanlar" veya "Özel" dışındaki tüm seçeneklerin seçimini kaldırın ve koşulları buna göre ayarlayın. Tamam'ı tıklayın. Bu, yalnızca o sütunda boş olmayan hücreleri görüntüler.
<br>
<image src="4.png" width="70%" />
1. Sonuç şu şekilde:
<br>
<image src="5.png" width="70%" />

##  **Aspose.Cells kullanarak Boşlukları Filtreleme**
 Bir sütun, birkaç hücrenin boş olacağı şekilde metin içeriyorsa ve yalnızca boş hücrelerin bulunduğu satırları seçmek için filtre gerekiyorsa,[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) Ve[AutoFilter.AddFilter(int fieldIndex, dize ölçütü)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) fonksiyonlar aşağıda gösterildiği gibi kullanılabilir.

 Lütfen aşağıdaki örnek koda bakın.[örnek Excel dosyası](sample.xlsx) bazı sahte veriler içeriyor. Örnek kod, boşlukları filtrelemek için üç yöntem kullanır. Daha sonra çalışma kitabını şu şekilde kaydeder:[Excel dosyasının çıktısı](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **Aspose.Cells'i kullanarak Boş Olmayanları Filtreleme**

 Lütfen aşağıdaki örnek koda bakın.[örnek Excel dosyası](sample.xlsx) bazı sahte veriler içeriyor. Dosyayı yükledikten sonra çağrı yapın.[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) Boş olmayan verileri filtreleme ve son olarak çalışma kitabını kaydetme işlevi[Excel dosyasının çıktısı](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

