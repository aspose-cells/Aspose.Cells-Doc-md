---
title: フォームコントロールにマクロコードを割り当てる
type: docs
weight: 400
url: /ja/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cellsでは、ボタンなどのフォームコントロールにマクロコードを割り当てることができます。ワークブック内のフォームコントロールに新しいマクロコードを割り当てるには、[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)メソッドを使用してください。

{{% /alert %}} 
## **Aspose.Cellsを使用してフォームコントロールにマクロコードを割り当てる**
次のサンプルコードは、新しいブックを作成し、フォームコントロールにマクロコードを割り当ててXLSM形式で出力します。 出力されたXLSMファイルをMicrosoft Excelで開くと、以下のマクロコードが表示されます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

マクロコードを含む出力XLSMファイルを生成するサンプルコードを以下に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
