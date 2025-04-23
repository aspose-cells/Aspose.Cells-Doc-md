---
title: Aspose.Cellsを使用してVBAまたはマクロコードを修正する
type: docs
weight: 90
url: /ja/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用してVBAまたはマクロコードを修正できます。Aspose.CellsはExcelファイル内のVBAプロジェクトを読み取り、修正するための次のクラスを追加しました。

- VbaProject
- VbaModuleCollection
- VbaModule

この記事では、Aspose.Cellsを使用してソースExcelファイル内のVBAまたはマクロコードを変更する方法を説明します。

{{% /alert %}} 
## **例**
次のサンプルコードは、次のようなVBAまたはマクロコードが含まれているソースExcelファイルをロードします。

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cellsのサンプルコードの実行後、VBAまたはマクロコードは次のように変更されます。

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

ソースExcelファイルと出力Excelファイルを[こちらのリンク](5472596.xlsm)からダウンロードできます。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






{{< app/cells/assistant language="java" >}}
