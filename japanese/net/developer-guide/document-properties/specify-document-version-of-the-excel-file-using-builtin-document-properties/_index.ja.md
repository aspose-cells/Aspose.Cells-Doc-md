---
title: ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する
type: docs
weight: 20
url: /ja/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **可能な使用シナリオ**

Excelファイルの**バージョン番号**を変更するには、ファイルを右クリックして [プロパティ] > [詳細] を選択し、その後 **バージョン番号** フィールドを編集します。Aspose.CellsのAPIを使用してプログラムで変更するには、[**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/documentversion) プロパティを使用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する**

次のサンプルコードでは、ワークブックを作成し、そのタイトル、著者、バージョン番号を含むビルトインドキュメントプロパティを変更します。そのコードで生成される出力Excelファイルと、[**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/documentversion) プロパティによって変更されたバージョン番号を示すスクリーンショットを参照してください。

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.cs" >}}
