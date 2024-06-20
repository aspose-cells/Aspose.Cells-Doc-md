---
title: Aspose.Cells 8.9.2 de Kamu API Değişiklikleri
type: docs
weight: 330
url: /tr/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 8.9.1'den 8.9.2'ye Aspose.Cells API'sindeki değişiklikleri açıklar ki bu, modül/uygulama geliştiricilerinin ilgisini çekebilir. Yalnızca yeni ve güncellenmiş kamu yöntemleri, eklendi & kaldırılan sınıflar vb. değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliği de içerir.

{{% /alert %}} {{% alert color="primary" %}} 

Lütfen [Aspose.Cells for Java 8.9.1'de Tanıtılan Kamu API Değişikliklerini](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1) de kontrol edin

{{% /alert %}} 
## **Eklenen API'lar**
### **TextOptions Sınıfı & FontSettings.TextOptions Özelliği eklendi**
Aspose.Cells for Java, bir Şeklin metin kısımlarının yapısını kontrol etmek için TextOptions sınıfını ve FontSettings.TextOptions özelliğini açığa çıkardı.

FontSettings.TextOptions özelliğinin basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

{{< /highlight >}}
### **TextOptions.Fill, Outline & Shadow Özellikleri Eklendi**
Aspose.Cells for Java 8.9.2, metin içeriğinin görünümünü kontrol etmeye izin veren TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow özelliklerini açıkladı. 

Yukarıdaki özelliklerin basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Add text to Shape

shape.setText("Aspose");

//Access TextOptions of Shape

TextOptions textOptions =  ((FontSetting)shape.getCharacters().get(0)).getTextOptions();

//Set shadow 

textOptions.getShadow().setPresetType(PresetShadowType.BELOW);

//Set fill color

textOptions.getFill().setFillType(FillType.SOLID);

textOptions.getFill().getSolidFill().setColor(Color.getRed());

//Set outline color

textOptions.getOutline().setOneColorGradient(Color.getBlue(), 0.3, GradientStyleType.HORIZONTAL, 2);

{{< /highlight >}}
### **Eklenen Shape.Line Özelliği**
Aspose.Cells for Java, Shape.Line özelliğini ortaya çıkarmıştır; bu, Bir Şeklin dış hatlarının görünümünü kontrol etmek için bir LineFormat örneği döndürür.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access LineFormat of Shape

LineFormat line = shape.getLine();

//Set weight of line

line.setWeight(4);

{{< /highlight >}}
### **Eklenen Shape.Fill özelliği**
Aspose.Cells for Java 8.9.2, Shape.Fill özelliğini ortaya çıkarmıştır; bu, şekil alanının farklı yönlerini kontrol etmek için bir FillFormat örneği döndürür.

İşte Shape.Fill özelliğinin basit kullanım senaryosu.

**Java**

{{< highlight csharp >}}

 //Initialize Workbook instance

Workbook book = new Workbook();

//Access first worksheet from collection

Worksheet sheet = book.getWorksheets().get(0);

//Add a Shape of type TextBox to the collection 

Shape shape = sheet.getShapes().addShape(MsoDrawingType.TEXT_BOX, 0, 0, 0, 0, 100, 200);

//Access FillFormat of Shape

FillFormat fill = shape.getFill();

//Set color for fill

fill.setFillType(FillType.SOLID);

fill.getSolidFill().setColor(Color.getBlue());

{{< /highlight >}}
## **Eskimiş API'lar**
### **Eskiye Dair ShapeFont Sınıfı**
Lütfen bunun yerine TextOptions sınıfını kullanın.
### **Eskiye Dair ShapeFormat Sınıfı**
Lütfen doğrudan Shape.Fill ve Shape.Line özelliklerini kullanın.
### **Eskiye Dair Shape.Format Özelliği**
Lütfen doğrudan Shape.Fill ve Shape.Line özelliklerini kullanın.
### **Eskiye Dair Shape.LineFormat Özelliği**
Lütfen bunun yerine Shape.Line özelliğini kullanın.
### **Eskiye Dair Shape.FillFormat Özelliği**
Lütfen bunun yerine Shape.Fill özelliğini kullanın.
### **Eskiye Dair FontSetting.ShapeFont Özelliği**
Lütfen bunun yerine FontSetting.TextOptions özelliğini kullanın.
