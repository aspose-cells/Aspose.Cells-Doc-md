---
title: ヘッディングと本文のテーマフォントをGolang via C++で設定
linktitle: 見出しと本文のテーマフォント
description: Aspose.Cellsはスプレッドシートファイルの操作に使えるC++ライブラリです。Excelドキュメント内の見出しと本文のテーマフォントを設定でき、ドキュメントの外観やスタイルをカスタマイズ可能です。この記事では、Aspose.Cellsライブラリを使用してExcelドキュメントの見出しと本文のテーマフォントを操作する方法を紹介します。
keywords: Aspose.Cells、Excelドキュメント、見出し、本文、テーマフォント、外観、スタイル
type: docs
weight: 120
url: /ja/go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

リージョン設定が変更されると、既定のフォントは自動的に変更されます。

デフォルトフォントが変更されると、行の高さや列の幅も変更され、ページレイアウトが乱れることさえあります。

デフォルトフォントの変更の原因は何ですか？

Excelのテーマフォントが設定されている場合、Excelは現在の言語環境に応じて自動的に異なるフォントに切り替えます。

{{% /alert %}}

## **Excelでの見出しと本文のテーマフォント**

Excelでホームタブを選択し、フォントのドロップダウンボックスをクリックすると、「テーマフォント」が表示され、英語の地域設定においては「Calibri Light」（見出し）と「Calibri」（本文）の2つのテーマフォントが上部に表示されます。

**![テーマフォント](Theme-Fonts.png)**

テーマフォントを選択すると、フォント名は地域によって異なる表示になります。
地域によって自動的にフォントが変更されたくない場合は、2つのテーマフォントを選択しないでください。

## **ヘッダーと本文のフォントをプログラムで変更**
Aspose.Cells for C++を使えば、デフォルトのフォントがテーマフォントかどうかを確認したり、[**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/)プロパティを用いてテーマフォントを設定したりできます。

以下のサンプルコードは、テーマフォントの操作方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}
## **動的にローカルテーマフォントをプログラム的に取得**
時々、サーバーとユーザーのマシンが同じ地域にないことがあります。ユーザーがファイル処理に望むフォントをどのように取得すればよいでしょうか？

[**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/) プロパティを持つファイルを読み込む前に、システムの地域設定を設定する必要があります。

次のサンプルコードは、ローカルテーマフォントを取得する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}
