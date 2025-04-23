---
title: Excelファイルのワークシートの既存のPrinterSettingsを削除する方法
type: docs
weight: 40
url: /ja/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **可能な使用シナリオ**
開発者は、保存されたXLSXファイルで*.bin*ファイルを含めないようにすることがあります。プリンター設定ファイルは*「[file "root"]\xl\printerSettings」*の下にあります。このドキュメントでは、Aspose.Cells APIを使用して既存のプリンター設定を削除する方法について説明します。
## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cellsを使用して、Excelファイルの異なるシートに指定された既存のプリンター設定を削除することができます。次のサンプルコードは、ワークブック内のすべてのワークシートに対して既存のプリンター設定を削除する方法を示しています。[サンプルExcelファイル](45056023.xlsx)、[出力Excelファイル](45056024.xlsx)、コンソール出力、および参照用のスクリーンショットをご覧ください。
## **スクリーンショット**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **コンソール出力**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
