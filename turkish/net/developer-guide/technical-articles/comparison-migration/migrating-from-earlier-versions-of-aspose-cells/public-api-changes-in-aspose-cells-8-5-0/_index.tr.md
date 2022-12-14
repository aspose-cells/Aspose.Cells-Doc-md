---
title: Genel API Aspose.Cells 8.5.0'daki değişiklikler
type: docs
weight: 160
url: /tr/net/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.4.2'den 8.5.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-5-0/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **ICustomFunction.CalculateCustomFunction Parametreleri Değiştirildi**
Özel işlev için bir parametre hücre referansıysa, eski sürüm Aspose.Cells'de API'ler, hücre referansını başvurulan alandaki tüm hücre değerlerinin bir nesne dizisine veya bir hücre değerine dönüştürmek için kullanılır. Bununla birlikte, birçok işlev ve kullanıcı için, başvurulan alandaki tüm hücreler için hücre değerleri dizisi gerekli değildir, yalnızca formülün konumuna karşılık gelen tek bir hücreye ihtiyaç duyarlar veya hücre değeri veya değer dizisi yerine yalnızca başvurunun kendisine ihtiyaç duyarlar. . Bazı durumlarda, tüm hücre değerlerinin getirilmesi döngüsel referans hatası riskini bile artırdı.

Bu tür bir gereksinimi desteklemek için Aspose.Cells for .NET 8.5.0, belirtilen alan için parametre değerini "paramsList" olarak değiştirmiştir. v8.5.0'dan bu yana, API, karşılık gelen parametre bir referans olduğunda veya hesaplanan sonucu referans olduğunda, ReferredArea nesnesini "paramsList" içine koyar. Referansın kendisine ihtiyacınız varsa, doğrudan ReferredArea'yı kullanabilirsiniz. Formülün konumuna karşılık gelen referanstan tek bir hücre değeri almanız gerekiyorsa, ReferredArea.GetValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Tüm alan için hücre değerleri dizisine ihtiyacınız varsa, o zaman ReferredArea.GetValues yöntemini kullanabilirsiniz.

Artık Aspose.Cells for .NET 8.5.0 "paramsList" içindeki ReferredArea'yı verdiğinden, "contextObjects" içindeki ReferredAreaCollection'a artık gerek kalmayacak (eski sürümlerde her zaman özel işlevin parametrelerine bire bir harita veremiyordu), bu nedenle, bu sürüm onu artık "contextObjects" ten de kaldırmıştır.

Bu değişiklik, referans parametresinin değerine/değerlerine ihtiyacınız olduğunda ICustomFunction için uygulama kodunda biraz değişiklik gerektirir.

**Eski Uygulama**

