---
title: Aspose.Cells 16.10.0 daki Genel API Değişiklikleri
type: docs
weight: 340
url: /tr/net/public-api-changes-in-aspose-cells-16-10-0/
---

{{% alert color="primary" %}} 

Bu belge, geliştiricilerin ilgisini çekebilecek Aspose.Cells API'sindeki değişiklikleri 9.0.0'dan 16.10.0'a kadar açıklamaktadır. Yeni ve güncellenmiş genel yöntemler, eklenen ve kaldırılan sınıflar vb. ve Aspose.Cells'in arkasındaki davranışta herhangi bir değişiklik açıklanmaktadır.

{{% /alert %}} 
## **Eklenen API'lar**
### **Yansıma Efektleri için Destek**
Aspose.Cells 16.10.0, bir Şekil nesnesinin yansıma efektlerini kontrol etmek için Shape.Reflection özelliği ile birlikte ReflectionEffect sınıfını ortaya çıkardı. ReflectionEffect sınıfının aşağıdaki özellikleri bulunmaktadır.

- ReflectionEffect.Blur: Nokta birimi cinsinden bulanıklık yarıçapını alır/ayarlar.
- ReflectionEffect.Direction: Alfa gradyan basamağının şekle göre yönünü alır/ayarlar.
- ReflectionEffect.Distance: Nokta birimi cinsinden yansımanın mesafesini alır/ayarlar.
- ReflectionEffect.FadeDirection: Yansımayı ofsetlemek için yönü alır/ayarlar.
- ReflectionEffect.RotWithShape: Yansıma şekille birlikte mi dönsün, alır/ayarlar.
- ReflectionEffect.Size: Bitiş alfa değerinin (alfa gradyan rampasında) son pozisyonunu yüzde biriminde alır/ayarlar.
- ReflectionEffect.Transparency: Başlangıç yansıma şeffaflığını 0.0 (opak) ile 1.0 (saydam) arasında bir değer olarak alır/ayarlar.
- ReflectionEffect.Type: Önceden belirlenmiş yansıma efektini alır/ayarlar.

İşte Shape.Reflection özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Yansıma Efektleri ile Çalışma](/cells/tr/net/working-with-the-reflection-effect-of-shape-or-chart/) başlıklı detaylı makaleye göz atın

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ReflectionEffect from the Shape object

var reflection = shape.Reflection;

// Set its Blur, Size, Transparency and Distance properties

reflection.Blur = 30;

reflection.Size = 90;

reflection.Transparency = 0.5;

reflection.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Gölgeli Efektlerin Desteklenmesi**
Aspose.Cells 16.10.0, Shape.ShadowEffect özelliğini ve birlikte kullanılabilen ShadowEffect sınıfını ortaya çıkarmıştır. ShadowEffect sınıfının aşağıdaki özellikleri bulunmaktadır.

- ShadowEffect.Angle: Işık açısını 0 ile 359.9 derece arasında alır/ayarlar.
- ShadowEffect.Blur: Gölgeliğin 0 ile 100 nokta aralığında bulanıklığını alır/ayarlar.
- ShadowEffect.Color: Gölgeliğin rengini alır/ayarlar.
- ShadowEffect.Distance: Gölgeliğin 0 ile 200 nokta aralığında mesafesini alır/ayarlar.
- ShadowEffect.PresetType: Gölgeliğin önceden belirlenmiş gölge tipini alır/ayarlar.
- ShadowEffect.Size: Gölgeliğin 0 ile 2.0 arasındaki boyutunu alır/ayarlar. İç gölge durumunda anlamsız olacaktır.
- ShadowEffect.Transparency: Gölgeliğin saydamlığını 0.0 (opak) ile 1.0 (saydam) arasında bir derece olarak alır/ayarlar.

