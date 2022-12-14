---
title: Satırları ve Sütunları Kopyalama
type: docs
weight: 30
url: /tr/java/copying-rows-and-columns/
---
## **giriiş**
Bazen, tüm çalışma sayfasını kopyalamadan çalışma sayfasındaki satırları ve sütunları kopyalamanız gerekir. Aspose.Cells ile çalışma kitaplarının içinde veya arasında satır ve sütun kopyalamak mümkündür.

Bir satır (veya sütun) kopyalandığında, güncellenmiş referanslara sahip formüller ve değerler, yorumlar, biçimlendirme, gizli hücreler, resimler ve diğer çizim nesneleri de dahil olmak üzere içerdiği veriler de kopyalanır.
## **Microsoft Excel ile Satırları ve Sütunları Kopyalama**
1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1.  Satırları veya sütunları kopyalamak için tıklayın**Kopyala** üzerinde**Standart** araç çubuğu veya tuşuna basın**CTRL**+**C**.
1. Seçiminizi kopyalamak istediğiniz yerin altından veya sağından bir satır veya sütun seçin.
1.  Satırları veya sütunları kopyalarken,**Cells kopyalandı** üzerinde**Sokmak** Menü.

{{% alert color="primary" %}} 

 eğer tıklarsan**Yapıştırmak** üzerinde**Standart** araç çubuğu veya basın**CTRL**+** üzerindeki bir komuta tıklamak yerine V****Ekle** menüsünde, hedef hücrelerin içeriği değiştirilir.

{{% /alert %}} 

## **Tek Satır Kopyalama**

 Aspose.Cells şunları sağlar:[kopya satırı](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)sınıf. Bu yöntem, formüller, değerler, yorumlar, hücre formatları, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak satırdan hedef satıra kopyalar.

 bu[kopya satırı](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) yöntemi aşağıdaki parametreleri alır:

-  kaynak[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)nesne,
- kaynak satır dizini ve
- hedef satır dizini.

 Bir sayfadaki bir satırı veya başka bir sayfaya kopyalamak için bu yöntemi kullanın. bu[kopya satırı](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) yöntemi, Microsoft Excel'e benzer şekilde çalışır. Yani, örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yoktur, o değer de kopyalanır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl kopyalanacağını gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı kopyalar (veriler, biçimlendirme, yorumlar, resimler vb. İle birlikte) ve aynı çalışma sayfasındaki 12. satıra yapıştırır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Aşağıdaki kod çalıştırıldığında aşağıdaki çıktı üretilir.

**Satır, en yüksek düzeyde kesinlik ve doğrulukla kopyalanır** 

![yapılacaklar:resim_alternatif_Metin](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Microsoft Excel'de olduğu gibi, satırları kopyalarken ilgili resimleri, çizelgeleri veya diğer çizim nesnelerini not etmek önemlidir:

1. Kaynak satır dizini 5 ise, resim, grafik vb. üç satırda bulunuyorsa kopyalanır (başlangıç satır dizini 4 ve bitiş satır dizini 6'dır).
1. Hedef satırdaki mevcut resimler, çizelgeler vb. kaldırılmayacaktır.

{{% /alert %}} 

## **Birden Çok Satırı Kopyalama**

 kullanırken birden çok satırı yeni bir hedefe de kopyalayabilirsiniz.[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) kopyalanacak kaynak satır sayısını belirtmek için tamsayı türünde ek bir parametre alan yöntem.

Aşağıda, 3 satır veri içeren giriş e-tablosunun bir anlık görüntüsü bulunurken, aşağıda verilen kod parçacığı, 3 satırın tümünü 7. sıradan başlayarak yeni bir konuma kopyalar.

![yapılacaklar:resim_alternatif_Metin](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

İşte yukarıdaki kod parçacığını yürüttükten sonra ortaya çıkan elektronik tablo görünümü.

![yapılacaklar:resim_alternatif_Metin](copy-rows-and-columns_4.png)

## **Tek Sütunu Kopyalama**

 Aspose.Cells şunları sağlar:[kopya sütunu](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Bu yöntem, güncellenmiş referanslarla formüller ve değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kaynak sütundan hedef sütuna kopyalar.

 bu[kopya sütunu](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) yöntemi aşağıdaki parametreleri alır:

-  kaynak[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)nesne,
- kaynak sütun dizini ve
- hedef sütun dizini.

 Kullan[kopya sütunu](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) bir sayfadaki bir sütunu veya başka bir sayfaya kopyalama yöntemi.

Bu örnek, bir çalışma sayfasındaki bir sütunu kopyalar ve başka bir çalışma kitabındaki bir çalışma sayfasına yapıştırır.

**Bir sütun bir çalışma kitabından diğerine kopyalanır** 

![yapılacaklar:resim_alternatif_Metin](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Birden Çok Sütunu Kopyalama**

 Benzer[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) ) yöntemi, Aspose.Cells API'leri ayrıca şunları sağlar:[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) yöntemi, birden çok kaynak sütunu yeni bir konuma kopyalamak için kullanılır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Kaynak ve sonuçtaki e-tabloların Excel'de nasıl göründüğü aşağıda açıklanmıştır.

![yapılacaklar:resim_alternatif_Metin](copy-rows-and-columns_7.png)

![yapılacaklar:resim_alternatif_Metin](copy-rows-and-columns_8.png)


## **Yapıştırma Seçenekleriyle Satırları/Sütunları Yapıştırma**
 Aspose.Cells şimdi sağlıyor[Seçenekleri Yapıştır](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) fonksiyonları kullanırken[Satırları Kopyala](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) ve[Sütunları Kopyala](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Excel'e benzer uygun yapıştırma seçeneklerinin ayarlanmasına izin verir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

