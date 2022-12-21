---
title: パブリック API Aspose.Cells の変更点 8.1.2
type: docs
weight: 60
url: /ja/net/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.1.1 から 8.1.2 への Aspose.Cells API の変更点について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **フォントの置換が発生した場合の警告のサポートを追加**
Aspose.Cells for .NET 8.1.2 では、WarningInfo、WarningType クラス、IWarningCallback インターフェイス、および SaveOptions.WarningCallback、ImageOrPrintOptions.WarningCallback プロパティが追加され、スプレッドシートを画像または PDF 形式に変換する際にフォントの置換が発生した場合に、ユーザーが警告を簡単に受け取ることができるようになりました。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[スプレッドシートのレンダリング中にフォントの置換に関する警告が表示される](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **古い PdfSaveOptions.ChartImageType プロパティを削除**
Aspose.Cells for .NET 8.1.2 では、廃止された PdfSaveOptions.ChartImageType プロパティがパブリック API から削除されました。
