---
title: Xamarin による iOS の場合は Aspose.Cells の制限事項と API の相違点
type: docs
weight: 10
url: /ja/net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---
## Xamarin 経由の iOS 用の Aspose.Cells の最新バージョンは、古い Xamarin.iOS バージョンでは動作しない場合があります
Xamarin 経由の iOS 用の Aspose.Cells は、常に Xamarin および Xamarin.iOS プラットフォームの最新の安定したバージョンを使用してビルドされることに注意してください。 Xamarin.Android アプリケーションで Xamarin 経由で iOS 用の Aspose.Cells を使用しているときに問題が発生した場合は、最新の Xamarin および Xamarin.iOS バージョンがインストールされていることを確認してください。 Xamarin 経由の iOS 用の Aspose.Cells は、Xamarin の古いバージョンでは機能しない最新の Xamarin (Xamarin.iOS) バージョンを使用してビルドされることがあります。
## Xamarin を介した iOS の場合は Aspose.Cells
- 画像の挿入 - サポートされていません。
- グラフの作成 - サポートされていません。
- グラデーション背景の設定 - サポートされていません。
- セルへのコメントの追加 - サポートされていません。
- データ検証の実装 - サポートされていません。
- カスタム改ページの作成 - サポートされていません。
- スマート マーカーの実装 - サポートされていません。
- ワークシートの保護/保護解除 - サポートされていません。
- Excel XP 以降のバージョンで導入された高度な保護オプションの指定 - サポートされていません。
- フォーム コントロールおよびその他の描画図形/オブジェクトの挿入 - サポートされていません。
- ピボット テーブルとピボット チャートの作成 - サポートされていません。
- アドイン、VBA、マクロの保持または削除 - サポートされていません。
- 転置オプションの実装 - サポートされていません。
- カスタム グラフの作成 - サポートされていません。
- スプレッドシートからの OLE オブジェクトの追加、保持、または抽出 - サポートされていません。
- Microsoft Excel 2010 スパーク ラインの実装 - サポートされていません。
- ファイルの暗号化 - サポートされていません。
## Public API (名前空間) の違い
Xamarin 経由の iOS の Aspose.Cells では、.NET API の System.Drawing の代わりに Aspose.Cells.Drawing 名前空間が使用されます。影響を受けるオブジェクトのリストは次のとおりです。

- Aspose.Cells.Drawing.Color
- Aspose.Cells.Drawing.ColorConverter
- Aspose.Cells.Drawing.ColorTranslator
- Aspose.Cells.Drawing.FontStyle
- Aspose.Cells.Drawing.GraphicsUnit
- Aspose.Cells.Drawing.ImageFormatConverter
- Aspose.Cells.Drawing.KnownColor
- Aspose.Cells.Drawing.KnownColors
- Aspose.Cells.Drawing.Locale
- Aspose.Cells.Drawing.SystemColors
- Aspose.Cells.Drawing.Imaging.PixelFormat
- Aspose.Cells.Drawing.Imaging.ImageFormat
- Aspose.Cells.Drawing.Imaging.ImageFlags
- Aspose.Cells.Drawing.Drawing2D.SmoothingMode
- Aspose.Cells.Drawing.Drawing2D.PathPointType
- Aspose.Cells.Drawing.Drawing2D.PathData
- Aspose.Cells.Drawing.Drawing2D


