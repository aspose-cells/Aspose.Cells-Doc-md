---
title: Genel API Aspose.Cells 16.10.0'daki değişiklikler
type: docs
weight: 340
url: /tr/net/public-api-changes-in-aspose-cells-16-10-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek Aspose.Cells API sürüm 9.0.0'dan 16.10.0'a yapılan değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Yansıma Efektleri Desteği**
Aspose.Cells 16.10.0, bir Shape nesnesinin yansıma etkilerini kontrol etmek için ReflectionEffect sınıfını Shape.Reflection özelliğiyle birlikte kullanıma sundu. ReflectionEffect sınıfı aşağıdaki özelliklere sahiptir.

- ReflectionEffect.Blur: Nokta birimi cinsinden bulanıklık yarıçapını alır/ayarlar.
- ReflectionEffect.Direction: Şeklin kendisine göre alfa gradyan rampasının yönünü alır/ayarlar.
- ReflectionEffect.Distance: Nokta birimi cinsinden yansımanın uzaklığını alır/ayarlar.
- ReflectionEffect.FadeDirection: Yansımayı dengelemek için yönü alır/ayarlar.
- ReflectionEffect.RotWithShape: Yansımanın şekille birlikte dönmesi gerekip gerekmediğini alır/ayarlar.
- ReflectionEffect.Size: Son alfa değerinin bitiş konumunu (alfa gradyan rampası boyunca) yüzde birimi cinsinden alır/ayarlar.
- ReflectionEffect.Transparency: Başlangıç yansıma şeffaflığının derecesini 0,0 (opak) ile 1,0 (berrak) arasında bir değer olarak alır/ayarlar.
- ReflectionEffect.Type: Ön ayarlı yansıma efektini alır/ayarlar.

