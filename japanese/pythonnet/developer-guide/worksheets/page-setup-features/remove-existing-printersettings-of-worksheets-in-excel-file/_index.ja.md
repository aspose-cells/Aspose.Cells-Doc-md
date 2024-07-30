---
title: Excelファイルのワークシートの既存のPrinterSettingsを削除する方法
type: docs
weight: 60
url: /ja/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: この記事では、Aspose.Cells for Pythonエクセルライブラリを使用して、Excelファイル内のワークシートの既存のPrinterSettingsをプログラムでPage Setupオブジェクトを介して削除する方法についてのサンプルコードを提供します。
keywords: Pythonエクセルライブラリ、ワークシートのプリンタ設定を削除するPythonのサンプルコード、Excelワークシートのプリンタ設定を削除するPythonのサンプルコード。
---

## **可能な使用シナリオ**
時々開発者は、保存されたXLSXファイルに*.bin*ファイルのプリンタ設定が含まれないようにしたいと考えることがあります。プリンタ設定ファイルは*“[file "root"]\xl\printerSettings”*の下にあります。この文書では、Aspose.Cells for Python via .NET APIを使用して既存のプリンタ設定を削除する方法について説明します。

## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cells for Python via .NETを使用すると、Excelファイル内の異なるシートに指定された既存のプリンタ設定を削除できます。次のサンプルコードは、ワークブックのすべてのワークシートの既存のプリンタ設定を削除する方法を示しています。参考のために、[サンプルExcelファイル](45056020.xlsx)、[出力Excelファイル](45056021.xlsx)、コンソールの出力、およびスクリーンショットもご覧ください。

## **スクリーンショット**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
