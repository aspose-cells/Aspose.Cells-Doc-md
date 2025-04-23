---
title: Aspose.Cells 8.7.2 での公開 API 変更
type: docs
weight: 250
url: /ja/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.7.1 から 8.7.2 への変更について、モジュール/アプリケーション開発者に興味を持つ可能性がある内容が記載されています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の背後での挙動に変更があった場合についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **デフォルト計算エンジンの拡張**
Aspose.Cells API には強力な計算エンジンがあり、ほとんどすべての Microsoft Excel 関数を計算できます。さらに、Aspose.Cells API では、デフォルトの計算エンジンを拡張して、任意のアプリケーションのカスタム計算要件に適合させることができます。

以下は、Aspose.Cells for .NET 8.7.2のリリースとともに追加されたAPIです。

1. AbstractCalculationEngine クラス
1. CalculationData クラス
1. CalculationOptions.CustomEngine プロパティ

{{% alert color="primary" %}} 

上記の API は、より柔軟性を持ってすべての関数（Excel のネイティブ関数を含む）にカスタム計算エンジンを実装できるようにします。

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、[デフォルトの計算エンジンを拡張するためのカスタム計算エンジンの実装](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)の詳細記事をご覧ください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **TextBoxCollection用のオーバーロードされたインデクサを追加しました**
Aspose.Cells for .NET 8.7.2では、TextBoxCollectionクラスにおいて名前を使用してTextBoxのインスタンスにアクセスするためのオーバーロードされたインデクサーが公開されました。

{{% alert color="primary" %}} 

この機能の詳細については、[名前を使用してTextBoxにアクセス](/cells/ja/net/access-the-text-box-by-the-name/)の詳細記事をご覧ください

{{% /alert %}} 

シンプルな使用シナリオは次のようになります。

**C#**

{{< highlight csharp >}}

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


### **GridWeb用のOnAfterColumnFilterイベントを追加しました**
Aspose.Cells.GridWeb for .NET 8.7.2では、GridWeb UIを介したフィルタリングメカニズムに対するコールバックとしてOnAfterColumnFilterイベントが公開されました。イベント名が示すように、このイベントは列のフィルタリングが適用された後にトリガされ、フィルタリング情報（適用された列インデックスや選択されたフィルタ値など）を取得するために使用できます。

シンプルな使用シナリオは次のようになります。

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
