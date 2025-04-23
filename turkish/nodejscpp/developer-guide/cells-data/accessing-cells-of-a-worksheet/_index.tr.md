---
title: Çalışma Sayfasının Hücrelerine Erişme
type: docs
weight: 10
url: /tr/nodejs-cpp/accessing-cells-of-a-worksheet/
description: Bu makale, çalışma sayfasının maksimum görüntüleme aralığını nasıl elde edeceğinizi ve hücrelere erişim sağlayacağınızı Aspose.Cells for Node.js via C++ API si ile anlatmaktadır.
keywords: Hücre nesnesine erişme, Hücrelere Erişme, Çalışma sayfasının maksimum görüntüleme aralığını alın. 
---

{{% alert color="primary" %}}

Biliyoruz ki, tüm çalışma sayfaları temel olarak hücrelerde saklanan verileri içerir (bir çalışma sayfası hücrelerden oluşur). Bir hücre, tüm çalışma sayfasını satır ve sütun dizisi şeklinde yapılandırmak için kullanılan temel bir unsurdur. Bir çalışma sayfasından veri erişimi yapmadan önce, hücrelerine erişmeniz gerekir. Bu nedenle, bu konuda, çalışma sayfası hücrelerine çalışma zamanında erişmek için bazı temel yaklaşımları tartışacağız, bunlar Aspose.Cells for Node.js via C++ kullanılarak yapılacaktır.

{{% /alert %}}

## **Hücrelere Nasıl Erişilir**

Aspose.Cells for Node.js via C++, Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu sağlar.

Çalışma sayfasında hücrelere erişmek için [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunu kullanabiliriz. Aspose.Cells for Node.js via C++, çalışma sayfasında hücrelere erişmek için temel üç yaklaşım sunar:

1. Hücre adını kullanarak.
2. Bir hücrenin satır ve sütun indisini kullanarak.
3. Bir hücrenin [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundaki hücre endeksini kullanarak

**ÖNEMLİ:** 3. yaklaşımın en hızlı, 1. yaklaşımın ise en yavaş olduğunu belirttik. Yaklaşımlar arasındaki performans farkı çok küçüktür, bu yüzden hangi yaklaşımı kullanırsanız kullanın, performans düşüşü endişelenecek bir şey değildir.

### **Hücre Nesnesini Hücre Adıyla Nasıl Alınır**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonuna, hücre adını bir [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu olarak dizin olarak geçirerek herhangi bir belirli hücreye erişebilirler.

Eğer başlangıçta boş bir çalışsayısı oluşturursanız, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun sayısı sıfırdır. Bu yaklaşımı kullanarak bir hücreye erişmeye çalıştığınızda, bu hücrenin koleksiyonda var olup olmadığını kontrol eder. Eğer varsa, hücre nesnesini koleksiyonda döndürür, aksi halde yeni bir [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) nesnesi oluşturur, nesneyi [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonuna ekler ve ardından nesneyi döndürür. Bu yaklaşım, Microsoft Excel ile tanıdık olanlar için hücreye erişmenin en kolay yoludur, ancak diğer yaklaşımlarla karşılaştırıldığında en yavaş olanıdır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **Hücrenin Satır ve Sütun İndisine Göre Hücre Nesnesi Nasıl Alınır**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonuna, hücrenin satır ve sütun indislerini geçirerek herhangi bir belirli hücreye erişebilirler.

Bu yaklaşım, ilk yaklaşımın çalışma şekliyle aynı şekilde çalışır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **Hücre Endeksindeki Hücre Nesnesi Nasıl Alınır**

Bir hücre, hücrenin sayısal endeksini [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonuna geçirerek de erişilebilir.

Bu yaklaşımı kullanarak hücrelere eriştğinizde, hücrenin sayısal endeksi koleksiyondaki aralık dışındaysa bir istisna fırlatılabilir. Bu yaklaşım, hücrelere erişmek için en hızlı olanıdır ancak hücre nesnesine erişmek için bu yaklaşımı kullandığınızda, sayısal indeks, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonuna yeni hücreler eklendiğinde değişebilir. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonundaki hücre nesneleri, satır ve sütun indisleri tarafından içsel olarak sıralanır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **Çalışsayının Maksimum Görüntü Aralığını Nasıl Alınır**

Node.js ile C++ kullanarak Aspose.Cells for Node.js via C++, bir çalışma sayfasının maksimum görüntülenebilir alanına erişmenizi sağlar. Maksimum görüntüleme alanı - içerik bulunan ilk ve son hücre arasındaki hücre aralığı - bir çalışma sayfasının tüm içeriğini kopyalamak, seçmek veya resimde görüntülemek istediğinizde faydalıdır.

[**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) kullanarak bir çalışsayısının maksimum görüntü aralığına erişebilirsiniz. Aşağıdaki örnek kod, [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) özelliğine erişmenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

