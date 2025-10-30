---
title: 見出しと本文のテーマフォント
linktitle: 見出しと本文のテーマフォント
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのNode.jsライブラリです。Excelドキュメントに見出しと本文のテーマフォントを設定でき、ドキュメントの外観とスタイルをカスタマイズ可能です。この記事では、Aspose.Cellsライブラリを使用してExcelドキュメントの見出しと本文のテーマフォントを操作する方法を紹介します。
keywords: Aspose.Cells、Excelドキュメント、見出し、本文、テーマフォント、外観、スタイル、C++を介したNode.js
type: docs
weight: 120
url: /ja/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

リージョン設定が変更されると、既定のフォントは自動的に変更されます。

デフォルトフォントが変更されると、行の高さや列の幅も変更され、ページレイアウトが乱れることさえあります。

デフォルトフォントの変更の原因は何ですか？

Excelのテーマフォントが設定されている場合、Excelは現在の言語環境に応じて自動的に異なるフォントに切り替えます。

{{% /alert %}}

## **Excelでの見出しと本文のテーマフォント**

Excelで、ホームタブを選択し、フォントのドロップダウンボックスをクリックすると、「テーマフォント」が表示され、上部に英語のリージョン設定でCalibri Light（見出し）とCalibri（本文）の2つのテーマフォントがあります。

**![テーマフォント](Theme-Fonts.png)**

テーマフォントを選択すると、フォント名は異なるリージョンで異なる表示になります。リージョンに応じて自動的にフォントが変わるのを避けたい場合は、2つのテーマフォントを選択しないでください。

## **ヘッダーと本文のフォントをプログラムで変更**
Aspose.Cells for Node.js via C++を使用すると、既定のフォントがテーマフォントかどうかを確認したり、[**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-)メソッドを使用してテーマフォントを設定できます。

次のサンプルコードは、テーマフォントを操作する方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **動的にローカルテーマフォントをプログラム的に取得**
時々、サーバーとユーザーのマシンが同じ地域にないことがあります。ユーザーがファイル処理に望むフォントをどのように取得すればよいでしょうか？

ファイルを読み込む前に、[**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-)メソッドを使用してシステムのリージョン設定を設定する必要があります。

以下のサンプルコードは、ローカルのテーマフォントを取得する方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
