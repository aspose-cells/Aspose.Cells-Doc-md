---
title: Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する
type: docs
weight: 730
url: /ja/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、Microsoft Excelでワークブックを開いたときにOLEオブジェクトを更新するための[OleObject.AutoLoad](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#AutoLoad)プロパティを提供します。このプロパティにより、OLEオブジェクトはMicrosoft Excelによって生成された正しいOLEイメージが表示されます。

{{% /alert %}} 
## **Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する**
次のサンプルコードは、非実在のOLEイメージを含む[サンプルエクセルファイル](5473423.xlsx)をロードします。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルエクセルファイルではMicrosoft Wordのイメージの代わりに動物のイメージが表示されます。ただし、[出力エクセルファイル](5473429.xlsx)を開くと、Microsoft Excelが正しいOLEイメージを表示します。

次のスクリーンショットは、Microsoft Excelで開いた[サンプルエクセルファイル](5473423.xlsx)の外観を示しています。

![todo:image_alt_text](automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells_1.png)

次のスクリーンショットは、Microsoft Excelで開いた[出力エクセルファイル](5473429.xlsx)の外観を示しています。

![todo:image_alt_text](automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AutomaticallyrefreshOLEobject-AutomaticallyrefreshOLEobject.java" >}}
