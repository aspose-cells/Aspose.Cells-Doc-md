---
title: Python.NETを使ってExcelを縮小ページ幅と高さに印刷するにはどうすればいいですか
linktitle: Excelを縮小ページ幅と高さに印刷するにはどうすればよいですか
type: docs
weight: 200
url: /ja/python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Aspose.Cells for Python via .NETを使用して、Excel印刷のためにfit_to_pages_wideと fit_to_pages_tallのプロパティを設定する方法を学びます。
keywords: Python Excel印刷、Pythonの用紙合わせ設定、PythonのFitToPagesWide、PythonのFitToPagesTall、Pythonでワークシートを一ページに印刷、Pythonですべての列を一ページに印刷
---

## **紹介**

fit_to_pages_wide と fit_to_pages_tall 設定は、印刷時のスプレッドシートのスケーリングを制御します。これらの設定は、印刷された出力が指定されたページの寸法内に収まるようにします：

1. **fit_to_pages_wide**：印刷の横方向のページ数を指定
1. **fit_to_pages_tall**：印刷の縦方向のページ数を指定

## **FitToPagesWide と FitToPagesTall を使用する理由**
主な利点は次のとおりです：
1. 正確な印刷レイアウトの制御
1. 一貫した複数シートの書式設定
1. プロフェッショナルな文書の提示

## **Excelでファイルを横長・縦長のフィットページとして印刷する方法**
Microsoft Excel で設定するには：
1. ブックを開き、ワークシートを選択
1. **ページレイアウト** → **ページ設定** ダイアログに移動
1. **ページ**タブの**スケーリング**の下で：
   - "Fit to" を選択する
   - 横（幅）と縦（高さ）のページ数を指定する

<br>
<img src="2.png" width=60% />

## **Aspose.Cells を使用して Excel を横長・縦長フィットページとして印刷する方法**
プログラム的に構成するには：
1. [サンプルファイル](input.xlsx)を読み込む
1. ワークシートの [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) オブジェクトにアクセス
1. [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) と [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/) のプロパティを設定

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

出力結果：
<br>
<img src="1.png" width=60% />

## **ワークシートを1ページとして印刷する方法**
単一ページ出力を強制するには：
1. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)を使用する
1. [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/) プロパティを設定する

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

出力結果：
<br>
<img src="3.png" width=60% />

## **すべての列を1ページに印刷する方法**
列を横方向に集約するには：
1. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) を設定
1. [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/) プロパティを有効にする

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

出力結果：
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
