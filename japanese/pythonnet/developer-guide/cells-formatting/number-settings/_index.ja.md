---
title: 数字の設定
description: Aspose.Cellsは、セル番号設定を多様にサポートするスプレッドシート操作用Pythonライブラリです。この記事では、Aspose.Cellsライブラリを利用してセルの番号形式を管理し、必要に応じてスプレッドシート内の番号フォーマットを調整する方法を紹介します。
keywords: Aspose.Cells、Pythonライブラリ、電子スプレッドシート、セル番号設定、書式設定、管理、ナンバーと日付のフォーマット
type: docs
weight: 10
url: /ja/python-net/cells-number-settings/
---

## **数字と日付の表示形式を設定する方法**

Microsoft Excelの非常に強力な機能の1つは、ユーザーが数値値や日付の表示形式を設定できることです。数値データは10進数、通貨、パーセンテージ、分数、会計などを含むさまざまな値を表すために使用できることを知っています。すべてのこれらの数値値は、それが表す情報の種類に応じて異なる形式で表示されます。同様に、日付や時刻を表示するための多くの形式があります。
Aspose.Cells for Python via .NETは、この機能をサポートしており、開発者が数字や日付の表示形式を任意に設定できます。

### **Microsoft Excelで表示形式を設定する方法**

Microsoft Excelで表示形式を設定するには：

1. 任意のセルを右クリックします。
1. **セルの書式設定** を選択します。ダイアログが表示され、さまざまな種類の値の表示形式を設定するのに使用されます。

ダイアログの左側には、**標準**, **数値**, **通貨**, **会計**, **日付**, **時刻**, **パーセンテージ**など、多くの値のカテゴリがあります。Aspose.Cells for Python via .NETはこれらすべての表示フォーマットをサポートしています。

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションの各アイテムは[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスのオブジェクトを表します。

Aspose.Cells for Python via .NETは、[**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)および[**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)メソッドを提供します。これらのメソッドはセルの書式設定を取得および設定するために使用されます。[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)クラスは、数字や日付の表示形式を扱うための便利なプロパティをいくつか提供します。

### **組み込みの数値形式の使用方法**

Aspose.Cells for Python via .NETは、数値や日付の表示形式を設定するための組み込みの数値形式を提供しています。これらの組み込み数値形式は、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトの [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) プロパティを使用して適用できます。すべての組み込み数値形式には一意の数値値が付与されています。開発者は、表示形式を適用するために [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) プロパティに任意の数値値を割り当てることができます。この方法は高速です。Aspose.Cellsがサポートする組み込みの数値形式は以下の通りです。

|**値**|**タイプ**|**フォーマット文字列**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **カスタム数値形式の使用方法**

表示形式を設定するために独自のカスタムフォーマット文字列を定義するには、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)オブジェクトの[**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)プロパティを使用します。この方法は事前に設定された形式を使用するよりも速くはありませんが、柔軟性があります。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

[**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)プロパティを使用して数値形式を設定する場合、[**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)プロパティを使用して設定された以前の形式は上書きされ、その逆も同様です。

{{% /alert %}}

## **高度なトピック**
- [Style.Customプロパティを設定する際のカスタム数値形式を確認する](/cells/ja/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [サポートされている数値形式のリスト](/cells/ja/python-net/list-of-supported-number-formats/)
- [カスタム日付形式パターン g および ge mm dd の表現](/cells/ja/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [ブックでのカスタム数値小数点およびグループの区切りの指定](/cells/ja/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [DBNumカスタムパターンの書式設定の指定](/cells/ja/python-net/specifying-dbnum-custom-pattern-formatting/)

{{< app/cells/assistant language="python-net" >}}
