---
title: Aspose.Cells 8.9.2 de Kamu API Değişiklikleri
type: docs
weight: 320
url: /tr/net/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 8.9.1'den 8.9.2'ye Aspose.Cells API'sindeki değişiklikleri açıklar ki bu, modül/uygulama geliştiricilerinin ilgisini çekebilir. Yalnızca yeni ve güncellenmiş kamu yöntemleri, eklendi & kaldırılan sınıflar vb. değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliği de içerir.

{{% /alert %}} {{% alert color="primary" %}} 

Ayrıca [Aspose.Cells for .NET 8.9.1'de Tanıtılan Genel API Değişikliklerine](http://aspose.com/docs/display/cellsnet/Public+API+Changes+in+Aspose.Cells+8.9.1) de bakınız.

{{% /alert %}} 
## **Eklenen API'lar**
### **TextOptions Sınıfı & FontSettings.TextOptions Özelliği eklendi**
Aspose.Cells for .NET, Şekil'in metinsel kısımlarının görünümünü kontrol etmek için FontSettings.TextOptions özelliği ile birlikte TextOptions sınıfını sunmuştur.

FontSettings.TextOptions özelliğinin basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.9.2, şeklin metin içeriğinin görünümünü kontrol etmek için Fill, Outline ve Shadow özelliklerini içeren TextOptions.Fill, TextOptions.Outline ve TextOptions.Shadow özelliklerini sunmuştur.

Yukarıdaki özelliklerin basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **Eklenen Shape.Line Özelliği**
Aspose.Cells for .NET, Şekil'in dış çizgilerinin görünümünü kontrol etmek için Line özelliğini sunmuştur.

İşte Shape.Line özelliğinin basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

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


### **Eklenen Shape.Fill özelliği**
Aspose.Cells for .NET 8.9.2, şekil alanının farklı yönlerini kontrol etmek için FillFormat örneğini döndüren Shape.Fill özelliğini sunmuştur.

İşte Shape.Fill özelliğinin basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
