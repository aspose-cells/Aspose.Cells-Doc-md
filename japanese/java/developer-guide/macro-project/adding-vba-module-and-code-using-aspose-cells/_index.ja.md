---
title: Aspose.Cells を使用して VBA モジュールとコードを追加する
type: docs
weight: 20
url: /ja/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、Aspose.Cells を使用して新しい VBA モジュールとマクロ コードを追加できます。[**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) ワークブック内に新しい VBA モジュールを追加するメソッド

{{% /alert %}}

## **Aspose.Cells を使用して VBA モジュールとコードを追加する**

次のサンプル コードは、新しいワークブックを作成し、新しい VBA モジュールとマクロ コードを追加して、出力を XLSM 形式で保存します。一度、出力された XLSM ファイルを Microsoft Excel で開き、**開発者 > Visual Basic**メニュー コマンドを実行すると、"TestModule" という名前のモジュールが表示され、その中に次のマクロ コードが表示されます。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## サンプルコード

以下は、VBA モジュールとマクロ コードを使用して出力 XLSM ファイルを生成するサンプル コードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