İşte Shape.Reflection özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Yansıma Efektleriyle Çalışmak](/cells/tr/net/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **Gölge Efektleri Desteği**
Aspose.Cells 16.10.0, Shape.ShadowEffect özelliğinin yanı sıra, bir Shape nesnesi üzerinde gölge efektinin ayarlanmasına izin veren ShadowEffect sınıfını kullanıma sundu. ShadowEffect sınıfı aşağıdaki özelliklere sahiptir.

- ShadowEffect.Angle: Aydınlatma açısını 0 ila 359,9 derece arasında alır/ayarlar.
- ShadowEffect.Blur: Gölgenin bulanıklığını 0 ila 100 puan arasında alır ve ayarlar.
- ShadowEffect.Color: Gölgenin rengini alır/ayarlar.
- ShadowEffect.Distance: Gölgenin mesafesini 0 ila 200 puan arasında alır/ayarlar.
- ShadowEffect.PresetType: Gölgenin ön ayarlı gölge türünü alır/ayarlar.
- ShadowEffect.Size: Gölge boyutunu 0 ile 2.0 arasında alır/ayarlar. İç gölge durumunda anlamsız olacaktır.
- ShadowEffect.Transparency: Gölgenin saydamlık derecesini 0,0 (opak) ila 1,0 (net) arasında alır/ayarlar.

İşte yukarıda belirtilen mülkün basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Gölge Efektleriyle Çalışmak](/cells/tr/net/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **Işıma Efektleri Desteği**
Aspose.Cells 16.10.0, Shape.Glow özelliğinin yanı sıra GlowEffect sınıfının hepsini birlikte bir Shape nesnesinin ışıma efektini ayarlamaya izin verir. GlowEffect sınıfı, aşağıdaki özellikleri kullanarak nesnenin kenarlarının dışına rengi bulanıklaştırılmış bir dış çizginin eklendiği bir parlama efektini belirtir.

- GlowEffect.Size: Işıma yarıçapını nokta birimi cinsinden alır/ayarlar.
- GlowEffect.Transparency: Işıma efektinin şeffaflık derecesini 0,0 (opak) ila 1,0 (berrak) arasında alır/ayarlar.

İşte Shape.Glow özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Işıma Efekti ile Çalışma](/cells/tr/net/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **3D Format Desteği**
Aspose.Cells 16.10.0, Shape nesnesinin 3B biçimlendirmesini denetlemek için birlikte kullanılabilen ThreeDFormat sınıfıyla birlikte Shape.ThreeDFormat özelliğini kullanıma sundu. ThreeDFormat sınıfı, bir şeklin üç boyutlu biçimlendirmesini temsil eder ve aşağıdaki özelliklere sahiptir.

- ThreeDFormat.BottomBevelHeight: Alt eğimin yüksekliğini veya uygulandığı şeklin ne kadar içine kadar Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.BottomBevelType: Alt eğimin türünü veya uygulandığı şeklin ne kadar içine kadar Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.BottomBevelWidth: Alt eğimin genişliğini veya uygulanan şeklin ne kadar içine kadar Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.ContourColor: Bir şeklin kontur rengini alır/ayarlar.
- ThreeDFormat.ContourWidth: Şekildeki kontur genişliğini Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.ExtrusionColor: Şekildeki ekstrüzyon rengini alır.
- ThreeDFormat.ExtrusionHeight: Şekle uygulanan ekstrüzyon yüksekliğini Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.LightAngle: Ekstrüzyon ışıklarının açısını alır/ayarlar.
- ThreeDFormat.Lighting: Hafif donanım türünü alır/ayarlar.
- ThreeDFormat.LightingDirection: Sahneye göre ışık teçhizatının yönlendirildiği yönü alır/ayarlar.
- ThreeDFormat.Material: Bir şeklin son görünümünü ve hissini vermek için aydınlatma özellikleriyle birleştirilen ön ayarlı malzemeyi temsil eder.
- ThreeDFormat.Perspective: Bir ThreeDFormat nesnesinin görüntülenebileceği açıyı alır/ayarlar.
- ThreeDFormat.PresetCameraType: Ekstrüzyon ön ayarlı kamerayı alır/ayarlar.
- ThreeDFormat.RotationX: Ekstrüde şeklin X ekseni etrafındaki dönüşünü Derece birimi cinsinden alır/ayarlar.
- ThreeDFormat.RotationY: Ekstrüde şeklin Y ekseni etrafındaki dönüşünü Derece birimi cinsinden alır/ayarlar.
- ThreeDFormat.RotationZ: Ekstrüde şeklin Z ekseni etrafındaki dönüşünü Derece birimi cinsinden alır/ayarlar.
- ThreeDFormat.TopBevelHeight: Üst eğimin yüksekliğini veya uygulandığı şeklin ne kadar içine kadar Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.TopBevelType: Üst eğimin türünü veya uygulandığı şeklin ne kadar içine kadar Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.TopBevelWidth: Üst eğimin genişliğini veya uygulanan şeklin ne kadar içine kadar Nokta birimi cinsinden alır/ayarlar.
- ThreeDFormat.Z: 3B şekil için yerden olan mesafeyi tanımlar.

Shape.ThreeDFormat özelliğinin basit kullanım senaryosu aşağıdadır.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[3B Biçimlendirme ile Çalışma](/cells/tr/net/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **Shape Metninde WordArt Stilleri Desteği**
Aspose.Cells 16.10.0, önceden ayarlanmış WordArt stilini Shape nesnesinin metnine ayarlamak için FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle yöntemlerini kullanıma sundu.

İşte yukarıda belirtilen yöntemlerin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[WordArt Stilleriyle Çalışma](/cells/tr/net/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create workbook object

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Create a TextBox with some text

var textBox = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 700);

textBox.Text = "Aspose File Format APIs";

textBox.Font.Size = 44;

// Set preset WordArt style to the text of the shape

FontSetting fntSetting = textBox.GetCharacters()[0]as FontSetting;

fntSetting.SetWordArtStyle(PresetWordArtStyle.WordArtStyle3);

{{< /highlight >}}


### **WordArt Yerleşik Stilleri için Destek**
Aspose.Cells 16.10.0, Excel 2007'den beri önceden ayarlanmış WordArt nesneleri ekleme desteği sağlamak için ShapeCollection.AddWordArt yöntemini PresetWordArtStyle numaralandırmasıyla birlikte kullanıma sunmuştur.

İşte ShapeCollection.AddWordArt yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Yerleşik Stillerle WordArt Ekleme](/cells/tr/net/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells, bir elektronik tabloya Xml Haritası eklemeye izin veren XmlMapCollection.Add yöntemini kullanıma sundu. İşte XmlMapCollection.Add yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[E-tabloya XML Haritası Ekleme](/cells/tr/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Add xml map from the sample.xml to the workbook

book.Worksheets.XmlMaps.Add("sample.xml");

{{< /highlight >}}


### **Cells.LinkToXmlMap Yöntemi Eklendi**
Aspose.Cells, hücreleri XML eşleme öğeleriyle bağlamak için Cells.LinkToXmlMap yöntemini kullanıma sundu.

İşte Cells.LinkToXmlMap yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Cells'i XML Eşleme Öğelerine Bağla](/cells/tr/net/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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


### **ListColumn.Formula Özelliği Eklendi**
Aspose.Cells 16.10.0, formülü yeni eklenen satırlara otomatik olarak yaymak için ListColumn.Formula özelliğini kullanıma sundu.

İşte ListColumn.Formula özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Liste Nesnesinde Formülü Otomatik Olarak Yay](/cells/tr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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

listObject.ListColumns[1].Formula = "=[Column A]+ 1";

// Save the result in XLSX format

book.Save("output.xlsx");

{{< /highlight >}}


### **GridWeb ile Özel İşlevleri Hesaplama Desteği**
Aspose.Cells.GridWeb 16.10.0, GridWeb bileşeni içinden özel işlevleri tanımlamaya ve hesaplamaya hep birlikte izin veren GridAbstractCalculationEngine sınıfıyla birlikte GridWeb.CustomCalculationEngine özelliğini ortaya çıkardı.

İşte yukarıda bahsedilen API'lerin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[GridWeb ile Özel İşlevleri Hesaplama](/cells/tr/net/calculate-custom-functions-in-gridweb/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

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
