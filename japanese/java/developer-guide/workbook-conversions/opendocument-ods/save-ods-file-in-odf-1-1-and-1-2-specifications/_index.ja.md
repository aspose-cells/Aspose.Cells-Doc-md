---
title: ODS ファイルを ODF 1.1 および 1.2 仕様で保存
type: docs
weight: 170
url: /ja/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---
{{% alert color="primary" %}}

Aspose.Cells は保存をサポートします (**OpenDocument スプレッドシート**ODS ファイル (**OpenDocument 形式** ODF 1.1 および ODF 1.2 仕様。 Aspose.Cells が追加されました[**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) ODS ファイルの保存に ODF 1.1 仕様を使用するプロパティ。このプロパティのデフォルト値は**間違い**したがって、この特別な設定なしで保存された ODS ファイルは 1.2 仕様を使用します。

{{% /alert %}}

以下のサンプル コードは、ワークブック オブジェクトを作成し、最初のワークシートのセル A1 に値を追加してから、ODS ファイルを ODF 1.1 および 1.2 仕様で保存します。デフォルトでは、ODS ファイルは ODF 1.2 仕様で保存されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
