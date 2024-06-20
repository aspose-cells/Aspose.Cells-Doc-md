---
title: Çalışma Sayfasının Hücrelerine Erişme
type: docs
weight: 10
url: /tr/net/accessing-cells-of-a-worksheet/
description: Bu makale, çalışma sayfasının maksimum görüntüleme aralığını nasıl alınır ve Aspose.Cells for .NET API si aracılığıyla hücrelere erişilir göstermektedir.
keywords: Hücre nesnesine erişme, Hücrelere Erişme, Çalışma sayfasının maksimum görüntüleme aralığını alın. 
---

{{% alert color="primary" %}}

Tüm çalışma sayfalarının temelini oluşturan hücrelerde depolanan temelde veri içeren verileri içerebileceğini biliyoruz. Bir hücre, çalışma sayfasının tümünü satırlar ve sütunlar dizisi olarak oluşturmak için kullanılan çalışma sayfasının temel parçasıdır. Bir çalışma sayfasından veri almadan önce, hücrelerine erişim sağlamamız gerekecektir. Bu nedenle, bu konuda, Aspose.Cells'i kullanarak çalışma sayfasının çalışma zamanında hücrelere erişmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}}

## **Hücrelere Nasıl Erişilir**

Aspose.Cells, bir Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu sağlar.

Bir çalışma sayfasında hücrelere erişmek için [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunu kullanabiliriz. Aspose.Cells, çalışma sayfasındaki hücrelere erişmek için üç temel yaklaşım sağlar:

1. Hücre adını kullanarak.
2. Bir hücrenin satır ve sütun indisini kullanarak.
3. Bir hücrenin [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonundaki hücre endeksini kullanarak

**ÖNEMLİ:** 3. yaklaşımın en hızlı, 1. yaklaşımın ise en yavaş olduğunu belirttik. Yaklaşımlar arasındaki performans farkı çok küçüktür, bu yüzden hangi yaklaşımı kullanırsanız kullanın, performans düşüşü endişelenecek bir şey değildir.

### **Hücre Nesnesini Hücre Adıyla Nasıl Alınır**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonuna, hücre adını bir [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonu olarak dizin olarak geçirerek herhangi bir belirli hücreye erişebilirler.

Eğer başlangıçta boş bir çalışsayısı oluşturursanız, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonunun sayısı sıfırdır. Bu yaklaşımı kullanarak bir hücreye erişmeye çalıştığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol eder. Eğer varsa, hücre nesnesini koleksiyonda döndürür, aksi halde yeni bir [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesnesi oluşturur, nesneyi [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonuna ekler ve ardından nesneyi döndürür. Bu yaklaşım, Microsoft Excel ile tanıdık olanlar için hücreye erişmenin en kolay yoludur, ancak diğer yaklaşımlarla karşılaştırıldığında en yavaş olanıdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Hücrenin Satır ve Sütun İndisine Göre Hücre Nesnesi Nasıl Alınır**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonuna, hücrenin satır ve sütun indislerini geçirerek herhangi bir belirli hücreye erişebilirler.

Bu yaklaşım, ilk yaklaşımın çalışma şekliyle aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Hücre Endeksindeki Hücre Nesnesi Nasıl Alınır**

Bir hücre, hücrenin sayısal endeksini [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonuna geçirerek de erişilebilir.

Bu yaklaşımı kullanarak hücrelere eriştğinizde, hücrenin sayısal endeksi koleksiyondaki aralık dışındaysa bir istisna fırlatılabilir. Bu yaklaşım, hücrelere erişmek için en hızlı olanıdır ancak hücre nesnesine erişmek için bu yaklaşımı kullandığınızda, sayısal indeks, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonuna yeni hücreler eklendiğinde değişebilir. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyonundaki hücre nesneleri, satır ve sütun indisleri tarafından içsel olarak sıralanır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Çalışsayının Maksimum Görüntü Aralığını Nasıl Alınır**

Aspose.Cells, geliştiricilere bir çalışma sayfasının maksimum görüntüleme aralığına erişme imkanı sunar. Maksimum görüntüleme aralığı - içerik bulunan ilk ve son hücre aralığı - bir çalışma sayfasının tüm içeriğini bir resimde kopyalamak, seçmek veya görüntülemek istediğinizde kullanışlıdır.

[**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) kullanarak bir çalışsayısının maksimum görüntü aralığına erişebilirsiniz. Aşağıdaki örnek kod, [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) özelliğine erişmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
