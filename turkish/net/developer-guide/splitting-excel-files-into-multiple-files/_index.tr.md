---
title: Excel Dosyalarını Birden Çok Dosyaya Bölme
linktitle: Excel Dosyalarını Birden Çok Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir .NET kütüphanesidir ve tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini anlatacaktır.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, Excel dosyasını böl, çalışma sayfasını kopyala, aralığı kopyala, birden çok çalışma kitabı, ayrı dosyalar olarak kaydet
type: docs
weight: 195
url: /tr/net/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tek bir Excel dosyasını birden fazla dosyaya bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri tek tek işleme için ayırmanız gerektiğinde her iki yaklaşım da yararlıdır.
{{% /alert %}}

## **Introduction**
Bir geliştiricinin tek bir Excel dosyasını birkaç küçük dosyaya bölmesi gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı departman başına bir çalışma sayfası içerebilir ve her departman yöneticisinin yalnızca kendi sayfasını alması gerekir. Diğer durumlarda, bir çalışma sayfasından belirli bir tabloyu veya veri bloğunu çıkarmak ve çalışma kitabının geri kalanını açığa çıkarmadan e-posta yoluyla bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük konsolide çalışma kitaplarının da daha kolay işleme, daha hızlı yükleme veya diğer sistemler tarafından sonraki işlemeler için daha küçük parçalara bölünmesi gerekebilir.
Aspose.Cells bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını yineleyerek içeriğini yepyeni bir `Workbook` örneğine kopyalar ve her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfası içindeki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: kaynak çalışma kitabını `Workbook` sınıfını kullanarak yükleyin, ilgili verilere `Worksheet` ve `Cells` nesneleri aracılığıyla erişin, içeriği hedef `Workbook`'a aktarın ve ardından hedefi diske kaydedin.

## **Splitting an Excel File by Copying Each Worksheet to a New Workbook**

### **Approach Overview**
Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği daha sonra hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, adı kaynak çalışma sayfasının adından türetilen bir dosya olarak kaydedilir. Sonuç, çalışma sayfası başına bir çıktı dosyasıdır ve her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.
Bu yöntem, kaynak çalışma kitabınızdaki her çalışma sayfası mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiğinde ve her birimi kendi başına teslim etmek veya işlemek istediğinizde doğru seçimdir.

### **Steps**
Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:
1. Bir `Workbook` nesnesi örnekleyerek ve dosya yolunu kurucusuna ileterek kaynak Excel dosyasını açın.
2. Kaynak dosyadaki her `Worksheet`'in işlenmesi için `for` veya `foreach` döngüsü kullanarak `Workbook.Worksheets` koleksiyonunu yineleyin.
3. Döngü içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreleri yineleyerek ve değerlerini hedef çalışma sayfasının karşılık gelen hücrelerine yazarak veya bir seferde tüm bir aralığı aktarmak için `Cells.Copy` yöntemini kullanarak yapılabilir.
6. Her oluşturulan dosyanın benzersiz bir ada sahip olması için kaynak çalışma sayfasının adını (örneğin, `dataDir + worksheet.Name + ".xls"`) içeren bir çıktı dosya yolu oluşturun.
7. Dosyayı diske yazmak için hedef `Workbook.Save` yöntemini çağırın.
8. Tüm çalışma sayfaları işlenene kadar sonraki çalışma sayfası için 3'ten 7'ye kadar olan adımları tekrarlayın.

### **Code Example**

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

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki çalışma sayfası başına bir dosya olmak üzere yeni dosyalardan oluşan bir kümedir. Her dosya, karşılık gelen kaynak sayfasının adıyla adlandırılır ve dosya o tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Splitting an Excel File by Copying a Range to a New Workbook**

### **Approach Overview**
Bazen bölmeniz gereken veriler tüm bir çalışma sayfasına değil, bir çalışma sayfasının belirli bir dikdörtgen bölgesine karşılık gelir; örneğin `A1:D10` veya belirli bir tabloyu temsil eden adlandırılmış bir aralık. Bu gibi durumlarda, tüm çalışma sayfalarını kopyalamak israfçadır ve daha hassas bir yaklaşım gereklidir: kaynak aralığı tanımlayın, yalnızca o aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.
Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tablo, rapor bloğu veya veri alanı çıkarmak istediğinizde idealdir. Ayrıca bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de yararlıdır.

### **Steps**
Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasının nasıl bölüneceğini açıklar:
1. Bir `Workbook` nesnesini dosya yoluyla örnekleyerek kaynak Excel dosyasını açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i dizine (örneğin, ilk sayfa) veya `Worksheets` koleksiyonundan ada göre alın.
3. Kopyalanacak aralığı tanımlayın. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı veya `Worksheet.Cells` koleksiyonu aracılığıyla elde edilen adlandırılmış bir aralık veya `Worksheet.Cells.CreateRange` aracılığıyla oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Hedef `Cells` koleksiyonundaki `Cells.Copy` yöntemi, tüm bir aralığı kopyalamak için kullanılabilir veya kaynak aralığın hücrelerini yineleyerek değerlerini `PutValue` ile hedef hücrelere yazabilirsiniz. Ne aktarılacağını kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir (yalnızca değerler, değerler ve stiller, formüller vb.).
7. `Workbook.Save` yöntemini kullanarak hedef çalışma kitabını diskteki yeni bir dosya yoluna kaydedin.

### **Code Example**
Beklenen çıktı, veri dizininde kaynak çalışma kitabından çıkarılan belirtilen aralığın yalnızca değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki başka herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayan çıkarılmış aralığı içerir.

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/tr/net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for .NET](/cells/tr/net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/tr/net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for .NET](/cells/tr/net/convert-sparkline-to-image-and-html/)
- [Converting Excel to OFD Format](/cells/tr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}