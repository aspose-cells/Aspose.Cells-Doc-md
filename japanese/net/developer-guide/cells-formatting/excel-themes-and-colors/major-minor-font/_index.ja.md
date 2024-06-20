---
title: 見出しと本文のテーマフォント
description: Aspose.Cellsは、Excel文書で見出しと本文のテーマフォントを設定する機能をサポートしています。これにより、文書の外観とスタイルをカスタマイズすることができます。
keywords: Aspose.Cells、Excelドキュメント、見出し、本文、テーマフォント、外観、スタイル
type: docs
weight: 120
url: /ja/net/headings-and-body-theme-font/
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
Aspose.Cells for .Net を使用すると、デフォルトのフォントがテーマフォントかどうかを確認したり、 [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) プロパティでテーマフォントをセットしたりすることができます。

以下のサンプルコードは、テーマフォントの操作方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **動的にローカルのテーマフォントを取得する**
時々、サーバーとユーザーのマシンが同じ地域にないことがあります。ユーザーがファイル処理に望むフォントをどのように取得すればよいでしょうか？

ファイルを [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) プロパティでロードする前にシステムの地域設定を変更する必要があります

以下のサンプルコードは、ローカルのテーマフォントを取得する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
