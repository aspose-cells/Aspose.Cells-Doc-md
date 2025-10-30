---
title: GolangとC++を使ってワークブックの読み込み中にVBAプロジェクトをフィルターする
linktitle: ワークブックを読み込む際にVBAプロジェクトをフィルタリングする
type: docs
weight: 140
url: /ja/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Aspose.CellsとGolangを使ってExcelワークブックの読み込み時にVBAプロジェクトをフィルタリングする方法
---

## **Excelワークブックの読み込み時にVBAプロジェクトをフィルタリング（C++）**

一部の.xlsm/.xslbファイルには非常に大量のマクロ（または非常に長いマクロ）が含まれている場合があります。Aspose.Cellsは、そのようなワークブックを開く際に無条件でメタデータを読み込みます。ただし、多数のワークブックからシート名のみ抽出したい場合は、[**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions)を使用して制御し、不要なコンテンツをスキップできます。このフィルターは、新しいオプション[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions)を導入することで提供されます。

## **サンプルコード**

以下のサンプルコードは、VBAのみがフィルタリングされたワークブックを読み込みます。この機能のテスト用に使用されるサンプルファイルを提供するリンクがあります。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
