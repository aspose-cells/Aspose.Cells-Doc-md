---
title: データテーブルの配列式の計算
description: Microsoft Excelのデータテーブルで配列式を計算するためにAspose.Cellsライブラリを使用する方法について説明します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成することで、Aspose.Cellsが提供するメソッドを使用してデータテーブルの配列式を計算し、結果を取得できます。最後に変更されたExcelファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, データテーブル、配列式、計算
type: docs
weight: 70
url: /ja/net/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft Excelでデータテーブルを作成するには、データ > 何れかの分析 > データテーブル... を使用します。 Aspose.Cellsでは今、データテーブルの配列式を計算することができます。任意のタイプの数式を計算するために通常通り [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) を使用してください。

{{% /alert %}}

次のサンプルコードでは、[元のExcelファイル](5115535.xlsx) を使用しました。セルB1の値を100に変更すると、黄色で塗られたデータテーブルの値が120になる様子が次の画像で示されます。サンプルコードは、[出力PDF](5115538.pdf) を生成します。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下は[元のExcelファイル](5115535.xlsx) から[出力PDF](5115538.pdf) を生成するために使用されたサンプルコードです。詳細についてはコメントをお読みください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
