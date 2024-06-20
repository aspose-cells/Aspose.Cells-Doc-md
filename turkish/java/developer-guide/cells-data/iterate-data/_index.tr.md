---
title: Iterator ların Nasıl ve Nerede Kullanılacağı
linktitle: Verileri Yinele
type: docs
weight: 640
url: /tr/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

Iterator arabirimine ait bir nesne, bir koleksiyonun tüm elemanlarında dolaşmak için kullanılabilir. Iterator'lar bir koleksiyondaki verileri incelemek için kullanılabilir, ancak temel koleksiyonu değiştirmek için kullanılamazlar. Genel olarak, bir koleksiyonun içeriğinde döngü yapmak için şu adımlar izlenmelidir:

1. Koleksiyonun iterator yöntemini çağırarak koleksiyonun başlangıcına bir iterator elde edin.
1. hasNext yöntemini çağıran bir döngü kurun. Döngünün hasNext yöntemi true döndüğü sürece devam etmesini sağlayın.
1. Döngü içinde next yöntemini çağırarak her bir elemanı alın.

Aspose.Cells API'leri birçok iterator sağlar, ancak bu makale ağırlıklı olarak aşağıda listelenen üç türü tartışmaktadır.

1. Hücreler Iterator'ı
1. Satırlar Iterator'ı
1. Sütunlar Iterator'ı

{{% /alert %}} 
## **Iterator'ların Nasıl Kullanılacağı**
### **Hücreler Iterator'ı**
Hücrelerin iterator'una erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak herhangi birini kullanabilirsiniz. İşte hücrelerin iterator'ını döndüren yöntemler:

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Yukarıda bahsedilen tüm yöntemler, başlatılmış hücreler koleksiyonunu dolaşmaya izin veren iterator'ı döndürür.

{{% alert color="primary" %}} 

Hücreleri dolaşırken koleksiyonun değiştirilmemesi gerekir (yeni bir Hücre oluşturan veya mevcut bir Hücreyi silen işlemler). Aksi takdirde iterator tüm hücreleri düzgün bir şekilde dolaşamayabilir (bazı elemanlar tekrarlanabilir veya atlanabilir).

{{% /alert %}} 

Aşağıdaki kod örneği, bir hücre koleksiyonu için Iterator sınıfının uygulanmasını göstermektedir.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Satırlar Iterator'ı**
Satırlar Iterator'ı, RowCollection.iterator yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, RowCollection sınıfı için Iterator'ın uygulanmasını göstermektedir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Sütunlar Iterator'ı**
Sütunlar Iterator'ı, ColumnCollection.iterator yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, ColumnCollection sınıfı için Iterator'ın uygulanmasını göstermektedir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Iterator'ların Nerede Kullanılacağı**
Iterator'ların kullanılmasının avantajlarını tartışmak için gerçek bir örnek ele alalım.
##### **Senaryo**
Bir uygulama gereksinimi, belirli bir Çalışma Sayfasındaki tüm hücreleri gezinerek değerlerini okumaktır. Bu hedefi uygulamanın birkaç yolu olabilir. Bazıları aşağıda gösterilmiştir.
###### **Görüntü Aralığı Kullanarak**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **MaxDataRow & MaxDataColumn Kullanarak**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Yukarıda bahsedilen her iki yaklaşımın da oldukça benzer mantığı kullandığını görebilirsiniz; yani, koleksiyondaki tüm hücrelerin üzerinden dolaşmak. Bu, aşağıda tartışılan birkaç nedenle sorunlu olabilir.

1. MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange gibi API'ler, ilgili istatistikleri toplamak için ekstra zaman gerektirir. Veri matrisi (satır x sütun) büyükse, bu API'leri kullanmak performans cezası getirebilir.
1. Çoğu durumda, verilen bir aralıktaki tüm hücreler oluşturulmamıştır. Bu tür durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmekten daha verimli değildir.
1. Bir döngü içinde Cells.get(rowIndex, columnIndex) gibi bir hücreye erişmek, bir aralıktaki tüm hücre nesnelerinin oluşturulmasına neden olur, bu da sonunda OutOfMemoryError'a neden olabilir.
##### **Sonuç**
Yukarıda belirtilen gerçeklere dayanarak, yineleyicilerin kullanılması gereken olası senaryolar aşağıda belirtilmiştir.

1. Hücre koleksiyonunun salt okunur erişimi gereklidir; yani, yalnızca hücreleri denetlemek gereklidir.
1. Büyük sayıda hücre gezilmelidir.
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar gezilmelidir.
