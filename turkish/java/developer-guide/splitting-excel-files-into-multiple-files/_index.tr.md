---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Java kütüphanesidir ve tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini anlatacaktır.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, Excel dosyası bölme, çalışma sayfası kopyalama, aralık kopyalama, birden çok çalışma kitabı, ayrı dosyalar olarak kaydetme
type: docs
weight: 195
url: /tr/java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabının her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri tek tek işlenmek üzere izole etmeniz gerektiğinde her iki yaklaşım da faydalıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman yöneticisinin yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan bağımsız bir dosya olarak e-posta ile göndermek isteyebilirsiniz. Büyük ve birleştirilmiş çalışma kitaplarının da daha kolay yönetim, daha hızlı yükleme veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineler ve içeriğini yepyeni bir `Workbook` örneğine kopyalayarak her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: kaynak çalışma kitabını `Workbook` sınıfını kullanarak yükleyin, ilgili verilere `Worksheet` ve `Cells` nesneleri aracılığıyla erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyası Bölme**

### **Yaklaşıma Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır, ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Daha sonra kaynak çalışma sayfasının içeriği hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, kaynak çalışma sayfasının adını taşıyan bir dosya olarak kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde bu yöntem doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturarak ve dosya yolunu yapıcısına geçirerek kaynak Excel dosyasını açın.
2. `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonu boyunca yineleyin, böylece kaynak dosyadaki her `Worksheet` işlenir.
3. Döngü içinde, mevcut çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın; ideal olarak kaynak çalışma sayfasının `Name` özelliğiyle aynı olmalıdır.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreler üzerinde yineleyerek ve değerlerini hedef çalışma sayfasının ilgili hücrelerine yazarak veya bir seferde tüm bir aralığı aktarmak için `Cells.copy` yöntemini kullanarak yapılabilir.
6. Kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.getName() + ".xls"`) böylece oluşturulan her dosyanın benzersiz bir adı olur.
7. Dosyayı diske yazmak için hedef `Workbook.save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar sonraki çalışma sayfası için 3'ten 7'ye kadar olan adımları tekrarlayın.

### **Kod Örneği**

```java
import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olmak üzere yeni dosyalardan oluşan bir kümedir. Her dosya, karşılık gelen kaynak sayfanın adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyası Bölme**

### **Yaklaşıma Genel Bakış**

Bazen bölmeniz gereken veriler bir çalışma sayfasının tamamına değil, belirli bir dikdörtgen bölgesine karşılık gelir; örneğin `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralık. Bu gibi durumlarda, tüm çalışma sayfalarını kopyalamak verimsizdir ve daha hassas bir yaklaşım gereklidir: kaynak aralığı belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Ayrıca bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Dosya yolu ile bir `Workbook` nesnesi oluşturarak kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine göre (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı, `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.createRange` ile oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Hedef `Cells` koleksiyonundaki `Cells.copy` yöntemi, tüm bir aralığı kopyalamak için kullanılabilir veya kaynak aralığın hücreleri üzerinde yineleyebilir ve değerlerini `putValue` ile hedef hücrelere yazabilirsiniz. Ne aktarılacağını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. Hedef çalışma kitabını `Workbook.save` yöntemini kullanarak diskte yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```java
import com.aspose.cells.*;

// Veri dizinini ve dosya yollarını tanımla
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// Kaynak Excel dosyasını aç
Workbook sourceWorkbook = new Workbook(sourcePath);

// Kaynak çalışma kitabından ilk çalışma sayfasını al
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Kaynak hücre aralığını A1:C10 olarak tanımla (0. satır, 0. sütundan başlayan 10 satır, 3 sütun)
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Yeni bir hedef çalışma kitabı oluştur
Workbook destWorkbook = new Workbook();

// Hedef çalışma kitabındaki ilk çalışma sayfasına eriş
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// Hedef aralığı A1'de kaynak aralıkla aynı boyutlarda oluştur
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Kaynak aralığı hedef aralığa kopyala
destRange.copy(sourceRange);

// Hedef çalışma kitabını yeni bir .xls dosyasına kaydet
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);
```

Beklenen çıktı, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren, veri dizininde tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayan çıkarılmış aralığı içerir.

## **İlgili Makaleler**

- [Satırları ve Sütunları Kopyalama](/tr/cells/java/copying-rows-and-columns/)
- [Hücreleri Birleştirme ve Birleştirmeyi Kaldırma](/tr/cells/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}