---
title: Excel を Word に変換する
type: docs
weight: 300
url: /ja/python-java/convert-excel-to-word/
description: Python を使用して、Excel ファイルをワードに変換する
keywords: Office 2013、Office 2016、Office 2019、および Office 365 なしで Word にワークブックをエクスポートする
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java は、Excel (.xls、xlsx、.xlsb、xlsm)、CSV、および OpenOffice (.ods) ファイルをワードファイルに変換する機能をサポートしています。

{{% /alert %}}

## **Excel Workbook を Word に変換する**

Excel Workbook を Word に変換する方法について疑問に思う必要はありません。なぜなら、Aspose.Cells for Python via Java ライブラリには最高の手段が用意されているからです。Aspose.Cells for Python via Java API では、スプレッドシートをワード形式に変換するサポートが提供されています。ワークブックをワードにエクスポートするには、第 2 パラメータとして [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) を [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)) メソッドに渡します。また、ワークシートを .docx ファイルにエクスポートする際には、追加の設定を指定するために [**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions) クラスを使用することもできます。

以下のコード例は、Excel Workbook を Word にエクスポートする方法を示しています。参照のためにコードを確認して、[ソースファイル](sample.xlsx) をワードファイルに変換するコードを参照してください。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


