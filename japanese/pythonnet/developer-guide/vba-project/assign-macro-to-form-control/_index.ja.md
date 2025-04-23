---
title: フォームコントロールにマクロを割り当てる
type: docs
weight: 60
url: /ja/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ボタンなどのフォームコントロールにマクロコードを割り当てることを可能にします。ワークブック内のフォームコントロールに新しいマクロコードを割り当てるために、[**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name)プロパティを使用してください。

{{% /alert %}}

新しいワークブックを作成し、フォームボタンにマクロコードを割り当て、出力をXLSM形式で保存するサンプルコードを以下に示します。作成されたXLSMファイルをMicrosoft Excelで開くと、指定のマクロコードが表示されます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Pythonでフォームコントロールにマクロを割り当て**

新しいXLSM ファイルとマクロコードを生成するサンプルコードを以下に示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
