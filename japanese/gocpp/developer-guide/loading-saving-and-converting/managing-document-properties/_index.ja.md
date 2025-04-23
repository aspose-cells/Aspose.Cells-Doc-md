---
title: ドキュメントプロパティの管理
type: docs
weight: 30
url: /ja/go-cpp/managing-document-properties/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用すると、ビルトインおよびカスタムのドキュメントプロパティを操作できます。 ここにMicrosoft Excelインターフェースがあるので、これらの*ドキュメントプロパティ*を開くことが可能です。 このスクリーンショットに示されているように、*詳細設定*をクリックして表示できます。

![todo:image_alt_text](managing-document-properties_1.png)

## **ドキュメントプロパティの管理**

以下のサンプルコードは、[サンプルExcelファイル](#)をロードし、組み込みのドキュメントプロパティ（例：*Title*と*Subject*）を読み取り、それらを変更します。その後、カスタムドキュメントプロパティ（例：*MyCustom1*）を読み取り、新しいカスタムドキュメントプロパティ（例：*MyCustom5*）を追加し、結果のExcelファイルを保存します。コードの効果を示すスクリーンショットも併せて掲載しています。

![todo:image_alt_text](managing-document-properties_2.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **コンソール出力**

上記のサンプルコードを提供された[サンプルExcelファイル](23166989.xlsx)で実行したときのコンソール出力です。

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}
