---
title: 範囲の管理
linktitle: 範囲
type: docs
weight: 105
url: /ja/python-net/managing-ranges/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して範囲を管理する方法を示しています。
keywords: Python Excelライブラリ、Pythonでの範囲の管理、Pythonでの範囲の作成、範囲のセルに値を挿入するPython、範囲のセルのスタイルを設定するPython、範囲のCurrentRegionを取得するPython。
---

## **紹介**

Excelでは、マウスボックス選択で複数のセルを選択することができ、選択されたセルのセットを「範囲」と呼びます。

たとえば、Excelのセル"A1"で左クリックしてからセル"C4"にドラッグすることができます。選択した長方形領域は、Aspose.Cells for Python via .NETを使用して簡単にオブジェクトとして作成することもできます。

範囲を作成し、値を設定し、スタイルを設定し、"範囲"オブジェクトにさらなる操作を行う方法

## **Aspose.Cells for Python Excelライブラリを使用した範囲の管理**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションを提供します。

## **範囲の作成方法**

A1:C4にまたがる長方形領域を作成する場合は、次のコードを使用できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **セルの範囲に値を入力する方法**

A1:C4に広がる一連のセルがあるとします。この行列は4 * 3 = 12のセルを含みます。個々の範囲セルは順次配置されています。

次の例は、範囲のセルに値を入力する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **セルの範囲のスタイルを設定する方法**

次の例は、セルの範囲のスタイルを設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **範囲のCurrentRegionの取得方法**

CurrentRegionは、現在の範囲を表すRangeオブジェクトを返すプロパティです。 

現在の領域は、空白の行と列の組み合わせによって囲まれた範囲です。読み取り専用です。

Excelでは、以下の方法でCurrentRegionエリアを取得できます:
1. マウスのボックスでエリア（範囲1）を選択します。
2. "ホーム - 編集 - 検索と選択 - 特殊に移動 - CurrentRegion"をクリックするか、"Ctrl+Shift+*"を使用します。するとExcelが自動的にエリア（範囲2）を選択してくれます。これで、範囲2は範囲1のCurrentRegionになります。

Aspose.Cells for Python via .NETでは、"Range.current_region"プロパティを使用して同じ機能を実行できます。

以下のテストファイルをダウンロードし、Excelで開き、マウスのボックスを使用して"A1:D7"のエリアを選択し、次に"Ctrl+Shift+*"をクリックすると、"A1:C3"のエリアが選択されます。

[current_region.xlsx](current_region.xlsx)

次に、以下の例を実行して、Aspose.Cells for Python via .NETでの動作を確認してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **高度なトピック**
- [ExcelファイルのAutoFill範囲](/cells/ja/python-net/autofill-ranges/)
- [Excelの範囲をコピー](/cells/ja/python-net/copy-ranges-of-excel/)
- [Excelの範囲のデータをコピーする](/cells/ja/python-net/copy-range-data-only/)
- [スタイルで範囲データをコピー](/cells/ja/python-net/copy-range-data-with-style/)
- [ソースの範囲の行の高さのみをコピー](/cells/ja/python-net/copy-range-style-only/)
- [ユニオン範囲の作成](/cells/ja/python-net/create-union-range/)
- [範囲を切り取って貼り付ける](/cells/ja/python-net/cut-and-paste-cells/)
- [範囲を削除する](/cells/ja/python-net/delete-ranges-from-excel/)
- [範囲のアドレス、セル数、オフセット、列全体、行全体を取得する](/cells/ja/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [範囲を挿入する](/cells/ja/python-net/insert-ranges-to-excel/)
- [セルの範囲を結合または結合解除する](/cells/ja/python-net/merge-or-unmerge-range-of-cells/)
- [ワークシート内のセルの範囲を移動する](/cells/ja/python-net/move-range-of-cells-in-a-worksheet/)
- [ワークブックおよびワークシートスコープの名前付き範囲を作成する](/cells/ja/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [範囲内のデータを検索および置換する](/cells/ja/python-net/search-and-replace-data-in-a-range/)

