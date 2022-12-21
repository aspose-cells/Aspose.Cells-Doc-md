---
title: ODS ファイルで背景を操作する
type: docs
weight: 150
url: /ja/net/working-with-background-in-ods-files/
---
## **ODS ファイルの背景**

ODS ファイルのシートに背景を追加できます。背景は、色付きの背景またはグラフィックの背景のいずれかです。ファイルが開いているときは背景は表示されませんが、ファイルを PDF として印刷すると、生成された PDF に背景が表示されます。背景は、印刷プレビュー ダイアログにも表示されます。

Aspose.Cells は、背景情報を読み取り、ODS ファイルに背景を追加する機能を提供します。

## **ODS ファイルから背景情報を読み取る**

Aspose.Cells は[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)ODS ファイルの背景を管理するクラス。次のコード サンプルは、[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)クラスをロードして[ソース ODS](90112030.ods)ファイルと背景情報の読み取り。コードによって生成されたコンソール出力を参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **コンソール出力**

背景タイプ: グラフィック

バックゴーランドの位置: CenterCenter

## **ODS ファイルに色付きの背景を追加する**

Aspose.Cells は[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)ODS ファイルの背景を管理するクラス。次のコード サンプルは、[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color)プロパティを使用して、ODS ファイルに色の背景を追加します。をご覧ください[出力 ODS](90112031.ods)参照用のコードによって生成されたファイル。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **グラフィック背景を ODS ファイルに追加する**

Aspose.Cells は[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)ODS ファイルの背景を管理するクラス。次のコード サンプルは、[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)グラフィック背景を ODS ファイルに追加するプロパティ。をご覧ください[出力 ODS](90112030.ods)参照用のコードによって生成されたファイル。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
