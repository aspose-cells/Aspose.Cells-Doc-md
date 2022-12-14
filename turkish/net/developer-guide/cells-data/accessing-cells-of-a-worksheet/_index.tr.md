---
title: Bir Çalışma Sayfasının Cells'ine Erişme
type: docs
weight: 10
url: /tr/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

Tüm çalışma sayfalarının temel olarak hücrelerde saklanan (bir çalışma sayfasını oluşturan) veriler içerebileceğini biliyoruz. Hücre, çalışma sayfasının tamamını satırlar ve sütunlar dizisi olarak oluşturmak için kullanılan temel bir parçasıdır. Bir çalışma sayfasındaki verilere erişmeye çalışmadan önce, hücrelerine erişmemiz gerekir. Dolayısıyla, bu konuda, çalışma zamanında Aspose.Cells kullanarak çalışma sayfası hücrelerine erişmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}}

## **Cells'e erişim**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 Kullanabiliriz[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)çalışma sayfasındaki hücrelere erişmek için koleksiyon. Aspose.Cells, bir çalışma sayfasındaki hücrelere erişmek için üç temel yaklaşım sunar:

1. Hücre adını kullanma.
1. Bir hücrenin satır ve sütun indeksini kullanma.
1.  Bir hücre dizini kullanarak[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak

**ÖNEMLİ:**3. yaklaşımın en hızlı ve 1. yaklaşımın en yavaş olduğunu belirtmiştik. Yaklaşımlar arasındaki performans farkı çok küçüktür, bu nedenle hangi yaklaşımı kullanırsanız kullanın performans düşüşü konusunda endişelenmeyin.

### **Cell Adını Kullanma**

 Geliştiriciler, hücre adını şuraya geçirerek herhangi bir belirli hücreye erişebilir:[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)bir dizin olarak sınıf.

 Başlangıçta boş bir çalışma sayfası oluşturursanız,[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Koleksiyon sıfırdır. Bir hücreye erişmek için bu yaklaşımı kullandığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol edecektir. Evet ise, koleksiyondaki hücre nesnesini döndürür, aksi takdirde yeni bir hücre nesnesi oluşturur.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesne, nesneyi şuraya ekler:[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon ve ardından nesneyi döndürür. Bu yaklaşım, Microsoft Excel'e aşina iseniz, hücreye erişmenin en kolay yoludur, ancak diğer yaklaşımlara kıyasla en yavaş olanıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Cell'in Satır ve Sütun Dizinini Kullanma**

 Geliştiriciler, herhangi bir hücreye, satırının ve sütununun indekslerini[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

Bu yaklaşım, ilk yaklaşımla aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Cells Koleksiyonunda Cell Dizininin Kullanılması**

 Bir hücreye, hücrenin sayısal dizini hücreye geçirilerek de erişilebilir.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Toplamak.

 Hücrelere erişmek için bu yaklaşımı kullanırsanız, hücrenin sayısal dizini aralığın dışındaysa bir istisna atılabilir. Bu yaklaşım, hücrelere erişmek için en hızlı olanıdır, ancak bilinmesi gereken önemli bir şey, bu yaklaşımı bir hücre nesnesine erişmek için kullanırsanız, sayısal dizine yeni hücreler eklendikten sonra değişebilir.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. Hücredeki nesneler[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)koleksiyon dahili olarak satır ve sütun indekslerine göre sıralanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Çalışma Sayfasının Maksimum Görüntüleme Aralığına Erişme**

Aspose.Cells, geliştiricilerin bir çalışma sayfasının maksimum görüntüleme aralığına erişmesine olanak tanır. Maksimum görüntüleme aralığı (içeriğe sahip ilk ve son hücre arasındaki hücre aralığı), bir çalışma sayfasının tüm içeriğini bir görüntüde kopyalamanız, seçmeniz veya görüntülemeniz gerektiğinde kullanışlıdır.

 Bir çalışma sayfasının maksimum görüntüleme aralığına şunu kullanarak erişebilirsiniz:[**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Aşağıdaki örnek kod, nasıl erişileceğini gösterir.[**Maksimum Görüntü Aralığı**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
