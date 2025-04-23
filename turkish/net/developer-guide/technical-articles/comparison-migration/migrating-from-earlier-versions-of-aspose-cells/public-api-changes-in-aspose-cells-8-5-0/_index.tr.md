---
title: Aspose.Cells 8.5.0 da Genel API Değişiklikleri
type: docs
weight: 160
url: /tr/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Bu belge, uygulama geliştiriciler için önemli olabilecek Aspose.Cells API'sindeki değişiklikleri detaylandırır. Sadece yeni ve güncellenmiş genel yöntemleri, [eklenen sınıfları vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-5-0/), değil aynı zamanda Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **ICustomFunction.CalculateCustomFunction Parametreleri Değiştirildi**
Özel işlev için bir parametre hücre referansı ise, eski sürüm Aspose.Cells API'leri, hücre referansını tek bir hücre değerine veya atıfta bulunulan alandaki tüm hücre değerlerinin bir nesne dizisine dönüştürürdü. Ancak, birçok işlev ve kullanıcı için atıfta bulunan alanın tüm hücre değerleri dizisi gereksizdir, onlar sadece formülün pozisyonuna karşılık gelen tek bir hücreye ihtiyaç duyarlar veya sadece referansa ihtiyaçları vardır, hücre değeri veya değer dizisi yerine. Bazı durumlarda, tüm hücre değerlerini alımış riskinini arttırmasıdır.

Böyle bir gereksinimi desteklemek için Aspose.Cells for .NET 8.5.0, referans alanı için "paramsList"'e parametre değerini değiştirdi. V8.5.0'dan itibaren API, ilgili parametre bir referans ise veya hesaplanmış sonucu bir referans ise, ReferredArea objesini "paramsList"'e koyar. Referansın kendisi gerekiyorsa doğrudan ReferredArea'yı kullanabilirsiniz. Formülün pozisyonuna karşılık gelen referanstan tek bir hücre değeri almanız gerekiyorsa, ReferredArea.GetValue(satırOffset, sütunOffset) yöntemini kullanabilirsiniz. Tüm alan için hücre değerleri dizisine ihtiyacınız varsa, ReferredArea.GetValues yöntemini kullanabilirsiniz.

Artık Aspose.Cells for .NET 8.5.0, "paramsList" içinde ReferredArea'yı verdiği için, "contextObjects" içindeki ReferredAreaCollection artık gerekli olmayacaktır (eski sürümlerde, özel fonksiyonun parametreleriyle her zaman birbirine tekabül etmeyen bir eşleme yapamazdı), bu nedenle bu sürüm onu da "contextObjects"'ten kaldırmıştır.

Bu değişiklik, başvuru parametrelerinin değer/değerlerine ihtiyaç duyulduğunda, ICustomFunction uygulamasının kodunda biraz değişiklik gerektirir.

**Eski Uygulama**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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


### **CalculationOptions Sınıfı Eklendi**
Aspose.Cells for .NET 8.5.0, formül hesaplama motoru için daha fazla esneklik ve genişleme eklemek amacıyla CalculationOptions sınıfını kullanıma sunmuştur. Yeni eklenen sınıfın aşağıdaki özellikleri vardır.

1. CalculationOptions.CalcStackSize: Hücreleri tekrarlayarak hesaplama için yığın büyüklüğünü belirtir. -1, hesaplamanın karşılık gelen çalışma kitabının WorkbookSettings.CalcStackSize'ını kullanacağını belirtir.
1. CalculationOptions.CustomFunction: Özel formül hesaplama motoru ile formülü genişletir.
1. CalculationOptions.IgnoreError: Hata varsa gizlerken formülleri hesaplarken, hataların desteklenmeyen fonksiyondan, dış bağlantıdan veya daha fazlasından kaynaklanıp kaynaklanmadığını belirten bir Boolean tipi değeri.
1. CalculationOptions.PrecisionStrategy: Hesaplamanın hassasiyet işleme stratejisini belirten CalculationPrecisionStrategy tipinde bir değer.
### **Numaralandırma CalculationPrecisionStrategy Eklendi**
Aspose.Cells for .NET 8.5.0, formül hesaplama motoruna daha fazla esneklik eklemek için CalculationPrecisionStrategy numaralandırmasını ortaya çıkardı ve istenen sonuçları almak için aşağıdaki alanları ortaya çıkardı.

