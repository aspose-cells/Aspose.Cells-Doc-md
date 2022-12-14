---
title: Genel API Aspose.Cells 8.9.2'deki değişiklikler
type: docs
weight: 320
url: /tr/net/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.9.1 sürümünden 8.9.2 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} {{% alert color="primary" %}} 

 Lütfen ayrıca kontrol edin[Genel API Aspose.Cells for .NET 8.9.1'de yapılan değişiklikler](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **Eklenen API'ler**
### **TextOptions Sınıfı ve FontSettings.TextOptions Özelliği Eklendi**
Aspose.Cells for .NET, bir Şeklin metinsel bölümlerinin görünümünü kontrol etmek için TextOptions sınıfını FontSettings.TextOptions özelliğiyle birlikte kullanıma sundu.

İşte FontSettings.TextOptions özelliğinin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

{{< /highlight >}}


### **TextOptions.Fill, Outline & Shadow Özellikleri Eklendi**
Aspose.Cells for .NET 8.9.2, sırasıyla dolgu, gölge ve anahat gibi şeklin metin içeriğinin yönlerini kontrol etmeyi sağlayan TextOptions.Fill, TextOptions.Outline & TextOptions.Shadow özelliklerini ortaya çıkardı.

İşte yukarıda belirtilen özelliklerin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Set text for TextBox

shape.Text = "Aspose";

// Access TextOptions of Shape

var textOptions = shape.TextBody[1].TextOptions;

// Set shadow 

textOptions.Shadow.PresetType = PresetShadowType.Below;

// Set fill color

textOptions.Fill.FillType = FillType.Solid;

textOptions.Fill.SolidFill.Color = Color.Red;

// Set outline color

textOptions.Outline.SetOneColorGradient(Color.Blue, 0.3, GradientStyleType.Horizontal, 2);

{{< /highlight >}}


### **Shape.Line Özelliği Eklendi**
Aspose.Cells for .NET, Shape anahatlarının görünümünü kontrol etmek için LineFormat örneğini döndüren Shape.Line özelliğini kullanıma sundu.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access LineFormat of Shape

var line = shape.Line;

// Set weight of line

line.Weight = 1;

{{< /highlight >}}


### **Shape.Fill özelliği eklendi**
Aspose.Cells for .NET 8.9.2, şekil alanının farklı yönlerini kontrol etmek için bir FillFormat örneği döndüren Shape.Fill özelliğini ortaya çıkardı.

Shape.Fill özelliğinin basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Initialize Workbook instance

var book = new Workbook();

// Access first worksheet from collection

var sheet = book.Worksheets[0];

// Add a Shape of type TextBox to the collection 

var shape = sheet.Shapes.AddTextBox(0, 0, 0, 0, 100, 200);

// Access FillFormat of Shape

var fill = shape.Fill;

// Set color for fill

fill.SetOneColorGradient(Color.Red, 0.1, GradientStyleType.Horizontal, 2);

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
