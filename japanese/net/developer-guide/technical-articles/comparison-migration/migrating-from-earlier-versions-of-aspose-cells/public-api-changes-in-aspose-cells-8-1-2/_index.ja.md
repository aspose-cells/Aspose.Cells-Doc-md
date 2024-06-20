---
title: Aspose.Cells 8.1.2でのパブリックAPIの変更
type: docs
weight: 60
url: /ja/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.1.1から8.1.2へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの内部の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **フォントの代替が発生した場合に警告が表示されるサポートが追加されました**
Aspose.Cells for .NET 8.1.2では、WarningInfo、WarningTypeクラス、IWarningCallbackインターフェース、SaveOptions.WarningCallback、ImageOrPrintOptions.WarningCallbackプロパティが追加され、スプレッドシートを画像やPDF形式に変換する際にフォントの置換が発生した場合にユーザーが警告を受け取る機能が提供されます。 

{{% alert color="primary" %}} 

[Excel ファイルをレンダリングする際のフォントの置換に関する警告を取得する](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) の詳細な記事をご確認ください

{{% /alert %}}
## **非推奨のPdfSaveOptions.ChartImageTypeプロパティが削除されました**
Aspose.Cells for .NET 8.1.2 で、公開 API から非推奨の PdfSaveOptions.ChartImageType プロパティが削除されました。
