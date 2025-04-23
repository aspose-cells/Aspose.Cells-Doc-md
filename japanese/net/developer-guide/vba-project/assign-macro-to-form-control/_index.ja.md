---
title: フォームコントロールにマクロを割り当てる
type: docs
weight: 60
url: /ja/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、ボタンなどのフォームコントロールにマクロコードを割り当てることができます。Workbook内のフォームコントロールに新しいマクロコードを割り当てるには、[**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname)プロパティを使用してください。

{{% /alert %}}

新しいワークブックを作成し、フォームボタンにマクロコードを割り当て、出力をXLSM形式で保存するサンプルコードを以下に示します。作成されたXLSMファイルをMicrosoft Excelで開くと、指定のマクロコードが表示されます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **C#でフォームコントロールにマクロを割り当てる**

新しいXLSM ファイルとマクロコードを生成するサンプルコードを以下に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
