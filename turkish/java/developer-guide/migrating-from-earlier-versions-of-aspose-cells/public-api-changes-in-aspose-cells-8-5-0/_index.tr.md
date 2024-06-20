---
title: Aspose.Cells 8.5.0 da Genel API Değişiklikleri
type: docs
weight: 170
url: /tr/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sindeki sürüm 8.4.2'den 8.5.0'a değişiklikleri açıklar. Bu, sadece yeni ve güncellenmiş genel yöntemleri [eklenen sınıflar vs.](/cells/tr/java/public-api-changes-in-aspose-cells-8-5-0/) içermez, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliği de açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **ICustomFunction.CalculateCustomFunction Parametreleri Değiştirildi**
Özel işlev için bir parametre hücre referansı ise, eski sürüm Aspose.Cells API'leri, hücre referansını tek bir hücre değerine veya atıfta bulunulan alandaki tüm hücre değerlerinin bir nesne dizisine dönüştürürdü. Ancak, birçok işlev ve kullanıcı için atıfta bulunan alanın tüm hücre değerleri dizisi gereksizdir, onlar sadece formülün pozisyonuna karşılık gelen tek bir hücreye ihtiyaç duyarlar veya sadece referansa ihtiyaçları vardır, hücre değeri veya değer dizisi yerine. Bazı durumlarda, tüm hücre değerlerini alımış riskinini arttırmasıdır.

Bu tür gereksinimleri desteklemek için, Aspose.Cells for Java 8.5.0, atıfta bulunan alan için "paramsList" öğesine değişen, değere ihtiyaç durumunda ReferredArea nesnesini yükler. 8.5.0'dan itibaren, API, atıfta bulunan parametre bir referans ise veya hesaplanmış sonucu referans ise "paramsList" için ReferredArea nesnesini yerleştirir. Referans ihtiyacınız varsa, ReferredArea'yı doğrudan kullanabilirsiniz. Formülün pozisyonuyla karşılık gelen referanstan tek bir hücre değeri almanız gerekiyorsa, ReferredArea.getValue(rowOffset, int colOffset) yöntemini kullanabilirsiniz. Tüm alan için hücre değeri dizisine ihtiyacınız varsa, ReferredArea.getValues yöntemini kullanabilirsiniz.

Artık Aspose.Cells for Java 8.5.0, 'paramsList' içinde ReferredArea verdiğinden, 'contextObjects' içindeki ReferredAreaCollection artık gereksiz olmayacak(Eski sürümlerde, her zaman özel işlevin parametrelerine birebir eşleşememişti), bu sürümde ayrıca 'contextObjects' içinden kaldırıldı.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
Aspose.Cells for Java 8.5.0, hesaplama motoru için daha fazla esneklik ve genişletme eklemek için CalculationOptions sınıfını kullanıma sundu. Yeni eklenen sınıf aşağıdaki özelliklere sahiptir. 

1. CalculationOptions.CalcStackSize: Hücreleri tekrarlayarak hesaplama için yığın büyüklüğünü belirtir. -1, hesaplamanın karşılık gelen çalışma kitabının WorkbookSettings.CalcStackSize'ını kullanacağını belirtir.
1. CalculationOptions.CustomFunction: Özel formül hesaplama motoru ile formülü genişletir.
1. CalculationOptions.IgnoreError: Hata varsa gizlerken formülleri hesaplarken, hataların desteklenmeyen fonksiyondan, dış bağlantıdan veya daha fazlasından kaynaklanıp kaynaklanmadığını belirten bir Boolean tipi değeri.
1. CalculationOptions.PrecisionStrategy: Hesaplamanın hassasiyet işleme stratejisini belirten CalculationPrecisionStrategy tipinde bir değer.
### **Numaralandırma CalculationPrecisionStrategy Eklendi**
Aspose.Cells for Java 8.5.0, istenen sonuçları elde etmek için formül hesaplama motoruna daha fazla esneklik eklemek amacıyla CalculationPrecisionStrategy numaralandırması açıklanmıştır. Bu numaralandırma stratejileri hesaplama hassasiyet işlemini stratejize eder. IEEE 754 Kayan Noktalı Aritmetiğinin hassasiyet sorunu nedeniyle, bazı görünüşte basit formüller beklenen sonuçları vermemektedir, bu nedenle son API yapısı beklenen sonuçları elde etmek için aşağıdaki alanları açıklamıştır.

1. CalculationPrecisionStrategy.DECIMAL: Olabildiğince operanda ondalık kullanır ve performans düşünceleri açısından en verimsizdir.
1. CalculationPrecisionStrategy.ROUND: Hesaplama sonuçlarını anlamlı basamağa göre yuvarlar.
1. CalculationPrecisionStrategy.NONE: Herhangi bir strateji uygulanmaz, bu nedenle hesaplama sırasında motor orijinal çift değerini operatör olarak kullanır ve sonucu direkt olarak döndürür. Bu seçenek en verimli seçenektir ve çoğu durum için uygundur.
### **CalculationOptions'ı kullanmak için eklenen yöntemler**
v8.5.0 sürümüyle birlikte, Aspose.Cells API'si listelenen şekilde calculateFormula yöntemine aşırı yüklemeler eklemiştir.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Numaralandırma Alanı PasteType.ROW_HEIGHTS Eklendi**
Aspose.Cells API'ları, kopyalama işlemi sırasında aralıkları kopyalarken satır yüksekliklerini kopyalamak amacıyla PasteType.ROW_HEIGHTS numaralandırma alanını sağlamıştır. PasteOptions.PasteType özelliği ((PasteType.ROW_HEIGHTS}} olarak ayarlandığında, kaynak aralığındaki tüm satırların yükseklikleri hedef aralığa kopyalanacaktır.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Eklendi SheetRender.PageScale Özelliği**
**Fit to n page(s) wide by m tall** seçeneğini kullanarak Sayfa Ayarı Ölçeği ayarladığınızda, Microsoft Excel Sayfa Ayarı ölçek faktörünü hesaplar. Aynısı, Aspose.Cells for Java 8.5.0 tarafından açıklanan SheetRender.PageScale özelliği kullanılarak elde edilebilir. Bu özellik, yüzde değerine dönüştürülebilen bir çift değer döndürür. Örneğin, 0,507968245 döndürürse, ölçek faktörü %51'dir.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Numaralandırma CellValueFormatStrategy Eklendi**
Aspose.Cells for Java 8.5.0, hücre değerlerinin biçimlendirme uygulanmış veya uygulanmamış olması durumlarıyla başa çıkmak için yeni bir CellValueFormatStrategy numaralandırma eklemiştir. CellValueFormatStrategy numaralandırması aşağıdaki alanlara sahiptir. 

1. CellValueFormatStrategy.CELL_STYLE: Yalnızca hücrenin orijinal formatıyla biçimlendirilmiş.
1. CellValueFormatStrategy.DISPLAY_STYLE: Hücrenin görüntülenen stili ile biçimlendirilir.
1. CellValueFormatStrategy.NONE: Biçimlendirilmemiş.
### **Eklendi Cell.getStringValue Yöntemi**
CellValueFormatStrategy numaralandırmasını kullanmak için, v8.5.0 Cell.getStringValue yöntemi açıklanmıştır. Bu yöntem, CelValueFormatStrategy türünde bir parametre kabul edebilir ve belirtilen seçeneğe bağlı olarak değeri döndürür.

Aşağıdaki kod parçacığı, yeni açılmış Cell.getStringValue yöntemini nasıl kullanılacağını göstermektedir.

**Java**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
