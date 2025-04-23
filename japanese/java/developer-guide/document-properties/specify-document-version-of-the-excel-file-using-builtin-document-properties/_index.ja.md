---
title: ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する
type: docs
weight: 20
url: /ja/java/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **可能な使用シナリオ**

Excelファイルの*バージョン番号*を変更するには、ファイルを右クリックし、次に*プロパティ > 詳細*を選択してから*バージョン番号*フィールドを編集します。また、Aspose.CellsのAPIを使用してプログラムで変更するには、[**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion)プロパティを使用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する**

次のサンプルコードは、ブックを作成し、そのビルトインドキュメントプロパティ（*タイトル*、*作成者*、*バージョン番号*を含む）を変更します。コードによって生成された[出力Excelファイル](64716836.xlsx)と、[**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion)プロパティによって変更された*バージョン番号*を示すスクリーンショットをご覧ください。

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
