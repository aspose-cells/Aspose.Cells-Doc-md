---
title: ODSファイルでの背景の処理
type: docs
weight: 150
url: /ja/python-net/working-with-background-in-ods-files/
description: Python via .NET APIを使用したODSファイルで背景を操作する方法。
keywords: PythonでODSファイルで背景を操作する方法、ODSファイルから背景情報を読み取る方法、Python via NETを使用してODSファイルに色付き背景を追加する方法、Python via NETを使用してODSファイルにグラフィック背景を追加する方法。
---

## **ODSファイルでの背景**

ODSファイルにシートに背景を追加することができます。背景は塗りつぶしの背景やグラフィック背景のいずれかです。この背景はファイルが開かれている場合は見えませんが、PDFとして印刷されると、PDFに背景が表示されます。背景は印刷プレビューダイアログにも表示されます。

Python via .NETでは、背景情報を読み取り、ODSファイルに背景を追加する機能が提供されています。

## **ODSファイルの背景を読み込む**

Aspose.Cells for Python via .NETは、ODSファイルで背景を管理するための[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)クラスを提供します。[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)クラスを使用した以下のコードサンプルでは、[source ODS](90112030.ods)ファイルを読み込み、背景情報を読み取ります。参考のためにコードによって生成されたコンソール出力をご覧ください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **コンソール出力**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **ODSファイルに色付きの背景を追加する**

Aspose.Cells for Python via .NETは、ODSファイルで背景を管理するための[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)クラスを提供します。[**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/)プロパティを使用して、ODSファイルに色付き背景を追加する以下のコードサンプルをご覧ください。コードによって生成された[output ODS](90112031.ods)ファイルを参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **ODSファイルにグラフィックの背景を追加する**

Aspose.Cells for Python via .NETは、ODSファイルで背景を管理するための[**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)クラスを提供します。[**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/)プロパティを使用して、ODSファイルにグラフィック背景を追加する以下のコードサンプルをご覧ください。コードによって生成された[output ODS](90112030.ods)ファイルを参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
