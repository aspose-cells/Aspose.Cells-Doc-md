---
title: 印刷タイトルの設定方法
type: docs
weight: 200
url: /ja/net/how-to-set-print-titles/
description: この資料は、Aspose.Cellsライブラリを使用して印刷タイトルを設定するコード例を紹介しています。
keywords: 行と列を繰り返し印刷、C#での印刷タイトル設定、印刷タイトルの設定と解除、C#を使った印刷タイトルの追加・削除、Excelでの印刷タイトル設定・解除について解説します。
---

## **可能な使用シナリオ**

Excelで印刷タイトルを設定すると、特定の行または列がすべてのページで繰り返され、大きなスプレッドシートを複数ページにわたって印刷する場合に特に便利です。設定する理由は次の通りです：

1. 読みやすさの向上：印刷タイトルは、見出しをすべてのページで表示し続けることで、データの理解を助けます。各ページで情報を解釈しやすくなります。

1. 専門的な外観：各ページにヘッダーやラベルを一定して表示することで、印刷されたドキュメントに洗練されたプロフェッショナルな印象を与えます。

1. ナビゲーションの改善：膨大なデータを含むドキュメントでは、各ページでヘッダーを繰り返すことで、迅速にナビゲートおよび参照でき、ページの行き来を減らすことができます。

1. エラー低減：すべてのページにヘッダーがあると、誤解やデータ入力エラーの可能性が低減され、ユーザーがデータのコンテキストを簡単に理解できるためです。

1. 一貫性：重要な情報（列見出しや行ラベルなど）が常に表示されることにより、ドキュメント全体の一貫性と明確さが保たれます。

## **Excelで印刷タイトルを設定する方法**

Excelで印刷タイトルを設定するには、次の手順に従います：

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。
1. 印刷タイトルにアクセス： "ページ設定" グループ内の "印刷タイトル" をクリックします。
1. 行の繰り返し設定： "ページ設定" ダイアログボックスの "シート" タブに移動します。 "印刷タイトル" セクションで、 "上部で繰り返す行" の横のボックスをクリックし、繰り返す行を選択します。
1. 列の繰り返し設定（必要に応じて）：同様に、 "左側で繰り返す列" の横のボックスをクリックし、繰り返す列を選択します。
<br>
<img src="3.png" width=60% />

1. 確認して印刷："OK" をクリックして設定を適用します。ワークシートを印刷すると、指定した行や列がすべてのページに表示されます。

## **Excelで印刷タイトルをクリアする方法**

Excelで印刷タイトルをクリアするには、繰り返す設定された行または列を削除する必要があります。次の手順です：

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。
1. 印刷タイトルにアクセス： "ページ設定" グループ内の "印刷タイトル" をクリックします。
1. 印刷タイトルをクリア：「ページ設定」ダイアログボックスの「シート」タブに移動します。「先頭行を繰り返す」および「左端列を繰り返す」のテキストボックス内の内容を削除してクリアします。
<br>
<img src="4.png" width=60% />

1. 確認して閉じる：「OK」をクリックして変更を適用します。


## **Aspose.Cellsを使用した印刷タイトル設定方法**

指定したシートにプリントタイトルを設定するには、まず[サンプルファイル](input.xlsx)を読み込み、次に望むシートの[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/)オブジェクトの[**Worksheet.PageSetup.PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlerows/)と[**Worksheet.PageSetup.PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlecolumns/)のプロパティを変更します。これらのプロパティに範囲文字列を設定するとプリントタイトルが設定されます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-print-titles.cs" >}}

出力結果：
<br>
<img src="1.png" width=60% />

## **Aspose.Cellsを使用した印刷タイトルのクリア方法**

指定したシートのプリントタイトルをクリアするには、まず[サンプルファイル](input.xlsx)を読み込み、次に望むシートの[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/)オブジェクトの[**Worksheet.PageSetup.PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlerows/)と[**Worksheet.PageSetup.PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printtitlecolumns/)のプロパティを変更します。これらのプロパティを空文字に設定するとプリントタイトルがクリアされます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-clear-print-titles.cs" >}}

出力結果：
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
