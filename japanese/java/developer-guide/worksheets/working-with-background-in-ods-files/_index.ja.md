---
title: ODS ファイルの背景の操作
type: docs
weight: 170
url: /ja/java/working-with-background-in-ods-files/
---
## **ODS ファイルの背景**

背景は、ODS ファイルのシートに追加できます。背景は、カラー背景またはグラフィック背景のいずれかです。ファイルが開いているときは背景は表示されませんが、ファイルが PDF として印刷される場合、背景は生成された PDF で表示されます。背景は印刷プレビュー ダイアログでも表示されます。

Aspose.Cells は、背景情報を読み取り、ODS ファイルに背景を追加する機能を提供します。

## **OSD ファイルから背景情報を読み取る**

Aspose.Cells は[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)ODS ファイルの背景を管理するクラス。次のコード サンプルは、[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)クラスをロードして[ソース ODS](GraphicBackground.ods)ファイルと背景情報の読み取り。コードによって生成されたコンソール出力を参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **コンソール出力**

背景タイプ: グラフィック

背景の位置: CENTER_CENTER

## **ODS ファイルに色付きの背景を追加**

Aspose.Cells は[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)ODS ファイルの背景を管理するクラス。次のコード サンプルは、[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)プロパティを使用して、ODS ファイルに色の背景を追加します。をご覧ください[出力 ODS](ColoredBackground.ods)参照用のコードによって生成されたファイル。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **グラフィック背景を ODS ファイルに追加**

Aspose.Cells は[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)ODS ファイルの背景を管理するクラス。次のコード サンプルは、[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)グラフィック背景を ODS ファイルに追加するプロパティ。をご覧ください[出力 ODS](GraphicBackground.ods)参照用のコードによって生成されたファイル。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
