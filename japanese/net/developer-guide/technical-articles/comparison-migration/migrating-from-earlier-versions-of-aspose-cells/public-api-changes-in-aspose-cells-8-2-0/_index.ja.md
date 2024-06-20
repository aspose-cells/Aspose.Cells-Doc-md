---
title: Aspose.Cells 8.2.0でのパブリックAPIの変更
type: docs
weight: 70
url: /ja/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.1.2から8.2.0へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの内部の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **CellsクラスのためのMultiThreadReadingプロパティが追加されました**
Aspose.Cells for .NET 8.2.0 で、Cells クラスに MultiThreadReading プロパティが追加されました。このプロパティは複数のスレッドで同時にセルの値を読み取るより強固なメカニズムを提供するためのものです。マルチスレッド アプリケーションで Boolean 型のプロパティを true に設定すると、各スレッドが正しいセルの値を受け取ることが保証されます。

{{% alert color="primary" %}} 

[マルチスレッド環境で同時にセルの値を読み取る](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) に関する詳細な記事をご確認ください

{{% /alert %}}
## **AutoFitRowsおよびAutoFitColumnsメソッドのオーバーロードを追加しました**
WorksheetクラスにAutoFitRowsおよびAutoFitColumnsの新しいオーバーロードが追加され、開発者はそれぞれの範囲に基づいて行と列を自動的にフィットさせることができるようになりました。AutoFitterOptionsクラスのインスタンスを渡すことができます。 

上記のメソッドのシグネチャは次の通りです:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

[行と列の自動調整](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns)の詳細記事をご確認ください。

{{% /alert %}}
