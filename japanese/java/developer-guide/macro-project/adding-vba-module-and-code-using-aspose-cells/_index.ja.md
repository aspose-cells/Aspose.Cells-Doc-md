---
title: Aspose.Cellsを使用してVBAモジュールおよびマクロコードを追加できます。
type: docs
weight: 20
url: /ja/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して新しいVBAモジュールとマクロコードを追加できます。 [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) メソッドを使用して、ブック内に新しいVBAモジュールを追加してください。

{{% /alert %}}

## **Aspose.Cellsを使用してVBAモジュールとコードの追加**

次のサンプルコードは、新しいワークブックを作成し、新しいVBAモジュールとマクロコードを追加し、出力をXLSM形式で保存します。作業結果のXLSMファイルをMicrosoft Excelで開いて**開発者 > Visual Basic**メニューコマンドをクリックすると、「TestModule」というモジュールが表示され、その中に次のマクロコードが表示されます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## サンプルコード

VBAモジュールおよびマクロコードを含む出力XLSMファイルを生成するサンプルコードを以下に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