{{< highlight "csharp" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Yeni Uygulama**

{{< highlight "csharp" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **Sınıf Hesaplama Seçenekleri Eklendi**
Aspose.Cells for .NET 8.5.0, formül hesaplama motoruna daha fazla esneklik ve genişletilebilirlik eklemek için CalculationOptions sınıfını kullanıma sundu. Yeni eklenen sınıf aşağıdaki özelliklere sahiptir.

1. CalculationOptions.CalcStackSize: Hücreleri yinelemeli olarak hesaplamak için yığın boyutunu belirtti. -1, hesaplamanın karşılık gelen çalışma kitabının WorkbookSettings.CalcStackSize öğesini kullanacağını belirtir.
1. CalculationOptions.CustomFunction: Formül hesaplama motorunu özel formülle genişletir.
1. CalculationOptions.IgnoreError: Boole tipi değer, formüller hesaplanırken hataların gizlenip gizlenmeyeceğini, hataların desteklenmeyen işlevden, harici bağlantıdan veya daha fazlasından kaynaklanabileceğini gösterir.
1. CalculationOptions.PrecisionStrategy: Hesaplama kesinliğini işleme stratejisini belirten CalculationPrecisionStrategy türü değeri.
### **Numaralandırma HesaplamaKesinlikStratejisi Eklendi**
Aspose.Cells for .NET 8.5.0, istenen sonuçları elde etmek için formül hesaplama motoruna daha fazla esneklik eklemek için CalculationPrecisionStrategy numaralandırmasını kullanıma sundu. Bu numaralandırma, hesaplama hassaslığını işleme stratejileridir. IEEE 754 Kayan Nokta Aritmetiği'nin kesinlik sorunu nedeniyle, görünüşte basit olan bazı formüller beklenen sonuçları verecek şekilde hesaplanamayabilir, bu nedenle en son API derlemesi, seçime göre istenen sonuçları elde etmek için aşağıdaki alanları ortaya çıkardı.

1. CalculationPrecisionStrategy.Decimal: Mümkün olduğunda işlenen olarak ondalık sayı kullanır ve performans değerlendirmeleri açısından en verimsizdir.
1. CalculationPrecisionStrategy.Round: Hesaplama sonuçlarını anlamlı basamağa göre yuvarlar.
1. CalculationPrecisionStrategy.None: Herhangi bir strateji uygulanmaz, bu nedenle hesaplama sırasında motor orijinal çift değeri işlenen olarak kullanır ve sonucu doğrudan döndürür. Bu seçenek en verimli olanıdır ve çoğu durumda uygulanabilir.
### **CalculationOptions'ı kullanmak için Eklenen Yöntemler**
v8.5.0 sürümüyle birlikte Aspose.Cells API, aşağıda listelenen CalculateFormula yönteminin aşırı yük sürümlerini ekledi.

- Workbook.CalculateFormula(Hesaplama Seçenekleri)
- Worksheet.CalculateFormula(CalculationOptions seçenekleri, özyinelemeli bool)
- Cell.Hesapla(Hesaplama Seçenekleri)
### **Numaralandırma Alanı PasteType.RowHeights Eklendi**
Aspose.Cells API'ler, aralıkları kopyalarken satır yüksekliklerini kopyalamak amacıyla PasteType.RowHeights numaralandırma alanını sağlamıştır. PasteOptions.PasteType özelliği ((PasteType.RowHeights}} olarak ayarlandığında, kaynak aralıktaki tüm satırların yükseklikleri hedef aralığa kopyalanacaktır.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Özellik SheetRender.PageScale Eklendi**
Sayfa Düzeni Ölçekleme'yi kullanarak ayarladığınızda**Genişliğe m uzunluğa n sayfaya sığdır** seçeneği, Microsoft Excel, Sayfa Yapısı ölçekleme faktörünü hesaplar. Aynısı, Aspose.Cells for .NET 8.5.0 tarafından sunulan SheetRender.PageScale özelliği kullanılarak elde edilebilir. Bu özellik, yüzde değerine dönüştürülebilen bir çift değer döndürür. Örneğin, 0.507968245 döndürürse, ölçeklendirme faktörünün %51 olduğu anlamına gelir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Numaralandırma CellValueFormatStrateji Eklendi**
Aspose.Cells for .NET 8.5.0, hücre değerlerinin biçimlendirme uygulanarak veya uygulanmadan çıkarılması gereken durumların üstesinden gelmek için yeni bir CellValueFormatStrategy numaralandırması ekledi. Numaralandırma CellValueFormatStrategy aşağıdaki alanlara sahiptir.

1. CellValueFormatStrategy.CellStyle: Yalnızca hücrenin orijinal biçimiyle biçimlendirilir.
1. CellValueFormatStrategy.DisplayStyle: Hücrenin görüntülenen stiliyle biçimlendirilmiştir.
1. CellValueFormatStrategy.None: Biçimlendirilmemiş.
### **Yöntem Cell.GetStingValue Eklendi**
CellValueFormatStrategy numaralandırmasını kullanmak için v8.5.0, CellValueFormatStrategy türünde bir parametreyi kabul edebilen ve belirtilen seçeneğe bağlı olarak değer döndüren Cell.GetStingValue yöntemini kullanıma sunmuştur.

Aşağıdaki kod parçacığı, yeni kullanıma sunulan Cells.GetStingValue yönteminin nasıl kullanılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Özellik ExportTableOptions.FormatStrategy Eklendi**
Aspose.Cells for .NET 8.5.0, verileri biçimlendirmeli veya biçimlendirmeden DataTable'a aktarmak isteyen kullanıcılar için ExportTableOptions.FormatStrategy özelliğini kullanıma sundu. Bu özellik, CellValueFormatStrategy numaralandırmasını kullanır ve belirtilen seçeneğe göre verileri dışa aktarır.

Aşağıdaki kod, ExportTableOptions.FormatStrategy özelliğinin kullanımını açıklar.

**C#**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
