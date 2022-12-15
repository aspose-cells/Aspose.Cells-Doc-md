---
title: Bir Çalışma Sayfasının Cells'ine Erişme
type: docs
weight: 10
url: /tr/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Tüm çalışma sayfalarının temel olarak hücrelerde saklanan (bir çalışma sayfasını oluşturan) veriler içerebileceğini biliyoruz. Hücre, çalışma sayfasının tamamını satırlar ve sütunlar dizisi olarak oluşturmak için kullanılan temel bir parçasıdır. Bir çalışma sayfasındaki verilere erişmeye çalışmadan önce, hücrelerine erişmemiz gerekir. Dolayısıyla, bu konuda, çalışma zamanında Aspose.Cells kullanarak çalışma sayfası hücrelerine erişmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}} 
## **Cells'e erişim**
 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Bu bir Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel dosyasındaki her çalışma sayfasına erişmenizi sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 Kullanabiliriz[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)çalışma sayfasındaki hücrelere erişmek için koleksiyon. Aspose.Cells, bir çalışma sayfasındaki hücrelere erişmek için üç temel yaklaşım sunar:

1. Hücre adını kullanma.
1. Bir hücrenin satır ve sütun indeksini kullanma.
1.  Bir hücre dizini kullanarak[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Toplamak

{{% alert color="primary" %}} 

3. yaklaşımın en hızlı ve 1. yaklaşımın en yavaş olduğunu belirtmiştik. Yaklaşımlar arasındaki performans farkı çok küçüktür, bu nedenle hangi yaklaşımı kullanırsanız kullanın performans düşüşü konusunda endişelenmeyin.

{{% /alert %}} 
### **Cell Adını Kullanma**
 Geliştiriciler, hücre adını şuraya geçirerek herhangi bir belirli hücreye erişebilir:[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyonu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)bir dizin olarak sınıf.

 Başlangıçta boş bir çalışma sayfası oluşturursanız,[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Koleksiyon sıfırdır. Bir hücreye erişmek için bu yaklaşımı kullandığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol edecektir. Evet ise, koleksiyondaki hücre nesnesini döndürür, aksi takdirde yeni bir hücre nesnesi oluşturur.[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) nesne, nesneyi şuraya ekler:[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)koleksiyon ve sonra bu nesneyi döndürür. Bu yaklaşım, Microsoft Excel'e aşina iseniz, hücreye erişmenin en kolay yoludur, ancak diğer yaklaşımlara kıyasla en yavaş olanıdır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Cell'in Satır ve Sütun Dizinini Kullanma**
 Geliştiriciler, herhangi bir hücreye, satırının ve sütununun indekslerini[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) koleksiyonu[IÇalışma sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)sınıf. Bu yaklaşım, ilk yaklaşımla aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Çalışma Sayfasının Maksimum Görüntüleme Aralığına Erişme**
Aspose.Cells, geliştiricilerin bir çalışma sayfasının maksimum görüntüleme aralığına erişmesine olanak tanır. Maksimum görüntüleme aralığı - içeriğe sahip ilk ve son hücre arasındaki hücre aralığı - bir çalışma sayfasının tüm içeriğini bir görüntüde kopyalamanız, seçmeniz veya görüntülemeniz gerektiğinde kullanışlıdır.

 Bir çalışma sayfasının maksimum görüntüleme aralığına şunu kullanarak erişebilirsiniz:[MaxDisplayIAralığı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) yöntemi[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Toplamak.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
