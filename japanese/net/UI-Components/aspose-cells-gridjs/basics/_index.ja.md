---
title: Aspose.Cells.GridJsの基本
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/basics/
---
## GridJの基礎

Aspose.Cells.GridJs は .NET 標準ライブラリで、スプレッドシートをすばやく簡単に表示/編集する Web アプリケーションを開発できます。

Aspose.Cells.GridJs は、一般的なスプレッドシート (XLS、XLSX、XLSM、XLSB、CSV、SpreadsheetML、ODS) ファイル形式のインポートをサポートしています。

また、Excel ファイルを PDF や HTML などにエクスポートすることもできます。以下は、GridJs の Web アプリケーションを開発するための基本的なプロセスの手順です。

- GridCacheForStream を実装して、キャッシュ ストレージ用の独自のビジネス ロジックを記述します。
- スプレッドシート ファイルから json を取得するコントローラー アクションを設定します。 GridJsWorkbook.ImportExcelFile および GridJsWorkbook.ExportToJson API を使用できます。GridJs はスプレッド ファイルを自動的にキャッシュに保存します。
- 更新操作の json を取得するコントローラー アクションを設定します。GridJsWorkbook.UpdateCell API を使用できます。GridJs はキャッシュで更新操作を実行し、更新された json を返します。
- スプレッドシートで画像/形状ファイルの URL を取得するコントローラー アクションを設定します。GridJs はキャッシュ内のすべての画像/形状を自動的に圧縮します。GridCacheForStream.GetFileUrl API を使用します。
- キャッシュ内のファイルを取得するコントローラー アクションを設定します。これにより、画像/形状の zip ファイルまたはスプレッドシート ファイルをキャッシュ内に取得できます。これは GridCacheForStream.LoadStream API を使用します。
- スプレッドシートをダウンロードするコントローラー アクションを設定します。GridJsWorkbook.SaveToCacheWithFileName API を使用できます。

以下は、Aspose.Cells.GridJs の使用法を示す基本的なデモです: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

質問、要件、またはサポートが必要な場合は、次の Web サイトにフィードバックしてください https://forum.aspose.com/c/cells/9