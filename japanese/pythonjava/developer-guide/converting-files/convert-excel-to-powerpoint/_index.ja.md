---
title: ExcelをPowerPointに変換
type: docs
weight: 300
url: /ja/python-java/convert-excel-to-powerpoint/
description: Pythonを使用してExcelファイルをPPTに変換します。
keywords: Office 2013、Office 2016、Office 2019、およびOffice 365なしでワークブックをスライドにエクスポートする
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Javaは、Excel（.xls、.xlsx、.xlsb、xlsm）、CSV、およびOpenOffice（.ods）ファイルをPowerPointファイルに変換する操作をサポートしています。

{{% /alert %}}

## **ExcelワークブックをPPTに変換します**

ExcelワークブックをPowerPointに変換する必要があるときは、Aspose.Cells for Python via Javaライブラリに最適な決定があります。 Aspose.Cells for Python via Java APIは、スプレッドシートをPowerPoint形式に変換するサポートを提供します。ワークブックをPowerPointにエクスポートするには、[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\))メソッドの第2パラメータとして[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)を渡します。.pptxファイルにワークシートをエクスポートするための追加設定を指定するには、[**PptxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/PptxSaveOptions)クラスも使用できます。

以下のコード例は、Excel Workbook を PPT にエクスポートする方法を示しています。参照のためにコードを確認して、[ソースファイル](sample.xlsx) をワードファイルに変換するコードを参照してください。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Pptx.py" >}}


