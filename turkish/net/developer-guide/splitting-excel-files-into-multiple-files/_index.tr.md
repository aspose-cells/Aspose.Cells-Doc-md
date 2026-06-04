---
title: Excel Dosyalarını Birden Fazla Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir .NET kütüphanesidir ve tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini anlatacaktır.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, Excel dosyası bölme, çalışma sayfası kopyalama, aralık kopyalama, birden fazla çalışma kitabı, ayrı dosyalar olarak kaydetme
type: docs
weight: 195
url: /tr/net/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Her iki yaklaşım da veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri tek tek işlemek üzere ayırmanız gerektiğinde kullanışlıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç daha küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman başkanının yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarıp çalışma kitabının geri kalanını açığa çıkarmadan bağımsız bir dosya olarak e-posta yoluyla göndermek isteyebilirsiniz. Büyük ve birleştirilmiş çalışma kitaplarının da daha kolay işlenebilmesi, daha hızlı yüklenebilmesi veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineler ve içeriğini yepyeni bir `Workbook` örneğine kopyalayarak her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: `Workbook` sınıfını kullanarak kaynak çalışma kitabını yükleyin, `Worksheet` ve `Cells` nesneleri aracılığıyla ilgili verilere erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyası Bölme**

### **Yaklaşıma Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği, hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (örneğin bir departman, bölge, ay veya ürün hattı) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturarak ve dosya yolunu kurucusuna geçirerek kaynak Excel dosyasını açın.
2. Kaynak dosyadaki her `Worksheet`'in işlenmesi için bir `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonunu yineleyin.
3. Döngünün içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın, ideal olarak kaynak çalışma sayfasının `Name` özelliğiyle aynı adı verin.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreler yinelenerek ve değerleri hedef çalışma sayfasının ilgili hücrelerine yazılarak veya bir bütün aralığı bir kerede aktarmak için `Cells.Copy` yöntemi kullanılarak yapılabilir.
6. Oluşturulan her dosyanın benzersiz bir adı olması için kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.Name + ".xls"`).
7. Dosyayı diske yazmak için hedef `Workbook.Save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar bir sonraki çalışma sayfası için 3 ile 7 arasındaki adımları tekrarlayın.

### **Kod Örneği**

```csharp
using System;
using System.IO;
using Aspose.Cells;

string dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet sourceSheet = workbook.Worksheets[i];
    string sheetName = sourceSheet.Name;
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.Worksheets.Add();
    Worksheet destSheet = destWorkbook.Worksheets[destIndex];
    destSheet.Name = sheetName;
    
    destSheet.Copy(sourceSheet);
    
    string destFile = dataDir + sheetName + ".xls";
    destWorkbook.Save(destFile, SaveFormat.Excel97To2003);
}
```

Beklenen çıktı, veri dizininde yeni dosyalardan oluşan bir kümedir; kaynak çalışma kitabındaki her çalışma sayfası için bir dosya. Her dosya, karşılık gelen kaynak sayfanın adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyası Bölme**

### **Yaklaşıma Genel Bakış**

Bazen bölmeniz gereken veriler, bir çalışma sayfasının tamamına değil, belirli bir dikdörtgen bölgesine (örneğin `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralık) karşılık gelir. Bu gibi durumlarda, çalışma sayfalarının tamamını kopyalamak israftır ve daha hassas bir yaklaşım gereklidir: kaynak aralığını belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içerikleri atarken daha büyük bir çalışma sayfasından tek bir tablo, rapor bloğu veya veri alanı çıkarmak istediğinizde idealdir. Bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. `Workbook` nesnesini dosya yoluyla örnekleyerek kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine (örneğin ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlu bir hücre aralığı veya `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.CreateRange` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığını hedef çalışma sayfasına, genellikle `A1` hücresinden başlayarak kopyalayın. Hedef `Cells` koleksiyonundaki `Cells.Copy` yöntemi, bir bütün aralığı kopyalamak için kullanılabilir; alternatif olarak, kaynak aralığın hücrelerini yineleyebilir ve değerlerini `PutValue` ile hedef hücrelere yazabilirsiniz. Ne aktarılacağını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.Save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```csharp
using System;
using System.IO;
using Aspose.Cells;

// Veri dizinini ve dosya yollarını tanımla
string dataDir = "data/";
string sourcePath = dataDir + "book1.xls";
string outputPath = dataDir + "outputrange.xls";

// Kaynak Excel dosyasını aç
Workbook sourceWorkbook = new Workbook(sourcePath);

// Kaynak çalışma kitabından ilk çalışma sayfasını al
Worksheet sourceWorksheet = sourceWorkbook.Worksheets[0];

// Kaynak hücre aralığını A1:C10 olarak tanımla (0. satır, 0. sütundan başlayan 10 satır, 3 sütun)
var sourceRange = sourceWorksheet.Cells.CreateRange(0, 0, 10, 3);

// Yeni bir hedef çalışma kitabı oluştur
Workbook destWorkbook = new Workbook();

// Hedef çalışma kitabındaki ilk çalışma sayfasına eriş
Worksheet destWorksheet = destWorkbook.Worksheets[0];

// A1'de kaynak aralıkla aynı boyutlarda hedef aralık oluştur
var destRange = destWorksheet.Cells.CreateRange(0, 0, 10, 3);

// Kaynak aralığı hedef aralığa kopyala
destRange.Copy(sourceRange);

// Hedef çalışma kitabını yeni bir .xls dosyasına kaydet
destWorkbook.Save(outputPath, SaveFormat.Excel97To2003);
```

Beklenen çıktı, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren veri dizininde tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayan çıkarılmış aralığı içerir.

## **İlgili Makaleler**

- [Satırları ve Sütunları Kopyalama](/cells/tr/net/copying-rows-and-columns/)
- [Hücreleri Birleştirme ve Birleştirmeyi Kaldırma](/cells/tr/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}