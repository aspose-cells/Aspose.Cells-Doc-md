---
title: 見出しと本文のテーマのフォント
description: Aspose.Cells は、スプレッドシート ファイルを操作するための .NET ライブラリです。 Excel ドキュメントの見出しと本文のテーマ フォントの設定をサポートし、ユーザーがドキュメントの外観とスタイルをカスタマイズできるようにします。この記事では、Aspose.Cells ライブラリを使用して Excel ドキュメントの見出しと本文のテーマ フォントを操作する方法を紹介します。
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /ja/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

デフォルトのフォントは、再設定の変更時に自動的に変更されます。

デフォルトのフォントを変更すると、行の高さと列の幅も変更され、ページのレイアウトが崩れる可能性もあります。

デフォルトのフォントが変更された原因は何ですか?

Excel のテーマ フォントが設定されている場合、Excel は現在の言語環境に基づいて異なるフォントを自動的に切り替えます。


{{% /alert %}}

##  **Excelの見出しと本文のテーマフォント**

Excel で、[ホーム] タブを選択し、フォント ドロップダウン ボックスをクリックすると、2 つのテーマ フォントが含まれる「テーマ フォント」が表示されます。Calibri Light (見出し) と Calibri (本文) が上部にあり、英語地域が設定されています。

**![テーマフォント](Theme-Fonts.png)**

テーマフォントが選択されている場合、地域ごとに異なるフォント名が表示されます。
異なる地域でフォントが自動的に変更されることを望まない場合は、2 つのテーマ フォントを選択しないでください。


##  **プログラムによる見出しと本文のフォントの変更**
.Net の Aspose.Cells を使用すると、デフォルトのフォントがテーマ フォントであるかどうかを確認したり、テーマ フォントを設定したりできます。[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/)財産。

次のサンプル コードは、テーマのフォントを操作する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **ローカルのテーマフォントをプログラム的に動的に取得します**
場合によっては、サーバーとユーザーのマシンが同じリージョンにない場合があります。ユーザーがファイル処理に必要としているのと同じフォントを入手するにはどうすればよいでしょうか?

ファイルをロードする前に、システムの地域設定を設定する必要があります。[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/)財産

次のサンプル コードは、ローカル テーマ フォントを取得する方法を示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}