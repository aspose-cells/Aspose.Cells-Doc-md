---
title: パブリック API Aspose.Cells 8.9.2 の変更点
type: docs
weight: 330
url: /ja/java/public-api-changes-in-aspose-cells-8-9-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.9.1 から 8.9.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} {{% alert color="primary" %}} 

こちらもご確認ください[Public API Aspose.Cells for Java 8.9.1 で導入された変更](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1)

{{% /alert %}} 
## **追加された API**
### **TextOptions クラスと FontSettings.TextOptions プロパティを追加**
Aspose.Cells for Java は、Shape のテキスト部分の外観を制御するために、FontSettings.TextOptions プロパティと共に TextOptions クラスを公開しました。

FontSettings.TextOptions プロパティの簡単な使用シナリオを次に示します。

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
### **TextOptions.Fill、Outline、Shadow プロパティを追加**
Aspose.Cells for Java 8.9.2 では、TextOptions.Fill、TextOptions.Outline、TextOptions.Shadow プロパティが公開されており、それぞれ塗りつぶし、影、アウトラインなど、形状のテキスト コンテンツの側面を制御できます。

前述のプロパティの簡単な使用シナリオを次に示します。

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
### **Shape.Line プロパティを追加**
Aspose.Cells for Java は、Shape のアウトラインの外観を制御するために LineFormat のインスタンスを返す Shape.Line プロパティを公開しました。

Shape.Line プロパティの簡単な使用シナリオを次に示します。

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
### **Shape.Fill プロパティを追加**
Aspose.Cells for Java 8.9.2 は、形状領域のさまざまな側面を制御するために、FillFormat のインスタンスを返す Shape.Fill プロパティを公開しました。

以下は、Shape.Fill プロパティの簡単な使用シナリオです。

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
## **廃止された API**
### **廃止された ShapeFont クラス**
代わりに TextOptions クラスを使用してください。
### **廃止された ShapeFormat クラス**
Shape.Fill および Shape.Line プロパティを直接使用してください。
### **廃止された Shape.Format プロパティ**
Shape.Fill および Shape.Line プロパティを直接使用してください。
### **廃止された Shape.LineFormat プロパティ**
代わりに Shape.Line プロパティを使用してください。
### **廃止された Shape.FillFormat プロパティ**
代わりに Shape.Fill プロパティを使用してください。
### **廃止された FontSetting.ShapeFont プロパティ**
代わりに FontSetting.TextOptions プロパティを使用してください。
