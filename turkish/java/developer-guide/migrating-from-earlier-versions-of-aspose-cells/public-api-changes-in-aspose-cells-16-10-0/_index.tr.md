---
title: Genel API Aspose.Cells 16.10.0'daki değişiklikler
type: docs
weight: 350
url: /tr/java/public-api-changes-in-aspose-cells-16-10-0/
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

 Ayrıntılı makaleyi kontrol edin[Yansıma Efektleriyle Çalışmak](/cells/tr/java/working-with-the-reflection-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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

 Ayrıntılı makaleyi kontrol edin[Gölge Efektleriyle Çalışmak](/cells/tr/java/working-with-the-shadow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Işıma Efektleri Desteği**
Aspose.Cells 16.10.0, Shape.Glow özelliğinin yanı sıra GlowEffect sınıfının hepsini birlikte bir Shape nesnesinin ışıma efektini ayarlamaya izin verir. GlowEffect sınıfı, aşağıdaki özellikleri kullanarak nesnenin kenarlarının dışına rengi bulanıklaştırılmış bir dış çizginin eklendiği bir parlama efektini belirtir.

- GlowEffect.Size: Işıma yarıçapını nokta birimi cinsinden alır/ayarlar.
- GlowEffect.Transparency: Işıma efektinin şeffaflık derecesini 0,0 (opak) ila 1,0 (berrak) arasında alır/ayarlar.

İşte Shape.Glow özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Işıma Efekti ile Çalışma](/cells/tr/java/working-with-the-glow-effect-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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

 Ayrıntılı makaleyi kontrol edin[3B Biçimlendirme ile Çalışma](/cells/tr/java/working-with-the-threedformat-of-shape-or-chart/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Shape Metninde WordArt Stilleri Desteği**
Aspose.Cells 16.10.0, önceden ayarlanmış WordArt stilini Shape nesnesinin metnine ayarlamak için FontSettingCollection.SetWordArtStyle & FontSetting.SetWordArtStyle yöntemlerini kullanıma sundu.

İşte yukarıda belirtilen yöntemlerin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[WordArt Stilleriyle Çalışma](https://docs.aspose.com/cells/java/set-preset-wordart-style-to-the-text-of-the-shape/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **WordArt Yerleşik Stilleri için Destek**
Aspose.Cells 16.10.0, Excel 2007'den beri önceden ayarlanmış WordArt nesneleri ekleme desteği sağlamak için ShapeCollection.AddWordArt yöntemini PresetWordArtStyle numaralandırmasıyla birlikte kullanıma sunmuştur.

İşte ShapeCollection.AddWordArt yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Yerleşik Stillerle WordArt Ekleme](/cells/tr/java/add-word-art-text-with-built-in-styles/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells, bir elektronik tabloya Xml Haritası eklemeye izin veren XmlMapCollection.Add yöntemini kullanıma sundu. İşte XmlMapCollection.Add yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[E-tabloya XML Haritası Ekleme](/cells/tr/java/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Add XML map from the sample.xml to the workbook

book.getWorksheets().getXmlMaps().add("sample.xml");

{{< /highlight >}}
### **Cells.LinkToXmlMap Yöntemi Eklendi**
Aspose.Cells, hücreleri XML eşleme öğeleriyle bağlamak için Cells.LinkToXmlMap yöntemini kullanıma sundu. İşte Cells.LinkToXmlMap yönteminin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Cells'i XML Eşleme Öğelerine Bağla](/cells/tr/java/link-cells-to-xml-map-elements/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **ListColumn.Formula Özelliği Eklendi**
Aspose.Cells 16.10.0, formülü yeni eklenen satırlara otomatik olarak yaymak için ListColumn.Formula özelliğini kullanıma sundu.

İşte ListColumn.Formula özelliğinin basit kullanım senaryosu.

{{% alert color="primary" %}} 

 Ayrıntılı makaleyi kontrol edin[Liste Nesnesinde Formülü Otomatik Olarak Yay](/cells/tr/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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

listObject.getListColumns().get(1).setFormula("=[Column A]+ 1");

//Save the result in XLSX format

book.save("output.xlsx");

{{< /highlight >}}
