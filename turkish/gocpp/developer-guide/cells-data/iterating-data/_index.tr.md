---
title: Golang ile C++ üzerinden indisler ile Nasıl ve Nerede Kullanınabilir
linktitle: Verileri Yinele
type: docs
weight: 55
url: /tr/go-cpp/how-and-where-to-use-enumerators/
description: Aspose.Cells for C++ API kullanarak Tuna ve Nereye Enumeratörleri kullanmayı öğrenin.
keywords: Numaralandırıcıları Nasıl Kullanılır, Hücreler Numaralandırıcı, Satırlar Numaralandırıcı, Sütunlar Numaralandırıcı
---

{{% alert color="primary" %}}

Bir enumerator, bir kapsayıcı veya koleksiyon üzerinde gezinme yeteneği sağlayan bir nesnedir. Enumeratörler, koleksiyondaki veriyi okumak için kullanılabilir, ancak temel koleksiyonu değiştirmek için kullanılamazlar, oysa IEnumerable, bir GetEnumerator yöntemi tanımlayan arayüzdür ve bu da koleksiyona yalnızca okunabilir erişim sağlar.

Aspose.Cells API'ları bir dizi numaralandırıcı sağlar, ancak bu makale genellikle aşağıda listelenen üç türü tartışmaktadır.

1. Hücreler Numaralandırıcı
1. Satırlar Numaralandırıcı
1. Sütunlar Numaralandırıcı

{{% /alert %}}

## **Numaralandırıcıları Nasıl Kullanılır**

### **Hücreler Numaralandırıcı**

Hücreler Numaralandırıcısına erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak bu yöntemlerden herhangi biri kullanılabilir. İşte hücreler numaralandırıcısını döndüren yöntemler.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Yukarıda bahsedilen tüm yöntemler, başlatılmış hücre koleksiyonunu gezinmeyi sağlayan numaralandırıcıyı döndürür.

{{% alert color="primary" %}}

Hücreleri gezinirken koleksiyon değiştirilmemelidir (bir hücreyi yeni bir şekilde oluşturan işlemler veya var olan bir hücreyi sildiren işlemler). Aksi takdirde, numaralandırıcı tüm hücreleri doğru bir şekilde gezinemeyebilir (bazı öğeler tekrarlanabilir veya atlanabilir).

{{% /alert %}}

Aşağıdaki kod örneği, Hücreler koleksiyonu için IEnumerator arabirimi uygulamasını göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Satırlar Numaralandırıcı**

Rows Enumeratörü, [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) için IEnumerator arayüzünün uygulanmasını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **Sütunlar Al**

Sütunlar, [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/) için Get yönteminin uygulanmasını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Numaralandırıcıları Nerede Kullanılacağı**

Numaralandırıcıları kullanmanın avantajlarını tartışmak için, gerçek bir zaman örneği ele alalım.

**Senaryo**

Bir uygulamanın gereksinimlerinden biri, belirli bir [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) içindeki tüm hücreleri gezinerek değerlerini okumaktır. Bu amacı gerçekleştirmek için birkaç yöntem gösterilmiştir.

### **Görüntü Aralığı Kullanarak**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **MaxDataRow & MaxDataColumn Kullanarak**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Yukarıda bahsedilen her iki yaklaşımın da, tüm hücreleri döngü içinde dolaşarak hücre değerlerini okuma mantığına daha veya daha az benzer olduğunu gözlemleyebilirsiniz. Bu, aşağıda tartışılan birçok nedenden biri olabilir.

1. [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) ve [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) gibi API'ler, ilgili istatistikleri toplamak için ekstra zaman gerektirir. Veri matrisi (satırlar x sütunlar) büyükse, bu API'leri kullanmak performans düşüşüne neden olabilir.
1. Çoğu durumda, verilen bir aralıktaki tüm hücreler oluşturulmamıştır. Bu tür durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmekten daha verimli değildir.
1. Hücreye döngü içinde Cells satır, sütun olarak erişmek, bir aralıktaki tüm hücre nesnelerinin oluşturulmasına neden olabilir, bu da sonunda OutOfMemoryException'a neden olabilir.

## **Sonuç**

Yukarıda belirtilen gerçeklere dayanarak, aşağıdakiler, numaralandırıcıların kullanılması gereken olası senaryolarıdır.

1. Yalnızca hücre koleksiyonunun salt okunur erişimi gereklidir, yani; gereksinim yalnızca hücreleri incelemektir.
1. Birçok hücrenin dolaşılması gereklidir.
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar dolaşılmalıdır.
