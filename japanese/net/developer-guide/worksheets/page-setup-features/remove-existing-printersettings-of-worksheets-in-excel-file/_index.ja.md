---
title: Excelファイルのワークシートの既存のPrinterSettingsを削除する方法
type: docs
weight: 60
url: /ja/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: この記事では、ページ設定オブジェクトを使用してExcelファイル内のワークシートの既存のPrinterSettingsをプログラムで削除する方法について、C# APIまたは.NETライブラリを使用したサンプルコードを紹介します。
keywords: ワークシートの .bin ファイルを保存されたXLSXファイルに含めないようにしたいときがあります。プリンター設定ファイルは 「[file "root"]\xl\printerSettings」 の下にあります。このドキュメントでは、Aspose.Cells APIを使用して既存のプリンター設定を削除する方法について説明します。
---

## **可能な使用シナリオ**
開発者は、保存されたXLSXファイルにプリンター設定の*.bin*ファイルを含めないようにすることを望むことがあります。プリンター設定ファイルは*「[file "root"]\xl\printerSettings」*の下にあります。この文書では、Aspose.Cells APIを使用して既存のプリンター設定を削除する方法について説明しています。
## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cellsを使用して、Excelファイルの異なるシートに指定された既存のプリンター設定を削除することができます。以下のサンプルコードは、ワークブック内のすべてのワークシートの既存のプリンター設定を削除する方法を示します。参考のために、[sample Excel file](45056020.xlsx)、[output Excel file](45056021.xlsx)、コンソール出力、およびスクリーンショットをご覧ください。
## **スクリーンショット**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **コンソール出力**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
