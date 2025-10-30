---
title: GolangをC++経由で使用してデータテーブルの配列式を計算する
linktitle: データテーブルの配列式の計算
description: GolangをC++経由でAspose.Cellsライブラリを使用してMicrosoft Excelのデータテーブルの配列式を計算する方法。既存のExcelファイルを読み込むか、新規のExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用してデータテーブルの配列式を計算し、結果を取得します。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、データテーブル、配列数式、計算、C++
type: docs
weight: 70
url: /ja/go-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft Excelでデータテーブルを作成するには、データ > 何れかの分析 > データテーブル... を使用します。 Aspose.Cellsでは今、データテーブルの配列式を計算することができます。任意のタイプの数式を計算するために通常通り [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) を使用してください。

{{% /alert %}}

次のサンプルコードでは、[元のExcelファイル](5115535.xlsx) を使用しました。セルB1の値を100に変更すると、黄色で塗られたデータテーブルの値が120になる様子が次の画像で示されます。サンプルコードは、[出力PDF](5115538.pdf) を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下は[元のExcelファイル](5115535.xlsx) から[出力PDF](5115538.pdf) を生成するために使用されたサンプルコードです。詳細についてはコメントをお読みください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfArrayFormulaOfDataTables.go" >}}
