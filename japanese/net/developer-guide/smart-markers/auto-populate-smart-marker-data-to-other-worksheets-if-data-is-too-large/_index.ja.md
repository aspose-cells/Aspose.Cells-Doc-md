---
title: データが大きすぎる場合、スマート マーカー データを他のワークシートに自動入力
type: docs
weight: 50
url: /ja/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **考えられる使用シナリオ**
スマート マーカー データが大きすぎる場合に、他のワークシートに自動入力したい場合があります。データ ソースに 1500000 レコードがあるとします。これらは 1 つのワークシートのレコードが多すぎるため、残りのレコードを次のワークシートに移動できます。
## **データが大きすぎる場合、スマート マーカー データを他のワークシートに自動入力する**
次のサンプル コードには、21 個のレコードを持つデータ ソースがあります。 1 つのワークシートに 15 レコードのみを表示したい場合、残りのレコードは自動的に 2 番目のワークシートに移動します。 2 番目のワークシートにも同じスマート マーカー タグが必要であり、呼び出す必要があることに注意してください。[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2)両方のシートの方法。をご覧ください[出力エクセルファイル](60489775.xlsx)参照用のコードによって生成されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
