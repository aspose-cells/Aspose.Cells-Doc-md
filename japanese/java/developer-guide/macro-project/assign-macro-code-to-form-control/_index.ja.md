---
title: マクロ コードをフォーム コントロールに割り当てる
type: docs
weight: 400
url: /ja/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、ボタンのようなフォーム コントロールにマクロ コードを割り当てることができます。をご利用ください[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) メソッドを使用して、ワークブック内のフォーム コントロールに新しいマクロ コードを割り当てます。

{{% /alert %}} 
## **Aspose.Cells を使用してフォーム コントロールにマクロ コードを割り当てる**
次のサンプル コードは、新しいワークブックを作成し、マクロ コードをフォーム ボタンに割り当て、出力を XLSM 形式で保存します。出力 XLSM ファイルを Microsoft Excel で開くと、次のマクロ コードが表示されます。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

マクロ コードを使用して出力 XLSM ファイルを生成するサンプル コードを次に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
