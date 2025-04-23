---
title: Numaralandırıcıları Nasıl ve Nerede Kullanılır
linktitle: Verileri Yinele
type: docs
weight: 55
url: /tr/net/how-and-where-to-use-enumerators/
description: Aspose.Cells for .NET API üzerinden Numaralandırıcıları Nasıl ve Nerede Kullanacağınızı öğrenin.
keywords: Numaralandırıcıları Nasıl Kullanılır, Hücreler Numaralandırıcı, Satırlar Numaralandırıcı, Sütunlar Numaralandırıcı
---

{{% alert color="primary" %}}

Numaralandırıcı, bir koleksiyon veya topluluğu gezinme yeteneği sağlayan bir nesnedir. Numaralandırıcılar, koleksiyondaki verileri okumak için kullanılabilir, ancak altta yatan koleksiyonu değiştirmek için kullanılamazlar. Öte yandan IEnumerable, GetEnumerator metodunu tanımlayan bir arabirimdir, bu da sırasıyla bir IEnumerator arabirimini döndüren, bu da koleksiyona salt okunur erişim sağlar.

Aspose.Cells API'ları bir dizi numaralandırıcı sağlar, ancak bu makale genellikle aşağıda listelenen üç türü tartışmaktadır.

1. Hücreler Numaralandırıcı
1. Satırlar Numaralandırıcı
1. Sütunlar Numaralandırıcı

{{% /alert %}}

## **Numaralandırıcıları Nasıl Kullanılır**

### **Hücreler Numaralandırıcı**

Hücreler Numaralandırıcısına erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak bu yöntemlerden herhangi biri kullanılabilir. İşte hücreler numaralandırıcısını döndüren yöntemler.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Yukarıda bahsedilen tüm yöntemler, başlatılmış hücre koleksiyonunu gezinmeyi sağlayan numaralandırıcıyı döndürür.

{{% alert color="primary" %}}

Hücreleri gezinirken koleksiyon değiştirilmemelidir (bir hücreyi yeni bir şekilde oluşturan işlemler veya var olan bir hücreyi sildiren işlemler). Aksi takdirde, numaralandırıcı tüm hücreleri doğru bir şekilde gezinemeyebilir (bazı öğeler tekrarlanabilir veya atlanabilir).

{{% /alert %}}

Aşağıdaki kod örneği, Hücreler koleksiyonu için IEnumerator arabirimi uygulamasını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Satırlar Numaralandırıcı**

[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) kullanılırken Satırlar Numaralandırıcısına erişilebilir. Aşağıdaki kod örneği, [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) için IEnumerator arabiriminin uygulamasını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Sütunlar Numaralandırıcı**

[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) kullanılırken Sütunlar Numaralandırıcısına erişilebilir. Aşağıdaki kod örneği, [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) için IEnumerator arabirimini uygulamanın uygulamasını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Numaralandırıcıları Nerede Kullanılacağı**

Numaralandırıcıları kullanmanın avantajlarını tartışmak için, gerçek bir zaman örneği ele alalım.

**Senaryo**

Bir uygulama gereksinimi, belirli bir [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) içindeki tüm hücreleri gezerek değerlerini okumaktır. Bu hedefi uygulamanın birkaç yolu olabilir. Birkaç örnek aşağıda gösterilmektedir.

### **Görüntü Aralığı Kullanarak**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **MaxDataRow & MaxDataColumn Kullanarak**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Yukarıda bahsedilen her iki yaklaşımın da, tüm hücreleri döngü içinde dolaşarak hücre değerlerini okuma mantığına daha veya daha az benzer olduğunu gözlemleyebilirsiniz. Bu, aşağıda tartışılan birçok nedenden biri olabilir.

1. [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) ve [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) gibi API'lar, ilgili istatistikleri toplamak için ekstra zaman gerektirir. Veri matrisi (satır x sütun) büyükse, bu API'ların kullanılması performans cezası uygulayabilir.
1. Çoğu durumda, verilen bir aralıktaki tüm hücreler oluşturulmamıştır. Bu tür durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmekten daha verimli değildir.
1. Hücreye döngü içinde Cells satır, sütun olarak erişmek, bir aralıktaki tüm hücre nesnelerinin oluşturulmasına neden olabilir, bu da sonunda OutOfMemoryException'a neden olabilir.

## **Sonuç**

Yukarıda belirtilen gerçeklere dayanarak, aşağıdakiler, numaralandırıcıların kullanılması gereken olası senaryolarıdır.

1. Yalnızca hücre koleksiyonunun salt okunur erişimi gereklidir, yani; gereksinim yalnızca hücreleri incelemektir.
1. Birçok hücrenin dolaşılması gereklidir.
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar dolaşılmalıdır.
{{< app/cells/assistant language="csharp" >}}