1. CalculationPrecisionStrategy.Decimal: Mümkün olduğunda ondalık olarak operatör kullanır ve performans açısından en verimsizdir.
1. CalculationPrecisionStrategy.Round: Hesaplama sonuçlarını önemli basamağa göre yuvarlar.
1. CalculationPrecisionStrategy.None: Hiçbir strateji uygulanmaz, bu nedenle hesaplama sırasında motor orijinal çift değeri operatör olarak kullanır ve sonucu doğrudan geri döndürür. Bu seçenek en verimli olanıdır ve çoğu durum için uygundur.
### **CalculationOptions'ı kullanmak için eklenen yöntemler**
v8.5.0 sürümü ile Aspose.Cells API, CalculateFormula yönteminin aşağıda listelenen aşırı yüklemeli sürümlerini ekledi.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Numaralandırma Alanı PasteType.RowHeights Eklendi**
Aspose.Cells API'leri, aralıkları kopyalarken satır yüksekliklerini kopyalamak amacıyla PasteType.RowHeights numaralandırma alanını sağlamıştır.

**C#**

{{< highlight csharp >}}

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


### **Eklendi SheetRender.PageScale Özelliği**
Sayfa Ayarı Ölçeklendirme **Genişliğe göre n sayfa ve yüksekliğe göre m sayfa Uygun Olacak Şekilde Ayarla** seçeneğini kullanarak ayarlarsanız, Microsoft Excel Sayfa Ayarı ölçekleme faktörünü hesaplar. Aynısı, Aspose.Cells for .NET 8.5.0 tarafından ortaya çıkarılan SheetRender.PageScale özelliği ile elde edilebilir. Bu özellik, yüzde değerine dönüştürülebilen bir çift değer döndürür. Örneğin, 0.507968245 döndürürse, ölçekleme faktörü %51 olduğu anlamına gelir.

**C#**

{{< highlight csharp >}}

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


### **Numaralandırma CellValueFormatStrategy Eklendi**
Aspose.Cells for .NET 8.5.0, hücre değerlerinin biçimlendirme uygulanmış veya uygulanmamış olduğu durumları ele almak için yeni bir Enumeration CellValueFormatStrategy ekledi.

1. CellValueFormatStrategy.CellStyle: Yalnızca hücrenin orijinal biçimiyle biçimlendirilmiş.
1. CellValueFormatStrategy.DisplayStyle: Hücrenin görüntülenen stili ile biçimlendirilmiş.
1. CellValueFormatStrategy.None: Biçimlendirilmemiş.
### **Eklenen Cell.GetStingValue Yöntemi**
CellValueFormatStrategy numaralandırmasını kullanmak için, v8.5.0, Cell.GetStingValue yöntemini ortaya çıkardı. Bu yöntem, CellValueFormatStrategy türünde bir parametre kabul edebilir ve belirtilen seçeneğe bağlı olarak değeri döndürür.

Aşağıdaki kod parçası, yeni ortaya çıkarılan Cells.GetStingValue yönteminin nasıl kullanılacağını göstermektedir.

**C#**

{{< highlight csharp >}}

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


### **Eklenen ExportTableOptions.FormatStrategy Özelliği**
Aspose.Cells for .NET 8.5.0, verileri biçimlendirmeyle veya biçimlendirme olmadan DataTable'a aktarmak isteyen kullanıcılar için ExportTableOptions.FormatStrategy özelliğini ortaya çıkardı.

Aşağıdaki kod, ExportTableOptions.FormatStrategy özelliğinin nasıl kullanılacağını açıklamaktadır.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
