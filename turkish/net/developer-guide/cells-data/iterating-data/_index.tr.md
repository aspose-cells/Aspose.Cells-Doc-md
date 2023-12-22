---
title: Numaralandırıcılar Nasıl ve Nerede Kullanılır?
linktitle: Verileri Yinele
type: docs
weight: 55
url: /tr/net/how-and-where-to-use-enumerators/
description: Aspose.Cells for .NET API numaralı telefondan Numaralayıcıların Nasıl ve Nerede Kullanılacağını öğrenin.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

Numaralandırıcı, bir kapsayıcı veya koleksiyon arasında geçiş yapma olanağı sağlayan bir nesnedir. Numaralandırıcılar koleksiyondaki verileri okumak için kullanılabilir, ancak temeldeki koleksiyonu değiştirmek için kullanılamazlar; oysa IEnumerable, bir IEnumerator arayüzü döndüren GetEnumerator yöntemini tanımlayan bir arayüzdür; bu da, salt okunur erişime izin verir. bir koleksiyon.

Aspose.Cells API'ler bir dizi numaralandırıcı sağlar, ancak bu makalede esas olarak aşağıda listelenen üç tür tartışılmaktadır.

1. Cells Numaralandırıcı
1. Satır Numaralandırıcı
1. Sütun Numaralandırıcı

{{% /alert %}}

##  **Numaralandırıcılar nasıl kullanılır?**

###  **Cells Numaralandırıcı**

Cells Numaralandırıcıya erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak bu yöntemlerden herhangi biri kullanılabilir. Hücre numaralandırıcısını döndüren yöntemler şunlardır.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Yukarıda belirtilen yöntemlerin tümü, başlatılmış olan hücrelerin toplanmasına izin veren numaralandırıcıyı döndürür.

{{% alert color="primary" %}}

Hücreler arasında geçiş yapılırken koleksiyon değiştirilmemelidir (yeni bir Cell'in başlatılmasına veya mevcut Cell'in silinmesine neden olacak işlemler). Aksi takdirde, numaralandırıcı tüm hücrelerde doğru şekilde geçiş yapamayabilir (bazı öğeler tekrar tekrar geçilebilir veya atlanabilir).

{{% /alert %}}

Aşağıdaki kod örneği, Cells koleksiyonu için IEnumerator arabiriminin uygulanmasını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **Satır Numaralandırıcı**

 Satır Numaralandırıcıya, kullanılarak erişilebilir.[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) yöntem. Aşağıdaki kod örneği, IEnumerator arabiriminin uygulanmasını gösterir.[**Satır Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **Sütun Numaralandırıcı**

 Sütun Numaralandırıcıya, kullanılarak erişilebilir.[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) yöntem. Aşağıdaki kod örneği, IEnumerator arabiriminin uygulanmasını gösterir.[**SütunKoleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **Numaralandırıcılar nerede kullanılır?**

Numaralandırıcı kullanmanın avantajlarını tartışmak için gerçek zamanlı bir örnek alalım.

**Senaryo**

 Bir uygulama gereksinimi, belirli bir hücredeki tüm hücreleri geçmektir[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)değerlerini okumak için. Bu hedefi gerçekleştirmenin birkaç yolu olabilir. Birkaç tanesi aşağıda gösterilmiştir.

###  **Görüntü Aralığını Kullanma**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **MaxDataRow ve MaxDataColumn'u kullanma**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Gördüğünüz gibi yukarıda bahsedilen her iki yaklaşım da aşağı yukarı benzer mantık kullanıyor; Hücre değerlerini okumak için koleksiyondaki tüm hücrelerin üzerinde döngü yapın. Bu, aşağıda tartışıldığı gibi çeşitli nedenlerden dolayı sorunlu olabilir.

1.  API'ler gibi[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**Maksimum Sütun**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**Maksimum Görüntü Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)ilgili istatistikleri toplamak için ekstra zamana ihtiyaç vardır. Veri matrisinin (satır x sütun) büyük olması durumunda, bu API'lerin kullanılması performans kaybına neden olabilir.
1. Çoğu durumda, belirli bir aralıktaki hücrelerin tümü başlatılmaz. Bu gibi durumlarda matristeki her hücreyi kontrol etmek, yalnızca başlatılan hücreleri kontrol etmekle karşılaştırıldığında çok verimli değildir.
1. Döngüdeki bir hücreye Cells satır, sütun olarak erişilmesi, aralıktaki tüm hücre nesnelerinin başlatılmasına neden olur ve bu da sonuçta OutOfMemoryException'a neden olabilir.

##  **Çözüm**

Yukarıda belirtilen gerçeklere dayanarak, numaralandırıcıların kullanılması gereken olası senaryolar aşağıdadır.

1. Hücre koleksiyonuna salt okunur erişim gereklidir; gerekli olan sadece hücreleri incelemektir.
1. Çok sayıda hücrenin geçilmesi gerekiyor.
1. Yalnızca geçilecek hücreler/satırlar/sütunlar başlatıldı.
