---
title: Bir Çalışma Sayfasının Cells'ine erişme
type: docs
weight: 10
url: /tr/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Tüm çalışma sayfalarının, temel olarak hücrelerde (çalışma sayfasını oluşturan hücreler) depolanan verileri içerebileceğini biliyoruz. Hücre, çalışma sayfasının tamamını satır ve sütun dizisi halinde oluşturmak için kullanılan temel bir parçasıdır. Bir çalışma sayfasındaki verilere erişmeye çalışmadan önce hücrelerine erişmemiz gerekir. Bu nedenle, bu konuda, Aspose.Cells'i kullanarak çalışma zamanında çalışma sayfası hücrelerine erişmeye yönelik bazı temel yaklaşımları tartışacağız.

{{% /alert %}} 
##  **Cells'e erişiliyor**
 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel dosyasındaki her çalışma sayfasına erişmenizi sağlayan koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf sağlar[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 Kullanabiliriz[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Bir çalışma sayfasındaki hücrelere erişmek için koleksiyon. Aspose.Cells, çalışma sayfasındaki hücrelere erişim için üç temel yaklaşım sağlar:

1. Hücre adını kullanma.
1. Bir hücrenin satır ve sütun indeksini kullanma.
1.  Hücre indeksini kullanma[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Toplamak

{{% alert color="primary" %}} 

3. yaklaşımın en hızlı, 1. yaklaşımın ise en yavaş olduğunu belirtmiştik. Yaklaşımlar arasındaki performans farkı çok küçüktür; dolayısıyla hangi yaklaşımı kullanırsanız kullanın, performans düşüşü konusunda endişelenmeyin.

{{% /alert %}} 
###  **Cell Adını Kullanma**
 Geliştiriciler herhangi bir hücreye hücre adını ileterek erişebilirler.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)dizin olarak sınıf.

 Başlangıçta boş bir çalışma sayfası oluşturursanız,[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Koleksiyon sıfırdır. Bir hücreye erişmek için bu yaklaşımı kullandığınızda, bu hücrenin koleksiyonda var olup olmadığı kontrol edilecektir. Evetse, koleksiyondaki hücre nesnesini döndürür, aksi halde yeni bir tane oluşturur.[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) nesneyi nesneye ekler[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)toplama ve sonra bu nesneyi döndürür. Bu yaklaşım, Microsoft Excel'e aşina iseniz hücreye erişmenin en kolay yoludur ancak diğer yaklaşımlarla karşılaştırıldığında en yavaş olanıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **Cell'in Satır ve Sütun Dizinini Kullanma**
 Geliştiriciler herhangi bir hücreye, o hücrenin satır ve sütun indekslerini ileterek erişebilirler.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)sınıf. Bu yaklaşım ilk yaklaşımla aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **Maksimum Çalışma Sayfası Görüntüleme Aralığına Erişim**
Aspose.Cells, geliştiricilerin bir çalışma sayfasının maksimum görüntüleme aralığına erişmesine olanak tanır. Maksimum görüntüleme aralığı (içerik içeren ilk ve son hücre arasındaki hücre aralığı), bir çalışma sayfasının tüm içeriğini bir görüntüde kopyalamanız, seçmeniz veya görüntülemeniz gerektiğinde kullanışlıdır.

Bir çalışma sayfasının maksimum görüntüleme aralığına şunu kullanarak erişebilirsiniz:[Maksimum Görüntü Aralığı](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) yöntemi[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Toplamak.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
