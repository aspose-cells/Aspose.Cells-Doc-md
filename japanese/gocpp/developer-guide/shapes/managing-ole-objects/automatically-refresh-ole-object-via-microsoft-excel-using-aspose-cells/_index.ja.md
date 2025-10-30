---
title: Golangを使用したC++でMicrosoft ExcelのOLEオブジェクトを自動的にリフレッシュ
linktitle: 自動的にOLEオブジェクトを更新
type: docs
weight: 270
url: /ja/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aspose.Cellsを使用してGolangを用いたC++でMicrosoft Excel内のOLEオブジェクトを自動的にリフレッシュする方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft ExcelでExcelファイルを開いたときにOLEオブジェクトを更新する [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) プロパティを提供します。これにより、OLEオブジェクトはMicrosoft Excelが生成した正しいOLE画像を表示します。

{{% /alert %}}

次のサンプルコードは、非実際のOLE画像を持つ [サンプルExcelファイル](5115231.xlsx) をロードします。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルExcelファイルではMicrosoft Wordの画像の代わりに動物の画像を表示しています。ただし、[出力Excelファイル](5115225.xlsx)を開くと、Microsoft Excelが正しいOLE画像を表示しているのが確認できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
