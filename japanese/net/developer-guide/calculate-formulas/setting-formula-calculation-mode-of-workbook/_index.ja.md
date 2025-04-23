---
title: ワークブックの式の計算モードを設定する
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft Excelでブックの式計算モードを設定する方法について紹介しています。既存のExcelファイルを読み込むか新しいExcelファイルを作成し、Aspose.Cellsが提供するメソッドを使用して式計算モードを設定し、結果を取得することができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、ブック、式計算モード、設定
type: docs
weight: 110
url: /ja/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excelでは、フォーミュラ計算モード、つまりフォーミュラの計算方法を設定できます。3つの可能な値があります。

- 自動 - 何かが変更されるたびに再計算し、ワークブックが開かれるたびに再計算します。
- データテーブル以外自動 - 何かが変更されるたびに再計算しますが、データテーブルを除外します。
- マニュアル - ユーザーがF9またはCTRL+ALT+F9を押すか、ワークブックが保存されたときにのみ再計算します。

{{% /alert %}}

Microsoft Excelでの式計算モードを設定するには:

1. **式**、次に**計算オプション**を選択します。
1つのオプションを選択します。

Aspose.Cellsでは、**Formula Calculation Mode**を設定することもできます。 [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) モードプロパティを使用します。これに [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) 列挙型を割り当てることができます。この列挙型には次のいずれかの値が含まれています:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
