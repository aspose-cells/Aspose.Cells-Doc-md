---
title: Aspose.Cellsでのワークブックのフォーミュラ計算モードの設定
type: docs
weight: 100
url: /ja/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

Aspose.Cellsでも、FormulaSettings.CalculationModeプロパティを使用してフォーミュラの計算モードを設定できます。CalcModeType列挙型に以下の値の1つを割り当てることができます。

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

以下のサンプルコードはまずワークブックを作成し、次に式計算モードを**マニュアル**に設定し、ワークブックをディスク上の出力Excelファイルとして保存します。

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **実行例のダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