Yukarıdaki özelliğin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Gölge Efektleriyle Çalışma](/cells/tr/net/working-with-the-shadow-effect-of-shape-or-chart/) üzerine detaylı makaleye göz atın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ShadowEffect from the Shape object

var shadow = shape.ShadowEffect;

// Set its Angle, Blur, Size, Transparency and Distance properties

shadow.Angle = 150;

shadow.Blur = 30;

shadow.Size = 90;

shadow.Transparency = 0.5;

shadow.Distance = 80;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Parlama Efektleri Desteklenmesi**
Aspose.Cells 16.10.0, Shape.Glow özelliğini ve birlikte kullanılabilen GlowEffect sınıfını ortaya çıkarmıştır. GlowEffect sınıfı, aşağıdaki özellikleri kullanarak bir ışıltı efekti belirtir.

- GlowEffect.Size: Işıltının nokta birimindeki yarıçapını alır/ayarlar.
- GlowEffect.Transparency: Işıl ışıl efektinin saydamlığını 0.0 (opak) ile 1.0 (saydam) arasında bir derece olarak alır/ayarlar.

Shape.Glow özelliğinin basit kullanım senaryosu burada.

{{% alert color="primary" %}} 

[Parlama Efektiyle Çalışma](/cells/tr/net/working-with-the-glow-effect-of-shape-or-chart/) üzerine detaylı makaleye göz atın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of GlowEffect from the Shape object

var glow = shape.Glow;

// Set its Size & Transparency properties

glow.Size = 90;

glow.Transparency = 0.5;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **3B Formatının Desteklenmesi**
Aspose.Cells 16.10.0, Shape.ThreeDFormat özelliğini ve Shape nesnesinin 3B biçimlendirilmesini kontrol etmek için kullanılabilen ThreeDFormat sınıfını ortaya çıkarmıştır. ThreeDFormat sınıfı, bir şeklin üç boyutlu biçimlendirmesini temsil eder ve aşağıdaki özelliklere sahiptir.

- ThreeDFormat.BottomBevelHeight: Alt çıkıntı yüksekliği veya şekle uygulandığı mesafe biriminde Noktalar cinsinden alır/ayarlar.
- ThreeDFormat.BottomBevelType: Alt çıkıntı tipini veya şekle uygulandığı mesafeyi Noktalar cinsinden alır/ayarlar.
- ThreeDFormat.BottomBevelWidth: Alt çıkıntı genişliğini veya şekle uygulandığı mesafeyi Noktalar cinsinden alır/ayarlar.
- ThreeDFormat.ContourColor: Şeklin kontur rengini alır/ayarlar.
- ThreeDFormat.ContourWidth: Şekildeki kontur genişliğini Noktalar cinsinden alır/ayarlar.
- ThreeDFormat.ExtrusionColor: Bir şekildeki kabartma rengini alır.
- ThreeDFormat.ExtrusionHeight: Şekle uygulanan kabartma yüksekliğini Nokta biriminde alır/ayarlar.
- ThreeDFormat.LightAngle: Kabartma ışıklarının açısını alır/ayarlar.
- ThreeDFormat.Lighting: Işık takımının türünü alır/ayarlar.
- ThreeDFormat.LightingDirection: Işık takımının sahneden oryantasyonuna göre yönlendirilme açısını alır/ayarlar.
- ThreeDFormat.Material: Şeklin son görünümünü ve hissini vermek için ışık özellikleri ile birleştirilen önceden belirlenmiş malzemeyi temsil eder.
- ThreeDFormat.Perspective: Bir ThreeDFormat nesnesinin görüntülenebileceği açıyı alır/ayarlar.
- ThreeDFormat.PresetCameraType: Kabartma önceden belirlenmiş kamerasını alır/ayarlar.
- ThreeDFormat.RotationX: X-ekseni etrafında çıkartılmış şeklin dönüşünü Derece biriminde alır/ayarlar.
- ThreeDFormat.RotationY: Y-ekseni etrafında çıkartılmış şeklin dönüşünü Derece biriminde alır/ayarlar.
- ThreeDFormat.RotationZ: Z-ekseni etrafında çıkartılmış şeklin dönüşünü Derece biriminde alır/ayarlar.
- ThreeDFormat.TopBevelHeight: Üst yuvarlatma yüksekliğini veya şekle ne kadar uygulandığını Nokta biriminde alır/ayarlar.
- ThreeDFormat.TopBevelType: Üst yuvarlatma türünü veya şekle ne kadar uygulandığını Nokta biriminde alır/ayarlar.
- ThreeDFormat.TopBevelWidth: Üst yuvarlatma genişliğini veya şekle ne kadar uygulandığını Nokta biriminde alır/ayarlar.
- ThreeDFormat.Z: 3 Boyutlu şeklin zeminden uzaklığını tanımlar.

Shape.ThreeDFormat özelliğinin basit kullanım senaryosu aşağıdaki gibidir.

{{% alert color="primary" %}} 

[3B Biçimlendirme İle Çalışma](/cells/tr/net/working-with-the-threedformat-of-shape-or-chart/) başlıklı detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet containing a shape

// Alternatively create a new spreadsheet and add a shape

var book = new Workbook("sample.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first shape from the collection

var shape = sheet.Shapes[0];

// Get the instance of ThreeDFormat from the Shape object

var threeD = shape.ThreeDFormat;

// Set its ContourWidth & ExtrusionHeight properties

threeD.ContourWidth = 15;

threeD.ExtrusionHeight = 30;

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **Şekil Metninin WordArt Stilleri Desteği**
Aspose.Cells 16.10.0, FontSettingCollection.SetWordArtStyle ve FontSetting.SetWordArtStyle yöntemlerini metnin Şekil nesnesine önceden belirlenmiş WordArt stilini ayarlamak için ortaya çıkardı.

Yukarıda belirtilen yöntemlerin basit kullanım senaryosu aşağıda verilmiştir.

{{% alert color="primary" %}} 

[WordArt Stilleri İle Çalışma](/cells/tr/net/set-preset-wordart-style-to-the-text-of-the-shape/) başlıklı detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0] as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **Dahili WordArt Stilleri Desteği**
Aspose.Cells 16.10.0, Excel 2007'den bu yana önceden belirlenmiş WordArt nesneleri eklemek için ShapeCollection.AddWordArt yöntemini ve PresetWordArtStyle numaralandırmasını ortaya çıkardı.

Yukarıdaki ShapeCollection.AddWordArt yönteminin basit kullanım senaryosu aşağıdaki gibidir.

{{% alert color="primary" %}} 

[Yerleşik Stillerle WordArt Ekleme](/cells/tr/net/add-word-art-text-with-built-in-styles/) başlıklı detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access ShapeCollection of first worksheet

var shapes = sheet.Shapes;

// Add WordArt with built-in styles

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.AddWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **XmlMapCollection.Add Yöntemi Eklendi**
Aspose.Cells, bir elektronik tabloya XML Haritası eklemek için XmlMapCollection.Add yöntemini ortaya çıkardı. İşte XmlMapCollection.Add yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Elektronik Tabloya Xml Haritası Ekleme](/cells/tr/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/) başlıklı detaylı makaleyi kontrol edin

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Cells.LinkToXmlMap Yöntemi Eklendi**
Aspose.Cells, hücreleri XML harita öğeleriyle bağlamak için Cells.LinkToXmlMap yöntemini sunmaktadır. Yukarıda bahsedilen Cells.LinkToXmlMap yönteminin basit kullanım senaryosu bulunmaktadır.

[Hücreleri XML Harita Öğelerine Bağlama](/cells/tr/net/link-cells-to-xml-map-elements/) başlıklı detaylı makaleyi kontrol edin

{{% alert color="primary" %}} 

