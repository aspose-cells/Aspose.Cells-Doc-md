---
title: パブリック API Aspose.Cells の変更点 8.7.2
type: docs
weight: 250
url: /ja/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.7.1 から 8.7.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **デフォルトの計算エンジンを拡張**
Aspose.Cells API には、ほとんどすべての Microsoft Excel 関数を計算できる強力な計算エンジンがあります。さらに、Aspose.Cells API を使用すると、デフォルトの計算エンジンを拡張して、あらゆるアプリケーションのカスタム計算要件を満たすことができます。

Aspose.Cells for .NET 8.7.2 のリリースで、次の API が追加されました。

1. AbstractCalculationEngine クラス
1. 計算データ クラス
1. CalculationOptions.CustomEngine プロパティ

{{% alert color="primary" %}} 

上記の API を使用すると、すべての関数 (Excel のネイティブ関数を含む) のカスタム計算エンジンをより柔軟に実装できます。

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[カスタム計算エンジンの実装](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **TextBoxCollection のオーバーロードされたインデクサーを追加しました**
Aspose.Cells for .NET 8.7.2 は、名前を文字列として使用して TextBox のインスタンスにアクセスするために、TextBoxCollection クラスのオーバーロードされたインデックスを公開しました。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[名前を介して TextBox にアクセスする](/cells/ja/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

簡単な使用シナリオは次のようになります。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **GridWeb の OnAfterColumnFilter イベントを追加**
Aspose.Cells.GridWeb for .NET 8.7.2 は、Aspose.Cells.GridWeb UI を通じて行われるフィルタリング メカニズムへのコールバックとして機能する OnAfterColumnFilter イベントを公開しました。名前が示すように、イベントは列フィルタリングが適用された後にトリガーされ、フィルターが適用された列インデックスや選択されたフィルター値などのフィルター情報を取得するために使用できます。

簡単な使用シナリオは次のようになります。

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

イベントをGridWebコントロールに登録することを忘れないでください<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
