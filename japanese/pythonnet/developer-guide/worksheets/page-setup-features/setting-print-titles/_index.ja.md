---
title: Python.NETを使った印刷タイトルの設定
linktitle: 印刷タイトルの設定
type: docs
weight: 200
url: /ja/python-net/how-to-set-print-titles/
description: Aspose.Cells for Python via .NETを使った、印刷ページで繰り返す行/列の見出しの設定方法を学びましょう。
keywords: Pythonの繰り返し印刷ヘッダー、Pythonの印刷タイトル設定、Pythonの印刷タイトルクリア、Excelページ設定Python、Python.NETスプレッドシートの印刷
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

指定したワークシートに印刷タイトルを設定するには、まず[サンプルファイル](input.xlsx)を読み込み、次に[**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/)及び[**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/)のプロパティを変更します。これらのプロパティに範囲文字列を設定すると、印刷タイトルが構成されます。

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

出力結果：
<br>
<img src="1.png" width=60% />

## **Aspose.Cellsを使用した印刷タイトルのクリア方法**

印刷タイトルをクリアするには、印刷タイトルのプロパティを空文字に設定します：

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

出力結果：
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
