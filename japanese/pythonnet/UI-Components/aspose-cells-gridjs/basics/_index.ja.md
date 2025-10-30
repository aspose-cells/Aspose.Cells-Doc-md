---
title: Aspose.Cells.GridJsの基礎
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## GridJsの基礎

Aspose.Cells.GridJsは、クロスプラットフォームのWebアプリケーションを迅速かつ簡単にスプレッドシートファイルを表示または編集するためのライブラリです。 

## Aspose.Cells.GridJsの利用目的


- リアルタイムのアップデート、数式サポート、リッチなデータ視覚化ツールを備えた、伝統的なデスクトップアプリケーションと同様のスプレッドシートの作成、編集、書式設定、共同作業、安全に共有する機能を提供します。
- データ入力と編集、書式設定、スプレッドシートのナビゲーション、数式計算、データ操作、チャートと視覚化、インポートとエクスポート、セキュリティ、アドオンおよびカスタマイズをサポートし、開発者がエディタを特定のビジネスニーズに合わせてカスタマイズする機能を提供します。

## 機能


- 人気のあるスプレッドシートフォーマットのインポート、表示、編集が可能です。
- スプレッドシートをサポートされるさまざまなファイル形式にエクスポートします。
- 画像や図形、グラフのファイルの表示および管理を行います。
- グリッドのデザインやレイアウトのカスタマイズを行います。
- 複数のワークシートを管理します。
- Excel®数式の作成と計算を行います。

## サポートされるファイルフォーマット

https://docs.aspose.com/cells/python-net/supported-file-formats/

## 一般的な使用方法

以下はGridJsのWebアプリケーションを開発するための基本的なプロセス手順です。

- Config.set_file_cache_directory(`保存パス`) でキャッシュ保存ディレクトリを設定します。
- Config.set_license(`ライセンスパス`) でライセンスを設定します。
- GridJsWorkbook.set_image_url_base(`画像表示用のルート`) で画像のルートURLを設定します。
- スプレッドシートファイルから`json`を取得するためのルートアクションを設定します。`GridJsWorkbook.ImportExcelFile`および`GridJsWorkbook.ExportToJson`のAPIを使用すると、`GridJs`が自動的にスプレッドファイルをキャッシュに保存します。
- 更新操作のための`json`を取得するためのルートアクションを設定します。`GridJsWorkbook.UpdateCell`のAPIを使用すると、`GridJs`がキャッシュ内で更新操作を行い、更新された`json`を返します。
- キャッシュ内のファイルを取得するためのルートアクションを設定します。これにより、キャッシュ内のイメージ/図形のZIPファイルまたはスプレッドシートファイルを取得できます。
- スプレッドシートをダウンロードするためのルートアクションを設定します。`GridJsWorkbook.SaveToCacheWithFileName`のAPIを使用できます。

以下はAspose.Cells.GridJsの使用例を示す基本デモです：

https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs

デモでは、クライアント側ページのレンダリングに[gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet)を使用しています。

ご質問や要件、助けが必要な場合は、以下のウェブサイトにフィードバックしてください https://forum.aspose.com/c/cells/9
