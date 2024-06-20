---
title: Satır ve Sütunları Kopyalama
type: docs
weight: 30
url: /tr/java/copying-rows-and-columns/
---

## **Giriş**
Bazen, bir çalışma sayfasında tüm çalışma sayfasını kopyalamadan satır ve sütunları kopyalamanız gerekir. Aspose.Cells ile, çalışma kitapları arasında veya içinde satır ve sütunları kopyalamak mümkündür.

Bir satır (veya sütun) kopyalandığında, içindeki veriler, güncellenmiş referanslarla formülleri - ve değerleri, yorumları, biçimlendirmeyi, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini içeren veriler de kopyalanır.
## **Microsoft Excel ile Satır ve Sütunları Kopyalama**
1. Kopyalamak istediğiniz satırı veya sütunu seçin.
1. Satır veya sütunları kopyalamak için **Standart** araç çubuğunda **Kopyala**'yı tıklayın veya **CTRL**+**C**'ye basın.
1. Kopyalamak istediğiniz seçimin altında veya sağındaki bir satır veya sütunu seçin.
1. Satır veya sütunları kopyalarken, **Ekle** menüsünde **Kopyalanan Hücreler**'i tıklayın.

{{% alert color="primary" %}} 

Hedef hücrelerin içeriği herhangi bir içeriği Çıkar veya tıklamak yerine **Standart** araç çubuğunda **Yapıştır**'ı tıklarsanız değiştirilir.

{{% /alert %}} 

## **Tek Satır Kopyalama**

Aspose.Cells, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) sınıfının [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) metodunu sağlar. Bu metod, kaynak satırdan hedef satıra formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.

[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) metodu şu parametreleri alır:

- kaynak [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) nesnesi,
- kaynak satır dizini, ve
- hedef satır dizini.

Bu metodu bir sayfa içinde bir satırı kopyalamak veya başka bir sayfaya kopyalamak için kullanın. [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) metodu Microsoft Excel'de kullanılan şekilde çalışır. Örneğin, hedef satırın yüksekliğini açıkça ayarlamak zorunda değilsiniz, bu değer de kopyalanır.

Aşağıdaki örnek, bir çalışsayfasında bir satır kopyalamayı gösterir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veri, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı çalışsayfadaki 12. satıra yapıştırır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Aşağıdaki kod çalıştırıldığında aşağıdaki çıktı üretilir.

**Satır en yüksek hassasiyet ve doğrulukla kopyalanır** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Satırları kopyalarken, ilgili resimler, grafikler veya diğer çizim nesnelerinin Microsoft Excel ile aynı olduğu gibi dikkate alınması önemlidir:

1. Kaynak satır dizini 5 ise, resim, grafik vb., başlangıç satır dizini 4 ve bitiş satır dizini 6 içinde bulunduruluyorsa kopyalanır.
1. Var olan resimler, grafikler vb. hedef satırdan silinmez.

{{% /alert %}} 

## **Birden Fazla Satır Kopyalama**

[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) yöntemini kullanarak bir tamsayı türünde ek bir parametre kullanarak yeni bir hedefe birden çok satır kopyalayabilirsiniz.

Aşağıda, 3 veri satırı içeren giriş elektronik tablosunun bir görüntüsü bulunmakta, aşağıdaki kod örneği tüm 3 satırı 7. satırdan başlayarak yeni bir konuma kopyalar.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Yukarıdaki kod örneği yürütüldükten sonra elde edilen elektronik tablo görünümü aşağıda verilmektedir.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Tek Sütun Kopyalama**

Aspose.Cells, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) sınıfının [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metodunu sağlar, bu metod kaynak sütundan hedef sütuna formüller (güncellenmiş referanslarla) ve değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.

[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metodu şu parametreleri alır:

- kaynak [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) nesnesi,
- kaynak sütun indeksi ve
- hedef sütun indeksi.

[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metodunu bir sayfa içinde bir sütunu kopyalamak veya başka bir sayfaya kopyalamak için kullanın.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.

**Bir çalışma kitabından bir sütun diğerine kopyalanır** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Birden Çok Sütunun Kopyalanması**

[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) yöntemine benzer şekilde, Aspose.Cells API'leri ayrıca birden çok kaynak sütunu yeni bir konuma kopyalamak için [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) yöntemini sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

İşte Excel'de kaynak ve sonuç çalışma kitapları nasıl görünür:

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Yapıştırma Seçenekleri ile Satır/Sütunları Yapıştırma**
Aspose.Cells artık [Yapıştırma Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) sağlar ve aynı zamanda [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) ve [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)) fonksiyonlarını kullanırken uygun yapıştırma seçeneklerinin Excel'e benzer şekilde ayarlanmasına izin verir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

