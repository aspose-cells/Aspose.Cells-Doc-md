---
title: ODF 1.1および1.2仕様でODSファイルを保存する
type: docs
weight: 170
url: /ja/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、(**OpenDocument Format**) ODF 1.1およびODF 1.2仕様で(**OpenDocument Spreadsheet**) ODSファイルを保存することをサポートしています。Aspose.Cellsでは、ODSファイルを保存するための特別な設定にこの[**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11)プロパティを追加しました。このプロパティのデフォルト値は**false**なので、この特別な設定なしで保存されるODSファイルは1.2の仕様を使用します。

{{% /alert %}}

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1に値を追加し、ODF 1.1および1.2仕様でODSファイルを保存します。デフォルトでは、ODSファイルはODF 1.2仕様で保存されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
