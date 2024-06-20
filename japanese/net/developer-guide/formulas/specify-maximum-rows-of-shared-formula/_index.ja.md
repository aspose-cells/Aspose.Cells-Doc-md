---
title: 共有式の最大行数を指定
type: docs
weight: 40
url: /ja/net/specify-maximum-rows-of-shared-formula/
---

## **可能な使用シナリオ**

共有式のデフォルトの最大行数は 64 です。 任意の数を使用できます。たとえば、1000 にすることができます。共有式のパフォーマンスは、異なる行数を使用することによって変わります。したがって、Aspose.Cellsは、共有式の最大行数を指定するために使用できる [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) プロパティを提供しています。共有式の合計行数がそれを超える場合、共有式は複数の共有式に分割されます。

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **共有式の最大行数を指定**

以下のサンプルコードは、 [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) プロパティの使用方法について説明しています。それは共有式の最大行数を5に設定し、100行の共有式をセルD1に追加し、[出力Excelファイル](61767856.xlsx)に保存します。出力Excelファイルの内容を抽出して *sheet1.xml* を確認すると、前述のスクリーンショットでハイライトされているように、共有式が5行ごとに分割されていることがわかります。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
