---
title: 自動的にOLEオブジェクトを更新
type: docs
weight: 270
url: /ja/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、[**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load)プロパティを提供しており、Microsoft ExcelでExcelファイルを開いたときにOLEオブジェクトを更新します。このプロパティのおかげで、OLEオブジェクトはMicrosoft Excelによって生成された正しいOLE画像を表示します。

{{% /alert %}}

次のサンプルコードでは、実際のOLEイメージでないOLEオブジェクトを含む[サンプルExcelファイル](5115231.xlsx)を読み込みます。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルExcelファイルではMicrosoft Wordイメージの代わりに動物のイメージが表示されます。しかし、[出力Excelファイル](5115225.xlsx)を開くと、Microsoft Excelが正しいOLEイメージを表示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
