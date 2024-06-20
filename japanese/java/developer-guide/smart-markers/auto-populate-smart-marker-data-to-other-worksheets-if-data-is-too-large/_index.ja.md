---
title: データが大きすぎる場合、他のワークシートにSmart Markerデータを自動的にポピュレートする
type: docs
weight: 10
url: /ja/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **可能な使用シナリオ**

時々、データソースが1500000のレコードを持っていて、単一のワークシートに収まりきらない場合、残りのレコードを次のワークシートに移動する必要があります。

## **データが大きすぎる場合、他のワークシートにスマートマーカーデータを自動的に埋め込む**

以下のサンプルコードには、21のレコードを持つデータソースが含まれています。1つのワークシートには15のレコードのみを表示し、残りのレコードは自動的に2番目のワークシートに移動します。2番目のワークシートにも同じスマートマーカータグが必要で、両方のシートに対して[**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean))メソッドを呼び出す必要があります。また、このコードで使用されている[Microsoft Accessデータベースファイル](60489777.accdb)とコードによって生成された[出力Excelファイル](60489786.xlsx)を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
