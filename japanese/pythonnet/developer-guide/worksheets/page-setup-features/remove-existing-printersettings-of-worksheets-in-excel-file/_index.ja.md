---
title: Excelファイルのワークシートの既存のPrinterSettingsを削除する方法
type: docs
weight: 60
url: /ja/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: この記事では、Aspose.Cells for Python Excelライブラリを使用して、ページ設定オブジェクトを通じて既存のプリンタ設定をプログラム的に削除する方法をサンプルコードとともに学びます。
keywords: Python Excelライブラリを使い、Pythonでワークシートのプリンタ設定を削除します。
---

## **可能な使用シナリオ**
開発者の中には、保存されたXLSXファイルにプリンタ設定の **.bin* ファイルが含まれないようにしたい場合があります。プリンタ設定ファイルは *“[file "root"]\xl\printerSettings”* にあります。このドキュメントは、Aspose.Cells for Python via .NET APIを使用して既存のプリンタ設定を削除する方法を解説します。

## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cells for Python via .NETは、Excelファイル内の異なるシートに設定されたプリンタ設定を削除することを可能にします。以下のサンプルコードは、ブック内のすべてのワークシートの既存プリンタ設定を削除する方法を示します。参考として、それぞれの[サンプルExcelファイル](45056020.xlsx)、[出力Excelファイル](45056021.xlsx)、コンソール出力、スクリーンショットをご覧ください。

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
