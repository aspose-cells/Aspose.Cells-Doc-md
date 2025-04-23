---
title: Aspose.Cells te Öncül ve Bağımlıları İzleme
type: docs
weight: 130
url: /tr/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

Özellikle ortak geliştirilen karmaşık finansal çalışma tabloları, en utanç verici hataları saklayabilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, öncü hücreler ve bağımlı hücreleri kullanan formülün olduğu durumlarda zor olabilir.

- **Öncül hücreler**, başka bir Hücredeki bir formül tarafından başvurulan hücrelerdir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin öncül hücresidir.
- **Bağımlı hücreler**, diğer hücrelere başvuran formülleri içerir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresinin bağımlısıdır.

Elektronik tabloyu okunabilir hale getirmek için belki de bir formülde kullanılan hangi hücreleri açıkça göstermek istersiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenize ve hangi hücrelerin bağlı olduğunu bulmanıza olanak tanır.

{{% /alert %}} 
## **Öncekileri ve Bağımlı Hücreleri İzleme: Microsoft Excel**
Formüller, bir müşteri tarafından yapılan değişikliklere bağlı olarak değişebilir. Örneğin, C1 hücresi C3 ve C4 içeren bir formüle bağımlı ise ve C1 değiştirilirse (böylece formül geçersiz kılınırsa), C3 ve C4 veya diğer hücreler, iş kurallarına göre elektronik tabloyu dengelemek için değişmelidir.

Benzer şekilde, C1'in "=(B1*22)/(M2*N32)" formülünü içerdiğini varsayalım. C1'e bağımlı olan yani önce gelen B1, M2 ve N32 hücrelerini bulmak istiyorum.

Belirli bir hücrenin bağımlılığını diğer hücrelere takip etmeniz gerekebilir. İş kuralları formüllere gömülü ise, bağımlılığı bulmak ve buna göre bazı kuralları uygulamak isteriz. Benzer şekilde belirli bir hücrenin değeri değiştirildiğinde, çalışma sayfasında bu değişiklikten etkilenen hücreler hangileridir?

Microsoft Excel, öncekileri ve bağımlıları izlemek için kullanıcılara olanak sağlar.

1. **Görünüm Araç Çubuğu**'nda **Formül Denetimi**'ni seçin.
   Formül Denetimi iletişim kutusu görüntülenir. 
   **Formül Denetimi iletişim kutusu** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Önceden Gelenleri İzleme:
   1. Önceden gelen hücreleri bulmak istediğiniz formül içeren hücreyi seçin.
   1. Doğrudan veri sağlayan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Önceden Gelenleri İzle**'yi tıklatın.
1. Belirli bir hücreyi referans olarak alan formülleri izle (bağımlılar)
   1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
   1. Aktif hücreye bağımlı olan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Bağımlıları İzle**'yi tıklatın.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Aspose.Cells**
### **Öncüleri İzleme**
Aspose.Cells, öncelikli hücreleri almayı kolaylaştırır. Sadece basit bir formülün öncekilerini değil, adlandırılmış aralıklarla karmaşık bir formülün önceliklerini de bulabilir.

Aşağıdaki örnekte, bir şablon excel dosyası olan Book1.xls kullanılmıştır. Elektronik tabloda veri ve formüller bulunmaktadır.

**Giriş elektronik tablosu** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells, bir hücrenin önceliklerini izlemek için kullanılan Cell sınıfının GetPrecedents yöntemini sağlar. Bir ReferredAreaCollection döndürür. Yukarıda gördüğünüz gibi, Book1.xls'de B7 hücresi "=SUM(A1:A3)" formülünü içerir. Bu nedenle A1:A3 hücreleri, B7 hücresinin öncelikli hücreleridir. Aşağıdaki örnek, şablon dosya Book1.xls kullanılarak öncekileri izleme özelliğini göstermektedir.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells, elektronik tablolardaki bağımlı hücreleri almanıza olanak sağlar. Aspose.Cells, yalnızca basit bir formülle ilgili veri sağlayan hücreleri alabilir, aynı zamanda adlandırılmış aralıklarla karmaşık bir formülün bağımlılarını da bulabilir.

Aspose.Cells, bir hücrenin bağımlılarını izlemek için kullanılan Cell sınıfının GetDependents yöntemini sağlar. Örneğin, Book1.xlsx dosyasında B2 ve C2 hücrelerinde sırasıyla "=A1+20" ve "=A1+30" formülleri bulunmaktadır. A1 hücresinin bağımlılarını izlemenin örneğini aşağıdaki örnek göstermektedir.

**C#**

{{< highlight csharp >}}

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
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

{{< app/cells/assistant language="csharp" >}}
