---
title: パブリック API Aspose.Cells の変更点 8.7.2
type: docs
weight: 260
url: /ja/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.7.1 から 8.7.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **デフォルトの計算エンジンを拡張**
Aspose.Cells API には、ほとんどすべての Microsoft Excel 関数を計算できる強力な計算エンジンがあります。さらに、Aspose.Cells API を使用すると、デフォルトの計算エンジンを拡張して、あらゆるアプリケーションのカスタム計算要件を満たすことができます。

Aspose.Cells for Java 8.7.2 のリリースで、次の API が追加されました。

1. AbstractCalculationEngine クラス
1. 計算データ クラス
1. CalculationOptions.CustomEngine プロパティ

{{% alert color="primary" %}} 

上記の API を使用すると、すべての関数 (Excel のネイティブ関数を含む) のカスタム計算エンジンをより柔軟に実装できます。

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[カスタム計算エンジンの実装](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
### **TextBoxCollection のオーバーロードされたインデクサーを追加しました**
Aspose.Cells for Java 8.7.2 は、TextBoxCollection クラスのオーバーロードされたインデクサーを公開して、その名前を String として使用して TextBox のインスタンスにアクセスしました。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[名前を介して TextBox にアクセスする](/cells/ja/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

簡単な使用シナリオは次のようになります。

**Java**

{{< highlight "csharp" >}}

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
