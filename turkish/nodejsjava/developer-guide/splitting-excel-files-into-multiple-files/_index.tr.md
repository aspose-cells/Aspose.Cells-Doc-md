---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
linktitle: Excel Dosyalarını Birden Çok Dosyaya
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için Aspose.Cells for Node.js via Java kütüphanesidir ve tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini tanıtacaktır.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, elektronik tablo, excel dosyası bölme, çalışma sayfası kopyalama, aralık kopyalama, birden çok çalışma kitabı, ayrı dosyalar olarak kaydet
type: docs
weight: 195
url: /tr/nodejs-java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabının her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak ve her birini ayrı bir dosya olarak kaydederek ve (2) bir çalışma sayfasından belirli bir hücre aralığını yeni bir çalışma kitabına kopyalayarak. Her iki yaklaşım da veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri ayrı ayrı işlenmek üzere ayırmanız gerektiğinde kullanışlıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç daha küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman başkanının yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan bağımsız bir dosya olarak e-posta yoluyla göndermek isteyebilirsiniz. Büyük konsolide çalışma kitaplarının da daha kolay işleme, daha hızlı yükleme veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineler ve içeriğini yepyeni bir `Workbook` örneğine kopyalayarak her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: `Workbook` sınıfını kullanarak kaynak çalışma kitabını yükleyin, `Worksheet` ve `Cells` nesneleri aracılığıyla ilgili verilere erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği daha sonra hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturarak ve dosya yolunu kurucusuna geçirerek kaynak Excel dosyasını açın.
2. `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonu boyunca yineleyin, böylece kaynak dosyadaki her `Worksheet` işlenir.
3. Döngünün içinde, mevcut çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın, ideal olarak kaynak çalışma sayfasının `Name` özelliğiyle aynı olacak şekilde.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreler arasında yinelenerek ve değerlerinin hedef çalışma sayfasının ilgili hücrelerine yazılmasıyla veya tek seferde bir aralığın tamamını aktarmak için `Cells.copy` yöntemi kullanılarak yapılabilir.
6. Üretilen her dosyanın benzersiz bir ada sahip olması için kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.getName() + ".xls"`).
7. Dosyayı diske yazmak için hedef `Workbook.save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar 3 ila 7 arasındaki adımları bir sonraki çalışma sayfası için tekrarlayın.

### **Kod Örneği**

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

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

Beklenen çıktı, veri dizininde yeni dosyalardan oluşan bir kümedir; kaynak çalışma kitabındaki her çalışma sayfası için bir dosya. Her dosya, ilgili kaynak sayfanın adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bazen bölmeniz gereken veriler tüm bir çalışma sayfasına değil, bir çalışma sayfasının belirli bir dikdörtgen bölgesine, örneğin `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralığa karşılık gelir. Bu gibi durumlarda, tüm çalışma sayfalarını kopyalamak israf olur ve daha hassas bir yaklaşım gereklidir: kaynak aralığı belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Dosya yolu ile bir `Workbook` nesnesi oluşturarak kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı veya `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.createRange` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığını, genellikle `A1` hücresinden başlayarak, hedef çalışma sayfasına kopyalayın. Bir aralığın tamamını kopyalamak için hedef `Cells` koleksiyonundaki `Cells.copy` yöntemi kullanılabilir veya kaynak aralığın hücrelerini yineleyebilir ve değerlerini `putValue` ile hedef hücrelere yazabilirsiniz. Ne aktarılacağını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```javascript
let sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// Kaynak çalışma kitabından ilk çalışma sayfasını al
let sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Kaynak hücre aralığını A1:C10 olarak tanımla (0. satır, 0. sütundan başlayan 10 satır, 3 sütun)
let sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Yeni bir hedef çalışma kitabı oluştur
let destWorkbook = new AsposeCells.Workbook();

// Hedef çalışma kitabındaki ilk çalışma sayfasına eriş
let destWorksheet = destWorkbook.getWorksheets().get(0);

// A1'de kaynak aralıkla aynı boyutlarda bir hedef aralık oluştur
let destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Kaynak aralığı hedef aralığa kopyala
destRange.copy(sourceRange);

// Hedef çalışma kitabını yeni bir .xls dosyasına kaydet
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);
```

Beklenen çıktı, veri dizininde, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki diğer verilerle hiçbir ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayan çıkarılmış aralığı içerir.



{{< app/cells/assistant language="javascript" >}}