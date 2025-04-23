---
title: 空のワークシートを検出する
type: docs
weight: 410
url: /ja/python-net/detecting-empty-worksheets/
description: この記事では、Aspose.Cells for Python via .NETライブラリを使用してExcelワークブックの空のワークシートをプログラムで検出する方法についてのコードを紹介します。
keywords: Python Excelライブラリ、pythonを使用した空のワークシートの検出、pythonで空のExcelワークシートを見つける方法。
---

## **空の初期化されたセルのチェック**

ワークシートには、値が入力された1つ以上のセルがある場合があります。値は単純なもの（テキスト、数値、日付/時刻）または式または式に基づく値であることがあります。そのような場合、指定されたワークシートが空かどうかを検出することは簡単です。確認する必要があるのは、[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)または[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)プロパティのみです。上記のプロパティがゼロまたは正の値を返す場合、1つ以上のセルが埋められていることを意味します。ただし、これらのプロパティのいずれかが-1を返す場合、指定されたワークシートにセルが1つも埋められていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションは0から始まるインデックスを持っています。そのため、行0および列0のセルは、ワークシート内の最初のセルであるA1を意味します。

{{% /alert %}}

## **空の初期化されたセルのチェック**

値を持つセルは自動的に初期化されますが、ワークシートに書式だけが適用されたセルが存在する可能性もあります。その場合、[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)または[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)プロパティは-1を返し、値が設定されていないことを示します。ただし、セルの書式設定により初期化されたセルも検出できないため、ワークシートに空の初期化されたセルがあるかどうかを確認するには、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションから取得した列挙子のIEnumerator.MoveNextメソッドを使用してください。このメソッドが**true**を返す場合、そのワークシートには1つ以上の初期化されたセルが存在します。

## **図形のチェック**

特定のワークシートに値が設定されていない場合でも、コントロールやチャート、画像などのシェイプやオブジェクトが含まれている可能性があります。ワークシートにシェイプが含まれているかどうかを確認するには、[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)要素を調べます。正の値はシェイプが存在することを示します。

## **プログラミングサンプル**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
