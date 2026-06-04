---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Node.js kütüphanesidir ve tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini anlatacaktır.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, Excel dosyasını böl, çalışma sayfasını kopyala, aralığı kopyala, birden çok çalışma kitabı, ayrı dosyalar olarak kaydet
type: docs
weight: 195
url: /tr/nodejs-cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabının her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Verilerin alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri tek tek işlemek için ayırmanız gerektiğinde her iki yaklaşım da faydalıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç daha küçük dosyaya ayırması gerektiği birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman başkanının yalnızca kendi sayfasını alması gerekir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan e-posta yoluyla bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük birleştirilmiş çalışma kitaplarının da daha kolay işlenebilmesi, daha hızlı yüklenebilmesi veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineleyerek içeriğini yepyeni bir `Workbook` örneğine kopyalar ve her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: `Workbook` sınıfını kullanarak kaynak çalışma kitabını yükleyin, `Worksheet` ve `Cells` nesneleri aracılığıyla ilgili verilere erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyası Bölme**

### **Yaklaşım Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Ardından kaynak çalışma sayfasının içeriği hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde bu yöntem doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturarak ve dosya yolunu yapıcısına ileterek kaynak Excel dosyasını açın.
2. `for` veya `forEach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonu boyunca ilerleyin, böylece kaynak dosyadaki her `Worksheet` işlenir.
3. Döngü içinde, mevcut çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın; ideal olarak kaynak çalışma sayfasının `Name` özelliğiyle aynı olmalıdır.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreler üzerinde yineleme yapılarak ve değerlerinin hedef çalışma sayfasının ilgili hücrelerine yazılmasıyla veya tüm bir aralığı bir seferde aktarmak için `Cells.copy` yöntemi kullanılarak yapılabilir.
6. Kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.Name + ".xls"`) böylece oluşturulan her dosyanın benzersiz bir adı olsun.
7. Dosyayı diske yazmak için hedef `Workbook.save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar sonraki çalışma sayfası için 3 ila 7. adımları tekrarlayın.

### **Kod Örneği**

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "data/";
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);
    const sheetName = sourceSheet.getName();
    
    const destWorkbook = new AsposeCells.Workbook();
    const destIndex = destWorkbook.getWorksheets().add();
    const destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    const destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, AsposeCells.SaveFormat.Excel97To2003);
}
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olmak üzere yeni bir dosya kümesidir. Her dosya, karşılık gelen kaynak sayfanın adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyası Bölme**

### **Yaklaşım Genel Bakış**

Bazen bölmeniz gereken veriler, tüm bir çalışma sayfasına değil, çalışma sayfasının `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralık gibi belirli bir dikdörtgen bölgesine karşılık gelir. Bu durumlarda, tüm çalışma sayfalarını kopyalamak israf olur ve daha hassas bir yaklaşım gereklidir: kaynak aralığı belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de yararlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesini dosya yoluyla örnekleyerek kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı veya `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.createRange` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığını, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Hedef `Cells` koleksiyonundaki `Cells.copy` yöntemi, tüm bir aralığı kopyalamak için kullanılabilir veya kaynak aralığın hücrelerinde yineleme yapabilir ve değerlerini `putValue` ile hedef hücrelere yazabilirsiniz. Ne aktarıldığını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.save` yöntemini kullanarak hedef çalışma kitabını diskte yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```javascript
const AsposeCells = require("aspose.cells");

// Veri dizinini ve dosya yollarını tanımlayın
const dataDir = "data/";
const sourcePath = dataDir + "book1.xls";
const outputPath = dataDir + "outputrange.xls";

// Kaynak Excel dosyasını açın
const sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// Kaynak çalışma kitabından ilk çalışma sayfasını alın
const sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// A1:C10 kaynak hücre aralığını tanımlayın (0. satır, 0. sütundan başlayan 10 satır, 3 sütun)
const sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Yeni bir hedef çalışma kitabı oluşturun
const destWorkbook = new AsposeCells.Workbook();

// Hedef çalışma kitabındaki ilk çalışma sayfasına erişin
const destWorksheet = destWorkbook.getWorksheets().get(0);

// Kaynak aralıkla aynı boyutlarda A1'de hedef aralık oluşturun
const destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Kaynak aralığı hedef aralığa kopyalayın
destRange.copy(sourceRange);

// Hedef çalışma kitabını yeni bir .xls dosyasına kaydedin
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayarak çıkarılan aralığı içerir.

## **İlgili Makaleler**

- [Satırları ve Sütunları Kopyalama](/cells/tr/nodejs-cpp/copying-rows-and-columns/)
- [Hücreleri Birleştirme ve Birleştirmeyi Kaldırma](/cells/tr/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}