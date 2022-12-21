---
title: フォーム コントロールへのマクロの割り当て
type: docs
weight: 60
url: /ja/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、ボタンのようなフォーム コントロールにマクロ コードを割り当てることができます。をご利用ください[**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname)プロパティを使用して、ブック内のフォーム コントロールに新しいマクロ コードを割り当てます。

{{% /alert %}}

次のサンプル コードは、新しいワークブックを作成し、マクロ コードをフォーム ボタンに割り当て、出力を XLSM 形式で保存します。出力された XLSM ファイルを Microsoft Excel で開くと、次のマクロ コードが表示されます。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **C# でフォーム コントロールにマクロを割り当てます。**

マクロ コードを使用して出力 XLSM ファイルを生成するサンプル コードを次に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
