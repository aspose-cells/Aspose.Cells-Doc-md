---
title: ワークブックを読み込む際にVBAプロジェクトをフィルタリングする
type: docs
weight: 140
url: /ja/python-net/filter-vba-project-while-loading-a-workbook/
---

## **PythonでExcelワークブックの読み込み時にVBAプロジェクトをフィルタリング**

一部の.xlsm/.xlsbファイルには非常に多くのマクロ（またはとても長いマクロ）が含まれています。Aspose.Cells for Python via .NETは、これらのワークブックを開く際にこのメタデータを無条件でロードします。必要に応じて、[**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions)を使用して、シート名のみを抽出し、大量のワークブック間で不要な内容をスキップできるように制御することも可能です。このフィルタは、新しいオプションの[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)を導入することで提供されています。

## **サンプルコード**

以下のサンプルコードは、VBAのみがフィルタリングされたワークブックを読み込みます。この機能のテスト用に使用されるサンプルファイルを提供するリンクがあります。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

