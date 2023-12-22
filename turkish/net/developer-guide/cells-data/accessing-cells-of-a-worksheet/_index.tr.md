---
title: Bir Çalışma Sayfasının Cells'ine erişme
type: docs
weight: 10
url: /tr/net/accessing-cells-of-a-worksheet/
description: Bu makalede, Aspose.Cells for .NET API numaralı telefon aracılığıyla maksimum çalışma sayfası görüntüleme aralığının nasıl elde edileceği ve hücrelere nasıl erişileceği gösterilmektedir.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

Tüm çalışma sayfalarının, temel olarak hücrelerde (çalışma sayfasını oluşturan hücreler) depolanan verileri içerebileceğini biliyoruz. Hücre, çalışma sayfasının tamamını satır ve sütun dizisi halinde oluşturmak için kullanılan temel bir parçasıdır. Bir çalışma sayfasındaki verilere erişmeye çalışmadan önce hücrelerine erişmemiz gerekir. Bu nedenle, bu konuda, Aspose.Cells'i kullanarak çalışma zamanında çalışma sayfası hücrelerine erişmeye yönelik bazı temel yaklaşımları tartışacağız.

{{% /alert %}}

##  **Cells'e Nasıl Erişilir?**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Bu, Excel dosyasındaki her çalışma sayfasına erişime izin verir. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 Kullanabiliriz[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Bir çalışma sayfasındaki hücrelere erişmek için koleksiyon. Aspose.Cells, çalışma sayfasındaki hücrelere erişim için üç temel yaklaşım sağlar:

1. Hücre adını kullanma.
1. Bir hücrenin satır ve sütun indeksini kullanma.
1.  Hücre indeksini kullanma[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak

**ÖNEMLİ:**3. yaklaşımın en hızlı, 1. yaklaşımın ise en yavaş olduğunu belirtmiştik. Yaklaşımlar arasındaki performans farkı çok küçüktür; dolayısıyla hangi yaklaşımı kullanırsanız kullanın, performans düşüşü konusunda endişelenmeyin.

###  **Cell Nesnesini Cell Adına Göre Alma**

 Geliştiriciler herhangi bir hücreye hücre adını ileterek erişebilirler.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)dizin olarak sınıf.

 Başlangıçta boş bir çalışma sayfası oluşturursanız,[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Koleksiyon sıfırdır. Bir hücreye erişmek için bu yaklaşımı kullandığınızda, bu hücrenin koleksiyonda var olup olmadığı kontrol edilecektir. Evetse, koleksiyondaki hücre nesnesini döndürür, aksi halde yeni bir tane oluşturur.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesneyi nesneye ekler[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)toplama ve ardından nesneyi döndürür. Bu yaklaşım, Microsoft Excel'e aşina iseniz hücreye erişmenin en kolay yoludur ancak diğer yaklaşımlarla karşılaştırıldığında en yavaş olanıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **Cell'in Satır ve Sütun Dizinine Göre Cell Nesnesi Nasıl Alınır?**

 Geliştiriciler herhangi bir hücreye, o hücrenin satır ve sütun indekslerini ileterek erişebilirler.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

Bu yaklaşım ilk yaklaşımla aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **Cells Koleksiyonunda Cell Dizinine Göre Cell Nesnesi Nasıl Alınır?**

 Bir hücreye, hücrenin sayısal indeksi aktarılarak da erişilebilir.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak.

Hücrelere erişmek için bu yaklaşımı kullanırsanız, hücrenin sayısal dizini aralık dışındaysa bir istisna oluşturulabilir. Bu yaklaşım, hücrelere erişmenin en hızlı yoludur ancak bilmeniz gereken önemli bir nokta, bir hücre nesnesine erişmek için bu yaklaşımı kullanırsanız, hücreye yeni hücreler eklendikten sonra sayısal indeksin değişebileceğidir.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. Hücredeki nesneler[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon dahili olarak satır ve sütun endekslerine göre sıralanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **Çalışma Sayfasının Maksimum Görüntüleme Aralığı Nasıl Elde Edilir**

Aspose.Cells, geliştiricilerin bir çalışma sayfasının maksimum görüntüleme aralığına erişmesine olanak tanır. Maksimum görüntüleme aralığı (içerik içeren ilk ve son hücre arasındaki hücre aralığı), bir çalışma sayfasının tüm içeriğini bir görüntüde kopyalamanız, seçmeniz veya görüntülemeniz gerektiğinde kullanışlıdır.

Bir çalışma sayfasının maksimum görüntüleme aralığına şunu kullanarak erişebilirsiniz:[**Çalışma Sayfası.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Aşağıdaki örnek kod,[**Maksimum Görüntü Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
