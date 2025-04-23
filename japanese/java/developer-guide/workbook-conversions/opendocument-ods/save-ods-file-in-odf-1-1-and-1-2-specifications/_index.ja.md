---
title: ODSファイルをODF 1.1、1.2、1.3仕様で保存
type: docs
weight: 170
url: /ja/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、(OpenDocument Spreadsheet) ODSファイルを(基本となる) OpenDocument Format ODF 1.1、1.2、そしてODF 1.3仕様で保存することをサポートしています。Aspose.Cellsでは、ODFバージョンを指定してODSファイルを保存するための [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) プロパティを追加しています。このプロパティのデフォルト値は [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12) ですので、特別な設定なしで保存されたODSファイルは、バージョン1.2を使用します。

{{% /alert %}}

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1に値を追加し、ODF 1.1および1.2仕様でODSファイルを保存します。デフォルトでは、ODSファイルはODF 1.2仕様で保存されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
