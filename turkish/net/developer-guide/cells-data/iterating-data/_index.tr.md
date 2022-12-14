---
title: Numaralandırıcılar Nasıl ve Nerede Kullanılır?
linktitle: Verileri Yinele
type: docs
weight: 55
url: /tr/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

Numaralandırıcı, bir kapsayıcı veya koleksiyon arasında geçiş yapma yeteneği sağlayan bir nesnedir. Numaralandırıcılar, koleksiyondaki verileri okumak için kullanılabilir, ancak temeldeki koleksiyonu değiştirmek için kullanılamazlar, oysa IEnumerable, bir IEnumerator arabirimi döndüren GetEnumerator yöntemini tanımlayan bir arabirimdir; bu da, salt okunur erişime izin verir. bir koleksiyon.

Aspose.Cells API'ler bir grup numaralandırıcı sağlar, ancak bu makale temel olarak aşağıda listelenen üç türü tartışır.

1. Cells Numaralandırıcı
1. Satır Numaralandırıcı
1. Sütun Numaralandırıcı

{{% /alert %}}

## **Numaralandırıcılar nasıl kullanılır?**

### **Cells Numaralandırıcı**

Cells Numaralandırıcıya erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine göre bu yöntemlerden herhangi biri kullanılabilir. İşte hücre numaralandırıcısını döndüren yöntemler.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Yukarıda belirtilen yöntemlerin tümü, başlatılmış olan hücrelerin koleksiyonunda gezinmeye izin veren numaralandırıcıyı döndürür.

{{% alert color="primary" %}}

Hücreler arasında gezinirken koleksiyon değiştirilmemelidir (yeni bir Cell'in başlatılmasına veya mevcut Cell'in silinmesine neden olacak işlemler). Aksi takdirde, Numaralandırıcı tüm hücreleri doğru bir şekilde geçemeyebilir (bazı öğeler tekrar tekrar geçilebilir veya atlanabilir).

{{% /alert %}}

Aşağıdaki kod örneği, bir Cells koleksiyonu için IEnumerator arabiriminin uygulanmasını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Satır Numaralandırıcı**

 Satırlar Numaralandırıcı kullanılırken erişilebilir.[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) yöntem. Aşağıdaki kod örneği, IEnumerator arabiriminin uygulanmasını gösterir.[**Satır Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Sütun Numaralandırıcı**

 Sütun Numaralandırıcıya, kullanılırken erişilebilir.[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) yöntem. Aşağıdaki kod örneği, IEnumerator arabiriminin uygulanmasını gösterir.[**Sütun Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Numaralandırıcılar nerede kullanılır?**

Numaralandırıcı kullanmanın avantajlarını tartışmak için gerçek zamanlı bir örnek ele alalım.

**Senaryo**

 Bir uygulama gereksinimi, belirli bir hücredeki tüm hücreleri geçmektir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)değerlerini okumaktır. Bu hedefi gerçekleştirmenin birkaç yolu olabilir. Birkaçı aşağıda gösterilmiştir.

### **Görüntüleme Aralığını Kullanma**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **MaxDataRow ve MaxDataColumn'u Kullanma**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Yukarıda bahsedilen yaklaşımların her ikisinin de aşağı yukarı benzer bir mantık kullandığını gözlemleyebileceğiniz gibi; hücre değerlerini okumak için koleksiyondaki tüm hücreler üzerinde döngü yapın. Bu, aşağıda tartışıldığı gibi birkaç nedenden dolayı sorunlu olabilir.

1.  gibi API'ler[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**Maksimum Sütun**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**Maksimum Görüntü Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)ilgili istatistikleri toplamak için fazladan zaman gerektirir. Veri matrisinin (satır x sütun) büyük olması durumunda, bu API'lerin kullanılması performans düşüşüne neden olabilir.
1. Çoğu durumda, belirli bir aralıktaki tüm hücreler örneklenmez. Bu gibi durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmeye kıyasla o kadar verimli değildir.
1. Bir döngüdeki bir hücreye Cells satır, sütun olarak erişilmesi, bir aralıktaki tüm hücre nesnelerinin somutlaştırılmasına neden olur ve bu da sonunda OutOfMemoryException'a neden olabilir.

## **Çözüm**

Yukarıda belirtilen gerçeklere dayanarak, numaralandırıcıların kullanılması gereken olası senaryolar aşağıdadır.

1. Hücre koleksiyonuna salt okunur erişim gereklidir, yani; gereklilik sadece hücreleri incelemektir.
1. Çok sayıda hücre geçilecek.
1. Geçiş yapılacak yalnızca başlatılmış hücreler/satırlar/sütunlar.
