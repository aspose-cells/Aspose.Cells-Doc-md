---
title: Aspose.Cells 8.7.2 での公開 API 変更
type: docs
weight: 260
url: /ja/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.7.1 から 8.7.2 への変更について、モジュール/アプリケーション開発者に興味を持つ可能性がある内容が記載されています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の背後での挙動に変更があった場合についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **デフォルト計算エンジンの拡張**
Aspose.Cells API には強力な計算エンジンがあり、ほとんどすべての Microsoft Excel 関数を計算できます。さらに、Aspose.Cells API では、デフォルトの計算エンジンを拡張して、任意のアプリケーションのカスタム計算要件に適合させることができます。

Aspose.Cells for Java 8.7.2のリリースに伴い、次のAPIが追加されました。

1. AbstractCalculationEngine クラス
1. CalculationData クラス
1. CalculationOptions.CustomEngine プロパティ

{{% alert color="primary" %}} 

上記の API は、より柔軟性を持ってすべての関数（Excel のネイティブ関数を含む）にカスタム計算エンジンを実装できるようにします。

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、[デフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)する詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **TextBoxCollection用のオーバーロードされたインデクサを追加しました**
Aspose.Cells for Java 8.7.2では、TextBoxCollectionクラスのオーバーロードされたインデクサが公開され、Stringとしてその名前を使用してTextBoxのインスタンスにアクセスするためのものです。

{{% alert color="primary" %}} 

この機能の詳細については、[名前を使用したテキストボックスへのアクセス](/cells/ja/java/access-the-text-box-by-the-name/)の詳細な記事を参照してください

{{% /alert %}} 

シンプルな使用シナリオは次のようになります。 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
