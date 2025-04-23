---
title: ワークブックを読み込む際にVBAプロジェクトをフィルタリングする
type: docs
weight: 140
url: /ja/net/filter-vba-project-while-loading-a-workbook/
---

## **C#でExcelワークブックを読み込む際にVBAプロジェクトをフィルタリングする**

.xlsm/.xslbファイルの一部は非常に多くのマクロ（または非常に長いマクロ）を含んでいます。 Aspose.Cellsはこのようなワークブックを開く際にこの（メタ）データを無条件でロードします。そうした不要なコンテンツをスキップして複数のワークブックのシート名のみを抽出する必要がある場合は、[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)でこれを制御する必要があります。このフィルタは、[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)を導入することで提供されます。

## **サンプルコード**

以下のサンプルコードは、VBAのみがフィルタリングされたワークブックを読み込みます。この機能のテスト用に使用されるサンプルファイルを提供するリンクがあります。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
