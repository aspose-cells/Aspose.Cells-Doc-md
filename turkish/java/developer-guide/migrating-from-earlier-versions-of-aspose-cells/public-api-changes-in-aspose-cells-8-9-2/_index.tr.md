---
title: Genel API Aspose.Cells 8.9.2'deki değişiklikler
type: docs
weight: 330
url: /tr/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.9.1 sürümünden 8.9.2 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} {{% alert color="primary" %}} 

 Lütfen ayrıca kontrol edin[Genel API Aspose.Cells for Java 8.9.1'de yapılan değişiklikler](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Eklenen API'ler**
### **TextOptions Sınıfı ve FontSettings.TextOptions Özelliği Eklendi**
Aspose.Cells for Java, bir Şeklin metinsel bölümlerinin görünümünü kontrol etmek için TextOptions sınıfını FontSettings.TextOptions özelliğiyle birlikte kullanıma sundu.

İşte FontSettings.TextOptions özelliğinin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

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
 Aspose.Cells for Java 8.9.2, sırasıyla dolgu, gölge ve anahat gibi şeklin metin içeriğinin yönlerini kontrol etmeyi sağlayan TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow özelliklerini ortaya çıkardı.

İşte yukarıda belirtilen özelliklerin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

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
### **Shape.Line Özelliği Eklendi**
Aspose.Cells for Java, Shape anahatlarının görünümünü kontrol etmek için LineFormat örneğini döndüren Shape.Line özelliğini kullanıma sundu.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

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
### **Shape.Fill özelliği eklendi**
Aspose.Cells for Java 8.9.2, şekil alanının farklı yönlerini kontrol etmek için bir FillFormat örneği döndüren Shape.Fill özelliğini ortaya çıkardı.

Shape.Fill özelliğinin basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
## **Eski API'ler**
### **Eski ShapeFont Sınıfı**
Lütfen bunun yerine TextOptions sınıfını kullanın.
### **Eski ShapeFormat Sınıfı**
Lütfen doğrudan Shape.Fill ve Shape.Line özelliklerini kullanın.
### **Eski Shape.Format Özelliği**
Lütfen doğrudan Shape.Fill ve Shape.Line özelliklerini kullanın.
### **Eski Shape.LineFormat Özelliği**
Lütfen bunun yerine Shape.Line özelliğini kullanın.
### **Eski Shape.FillFormat Özellik**
Lütfen bunun yerine Shape.Fill özelliğini kullanın.
### **Eski FontSetting.ShapeFont Özelliği**
Lütfen bunun yerine FontSetting.TextOptions özelliğini kullanın.
