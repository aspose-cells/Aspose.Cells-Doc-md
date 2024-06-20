---
title: Çalışma Sayfasının Hücrelerine Erişme
type: docs
weight: 10
url: /tr/python-net/accessing-cells-of-a-worksheet/
description: Bu makale, Python via .NET API si aracılığıyla çalışma sayfasının maksimum gösterim aralığını ve hücrelere nasıl erişileceğini göstermektedir.
keywords: Python Excel Kütüphanesi, Hücre nesnesini alın, Hücrelere Erişin, Hücrenin Satır ve Sütun İndisi ile Hücre Nesnesi Nasıl Alınır, Hücre Endeksinde Hücre Nesnesi Nasıl Alınır, Hücrenin Satır ve Sütun İndisi ile Hücre Nesnesi Nasıl Alınır, Çalışsayının maksimum görüntü aralığını alın. 
---

{{% alert color="primary" %}}

Tüm çalışsayıların temelde hücrelerde depolanan verileri içerebileceğini biliyoruz (bir çalışsayısının oluşturulduğu). Bir hücre, bir çalışsayısının tümünü satırlar ve sütunlar dizisi olarak oluşturmak için kullanılan temel bir parçadır. Bir çalışsayısından veriye erişmeye çalışmadan önce, hücrelerine erişim sağlamamız gerekir. Bu konuda, Aspose.Cells Python via .NET kullanarak çalışma zamanında çalışsayı hücrelerine erişmek için bazı temel yaklaşımları tartışacağız.

{{% /alert %}}

## **Hücrelere Nasıl Erişilir**

Aspose.Cells Python via .NET, bir Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışsayısına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) içerir. Bir çalışsayısı [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, çalışsayısındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu sağlar.

Bir çalışsayıdaki hücrelere erişmek için [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunu kullanabiliriz. Aspose.Cells Python via .NET, bir çalışsayısındaki hücrelere erişmek için üç temel yaklaşım sağlar:

1. Hücre adını kullanarak.
2. Bir hücrenin satır ve sütun indisini kullanarak.
3. Bir hücrenin [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundaki hücre endeksini kullanarak

**ÖNEMLİ:** 3. yaklaşımın en hızlı, 1. yaklaşımın ise en yavaş olduğunu belirttik. Yaklaşımlar arasındaki performans farkı çok küçüktür, bu yüzden hangi yaklaşımı kullanırsanız kullanın, performans düşüşü endişelenecek bir şey değildir.

### **Hücre Nesnesini Hücre Adıyla Nasıl Alınır**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonuna, hücre adını bir [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonu olarak dizin olarak geçirerek herhangi bir belirli hücreye erişebilirler.

Eğer başlangıçta boş bir çalışsayısı oluşturursanız, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonunun sayısı sıfırdır. Bu yaklaşımı kullanarak bir hücreye erişmeye çalıştığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol eder. Eğer varsa, hücre nesnesini koleksiyonda döndürür, aksi halde yeni bir [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) nesnesi oluşturur, nesneyi [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonuna ekler ve ardından nesneyi döndürür. Bu yaklaşım, Microsoft Excel ile tanıdık olanlar için hücreye erişmenin en kolay yoludur, ancak diğer yaklaşımlarla karşılaştırıldığında en yavaş olanıdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **Hücrenin Satır ve Sütun İndisine Göre Hücre Nesnesi Nasıl Alınır**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonuna, hücrenin satır ve sütun indislerini geçirerek herhangi bir belirli hücreye erişebilirler.

Bu yaklaşım, ilk yaklaşımın çalışma şekliyle aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **Hücre Endeksindeki Hücre Nesnesi Nasıl Alınır**

Bir hücre, hücrenin sayısal endeksini [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonuna geçirerek de erişilebilir.

Bu yaklaşımı kullanarak hücrelere eriştğinizde, hücrenin sayısal endeksi koleksiyondaki aralık dışındaysa bir istisna fırlatılabilir. Bu yaklaşım, hücrelere erişmek için en hızlı olanıdır ancak hücre nesnesine erişmek için bu yaklaşımı kullandığınızda, sayısal indeks, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonuna yeni hücreler eklendiğinde değişebilir. [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) koleksiyonundaki hücre nesneleri, satır ve sütun indisleri tarafından içsel olarak sıralanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **Çalışsayının Maksimum Görüntü Aralığını Nasıl Alınır**

Aspose.Cells Python via .NET, geliştiricilere bir çalışsayısının maksimum görüntü aralığına erişme olanağı sağlar. Maksimum görüntü aralığı - içeriğe sahip ilk ve son hücre aralığı - bir çalışsayısının tamamını bir resimde kopyalamak, seçmek veya göstermek gerektiğinde faydalıdır.

[**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/) kullanarak bir çalışsayısının maksimum görüntü aralığına erişebilirsiniz. Aşağıdaki örnek kod, [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/) özelliğine erişmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
