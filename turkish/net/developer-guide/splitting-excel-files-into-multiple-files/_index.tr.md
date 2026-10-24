---
title: Excel Dosyalarını Birden Fazla Dosyaya Bölme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kitaplığıdır ve tek bir Excel dosyasını birden fazla dosyaya bölme desteği sunar. Bu makale, her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak Excel dosyalarının nasıl bölüneceğini açıklayacaktır.
linktitle: Excel Dosyalarını Birden Fazla Dosyaya Bölme
keywords: Aspose.Cells, .NET kitaplığı, elektronik tablo, Excel dosyası bölme, çalışma sayfası kopyalama, aralık kopyalama, birden fazla çalışma kitabı, ayrı dosyalar olarak kaydetme
type: docs
weight: 195
url: /tr/net/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tek bir Excel dosyasını birden fazla dosyaya bölme desteği sunar. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp her birini ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya verileri ayrı ayrı işlemeye ayırmanız gerektiğinde her iki yaklaşım da kullanışlıdır.
{{% /alert %}}

## **Giriş**
Gerçek dünyada tek bir Excel dosyasını birkaç daha küçük dosyaya ayırması gereken geliştiriciler için birçok senaryo vardır. Örneğin, bir çalışma kitabı departman başına bir çalışma sayfası içerebilir ve her departman yöneticisine yalnızca kendi sayfasını göndermesi gerekir. Başka durumlarda, belirli bir tabloyu veya veri bloğunu bir çalışma sayfasından çıkarıp çalışma kitabının geri kalanını açığa çıkarmadan e-posta ile bağımsız bir dosya olarak göndermek isteyebilirsiniz. Büyük birleştirilmiş çalışma kitaplarının da kolay yönetim, daha hızlı yükleme veya diğer sistemler tarafından sonraki işlemler için daha küçük parçalara bölünmesi gerekebilir.
Aspose.Cells bu görev için iki esnek yaklaşım sağlar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfası üzerinde yinelenir ve içeriğini tamamen yeni bir `Workbook` örneğine kopyalar; her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım ise bir çalışma sayfasındaki belirli bir hücre aralığına odaklanır ve yalnızca bu aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynıdır: `Workbook` sınıfını kullanarak kaynak çalışma kitabını yükleyin, ilgili veriye `Worksheet` ve `Cells` nesneleri üzerinden erişin, içeriği hedef `Workbook` nesnesine aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Bir Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**
Bu yaklaşımda kaynak çalışma kitabı bir kez açılır; ardından `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği, hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, kaynak çalışma sayfasının adından türetilen bir dosya adıyla kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır; her çıktı dosyası tek bir kaynak sayfanın verilerini içerir.
Bu yöntem, kaynak çalışma kitabınızda her çalışma sayfasının mantıksal olarak bağımsız bir bilgi birimini (departman, bölge, ay veya ürün hattı gibi) temsil ettiği ve her birimi ayrı ayrı teslim etmek veya işlemek istediğiniz durumlarda doğru seçimdir.

### **Adımlar**
Her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasını bölmek için aşağıdaki adımlar izlenir:
1. Kaynak Excel dosyasını bir `Workbook` nesnesi oluşturarak ve dosya yolunu yapıcısına geçirerek açın.
2. Kaynak dosyadaki her `Worksheet` öğesinin işlenmesini sağlamak için `Workbook.Worksheets` koleksiyonunda `for` veya `foreach` döngüsüyle yinelenin.
3. Döngü içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.
4. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu işlem, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreler üzerinde yinelenerek değerlerinin hedef çalışma sayfasındaki karşılık gelen hücrelere yazılmasıyla veya `Cells.Copy` yöntemiyle tüm aralığın tek seferde aktarılmasıyla gerçekleştirilebilir.
5. Her oluşturulan dosyaya benzersiz bir ad vermek için kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin, `dataDir + worksheet.Name + ".xls"`).
6. Dosyayı diske yazmak için hedef `Workbook.Save` yöntemini çağırın.
7. Tüm çalışma sayfaları işlenene kadar sonraki çalışma sayfası için 3 ila 6. adımları yineleyin.

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

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir olmak üzere yeni dosyalardan oluşan bir kümedir. Her dosya, karşılık gelen kaynak sayfanın adını taşır ve dosya yalnızca bu tek sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Belirli Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Bir Excel Dosyasını Bölme**

### **Yaklaşıma Genel Bakış**
Bazen bölmek istediğiniz veri, bir çalışma sayfasının tamamına değil, `A1:D10` gibi belirli bir dikdörtgen bölgesine veya belirli bir tabloyu temsil eden adlandırılmış bir aralığa karşılık gelir. Bu durumlarda tüm çalışma sayfalarını kopyalamak gereksizdir ve daha hassas bir yaklaşım gerekir: kaynak aralığı belirleyin, yalnızca bu aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.
Bu yaklaşım, ilgisiz tüm içeriği atarken daha büyük bir çalışma sayfasından tek bir tabloyu, rapor bloğunu veya veri alanını çıkarmak istediğinizde idealdir. Bir sayfanın kullanıcı tarafından seçilen bölgelerini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**
Belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasını bölmek için aşağıdaki adımlar izlenir:
1. Kaynak Excel dosyasını dosya yoluyla bir `Workbook` nesnesi oluşturarak açın.
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet` öğesini, `Worksheets` koleksiyonundan dizine (örneğin ilk sayfa) veya ada göre alın.
3. Kopyalanacak aralığı belirleyin. Bu, `A1:C10` gibi sabit kodlanmış bir hücre aralığı, `Worksheet.Cells` koleksiyonu üzerinden alınan adlandırılmış bir aralık veya `Worksheet.Cells.CreateRange` ile oluşturulan bir aralık olabilir.
4. Yeni bir hedef `Workbook` örneği oluşturun.
5. Hedef çalışma kitabının ilk `Worksheet` öğesine (varsayılan sayfa) erişin.
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Tüm aralığı kopyalamak için hedef `Cells` koleksiyonundaki `Cells.Copy` yöntemi kullanılabilir; alternatif olarak kaynak aralığın hücreleri üzerinde yinelenip değerlerini `PutValue` ile hedef hücrelere yazabilirsiniz. Aktarılacak içeriği (yalnızca değerler, değerler ve biçimler, formüller vb.) kontrol etmek için isteğe bağlı `CopyOptions` sağlanabilir.
7. `Workbook.Save` yöntemini kullanarak hedef çalışma kitabını diskte yeni bir dosya yoluna kaydedin.

### **Kod Örneği**
Beklenen çıktı, veri dizininde yalnızca kaynak çalışma kitabından çıkarılan belirtilen aralığın değerlerini (ve isteğe bağlı olarak biçimlendirmesini) içeren tek bir yeni dosyadır. Hedef dosyanın kaynak dosyadaki diğer herhangi bir veriyle ilişkisi yoktur; yalnızca ilk çalışma sayfasının `A1` hücresinden başlayarak çıkarılan aralığı içerir.

{{< app/cells/assistant language="csharp" >}}