[Hücreleri XML Harita Öğelerine Bağlama](/cells/tr/net/link-cells-to-xml-map-elements/) konusundaki detaylı makaleye göz atın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook("sample.xlsx");

// Access the XML Map from the spreadsheet

var map = book.Worksheets.XmlMaps[0];

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Map FIELD1 and FIELD2 to cell A1 and B2

sheet.Cells.LinkToXmlMap(map.Name, 0, 0, "/root/row/FIELD1");

sheet.Cells.LinkToXmlMap(map.Name, 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4

sheet.Cells.LinkToXmlMap(map.Name, 2, 2, "/root/row/FIELD4");

sheet.Cells.LinkToXmlMap(map.Name, 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6

sheet.Cells.LinkToXmlMap(map.Name, 4, 4, "/root/row/FIELD7");

sheet.Cells.LinkToXmlMap(map.Name, 5, 5, "/root/row/FIELD8");

{{< /highlight >}}


### **Added ListColumn.Formula Özelliği**
Aspose.Cells 16.10.0, ListColumn.Formula özelliğini yeni eklenen satırlara otomatik olarak yayınlamak için açığa çıkardı.

ListColumn.Formula özelliğinin basit kullanım senaryosu burada.

{{% alert color="primary" %}} 

[Tablo veya Liste Nesnesinde Formülü Otomatik Yayınlama](/cells/tr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/) konusundaki detaylı makaleye göz atın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add column headings in cell A1 and B1

sheet.Cells[0, 0].PutValue("Column A");

sheet.Cells[0, 1].PutValue("Column B");

// Add list object, set its name and style

var listObject = sheet.ListObjects[sheet.ListObjects.Add(0, 0, 1, sheet.Cells.MaxColumn, true)];

listObject.TableStyleType = TableStyleType.TableStyleMedium2;

listObject.DisplayName = "Table";

// Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.ListColumns[1].Formula = "=[Column A] + 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **GridWeb ile Özel Fonksiyonlar Hesaplama Desteği**
Aspose.Cells.GridWeb 16.10.0, GridAbstractCalculationEngine sınıfıyla birlikte özel fonksiyonları tanımlama ve hesaplama imkanı sağlayan GridWeb.CustomCalculationEngine özelliğini sunmaktadır. Yukarıda bahsedilen API'lerin basit kullanım senaryosu bulunmaktadır.

[GridWeb'de Özel Fonksiyonlar Hesaplama](/cells/tr/net/calculate-custom-functions-in-gridweb/) başlıklı detaylı makaleyi kontrol edin

{{% alert color="primary" %}} 

[GridWeb'de Özel Fonksiyonları Hesaplama](/cells/tr/net/calculate-custom-functions-in-gridweb/) konusundaki detaylı makaleye göz atın.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 private class GridWebCustomCalculationEngine : GridAbstractCalculationEngine

{

    public override void Calculate(GridCalculationData data)

    {

        //  Calculate MYTESTFUNC() with your own logic.

        //For example, you can multiply MYTESTFUNC() parameter with 2 so

        // MYTESTFUNC(3.0) will return 6

        // MYTESTFUNC(4.0) will return 8

        // MYTESTFUNC(5.0) will return 10

        if ("MYTESTFUNC".Equals(data.FunctionName.ToUpper()))

        {

            data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));

        }

    }

}


if (Page.IsPostBack == false && GridWeb1.IsPostBack == false)

{

    // Assign your own custom calculation engine to GridWeb

    GridWeb1.CustomCalculationEngine = new GridWebCustomCalculationEngine();

    // Access the active worksheet and add your custom function in cell B3

    GridWorksheet sheet = GridWeb1.ActiveSheet;

    GridCell cell = sheet.Cells["B3"];

    cell.Formula = "=MYTESTFUNC(9.0)";

    // Calculate the GridWeb formula

    GridWeb1.CalculateFormula();

}

{{< /highlight >}}
