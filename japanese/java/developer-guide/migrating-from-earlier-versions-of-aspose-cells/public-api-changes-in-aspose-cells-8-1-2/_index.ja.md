---
title: Aspose.Cells 8.1.2でのパブリックAPIの変更
type: docs
weight: 70
url: /ja/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.1.1から8.1.2へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの内部の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **フォントの代替が発生した場合に警告が表示されるサポートが追加されました**
Aspose.Cells for Java 8.1.2では、スプレッドシートを画像、XPSおよびPDF形式に変換する際にフォントの代替が発生した場合に開発者が警告を受け取るためのWarningInfoおよびWarningTypeクラス、IWarningCallbackインターフェース、SaveOptions.WarningCallbackおよびImageOrPrintOptions.WarningCallbackプロパティが追加されました。 

{{% alert color="primary" %}} 

詳細な記事は[スプレッドシートのレンダリング中にフォントの代替に対する警告を取得](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)をご確認ください。

{{% /alert %}}
## **非推奨のPdfSaveOptions.ChartImageTypeプロパティが削除されました**
Aspose.Cells for Java 8.1.2では、公開APIから非推奨のPdfSaveOptions.ChartImageTypeプロパティが削除されました。
