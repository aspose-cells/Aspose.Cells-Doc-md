---
title: Boş Çalışsayfası Bulma
type: docs
weight: 710
url: /tr/java/detecting-empty-worksheets/
---

## **Doldurulmuş Hücreleri Kontrol Etme**
Çalışsayfaları bir veya daha fazla hücrede (metin, sayısal, tarih/saat gibi) bir değer veya formül veya formül tabanlı bir değer içerebilir. Bu durumda, belirli bir çalışsayfanın boş olup olmadığını tespit etmek kolaydır. Tek yapmamız gereken [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özelliklerini kontrol etmektir. Yukarıdaki özellikler sıfır veya pozitif değerler döndürürse, bir veya daha fazla hücre doldurulmuş demektir, ancak bu özelliklerden herhangi biri -1 değerini döndürürse, bu, verilen çalışsayfada hiçbir hücrenin doldurulmadığını gösterir.

{{% alert color="primary" %}} 

Satırlar ve sütun koleksiyonlarının sıfır temelli bir dizini vardır, bu nedenle 0 satır & 0 sütun ile belirtilen bir hücre çalışsayfasındaki ilk hücre anlamına gelir, yani A1.

{{% /alert %}} 
## **Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir çalışsayfada yalnızca biçimlendirmesi olan hücrelerin olma olasılığı vardır. Bu durumda, [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre biçimlendirmesi nedeniyle başlatılmış ancak doldurulmuş değerlerin yokluğunu gösteren -1 değerini döndürecektir. Bir çalışsayfanın boş başlatılmış hücreler içerip içermediğini kontrol etmek için, Cells koleksiyonundan alınan bir yineç üzerinde *Iterator.hasNext* metodu kullanılması önerilir. *iterator.hasNext* metodu true döndürürse, bu durum verilen çalışsayfada bir veya daha fazla başlatılmış hücre bulunduğunu gösterir.**
Değerleri olan tüm hücreler otomatik olarak başlatılır, ancak bir elektronik tablonun yalnızca biçimlendirme uygulanan hücreleri olabileceği bir olasılık vardır. Bu durumda [Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow) veya [Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn) özellikleri, hücre değerlerinin olmamasını ancak başlatılmış hücreleri belirten -1 değerini döndürecektir. Bir elektronik tablonun boş başlatılmış hücrelere sahip olup olmadığını kontrol etmek için, hücre koleksiyonundan alınan iterator üzerinde *Iterator.hasNext* yöntemini kullanmanız tavsiye edilir. *Iterator.hasNext* yöntemi true döndürürse, bu, verilen elektronik tabloda bir veya daha fazla başlatılmış hücre olduğu anlamına gelir.

{{% alert color="primary" %}} 

Hücreler yineleyicisine ulaşmanın ayrıntıları [Yineleyicilerin Nasıl ve Nerede Kullanılacağı](/cells/tr/java/how-and-where-to-use-iterators/) bölümünde ayrıntılı olarak açıklanmıştır.

{{% /alert %}} 
## **Şekilleri Kontrol Etme**
Verilen bir çalışsayfanın doldurulmuş hücresi olmayabilir, ancak kontrol, grafikler, resimler vb. gibi şekil ve nesneler içerebilir. Bir çalışsayfanın herhangi bir şekil içerip içermediğini kontrol etmek için [ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count) özelliği incelenerek yapılabilir. Herhangi bir pozitif değer, çalışsayfada şekil(ler) bulunduğunu gösterir.
## **Programlama Örneği**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
