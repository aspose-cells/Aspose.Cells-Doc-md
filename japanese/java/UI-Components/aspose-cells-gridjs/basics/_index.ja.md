---
title: Aspose.Cells.GridJsの基礎
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: この記事では、GridJsのWebアプリケーションのセットアップの基本的な手順を紹介しています。
---

## GridJsの基礎

Aspose.Cells.GridJsは、ユーザーが簡単かつ迅速にスプレッドシートを表示/編集するための.NET標準ライブラリです。 

Aspose.Cells.GridJsは、人気のあるスプレッドシート（XLS、XLSX、XLSM、XLSB、CSV、SpreadsheetML、ODS）ファイル形式のインポートをサポートしています。

また、ExcelファイルをPDF、HTMLなどにエクスポートすることもできます。以下は、GridJsのWebアプリケーションを開発するための基本的な手順です。

- GridCacheForStreamを実装してキャッシュストレージのビジネスロジックを書きます。
- スプレッドシートファイルからJSONを取得するためのコントローラーアクションを設定します。GridJsWorkbook.ImportExcelFileおよびGridJsWorkbook.ExportToJson APIを使用でき、GridJsは自動的にスプレッドファイルをキャッシュに格納します。
- アップデート操作のためにJSONを取得するためのコントローラーアクションを設定します。GridJsWorkbook.UpdateCell APIを使用でき、GridJsはキャッシュでの更新操作を行い、更新されたJSONを返します。
- スプレッドシート内の画像/シェイプファイルのURLを取得するためのコントローラーアクションを設定します。GridJsは自動的にキャッシュ内のすべての画像/シェイプをZIP形式で圧縮します。GridCacheForStream.GetFileUrl APIを使用します。
- キャッシュ内のファイルを取得するためのコントローラーアクションを設定します。これにより、キャッシュ内の画像/シェイプのZIPファイルまたはスプレッドシートファイルを取得できます。GridCacheForStream.LoadStream APIを使用します。
- スプレッドシートをダウンロードするためのコントローラーアクションを設定します。GridJsWorkbook.SaveToCacheWithFileName APIを使用できます。

以下は、Aspose.Cells.GridJs の使用例の基本デモです：https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs


ご質問や要件、助けが必要な場合は、以下のウェブサイトにフィードバックしてください https://forum.aspose.com/c/cells/9
