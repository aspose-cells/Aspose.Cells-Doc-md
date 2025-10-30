---
title: Golangを使ってC++でODSファイルの背景を操作する
linktitle: ODSファイルでの背景の処理
type: docs
weight: 150
url: /ja/go-cpp/working-with-background-in-ods-files/
description: Aspose.CellsとGolangを使ってC++でODSファイルの色付きおよびグラフィック背景を管理する方法を学ぶ
---

## **ODSファイルでの背景**

ODSファイルにシートに背景を追加することができます。背景は塗りつぶしの背景やグラフィック背景のいずれかです。この背景はファイルが開かれている場合は見えませんが、PDFとして印刷されると、PDFに背景が表示されます。背景は印刷プレビューダイアログにも表示されます。

Aspose.Cellsは、ODSファイルで背景情報を読み込み、背景を追加する機能を提供します。

## **ODSファイルの背景を読み込む**

Aspose.Cellsは、ODSファイルの背景を管理するために[**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)クラスを提供します。以下のコード例は、[**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)クラスを使用してソースODS([source ODS](90112030.ods))ファイルを読み込み、背景情報を取得する方法を示しています。コードによって生成されるコンソール出力を参考にしてください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **コンソール出力**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **ODSファイルに色付きの背景を追加する**

Aspose.Cellsは、ODSファイルの背景を管理するために[**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)クラスを提供します。次のコード例は、[**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/)プロパティを使用してODSファイルに色の背景を追加する方法を示しています。コードで生成された[出力ODS](90112031.ods)ファイルを参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **ODSファイルにグラフィックの背景を追加する**

Aspose.Cellsは、ODSファイルの背景を管理するために[**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)クラスを提供します。次のコード例は、[**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/)プロパティを使用してグラフィック背景をODSファイルに追加する方法を示しています。コードで生成された[出力ODS](90112030.ods)ファイルを参照してください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
