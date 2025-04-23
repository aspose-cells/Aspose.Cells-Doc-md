---
title: Aspose.Cells 8.2.0でのパブリックAPIの変更
type: docs
weight: 80
url: /ja/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.1.2から8.2.0へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの内部の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **CellsクラスのためのMultiThreadReadingプロパティが追加されました**
Aspose.Cells for Java 8.2.0では、複数スレッドでセルの値を同時に読み取るためのより堅牢なメカニズムを提供するために、CellsクラスにMultiThreadReadingプロパティが追加されました。マルチスレッドアプリケーションでブール型のプロパティをtrueに設定すると、各スレッドが正しいセルの値を受信することが保証されます。

{{% alert color="primary" %}} 

詳細な記事は[マルチスレッド環境での同時にセル値を読み取る](/cells/ja/java/reading-cell-values-in-multiple-threads-simultaneously/)をご確認ください。

{{% /alert %}}
## **autoFitRowsおよびautoFitColumnsメソッドへのオーバーロードが追加されました**
Worksheetクラスに新しいautoFitRowsおよびautoFitColumnsのオーバーロードが追加され、AutoFitterOptionsクラスのインスタンスを渡すことで、それぞれの範囲に基づいて行および列を自動調整することが可能になりました。 

上記のメソッドのシグネチャは次の通りです:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

詳細な記事は[行および列の自動調整](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns)をご確認ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
