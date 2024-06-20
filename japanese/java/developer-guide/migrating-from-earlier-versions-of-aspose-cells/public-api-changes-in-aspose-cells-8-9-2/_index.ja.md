---
title: Aspose.Cells 8.9.2 でのパブリック API 変更
type: docs
weight: 330
url: /ja/java/public-api-changes-in-aspose-cells-8-9-2/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells API の 8.9.1 から 8.9.2 への変更点をモジュール/アプリケーション開発者にとって興味深いものについて説明しています。新しいおよび更新されたパブリックメソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の内部での動作の変更についても説明しています。

{{% /alert %}} {{% alert color="primary" %}} 

[Aspose.Cells for Java 8.9.1 で導入されたパブリック API の変更](http://aspose.com/docs/display/cellsjava/Public+API+Changes+in+Aspose.Cells+8.9.1) も併せてご確認ください。

{{% /alert %}} 
## **APIの追加**
### **TextOptions クラスと FontSettings.TextOptions プロパティが追加されました**
Aspose.Cells for Java では、TextOptions クラスと FontSettings.TextOptions プロパティが公開され、Shape のテキスト部分の外観を制御するために使用できます。

FontSettings.TextOptions プロパティの簡単な使用シナリオは次のとおりです。

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
### **TextOptions.Fill、Outline、Shadow プロパティが追加されました**
Aspose.Cells for Java 8.9.2 では、TextOptions.Fill、TextOptions.Outline、TextOptions.Shadow プロパティが公開され、テキストコンテンツの外観を制御することができます（例: 塗りつぶし、影、アウトラインなど）。 

前述のプロパティの簡単な使用シナリオは次のとおりです。

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
### **Shape.Line プロパティが追加されました**
Aspose.Cells for Java では、Shape.Line プロパティが公開され、Shape の輪郭の外観を制御するための LineFormat のインスタンスを返します。

以下はShape.Lineプロパティの簡単な使用シナリオです。

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
### **Shape.Fill プロパティが追加されました**
Aspose.Cells for Java 8.9.2 では、Shape.Fill プロパティが公開され、Shape エリアの異なる部分を制御するための FillFormat のインスタンスを返します。

Shape.Fill プロパティの簡単な使用シナリオは次のとおりです。

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
## **非推奨API**
### **非推奨のShapeFontクラス**
代わりにTextOptionsクラスを使用してください。
### **非推奨のShapeFormatクラス**
代わりにShape.FillおよびShape.Lineプロパティを直接使用してください。
### **非推奨のShape.Formatプロパティ**
代わりにShape.FillおよびShape.Lineプロパティを直接使用してください。
### **非推奨のShape.LineFormatプロパティ**
代わりにShape.Lineプロパティを使用してください。
### **非推奨のShape.FillFormatプロパティ**
代わりにShape.Fillプロパティを使用してください。
### **非推奨のFontSetting.ShapeFontプロパティ**
代わりにFontSetting.TextOptionsプロパティを使用してください。
