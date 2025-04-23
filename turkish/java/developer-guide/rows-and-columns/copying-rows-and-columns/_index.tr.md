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

Aspose.Cells, [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) metodunu sağlar. Bu metod kaynak satırdan hedef satıra formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.

[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) metodu aşağıdaki parametreleri alır:

- kaynak [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) nesnesi,
- kaynak satır dizini, ve
- hedef satır dizini.

Bu metod, bir sayfa içinde veya başka bir sayfaya satır kopyalamak için kullanılır. [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) metodu Microsoft Excel ile benzer şekilde çalışır. Yani, hedef satırın yüksekliğini açıkça ayarlamanıza gerek kalmaz, bu değer de kopyalanır.

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

[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) yöntemini kullanarak bir tamsayı türünde ek bir parametre kullanarak yeni bir hedefe birden çok satır kopyalayabilirsiniz.

Aşağıda, 3 veri satırı içeren giriş elektronik tablosunun bir görüntüsü bulunmakta, aşağıdaki kod örneği tüm 3 satırı 7. satırdan başlayarak yeni bir konuma kopyalar.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Yukarıdaki kod örneği yürütüldükten sonra elde edilen elektronik tablo görünümü aşağıda verilmektedir.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Tek Sütun Kopyalama**

Aspose.Cells, [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-)  metodunu sağlar ve bu yöntem, formüller ile güncellenmiş referanslar dahil olmak üzere tüm veri türlerini, değerleri, yorumları, hücre biçimlerini, gizli hücreleri, resimleri ve diğer çizim nesnelerini kaynak sütundan hedef sütuna kopyalar.

[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) yöntemi aşağıdaki parametreleri alır:

- kaynak [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) nesnesi,
- kaynak sütun indeksi ve
- hedef sütun indeksi.

Bir sütunu bir sayfa içinde veya başka bir sayfaya kopyalamak için [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) yöntemini kullanın.

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.

**Bir çalışma kitabından bir sütun diğerine kopyalanır** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Birden Çok Sütunun Kopyalanması**

[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) yöntemine benzer şekilde, Aspose.Cells API'leri ayrıca birden çok kaynak sütunu yeni bir konuma kopyalamak için [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns-com.aspose.cells.Cells-int-int-int-) yöntemini sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

İşte Excel'de kaynak ve sonuç çalışma kitapları nasıl görünür:

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Yapıştırma Seçenekleri ile Satır/Sütunları Yapıştırma**
Aspose.Cells şu anda [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) sağlar ve fonksiyonlar [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows-com.aspose.cells.Cells-int-int-int-com.aspose.cells.CopyOptions-com.aspose.cells.PasteOptions-) ve [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns-com.aspose.cells.Cells-int-int-int-com.aspose.cells.PasteOptions-) ile kullanılır. Bu, uygun yapıştırma seçenekleri ayarlamaya olanak tanır ve Excel'e benzer şekilde kullanılır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

{{< app/cells/assistant language="java" >}}
