---
title: 共有式の最大行数を指定
type: docs
weight: 40
url: /ja/python-net/specify-maximum-rows-of-shared-formula/
---

## **可能な使用シナリオ**

共有式のデフォルト最大行数は64ですが、任意の数に設定可能です（例：1000）。共有式の行数がこれを超える場合、複数の共有式に分割されます。これを制御するためにAspose.Cells for Python via .NETは[**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula)プロパティを提供しています。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **共有式の最大行数を指定**

以下のサンプルコードは、 [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) プロパティの使用方法について説明しています。それは共有式の最大行数を5に設定し、100行の共有式をセルD1に追加し、[出力Excelファイル](61767856.xlsx)に保存します。出力Excelファイルの内容を抽出して *sheet1.xml* を確認すると、前述のスクリーンショットでハイライトされているように、共有式が5行ごとに分割されていることがわかります。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

