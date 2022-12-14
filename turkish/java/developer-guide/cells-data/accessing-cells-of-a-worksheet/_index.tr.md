---
title: Bir Çalışma Sayfasının Cells'ine Erişme
type: docs
weight: 10
url: /tr/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Tüm çalışma sayfalarının temel olarak hücrelerde saklanan (bir çalışma sayfasını oluşturan) veriler içerebileceğini biliyoruz. Hücre, çalışma sayfasının tamamını satırlar ve sütunlar dizisi olarak oluşturmak için kullanılan temel bir parçasıdır. Bir çalışma sayfasındaki verilere erişmeye çalışmadan önce, hücrelerine erişmemiz gerekir. Dolayısıyla, bu konuda, çalışma zamanında Aspose.Cells kullanarak çalışma sayfası hücrelerine erişmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}} 
## **Cells'e erişim**
 Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 kullanabiliriz[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)çalışma sayfasındaki hücrelere erişmek için koleksiyon. Aspose.Cells, hücrelere erişim için farklı temel yaklaşımlar sunar:

1. [Hücre adını kullanma](/cells/tr/java/accessing-cells-of-a-worksheet/).
1. [Satır ve sütun indeksini kullanma](/cells/tr/java/accessing-cells-of-a-worksheet/).
### **Cell Adını Kullanma**
 Geliştiriciler, hücre adını şuraya geçirerek herhangi bir belirli hücreye erişebilir:[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf.

 Başlangıçta boş bir çalışma sayfası oluşturursanız,[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Koleksiyon sıfırdır. Bir hücreye erişmek için bu yaklaşımı kullandığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol edecektir. Evet ise, koleksiyondaki hücre nesnesini döndürür, aksi takdirde yeni bir hücre nesnesi oluşturur.[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) nesne, nesneyi şuraya ekler:[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)koleksiyon ve ardından nesneyi döndürür. Bu yaklaşım, Microsoft Excel'e aşina iseniz hücreye erişmenin en kolay yoludur, ancak diğer yaklaşımlardan daha yavaştır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Cell'in Satır ve Sütun Dizinini Kullanma**
 Geliştiriciler, herhangi bir hücreye, satırının ve sütununun indekslerini[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)sınıf.

Bu yaklaşım, ilk yaklaşımla aynı şekilde çalışır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **İlgili Makaleler**
{{% alert color="primary" %}} 

- [Adlandırılmış Aralıklar](/cells/tr/java/named-ranges/)

{{% /alert %}} 
## **Çalışma Sayfasının Maksimum Görüntüleme Aralığına Erişme**
Aspose.Cells, geliştiricilerin bir çalışma sayfasının maksimum görüntüleme aralığına erişmesine olanak tanır. Maksimum görüntüleme aralığı (içeriğe sahip ilk ve son hücre arasındaki hücre aralığı), bir çalışma sayfasının tüm içeriğini bir görüntüde kopyalamanız, seçmeniz veya görüntülemeniz gerektiğinde kullanışlıdır.

 Bir çalışma sayfasının maksimum görüntüleme aralığına şunu kullanarak erişebilirsiniz:[Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

Aşağıdaki şekilde, seçilen çalışma sayfasının maksimum görüntüleme aralığı A1:G15'tir.

**Bu çalışma sayfasının maksimum görüntüleme aralığı gösteriliyor** 

![yapılacaklar:resim_alternatif_Metin](accessing-cells-of-a-worksheet_1.png)

 Aşağıdaki örnek kod, nasıl erişileceğini gösterir.[Maksimum Görüntü Aralığı](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)Emlak. Kod aşağıdaki çıktıyı üretir.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
