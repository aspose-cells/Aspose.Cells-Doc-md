---
title: Aspose.Cells 16.10.0 daki Genel API Değişiklikleri
type: docs
weight: 350
url: /tr/java/public-api-changes-in-aspose-cells-16-10-0/
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

[Yansıma Efektleriyle Çalışma](/cells/tr/java/working-with-the-reflection-effect-of-shape-or-chart/) başlıklı detaylı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ReflectionEffect from the Shape object

ReflectionEffect reflection = shape.getReflection();

//Set its Blur, Size, Transparency and Distance properties

reflection.setBlur(30);

reflection.setSize(90);

reflection.setTransparency(0.5);

reflection.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

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

[Gölge Efektleriyle Çalışma](/cells/tr/java/working-with-the-shadow-effect-of-shape-or-chart/) başlıklı detaylı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ShadowEffect from the Shape object

ShadowEffect shadow = shape.getShadowEffect();

//Set its Angle, Blur, Size, Transparency and Distance properties

shadow.setAngle(150);

shadow.setBlur(30);

shadow.setSize(90);

shadow.setTransparency(0.5);

shadow.setDistance(80);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Parlama Efektleri Desteklenmesi**
Aspose.Cells 16.10.0, Shape.Glow özelliğini ve birlikte kullanılabilen GlowEffect sınıfını ortaya çıkarmıştır. GlowEffect sınıfı, aşağıdaki özellikleri kullanarak bir ışıltı efekti belirtir.

- GlowEffect.Size: Işıltının nokta birimindeki yarıçapını alır/ayarlar.
- GlowEffect.Transparency: Işıl ışıl efektinin saydamlığını 0.0 (opak) ile 1.0 (saydam) arasında bir derece olarak alır/ayarlar.

Shape.Glow özelliğinin basit kullanım senaryosu burada.

{{% alert color="primary" %}} 

[Işıl Işıl Efektiyle Çalışma](/cells/tr/java/working-with-the-glow-effect-of-shape-or-chart/) başlıklı detaylı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of GlowEffect from the Shape object

GlowEffect glow = shape.getGlow();

//Set its Size & Transparency properties

glow.setSize(90);

glow.setTransparency(0.5);

//Save the result in XLSX format

book.save("output.xlsx");

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

[3D Biçimlendirme ile Çalışma](/cells/tr/java/working-with-the-threedformat-of-shape-or-chart/) konusundaki ayrıntılı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet containing a shape

//Alternatively create a new spreadsheet and add a shape

Workbook book = new Workbook("sample.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first shape from the collection

Shape shape = sheet.getShapes().get(0);

//Get the instance of ThreeDFormat from the Shape object

ThreeDFormat threeD = shape.getThreeDFormat();

//Set its ContourWidth & ExtrusionHeight properties

threeD.setContourWidth(15);

threeD.setExtrusionHeight(30);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **Şekil Metninin WordArt Stilleri Desteği**
Aspose.Cells 16.10.0, FontSettingCollection.SetWordArtStyle ve FontSetting.SetWordArtStyle yöntemlerini metnin Şekil nesnesine önceden belirlenmiş WordArt stilini ayarlamak için ortaya çıkardı.

Yukarıda belirtilen yöntemlerin basit kullanım senaryosu aşağıda verilmiştir.

{{% alert color="primary" %}} 

[WordArt Stilleri ile Çalışma](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/) konusundaki ayrıntılı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Create a TextBox with some text

int index = sheet.getTextBoxes().add(0, 0, 100, 700);

TextBox textBox = (TextBox)sheet.getShapes().get(index);

textBox.setText("Aspose File Format APIs");

textBox.getFont().setSize(44);

//Set preset WordArt style to the text of the shape

FontSetting fntSetting = (FontSetting)textBox.getCharacters().get(0);

fntSetting.setWordArtStyle(PresetWordArtStyle.WORD_ART_STYLE_15);

{{< /highlight >}}
### **Dahili WordArt Stilleri Desteği**
Aspose.Cells 16.10.0, Excel 2007'den bu yana önceden belirlenmiş WordArt nesneleri eklemek için ShapeCollection.AddWordArt yöntemini ve PresetWordArtStyle numaralandırmasını ortaya çıkardı.

Yukarıdaki ShapeCollection.AddWordArt yönteminin basit kullanım senaryosu aşağıdaki gibidir.

{{% alert color="primary" %}} 

[Dahili Stillerle WordArt Ekleme](/cells/tr/java/add-word-art-text-with-built-in-styles/) konusundaki ayrıntılı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access ShapeCollection of first worksheet

ShapeCollection shapes = sheet.getShapes();

//Add WordArt with built-in styles

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_1, "Aspose File Format APIs", 00, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);

shapes.addWordArt(PresetWordArtStyle.WORD_ART_STYLE_5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
### **XmlMapCollection.Add Yöntemi Eklendi**
Aspose.Cells, bir elektronik tabloya XML Haritası eklemek için XmlMapCollection.Add yöntemini ortaya çıkardı. İşte XmlMapCollection.Add yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Elektronik Tabloya XML Haritası Ekleme](/cells/tr/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/) konusundaki ayrıntılı makaleyi kontrol edin.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Cells.LinkToXmlMap Yöntemi Eklendi**
Aspose.Cells artık hücreleri XML haritası öğeleriyle ilişkilendirmek için Cells.LinkToXmlMap yöntemini ortaya çıkardı. İşte Cells.LinkToXmlMap yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

[Link Hücreleri XML Haritası Öğelerine Bağlama](/cells/tr/java/link-hucreleri-xml-haritasina/) hakkındaki detaylı makaleye göz atın

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook("sample.xlsx");

//Access the XML Map from the spreadsheet

XmlMap map = book.getWorksheets().getXmlMaps().get(0);

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Map FIELD1 and FIELD2 to cell A1 and B2

sheet.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");

sheet.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

//Map FIELD4 and FIELD5 to cell C3 and D4

sheet.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");

sheet.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

//Map FIELD7 and FIELD8 to cell E5 and F6

sheet.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");

sheet.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

{{< /highlight >}}
### **Added ListColumn.Formula Özelliği**
Aspose.Cells 16.10.0, ListColumn.Formula özelliğini yeni eklenen satırlara otomatik olarak yayınlamak için açığa çıkardı.

ListColumn.Formula özelliğinin basit kullanım senaryosu burada.

{{% alert color="primary" %}} 

[Tablo veya Listeye Otomatik Yaymak](/cells/tr/java/tabloya-veya-listeye-otomatik-olarak-formul-yayma-yontemi-ekleyin/) için ayrıntılı makaleye göz atın

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add column headings in cell A1 and B1

sheet.getCells().get(0, 0).putValue("Column A");

sheet.getCells().get(0, 1).putValue("Column B");

//Add list object, set its name and style

ListObject listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));

listObject.setTableStyleType(TableStyleType.TABLE_STYLE_MEDIUM_14);

listObject.setDisplayName("Table");

//Set the formula of second column so that it could automatically propagate to new rows while entering data

listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
