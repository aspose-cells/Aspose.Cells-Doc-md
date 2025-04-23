---
title: ODSファイルでの背景の処理
type: docs
weight: 150
url: /ja/net/working-with-background-in-ods-files/
---

## **ODSファイルでの背景**

ODSファイルにシートに背景を追加することができます。背景は塗りつぶしの背景やグラフィック背景のいずれかです。この背景はファイルが開かれている場合は見えませんが、PDFとして印刷されると、PDFに背景が表示されます。背景は印刷プレビューダイアログにも表示されます。

Aspose.Cellsは、ODSファイルで背景情報を読み込み、背景を追加する機能を提供します。

## **ODSファイルの背景を読み込む**

Aspose.Cellsは、ODSファイルで背景を管理するための[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)クラスを提供します。以下のコードサンプルでは、[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)クラスを使用して[ソースのODS](90112030.ods)ファイルをロードし、背景情報を読み込んでいます。コンソール出力で生成される内容を参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **コンソール出力**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **ODSファイルに色付きの背景を追加する**

Aspose.Cellsは、ODSファイルで背景を管理するための[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)クラスを提供します。以下のコードサンプルでは、[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color)プロパティを使用してODSファイルに色の背景を追加しています。コードによって生成される[出力のODS](90112031.ods)ファイルを参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **ODSファイルにグラフィックの背景を追加する**

Aspose.Cellsは、ODSファイルで背景を管理するための[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)クラスを提供します。以下のコードサンプルでは、[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)プロパティを使用してODSファイルにグラフィック背景を追加しています。コードによって生成される[出力のODS](90112030.ods)ファイルを参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
