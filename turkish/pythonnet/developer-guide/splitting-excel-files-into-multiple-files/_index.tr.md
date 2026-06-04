---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Python via .NET kütüphanesidir ve tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini anlatacaktır.
keywords: Aspose.Cells, Python via .NET kütüphanesi, elektronik tablo, Excel dosyasını böl, çalışma sayfasını kopyala, aralığı kopyala, birden çok çalışma kitabı, ayrı dosyalar olarak kaydet
type: docs
weight: 195
url: /tr/python-net/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya tek tek işleme için verileri izole etmeniz gerektiğinde her iki yaklaşım da faydalıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç daha küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman yöneticisinin yalnızca kendi sayfasını alması gerekir. Diğer durumlarda, bir çalışma sayfasındaki belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan e-posta yoluyla bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük konsolide çalışma kitaplarının da daha kolay işlenmesi, daha hızlı yüklenmesi veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineler ve içeriğini yepyeni bir `Workbook` örneğine kopyalayarak her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: kaynak çalışma kitabını `Workbook` sınıfını kullanarak yükleyin, ilgili verilere `Worksheet` ve `Cells` nesneleri aracılığıyla erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Ardından kaynak çalışma sayfasının içeriği hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, çalışma sayfası başına bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi oluşturarak ve dosya yolunu yapıcısına ileterek kaynak Excel dosyasını açın.
2. Kaynak dosyadaki her `Worksheet`'in işlenmesi için `Workbook.worksheets` koleksiyonunu bir `for` döngüsü kullanarak yineleyin.
3. Döngü içinde, mevcut çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın, ideal olarak kaynak çalışma sayfasının `name` özelliğiyle aynı olmalıdır.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreleri yineleyerek ve değerlerini hedef çalışma sayfasının karşılık gelen hücrelerine yazarak veya tüm aralığı bir defada aktarmak için `Cells.copy` yöntemini kullanarak yapılabilir.
6. Kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.name + ".xls"`) böylece oluşturulan her dosyanın benzersiz bir adı olur.
7. Dosyayı diske yazmak için hedef `Workbook.save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar sonraki çalışma sayfası için 3'ten 7'ye kadar olan adımları tekrarlayın.

### **Kod Örneği**

```python
import aspose.cells as ac
import os

data_dir = "data/"
workbook = ac.Workbook(data_dir + "book1.xls")

for i in range(workbook.worksheets.count):
    source_sheet = workbook.worksheets[i]
    sheet_name = source_sheet.name
    
    dest_workbook = ac.Workbook()
    dest_index = dest_workbook.worksheets.add()
    dest_sheet = dest_workbook.worksheets[dest_index]
    dest_sheet.name = sheet_name
    
    dest_sheet.copy(source_sheet)
    
    dest_file = data_dir + sheet_name + ".xls"
    dest_workbook.save(dest_file, ac.SaveFormat.EXCEL97_TO_2003)
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olmak üzere yeni dosyalardan oluşan bir settir. Her dosya, karşılık gelen kaynak sayfanın adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bazen bölmeniz gereken veriler bir çalışma sayfasının tamamına değil, `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralık gibi çalışma sayfasının belirli bir dikdörtgen bölgesine karşılık gelir. Bu durumlarda, çalışma sayfalarının tamamını kopyalamak israf olur ve daha hassas bir yaklaşım gereklidir: kaynak aralığını belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Dosya yolu ile bir `Workbook` nesnesi oluşturarak kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, `worksheets` koleksiyonundan dizine (örneğin, ilk sayfa) veya ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı veya `Worksheet.cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.cells.create_range` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığını hedef çalışma sayfasına, genellikle `A1` hücresinden başlayarak kopyalayın. Tüm aralığı kopyalamak için hedef `Cells` koleksiyonu üzerindeki `Cells.copy` yöntemi kullanılabilir veya kaynak aralığın hücrelerini yineleyerek değerlerini `put_value` ile hedef hücrelere yazabilirsiniz. Ne aktarılacağını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```python
import aspose.cells as ac
import os

# Veri dizinini ve dosya yollarını tanımla
dataDir = "data/"
sourcePath = os.path.join(dataDir, "book1.xls")
outputPath = os.path.join(dataDir, "outputrange.xls")

# Kaynak Excel dosyasını aç
sourceWorkbook = ac.Workbook(sourcePath)

# Kaynak çalışma kitabından ilk çalışma sayfasını al
sourceWorksheet = sourceWorkbook.worksheets[0]

# Kaynak hücre aralığını A1:C10 olarak tanımla (0. satır, 0. sütundan başlayan 10 satır, 3 sütun)
sourceRange = sourceWorksheet.cells.create_range(0, 0, 10, 3)

# Yeni bir hedef çalışma kitabı oluştur
destWorkbook = ac.Workbook()

# Hedef çalışma kitabındaki ilk çalışma sayfasına eriş
destWorksheet = destWorkbook.worksheets[0]

# Kaynak aralıkla aynı boyutlarda A1'de hedef aralık oluştur
destRange = destWorksheet.cells.create_range(0, 0, 10, 3)

# Kaynak aralığı hedef aralığa kopyala
destRange.copy(sourceRange)

# Hedef çalışma kitabını yeni bir .xls dosyasına kaydet
destWorkbook.save(outputPath, ac.SaveFormat.EXCEL97_TO2003)
```

Beklenen çıktı, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren veri dizininde tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka hiçbir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayarak çıkarılan aralığı içerir.

## **İlgili Makaleler**

- [Satırları ve Sütunları Kopyalama](/cells/tr/python-net/copying-rows-and-columns/)
- [Hücreleri Birleştirme ve Birleştirmeyi Kaldırma](/cells/tr/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}