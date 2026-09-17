---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
linktitle: Excel Dosyalarını Birden Çok Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kütüphanesidir ve tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini açıklayacaktır.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, Excel dosyası bölme, çalışma sayfası kopyalama, aralık kopyalama, birden çok çalışma kitabı, ayrı dosyalar olarak kaydetme
type: docs
weight: 195
url: /tr/cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Her iki yaklaşım da veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri bireysel işleme için ayırmanız gerektiğinde kullanışlıdır.
{{% /alert %}}

## **Introduction**
Bir geliştiricinin tek bir Excel dosyasını birkaç daha küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman başkanının yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını ifşa etmeden e-posta yoluyla bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük birleştirilmiş çalışma kitaplarının da daha kolay işleme, daha hızlı yükleme veya diğer sistemler tarafından sonraki işleme için daha küçük parçalara bölünmesi gerekebilir.
Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineler ve içeriğini yepyeni bir `Workbook` örneğine kopyalayarak her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: kaynak çalışma kitabını `Workbook` sınıfını kullanarak yükleyin, `Worksheet` ve `Cells` nesneleri aracılığıyla ilgili verilere erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Splitting an Excel File by Copying Each Worksheet to a New Workbook**

### **Approach Overview**
Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Ardından kaynak çalışma sayfasının içeriği hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, çalışma sayfası başına bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.
Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Steps**
Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:
1. Bir `Workbook` nesnesi örnekleyerek ve dosya yolunu yapıcısına geçirerek kaynak Excel dosyasını açın.
2. Kaynak dosyadaki her `Worksheet`'in işlenmesi için `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonu boyunca yineleyin.
3. Döngünün içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabının ilk `Worksheet`'ine erişin; bu, kopyalanan içeriğin yerleştirileceği hedef sayfadır.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreler arasında yinelenerek ve değerlerini hedef çalışma sayfasının ilgili hücrelerine yazılarak veya bir bütün aralığı bir kerede aktarmak için `Cells.Copy` yöntemi kullanılarak yapılabilir.
6. Kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.Name + ".xls"`) böylece oluşturulan her dosya benzersiz bir ada sahip olur.
7. Dosyayı diske yazmak için hedef `Workbook.Save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar 3-7 arasındaki adımları bir sonraki çalışma sayfası için tekrarlayın.

### **Code Example**

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

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olmak üzere yeni dosyalardan oluşan bir kümedir. Her dosya, karşılık gelen kaynak sayfasının adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Splitting an Excel File by Copying a Range to a New Workbook**

### **Approach Overview**
Bazen bölmeniz gereken veriler tüm bir çalışma sayfasına değil, bir çalışma sayfasının `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralık gibi belirli bir dikdörtgen bölgesine karşılık gelir. Bu durumlarda, tüm çalışma sayfalarını kopyalamak verimsizdir ve daha hassas bir yaklaşım gereklidir: kaynak aralığını tanımlayın, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.
Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tablo, rapor bloğu veya veri alanı çıkarmak istediğinizde idealdir. Ayrıca bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Steps**
Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:
1. Bir `Workbook` nesnesini dosya yoluyla örnekleyerek kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine göre (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı tanımlayın. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı veya `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.CreateRange` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Tüm bir aralığı kopyalamak için hedef `Cells` koleksiyonundaki `Cells.Copy` yöntemi kullanılabilir veya kaynak aralığın hücreleri arasında yinelenerek değerleri `PutValue` ile hedef hücrelere yazabilirsiniz. Aktarılanı kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.Save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Code Example**
Beklenen çıktı, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren veri dizininde tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayarak çıkarılan aralığı içerir.

## Related Articles
- [Aspose.Cells for C++ ile Özet Tablosuna Filtre Alanları Ekleme](/cells/tr/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++ ile Özet Tablolarına Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
- [Özet Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/cpp/change-page-field-layout/)
- [Aspose.Cells for C++ ile Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/cpp/convert-sparkline-to-image-and-html/)
- [Excel'i OFD Formatına Dönüştürme](/cells/tr/cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="cpp" >}}