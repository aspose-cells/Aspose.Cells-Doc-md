---
title: ODSファイルでの背景の処理
type: docs
weight: 170
url: /ja/java/working-with-background-in-ods-files/
---

## **ODSファイルでの背景**

ODSファイルのシートには背景を追加できます。背景には色の背景またはグラフィックの背景があります。ファイルが開いている場合は背景が表示されませんが、PDFとして印刷されると、背景が生成されたPDFに表示されます。また、印刷プレビューダイアログでも背景が表示されます。

Aspose.Cellsは、ODSファイルでの背景情報の読み取りと背景の追加機能を提供します。

## **ODSファイルからの背景情報の読み取り**

Aspose.Cellsは、ODSファイルでの背景を管理する [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) クラスを提供します。以下のコードサンプルでは、[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) クラスの使用を示し、[元のODS](GraphicBackground.ods) ファイルを読み込んで背景情報を読み込みます。コードによって生成されたコンソール出力も参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **コンソール出力**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **ODSファイルに色付きの背景を追加する**

Aspose.Cellsは、ODSファイルでの背景を管理する [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) クラスを提供します。以下のコードサンプルでは、[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) プロパティの使用を示し、ODSファイルに色付きの背景を追加します。コードによって生成された[出力ODS](ColoredBackground.ods) ファイルも参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **ODSファイルにグラフィックの背景を追加する**

Aspose.Cellsは、ODSファイルでの背景を管理する [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) クラスを提供します。以下のコードサンプルでは、[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) プロパティの使用を示し、ODSファイルにグラフィックの背景を追加します。コードによって生成された[出力ODS](GraphicBackground.ods) ファイルも参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
