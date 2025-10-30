---
title: 特定のUnicode文字のフォントを変更してPDFに保存する方法（Python.NET）
linktitle: 特定のUnicode文字のフォントを変更する
type: docs
weight: 260
url: /ja/python-net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cells for Python via .NETを使用したPDF変換中に、特定のUnicode文字のフォントを変更する方法を学びます。文字レベルのフォント置換で正確な表示を実現します。
---

{{% alert color="primary" %}}

ユーザー指定のフォントでは表示できないUnicode文字がいくつかあります。その例が**ノンブレーキングハイフン**（U+2011）です。Unicode番号は8209で、「Times New Roman」では表示できませんが、「Arial Unicode MS」などのフォントでは表示可能です。

こうした文字が特定のフォント（例：Times New Roman）でフォーマットされたテキストに現れた場合、Aspose.Cellsは自動的にその単語や文のフォントを互換性のあるフォント（例：Arial Unicode MS）に変更します。特定の文字だけのフォントを変更したい場合は、[PdfSaveOptions.is_font_substitution_char_granularity](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsavingoptions/#is_font_substitution_char_granularity)プロパティを使って詳細な制御が可能です。

{{% /alert %}}

## **比較例サンプル**

以下のスクリーンショットは、設定の違いによる出力例です。最初のPDFは全テキストのフォント置換を示し、2番目のPDFは特定文字だけのフォント変更を示しています。

|**全文字の置換**|**文字レベルの置換**|
| :- | :- |
|![フォント変更（全Unicode文字）](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|![選択的フォント変更](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

## **実装手順**

文字レベルのフォント置換を有効にするには:

1. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) オブジェクトを作成します
2. [**Worksheet.cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) プロパティを使用してワークシートのセルにアクセスします
3. 特殊なUnicode文字を含むセル値を設定します
4. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) を次のように構成します:
   - `is_font_substitution_char_granularity = True`
5. ワークブックをPDF形式で保存します

```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create workbook object
workbook = Workbook()

# Access the first worksheet
worksheet = workbook.worksheets[0]

# Access cells
cell1 = worksheet.cells.get("A1")
cell2 = worksheet.cells.get("B1")

# Set the styles of both cells to Times New Roman
style = cell1.get_style()
style.font.name = "Times New Roman"
cell1.set_style(style)
cell2.set_style(style)

# Put the values inside the cell
cell1.put_value("Hello without Non-Breaking Hyphen")
cell2.put_value("Hello" + chr(8209) + " with Non-Breaking Hyphen")

# Autofit the columns
worksheet.auto_fit_columns()

# Save to Pdf without setting PdfSaveOptions.is_font_substitution_char_granularity
workbook.save(os.path.join(data_dir, "SampleOutput_out.pdf"))

# Save to Pdf after setting PdfSaveOptions.is_font_substitution_char_granularity to true
opts = PdfSaveOptions()
opts.is_font_substitution_char_granularity = True
workbook.save(os.path.join(data_dir, "SampleOutput2_out.pdf"), opts)
```

## **主要設定項目**

これらの重要なAPIコンポーネントを使用します:

- PDFレンダリング設定用の [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) クラス
- 文字レベルのフォント置換のための **is_font_substitution_char_granularity** プロパティ
- 出力生成のための [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/) メソッド

{{% alert color="note" %}} 
**APIの違いについて**: Python.NETでは、ブール値のプロパティはPascalCaseの代わりにsnake_case表記（`is_font_substitution_char_granularity`）を使用します。
{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
