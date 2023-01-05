---
title: エクセルをワードに変換
type: docs
weight: 300
url: /ja/python-java/convert-excel-to-word/
description: Python を使用して Excel ファイルを Word に変換します。
keywords: Exporting Workbook to word without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells for Python via Java は、Excel (.xls、xlsx、.xlsb、xlsm)、CSV、OpenOffice (.ods) ファイルの Word ファイルへの変換をサポートしています。

{{% /alert %}}

## **Excel ブックを Word に変換する**

Aspose.Cells for Python via Java ライブラリが最適な決定を下すため、Excel ワークブックを Word に変換する方法を考える必要はありません。 Aspose.Cells for Python via Java API は、スプレッドシートを Word 形式に変換するためのサポートを提供します。ブックを Word にエクスポートするには、次を渡します。[**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)の 2 番目のパラメータとして[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ） 方法。使用することもできます[**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions)クラスを使用して、ワークシートを .docx ファイルにエクスポートするための追加設定を指定します。

次のコード例は、Excel ブックを Word にエクスポートする方法を示しています。変換するコードを参照してください[ソースファイル](sample.xlsx)参照用のコードによって生成された Word ファイルに。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


