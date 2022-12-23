---
title: Excel を PowerPoint に変換
type: docs
weight: 300
url: /ja/python-java/convert-excel-to-powerpoint/
description: Python を使用して Excel ファイルを PPT に変換します。
keywords: Exporting Workbook to slide without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells for Python via Java は、Excel (.xls、xlsx、.xlsb、xlsm)、CSV および OpenOffice (.ods) ファイルから PowerPoint ファイルへの変換をサポートしています。

{{% /alert %}}

## **ExcelワークブックをPPTに変換**

Aspose.Cells for Python via Java ライブラリが最適な決定を行うため、Excel ワークブックを PowerPoint に変換する方法を考える必要はありません。 Aspose.Cells for Python via Java API は、スプレッドシートを PowerPoint 形式に変換するためのサポートを提供します。ワークブックを PowerPoint にエクスポートするには、次を渡します。[**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)の 2 番目のパラメータとして[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ） 方法。使用することもできます[**PptxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/PptxSaveOptions)クラスを使用して、ワークシートを .pptx ファイルにエクスポートするための追加設定を指定します。

次のコード例は、Excel ワークブックを PPT にエクスポートする方法を示しています。変換するコードを参照してください[ソースファイル](sample.xlsx)参照用のコードによって生成された Word ファイルに。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Pptx.py" >}}


