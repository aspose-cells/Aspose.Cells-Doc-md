---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
linktitle: Excel Dosyalarını Birden Çok Dosyaya
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için Python via Java kütüphanesidir ve tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bu makale, Excel dosyalarını her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak nasıl böleceğinizi anlatacaktır.
keywords: Aspose.Cells, Python via Java kütüphanesi, elektronik tablo, Excel dosyasını böl, çalışma sayfasını kopyala, aralığı kopyala, birden çok çalışma kitabı, ayrı dosyalar olarak kaydet
type: docs
weight: 195
url: /tr/python-java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, tek bir Excel dosyasını birden çok dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Her iki yaklaşım da veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri tek tek işleme için ayırmanız gerektiğinde kullanışlıdır.

{{% /alert %}}

## **Giriş**

Bir geliştiricinin tek bir Excel dosyasını birkaç küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her departman için bir çalışma sayfası içerebilir ve her departman yöneticisinin yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan e-posta yoluyla bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük konsolide çalışma kitaplarının da daha kolay işlenmesi, daha hızlı yüklenmesi veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.

Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineleyerek içeriğini yepyeni bir `Workbook` örneğine kopyalar ve her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: `Workbook` sınıfını kullanarak kaynak çalışma kitabını yükleyin, `Worksheet` ve `Cells` nesneleri aracılığıyla ilgili verilere erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır, ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.

Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Adımlar**

Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesi örnekleyerek ve dosya yolunu kurucusuna geçirerek kaynak Excel dosyasını açın.
2. `Workbook.Worksheets` koleksiyonunu `for` veya `foreach` döngüsü kullanarak yineleyin, böylece kaynak dosyadaki her `Worksheet` işlenir.
3. Döngü içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Hedef çalışma kitabına yeni bir `Worksheet` ekleyin (veya varsayılan ilk çalışma sayfasını kullanın) ve anlamlı bir ad atayın, ideal olarak kaynak çalışma sayfasının `Name` özelliğiyle aynı olacak şekilde.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreleri yineleyerek ve değerlerini hedef çalışma sayfasının ilgili hücrelerine yazarak ya da `Cells.copy` yöntemini kullanarak bir aralığı bir bütün olarak aktararak yapılabilir.
6. Kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.Name + ".xls"`) böylece oluşturulan her dosyanın benzersiz bir adı olur.
7. Dosyayı diske yazmak için hedef `Workbook.save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar bir sonraki çalışma sayfası için 3. adımdan 7. adıma kadar olan adımları tekrarlayın.

### **Kod Örneği**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

dataDir = "data/"
workbook = Workbook(dataDir + "book1.xls")

for i in range(workbook.getWorksheets().getCount()):
    sourceSheet = workbook.getWorksheets().get(i)
    sheetName = sourceSheet.getName()
    
    destWorkbook = Workbook()
    destIndex = destWorkbook.getWorksheets().add()
    destSheet = destWorkbook.getWorksheets().get(destIndex)
    destSheet.setName(sheetName)
    
    destSheet.copy(sourceSheet)
    
    destFile = dataDir + sheetName + ".xls"
    destWorkbook.save(destFile, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olmak üzere bir dizi yeni dosyadır. Her dosya, ilgili kaynak sayfanın adını taşır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**

Bazen bölmeniz gereken veriler bir çalışma sayfasının tamamına değil, `A1:D10` gibi belirli bir dikdörtgen bölgeye veya belirli bir tabloyu temsil eden adlandırılmış bir aralığa karşılık gelir. Bu durumlarda, tüm çalışma sayfalarını kopyalamak israftır ve daha hassas bir yaklaşım gereklidir: kaynak aralığı tanımlayın, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.

Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tablo, rapor bloğu veya veri alanı çıkarmak istediğinizde idealdir. Ayrıca bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**

Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:

1. Bir `Workbook` nesnesini dosya yoluyla örnekleyerek kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı tanımlayın. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı, `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.createRange` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığı hedef çalışma sayfasına, genellikle `A1` hücresinden başlayarak kopyalayın. Hedef `Cells` koleksiyonundaki `Cells.copy` yöntemi, bir aralığın tamamını kopyalamak için kullanılabilir veya kaynak aralığın hücreleri arasında yineleyerek değerlerini `putValue` ile hedef hücrelere yazabilirsiniz. Aktarılanları kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.save` yöntemini kullanarak hedef çalışma kitabını disk üzerinde yeni bir dosya yoluna kaydedin.

### **Kod Örneği**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# Veri dizinini ve dosya yollarını tanımlayın
dataDir = "data/"
sourcePath = dataDir + "book1.xls"
outputPath = dataDir + "outputrange.xls"

# Kaynak Excel dosyasını açın
sourceWorkbook = Workbook(sourcePath)

# Kaynak çalışma kitabından ilk çalışma sayfasını alın
sourceWorksheet = sourceWorkbook.getWorksheets().get(0)

# Kaynak hücre aralığını A1:C10 tanımlayın (0. satır, 0. sütundan başlayan 10 satır, 3 sütun)
sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3)

# Yeni bir hedef çalışma kitabı oluşturun
destWorkbook = Workbook()

# Hedef çalışma kitabındaki ilk çalışma sayfasına erişin
destWorksheet = destWorkbook.getWorksheets().get(0)

# A1'de kaynak aralıkla aynı boyutlarda hedef aralık oluşturun
destRange = destWorksheet.getCells().createRange(0, 0, 10, 3)

# Kaynak aralığı hedef aralığa kopyalayın
destRange.copy(sourceRange)

# Hedef çalışma kitabını yeni bir .xls dosyasına kaydedin
destWorkbook.save(outputPath, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayarak çıkarılan aralığı içerir.



{{< app/cells/assistant language="python" >}}