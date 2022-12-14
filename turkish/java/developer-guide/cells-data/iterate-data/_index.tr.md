---
title: Yineleyiciler Nasıl ve Nerede Kullanılır?
linktitle: Verileri Yinele
type: docs
weight: 640
url: /tr/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

Yineleyici arabiriminin bir nesnesi, bir koleksiyonun tüm öğeleri arasında gezinmek için kullanılabilir. Yineleyiciler, bir koleksiyondaki verileri incelemek için kullanılabilir, ancak temeldeki koleksiyonu değiştirmek için kullanılamaz. Genel olarak, bir koleksiyonun içerikleri arasında geçiş yapmak üzere bir yineleyici kullanmak için aşağıdaki adımlar atılmalıdır:

1. Koleksiyonun yineleyici yöntemini çağırarak koleksiyonun başlangıcına bir yineleyici edinin.
1. hasNext yöntemine çağrı yapan bir döngü kurun. HasNext yöntemi true değerini döndürdüğü sürece döngünün yinelenmesini sağlayın.
1. Döngü içinde, sonraki yöntemi çağırarak her bir öğeyi elde edin.

Aspose.Cells API'ler bir dizi yineleyici sağlar, ancak bu makale temel olarak aşağıda listelenen üç türü tartışır.

1. Cells Yineleyici
1. Satır Yineleyici
1. Sütunlar Yineleyici

{{% /alert %}} 
## **Yineleyiciler nasıl kullanılır?**
### **Cells Yineleyici**
Hücrelerin yineleyicisine erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine göre bu yöntemlerden herhangi biri kullanılabilir. İşte hücrelerin yineleyicisini döndüren yöntemler.

1. Cells.iterator
1. Satır.yineleyici
1. Range.iterator

Yukarıda belirtilen yöntemlerin tümü, başlatılmış olan hücrelerin koleksiyonunda gezinmeye izin veren yineleyiciyi döndürür.

{{% alert color="primary" %}} 

Hücreler arasında gezinirken koleksiyon değiştirilmemelidir (yeni bir Cell'in başlatılmasına veya mevcut Cell'in silinmesine neden olacak işlemler). Aksi takdirde, yineleyici tüm hücreleri doğru bir şekilde geçemeyebilir (bazı öğeler tekrar tekrar geçilebilir veya atlanabilir).

{{% /alert %}} 

Aşağıdaki kod örneği, bir hücre koleksiyonu için Iterator sınıfının uygulanmasını gösterir.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Satır Yineleyici**
Rows Iterator'a RowCollection.iterator yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, Iterator for RowCollection sınıfının uygulanmasını gösterir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Sütunlar Yineleyici**
Columns Iterator'a ColumnCollection.iterator yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, Iterator for ColumnCollection sınıfının uygulanmasını gösterir.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Yineleyiciler nerede kullanılır?**
Yineleyici kullanmanın avantajlarını tartışmak için gerçek zamanlı bir örnek alalım.
##### **Senaryo**
Bir uygulama gereksinimi, değerlerini okumak için belirli bir Çalışma Sayfasındaki tüm hücreleri geçmektir. Bu hedefi gerçekleştirmenin birkaç yolu olabilir. Birkaçı aşağıda gösterilmiştir.
###### **Görüntüleme Aralığını Kullanma**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **MaxDataRow ve MaxDataColumn'u Kullanma**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Yukarıda bahsedilen yaklaşımların her ikisinin de aşağı yukarı benzer bir mantık kullandığını gözlemleyebileceğiniz gibi; hücre değerlerini okumak için koleksiyondaki tüm hücreler üzerinde döngü yapın. Bu, aşağıda tartışıldığı gibi birkaç nedenden dolayı sorunlu olabilir.

1. MaxRow, MaxDataRow, MaxColumn, MaxDataColumn ve MaxDisplayRange gibi API'ler ilgili istatistikleri toplamak için fazladan zaman gerektirir. Veri matrisinin (satır x sütun) büyük olması durumunda, bu API'lerin kullanılması performans düşüşüne neden olabilir.
1. Çoğu durumda, belirli bir aralıktaki tüm hücreler örneklenmez. Bu gibi durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmeye kıyasla o kadar verimli değildir.
1. Döngüdeki bir hücreye Cells.get(rowIndex, columnIndex) olarak erişilmesi, bir aralıktaki tüm hücre nesnelerinin somutlaştırılmasına neden olur ve bu da sonunda OutOfMemoryError'a neden olabilir.
##### **Çözüm**
Yukarıda belirtilen gerçeklere dayanarak, yineleyicilerin kullanılması gereken olası senaryolar aşağıdadır.

1. Hücre koleksiyonuna salt okunur erişim gereklidir, yani; gereksinim sadece hücreleri incelemektir.
1. Çok sayıda hücre geçilecek.
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar geçilmelidir.
