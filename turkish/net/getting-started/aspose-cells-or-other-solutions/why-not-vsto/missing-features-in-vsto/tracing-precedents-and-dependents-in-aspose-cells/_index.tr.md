---
title: Aspose.Cells'de Emsallerin ve Bağımlıların İzlenmesi
type: docs
weight: 130
url: /tr/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

Karmaşık finansal çalışma sayfaları, özellikle işbirliği içinde geliştirilenler, en utanç verici hataları gizleyebilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, formül emsal hücreler ve bağımlı hücreler kullandığında zor olabilir.

- **emsal hücreler** başka bir Cell'deki bir formülle başvurulan hücrelerdir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin emsalidir.
- **Bağımlı hücreler** diğer hücrelere başvuran formüller içerir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresinin bağımlısıdır.

Elektronik tablonun okunmasını kolaylaştırmak için, formülde elektronik tablodaki hangi hücrelerin kullanıldığını açıkça göstermek isteyebilirsiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenizi ve hangilerinin bağlantılı olduğunu bulmanızı sağlar.

{{% /alert %}} 
## **Emsal ve Bağımlı İzleme Cells: Microsoft Excel**
Formüller, bir müşteri tarafından yapılan değişikliklere bağlı olarak değişebilir. Örneğin, C1 hücresi bir formül içeren C3 ve C4'e bağımlıysa ve C1 değiştirilirse (bu nedenle formül geçersiz kılınır), C3 ve C4 veya diğer hücrelerin, elektronik tabloyu iş kurallarına göre dengelemek için değişmesi gerekir.

Benzer şekilde, C1'in "=(B1*22)/(M2*N32)". C1'in bağlı olduğu hücreleri, yani öncül B1, M2 ve N32 hücrelerini bulmak istiyorum.

Belirli bir hücrenin diğer hücrelere bağımlılığını izlemeniz gerekebilir. İş kuralları formüllere gömülüyse, bağımlılığı bulmak ve buna dayalı olarak bazı kurallar uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücreler bu değişiklikten etkilenir?

Microsoft Excel, kullanıcıların emsalleri ve bağımlıları izlemesine olanak tanır.

1.  Üzerinde**Araç Çubuğunu Görüntüle** , seçme**Formül Denetimi**.
 Formül Denetimi iletişim kutusu görüntülenir.
   **Formül Denetimi iletişim kutusu** 

![yapılacaklar:resim_alternatif_metin](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Emsalleri İzleyin:
1. Emsal hücreleri bulmak istediğiniz formülü içeren hücreyi seçin.
 1. Etkin hücreye doğrudan veri sağlayan her hücreye bir izleme oku görüntülemek için,**Emsalleri İzleyin** üzerinde**Formül Denetimi** araç çubuğu.
1. Belirli bir hücreye başvuran formülleri izleme (bağımlı olanlar)
 1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
 1. Etkin hücreye bağımlı olan her hücreye bir izleme oku görüntülemek için Formül Denetimi araç çubuğunda Bağımlıları İzle'ye tıklayın.
## **Emsal ve Bağımlı İzleme Cells: Aspose.Cells**
### **Emsallerin İzini Sürmek**
Aspose.Cells, emsal hücreleri almayı kolaylaştırır. Yalnızca basit bir formül emsallerine veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık bir formül emsallerine veri sağlayan hücreleri de bulabilir.

Aşağıdaki örnekte, Book1.xls adlı bir şablon excel dosyası kullanılmıştır. Elektronik tablonun ilk Çalışma Sayfasında veriler ve formüller bulunur.

**Giriş e-tablosu** 

![yapılacaklar:resim_alternatif_metin](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells, Cell sınıfının bir hücrenin emsallerini izlemek için kullanılan GetPrecedents yöntemini sağlar. Bir ReferredAreaCollection döndürür. Yukarıda görebileceğiniz gibi, Book1.xls'de B7 hücresi "=SUM(A1:A3)" formülünü içerir. Yani A1:A3 hücreleri, B7 hücresinin öncül hücreleridir. Aşağıdaki örnek, Book1.xls şablon dosyasını kullanan emsalleri izleme özelliğini göstermektedir.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **Bağımlıları İzleme**
Aspose.Cells, elektronik tablolarda bağımlı hücreler almanızı sağlar. Aspose.Cells, yalnızca basit bir formülle ilgili veri sağlayan hücreleri almakla kalmaz, aynı zamanda adlandırılmış aralıklara sahip karmaşık bir formül bağımlılarına veri sağlayan hücreleri de bulabilir.

Aspose.Cells, bir hücrenin bağımlılarını izlemek için kullanılan Cell sınıfının GetDependents yöntemini sağlar. Örneğin, Book1.xlsx'te B2 ve C2 hücrelerinde sırasıyla "=A1+20" ve "=A1+30" formülleri vardır. Aşağıdaki örnek, Book1.xlsx şablon dosyası kullanılarak A1 hücresi için bağımlıların nasıl izleneceğini gösterir.

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

