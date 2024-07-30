---
title: 空のワークシートを検出する
type: docs
weight: 410
url: /ja/python-net/detecting-empty-worksheets/
description: Aspose.Cells for Python via .NETライブラリを使用して、Excelワークブックの空のワークシートをプログラムで検出する方法
keywords: Python Excelライブラリ、Pythonを使用した空のワークシートの検出、Pythonで空のExcelワークシートを検索します。
---

## **空の初期化されたセルのチェック**

ワークシートには、値が入力された1つ以上のセルがある場合があります。値は単純なもの（テキスト、数値、日付/時刻）または式または式に基づく値であることがあります。そのような場合、指定されたワークシートが空かどうかを検出することは簡単です。確認する必要があるのは、[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)または[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)プロパティのみです。上記のプロパティがゼロまたは正の値を返す場合、1つ以上のセルが埋められていることを意味します。ただし、これらのプロパティのいずれかが-1を返す場合、指定されたワークシートにセルが1つも埋められていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションは0から始まるインデックスを持っています。そのため、行0および列0のセルは、ワークシート内の最初のセルであるA1を意味します。

{{% /alert %}}

## **空の初期化されたセルのチェック**

値を持つすべてのセルは自動的に初期化されますが、ワークシートには書式のみが適用されたセルが含まれる可能性があります。そのようなシナリオでは、「[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)」または「[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)」プロパティが-1を返す可能性があります。これは、何らかの初期化された値がないことを示します。ただし、これにより初期化された空のセルは検出できません。「[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)」コレクションから取得した列挙子を使用してIEnumerator.MoveNextメソッドを確認することで、ワークシートに空の初期化されたセルがあるかどうかを確認できます。

## **図形のチェック**

特定のワークシートには、初期化されたセルが含まれていない可能性がありますが、コントロール、チャート、画像などのオブジェクトが含まれている可能性があります。ワークシートに形状が含まれているかどうかを確認する必要がある場合は、「[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)」要素を検査してください。正の値は、ワークシートに形状が存在することを示します。

## **プログラミングサンプル**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
