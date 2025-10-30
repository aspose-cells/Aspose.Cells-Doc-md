---
title: Golang経由のC++でBuiltInドキュメントプロパティを使ってExcelファイルのドキュメントバージョンを指定
linktitle: ドキュメントバージョンの指定
type: docs
weight: 20
url: /ja/go-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: ビルトインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する方法を学びます。Aspose.Cells for C++を使用して解説します。
---

## **可能な使用シナリオ**

Excelファイルの**バージョン番号**を変更するには、ファイルを右クリックし、[プロパティ]→[詳細]を選択し、**バージョン番号**の欄を編集してください。Aspose.Cells APIを使ってプログラムで変更するには[**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/)プロパティを使用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する**

次のサンプルコードは、ワークブックを作成し、そのビルトインドキュメントプロパティ（タイトル、作者、バージョン番号）を変更します。コードで生成された[出力Excelファイル](64716811.xlsx)と、その中のバージョン番号が[**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/)プロパティによって変更されたスクリーンショットを確認してください。

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyDocumentVersionOfTheExcelFileUsingBuiltinDocumentProperties.go" >}}
