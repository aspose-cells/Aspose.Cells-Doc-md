---
title: Çalışma Sayfasının Hücrelerine Erişme
type: docs
weight: 10
url: /tr/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Tüm çalışma sayfalarının temelini oluşturan hücrelerde depolanan temelde veri içeren verileri içerebileceğini biliyoruz. Bir hücre, çalışma sayfasının tümünü satırlar ve sütunlar dizisi olarak oluşturmak için kullanılan çalışma sayfasının temel parçasıdır. Bir çalışma sayfasından veri almadan önce, hücrelerine erişim sağlamamız gerekecektir. Bu nedenle, bu konuda, Aspose.Cells'i kullanarak çalışma sayfasının çalışma zamanında hücrelere erişmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}} 
## **Hücrelere Erişim**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) adlı bir sınıf sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışsayfaya erişim izni veren [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) koleksiyonunu içerir. Bir çalışsayfa, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, çalışsayfadaki tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonu sağlar.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunu, bir çalışsayfadaki hücrelere erişmek için kullanabiliriz. Aspose.Cells, hücrelere erişim için farklı temel yaklaşımlar sağlar:

1. [Hücre adı kullanarak](/cells/tr/java/accessing-cells-of-a-worksheet/).
1. [Satır ve sütun indeksi kullanarak](/cells/tr/java/accessing-cells-of-a-worksheet/).
### **Hücre Adı Kullanarak**
Geliştiriciler, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfının [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonuna hücre adını ileterek belirli bir hücreye erişebilirler.

Eğer başlangıçta boş bir çalışsayfa oluşturursanız, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun sayısı sıfırdır. Bu yaklaşımı hücreye erişmek için kullandığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol eder. Var ise, hücre nesnesini koleksiyonda döndürür, aksi takdirde yeni bir [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) nesnesi oluşturur, nesneyi [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonuna ekler ve sonra nesneyi döndürür. Bu yaklaşım, Microsoft Excel ile tanıdık iseniz, hücreye erişmenin en kolay yoludur ama diğer yaklaşımlardan daha yavaştır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Hücrenin Satır ve Sütun İndeksini Kullanma**
Geliştiriciler, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfının [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonuna hücrenin satır ve sütun indekslerini ileterek belirli bir hücreye erişebilirler.

Bu yaklaşım, ilk yaklaşımın çalışma şekliyle aynı şekilde çalışır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **İlgili Makaleler**
{{% alert color="primary" %}} 

- [Adlandırılmış Aralıklar](/cells/tr/java/named-ranges/)

{{% /alert %}} 
## **Çalışsayfanın Maksimum Görüntü Aralığına Erişme**
Aspose.Cells, geliştiricilere bir çalışma sayfasının maksimum görüntüleme aralığına erişme imkanı sunar. Maksimum görüntüleme aralığı - içerik bulunan ilk ve son hücre aralığı - bir çalışma sayfasının tüm içeriğini bir resimde kopyalamak, seçmek veya görüntülemek istediğinizde kullanışlıdır.

Bir çalışsayfanın maksimum görüntü aralığına, [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange) yöntemini kullanarak erişebilirsiniz.

Aşağıdaki şekilde, seçilen çalışsayfanın maksimum görüntü aralığı A1:G15'tir.

**Bu çalışma sayfasının maksimum görüntü aralığını gösteriyor** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

Aşağıdaki örnek kod, [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange) özelliğine nasıl erişileceğini açıklar. Kod aşağıdaki çıktıyı oluşturur.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
