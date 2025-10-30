---
title: GolangをC++経由でワークブックの式計算モードを設定する
linktitle: ワークブックの式の計算モードを設定する
description: この記事では、C++とAspose.Cellsライブラリを使用してMicrosoft Excelでワークブックの数式計算モードを設定する方法を紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成し、Aspose.Cellsのメソッドを使用して計算モードを設定し、結果を取得します。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、ワークブック、数式計算モード、設定、C++
type: docs
weight: 110
url: /ja/go-cpp/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cellsでは、**Formula Calculation Mode**を設定することもできます。 [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getcalculationmode/) モードプロパティを使用します。これに [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) 列挙型を割り当てることができます。この列挙型には次のいずれかの値が含まれています:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaCalculationModeOfWorkbook.go" >}}
