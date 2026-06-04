---
title: Excel Dosyalarını Birden Fazla Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kütüphanesidir ve tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini anlatacaktır.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, Excel dosyasını bölme, çalışma sayfası kopyalama, aralık kopyalama, birden fazla çalışma kitabı, ayrı dosyalar olarak kaydetme
type: docs
weight: 195
url: /tr/cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Verilerin alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri tek tek işlemek üzere ayırmanız gerektiğinde her iki yaklaşım da faydalıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman yöneticisinin yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan e-posta yoluyla bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük ve birleştirilmiş çalışma kitaplarının da daha kolay işlenmesi, daha hızlı yüklenmesi veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineleyerek içeriğini yepyeni bir `Workbook` örneğine kopyalar ve her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: kaynak çalışma kitabını `Workbook` sınıfını kullanarak yükleyin, ilgili verilere `Worksheet` ve `Cells` nesneleri aracılığıyla erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Daha sonra kaynak çalışma sayfasının içeriği hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç olarak, her çalışma sayfası için bir çıktı dosyası elde edilir ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde bu yöntem doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturup dosya yolunu yapıcısına geçirerek kaynak Excel dosyasını açın.
2. Kaynak dosyadaki her `Worksheet`'in işlenmesi için bir `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonu boyunca yineleyin.
3. Döngünün içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın; ideal olarak kaynak çalışma sayfasının `Name` özelliğiyle aynı olmalıdır.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücrelerde yineleyerek değerlerini hedef çalışma sayfasının ilgili hücrelerine yazarak veya tüm bir aralığı bir defada aktarmak için `Cells.Copy` yöntemini kullanarak yapılabilir.
6. Oluşturulan her dosyanın benzersiz bir ada sahip olması için kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.Name + ".xls"`).
7. Dosyayı diske yazmak için hedef `Workbook.Save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar bir sonraki çalışma sayfası için 3 ile 7 arasındaki adımları tekrarlayın.

### **Kod Örneği**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));

    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();

        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);

        destSheet.Copy(sourceSheet);

        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Beklenen çıktı, veri dizininde, kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olmak üzere bir dizi yeni dosyadır. Her dosya, ilgili kaynak sayfanın adını taşır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bazen bölmeniz gereken veriler tüm bir çalışma sayfasına değil, bir çalışma sayfasının `A1:D10` gibi belirli dikdörtgen bir bölgesine ya da belirli bir tabloyu temsil eden adlandırılmış bir aralığa karşılık gelir. Bu gibi durumlarda, tüm çalışma sayfalarını kopyalamak verimsizdir ve daha hassas bir yaklaşım gereklidir: kaynak aralığı belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içerikleri atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Ayrıca bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturup dosya yolunu geçirerek kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlu bir hücre aralığı, `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.CreateRange` yoluyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Tüm bir aralığı kopyalamak için hedef `Cells` koleksiyonundaki `Cells.Copy` yöntemi kullanılabilir ya da kaynak aralığın hücrelerinde yineleyerek değerlerini `PutValue` ile hedef hücrelere yazabilirsiniz. Ne aktarılacağını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.Save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Veri dizinini ve dosya yollarını tanımla
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Kaynak Excel dosyasını aç
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Kaynak çalışma kitabından ilk çalışma sayfasını al
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Kaynak hücre aralığını A1:C10 olarak tanımla (0. satır, 0. sütundan başlayarak 10 satır, 3 sütun)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Yeni bir hedef çalışma kitabı oluştur
    Workbook destWorkbook;

    // Hedef çalışma kitabındaki ilk çalışma sayfasına eriş
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // A1'de kaynak aralıkla aynı boyutlarda bir hedef aralık oluştur
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Kaynak aralığı hedef aralığa kopyala
    destRange.Copy(sourceRange);

    // Hedef çalışma kitabını yeni bir .xls dosyasına kaydet
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Beklenen çıktı, veri dizininde, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren tek bir yeni dosyadır. Hedef dosya, kaynak dosyadaki başka hiçbir veriyle ilişkili değildir; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayan çıkarılmış aralığı içerir.

## **İlgili Makaleler**

- [Satırları ve Sütunları Kopyalama](/cells/tr/cpp/copying-rows-and-columns/)
- [Hücreleri Birleştirme ve Birleştirmeyi Kaldırma](/cells/tr/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}