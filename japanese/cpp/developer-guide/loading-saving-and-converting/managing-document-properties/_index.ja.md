---
title: ドキュメントプロパティの管理
type: docs
weight: 30
url: /ja/cpp/managing-document-properties/
---

## **可能な使用シナリオ**
Aspose.Cellsを使用すると、ビルトインおよびカスタムのドキュメントプロパティを操作できます。 ここにMicrosoft Excelインターフェースがあるので、これらの*ドキュメントプロパティ*を開くことが可能です。 このスクリーンショットに示されているように、*詳細設定*をクリックして表示できます。

![todo:image_alt_text](managing-document-properties_1.png)
## **ドキュメントプロパティの管理**
次のサンプルコードは、[サンプルエクセルファイル](23166989.xlsx)を読み込み、*タイトル、サブジェクト*などのビルトインドキュメントプロパティを読み取り、それを変更します。 また、*MyCustom1*などのカスタムドキュメントプロパティを読み込み、*MyCustom5*などの新しいカスタムドキュメントプロパティを追加し、[出力エクセルファイル](23166986.xlsx)を書き込みます。 次のスクリーンショットは、サンプルコードがサンプルエクセルファイルに与える影響を示しています。

![todo:image_alt_text](managing-document-properties_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **コンソール出力**
これは提供された[サンプルエクセルファイル](23166989.xlsx)を使用して上記のサンプルコードを実行した際のコンソール出力です。

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
