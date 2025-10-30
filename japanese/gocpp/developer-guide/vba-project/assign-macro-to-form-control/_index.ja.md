---
title: GolangとC++でフォームコントロールにマクロを割り当て
linktitle: フォームコントロールにマクロを割り当てる
type: docs
weight: 60
url: /ja/go-cpp/assign-macro-to-form-control/
description: Aspose.Cells for C++を使用して、ボタンなどのフォームコントロールにマクロコードを割り当てる方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、ボタンなどのフォームコントロールにマクロコードを割り当てることができます。Workbook内のフォームコントロールに新しいマクロコードを割り当てるには、[**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/)プロパティを使用してください。

{{% /alert %}}

 以下のサンプルコードは、新しいワークブックを作成し、フォームボタンにマクロコードを割り当て、その出力をXLSM形式で保存します。Microsoft Excelで出力されたXLSMファイルを開くと、次のマクロコードが見えます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **C++でフォームコントロールにマクロを割り当てる**

新しいXLSM ファイルとマクロコードを生成するサンプルコードを以下に示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
