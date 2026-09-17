---
title: Excel Dosyalarını Birden Fazla Dosyaya Bölme
linktitle: Excel Dosyalarını Birden Fazla Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Java kütüphanesidir ve tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bu makale, Excel dosyalarını her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak nasıl böleceğinizi anlatacaktır.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, Excel dosyası bölme, çalışma sayfası kopyalama, aralık kopyalama, birden fazla çalışma kitabı, ayrı dosyalar olarak kaydetme
type: docs
weight: 195
url: /tr/java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabının her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasından belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Her iki yaklaşım da veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri ayrı ayrı işlenmek üzere izole etmeniz gerektiğinde kullanışlıdır.
{{% /alert %}}

## **Introduction**
Bir geliştiricinin tek bir Excel dosyasını birkaç küçük dosyaya ayırması gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı departman başına bir çalışma sayfası içerebilir ve her departman yöneticisinin yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarıp çalışma kitabının geri kalanını açığa çıkarmadan bağımsız bir dosya olarak e-posta ile göndermek isteyebilirsiniz. Büyük konsolide çalışma kitaplarının da daha kolay işleme, daha hızlı yükleme veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.
Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineler ve içeriğini yepyeni bir `Workbook` örneğine kopyalayarak her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: kaynak çalışma kitabını `Workbook` sınıfını kullanarak yükleyin, ilgili verilere `Worksheet` ve `Cells` nesneleri aracılığıyla erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Splitting an Excel File by Copying Each Worksheet to a New Workbook**

### **Approach Overview**
Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır, ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği daha sonra hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, çalışma sayfası başına bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.
Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Steps**
Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:
1. Dosya yolunu kurucusuna geçirerek bir `Workbook` nesnesi oluşturarak kaynak Excel dosyasını açın.
2. Kaynak dosyadaki her `Worksheet`'in işlenmesi için `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonunu yineleyin.
3. Döngü içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu işlem, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreleri yinelemek ve değerlerini hedef çalışma sayfasının ilgili hücrelerine yazmak ya da tüm bir aralığı bir seferde aktarmak için `Cells.copy` yöntemini kullanmak suretiyle yapılabilir.
6. Üretilen her dosyanın benzersiz bir ada sahip olması için kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.getName() + ".xls"`).
7. Dosyayı diske yazmak için hedef `Workbook.save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar sonraki çalışma sayfası için 3 ila 7 arasındaki adımları tekrarlayın.

### **Code Example**

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

Beklenen çıktı, veri dizinindeki yeni dosyalardan oluşan bir kümedir; kaynak çalışma kitabındaki her çalışma sayfası için bir dosya. Her dosya, karşılık gelen kaynak sayfanın adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Splitting an Excel File by Copying a Range to a New Workbook**

### **Approach Overview**
Bazen bölmeniz gereken veriler tüm bir çalışma sayfasına değil, `A1:D10` gibi belirli bir dikdörtgen bölgeye veya belirli bir tabloyu temsil eden adlandırılmış bir aralığa karşılık gelir. Bu gibi durumlarda tüm çalışma sayfalarını kopyalamak israf olur ve daha hassas bir yaklaşım gerekir: kaynak aralığı belirleyin, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.
Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Steps**
Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:
1. Dosya yolu ile bir `Workbook` nesnesi oluşturarak kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, dizine göre (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı veya `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık ya da `Worksheet.Cells.createRange` ile oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Hedef `Cells` koleksiyonu üzerindeki `Cells.copy` yöntemi tüm bir aralığı kopyalamak için kullanılabilir veya kaynak aralığın hücreleri arasında yinelenebilir ve değerleri `putValue` ile hedef hücrelere yazabilirsiniz. Aktarılanları kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Code Example**
Beklenen çıktı, kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren veri dizininde tek bir yeni dosyadır. Hedef dosya, kaynak dosyadaki başka herhangi bir veriyle ilişkili değildir; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayan çıkarılmış aralığı içerir.

## Related Articles
- [Aspose.Cells for Java'da Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java'da Pivot Tablolarına Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/java/change-page-field-layout/)
- [Aspose.Cells for Java'da Mini Grafiği Görüntüye ve HTML'ye Dönüştürme](/cells/tr/java/convert-sparkline-to-image-and-html/)
- [Excel'i OFD Formatına Dönüştürme](/cells/tr/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}