---
title: データが大きすぎる場合、他のワークシートにSmart Markerデータを自動的にポピュレートする
type: docs
weight: 50
url: /ja/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **可能な使用シナリオ**
時々、データソースが1500000レコードなど非常に多い場合、それを1つのワークシートに表示するのは不可能です。そのような場合には、残りのレコードを次のワークシートに移動することができます。 
## **データが大きすぎる場合、他のワークシートにSmart Markerデータを自動的にポピュレートする**
以下のサンプルコードには、21件のレコードを持つデータソースが含まれています。1つのワークシートには15件のみ表示し、残りのレコードは自動的に2番目のワークシートに移動します。なお、2番目のワークシートも同じSmartMarkerタグを持つ必要があり、両方のシートに対して[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) メソッドを呼び出す必要があります。生成された [出力Excelファイル](60489775.xlsx) も参照してください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
