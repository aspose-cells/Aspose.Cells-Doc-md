---
title: WorkbookSetting.StreamProvider を使用して外部リソースを制御する
type: docs
weight: 10
url: /ja/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **可能な使用シナリオ**
Excelファイルにリンクされた画像などの外部リソースが含まれる場合があります。Aspose.Cellsを使用すると、[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)を使用してこれらの外部リソースを制御できます。これには、[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)インターフェースの実装を取る[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)が使用されます。リンクされた画像などの外部リソースを含むワークシートをレンダリングしようとすると、[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)インターフェースのメソッドが呼び出され、外部リソースに適切な操作を実行することが可能になります。
## **[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)を使用して外部リソースを制御する**
次のサンプルコードは、[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)の使用方法を説明しています。リンクされた画像を含む[sample Excel file](61767877.xlsx)をロードします。コードはリンクされた画像を[Aspose Logo](61767874.png)で置き換え、[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)クラスを使用してシート全体を1つのイメージにレンダリングします。次のスクリーンショットは、サンプルExcelファイルと参照用の[レンダリングされた出力イメージ](61767874.png)を示しています。リンクされた画像がAspose Logoで置き換わっていることがわかります。

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
