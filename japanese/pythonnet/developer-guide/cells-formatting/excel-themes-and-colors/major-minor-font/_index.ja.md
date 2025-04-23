---
title: 見出しと本文のテーマフォント
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのPythonライブラリです。Excelドキュメント内で見出しや本文のテーマフォントを設定することをサポートし、ドキュメントの外観とスタイルをカスタマイズ可能です。この記事では、Aspose.Cells for Python via .NETライブラリを使用してExcelドキュメント内の見出しと本文のテーマフォントを操作する方法を紹介します。
keywords: Aspose.Cells for Python via .NET、Excelドキュメント、見出し、本文、テーマフォント、外観、スタイル
type: docs
weight: 120
url: /ja/python-net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

デフォルトフォントは、地域設定が変更されると自動的に変更されます。 

デフォルトフォントが変更されると、行の高さや列の幅も変更され、ページレイアウトが乱れることさえあります。

デフォルトフォントの変更の原因は何ですか？

Excelのテーマフォントが設定されている場合、Excelは現在の言語環境に応じて自動的に異なるフォントに切り替えます。


{{% /alert %}}

## **Excelでの見出しと本文のテーマフォント**

Excelでは、[ホーム]タブを選択し、フォントのドロップダウンボックスをクリックすると、「テーマフォント」という名前の2つのテーマフォント（見出し用のCalibri Lightと本文用のCalibri）が英語の地域設定に応じてトップに表示されます。

**![テーマフォント](Theme-Fonts.png)**

テーマフォントが選択されている場合、異なる地域でフォント名が異なることが表示されます。
異なる地域でフォントが自動的に変更されないようにしたい場合は、2つのテーマフォントを選択しないでください。


## **見出しと本文のフォントをプログラムで変更する**
Aspose.Cells for Python via .NETを使えば、デフォルトのフォントがテーマフォントかどうかを確認したり、[**Font.scheme_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font/scheme_type)プロパティを使ってテーマフォントを設定したりできます。

以下のサンプルコードは、テーマフォントの操作方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Headings-and-body-font.py" >}}


## **動的にローカルのテーマフォントを取得する**
時々、サーバーとユーザーのマシンが同じ地域にないことがあります。ユーザーがファイル処理に望むフォントをどのように取得すればよいでしょうか？

ファイルを [**LoadOptions.region**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/region) プロパティでロードする前にシステムの地域設定を変更する必要があります

以下のサンプルコードは、ローカルのテーマフォントを取得する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Local-Theme-Font.py" >}}

