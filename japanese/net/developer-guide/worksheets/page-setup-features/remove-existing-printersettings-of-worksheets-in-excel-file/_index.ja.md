---
title: Excel ファイルのワークシートの既存の PrinterSettings を削除する
type: docs
weight: 60
url: /ja/net/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **考えられる使用シナリオ**
開発者は、Excel が含まれないようにしたい場合があります。*。置き場*保存された XLSX ファイル内のプリンター設定のファイル。プリンター設定ファイルは次の場所にあります。*「[ファイル「ルート」]\xl\printerSettings」.*このドキュメントでは、Aspose.Cells API を使用して既存のプリンター設定を削除する方法について説明します。
## **Excel ファイルのワークシートの既存の PrinterSettings を削除する**
Aspose.Cells を使用すると、Excel ファイル内の異なるシートに指定されている既存のプリンター設定を削除できます。次のサンプル コードは、ブック内のすべてのワークシートの既存のプリンター設定を削除する方法を示しています。ご覧ください[サンプル Excel ファイル](45056020.xlsx), [出力エクセルファイル](45056021.xlsx)、コンソール出力、および参照用のスクリーンショット。
## **スクリーンショット**
![todo:画像_代替_文章](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **コンソール出力**
{{< highlight "java" >}}

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
