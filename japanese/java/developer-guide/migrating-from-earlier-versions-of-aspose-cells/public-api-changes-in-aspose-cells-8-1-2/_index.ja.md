---
title: パブリック API Aspose.Cells の変更点 8.1.2
type: docs
weight: 70
url: /ja/java/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.1.1 から 8.1.2 への Aspose.Cells API の変更点について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **フォントの置換が発生した場合の警告のサポートを追加**
Aspose.Cells for Java 8.1.2 では、WarningInfo および WarningType クラス、IWarningCallback インターフェイス、SaveOptions.WarningCallback および ImageOrPrintOptions.WarningCallback プロパティが追加され、スプレッドシートを画像、XPS および PDF 形式に変換するときにフォントの置換が発生したときに開発者が警告を受け取ることができるようになりました。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[スプレッドシートのレンダリング中にフォントの置換に関する警告が表示される](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)詳細については。

{{% /alert %}}
## **古い PdfSaveOptions.ChartImageType プロパティを削除**
Aspose.Cells for Java 8.1.2 では、廃止された PdfSaveOptions.ChartImageType プロパティがパブリック API から削除されました。
