---
title: Aspose.Cells 8.2.1でのパブリックAPIの変更
type: docs
weight: 80
url: /ja/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.2.0から8.2.1へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの内部の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **CellクラスにGetValidation()メソッドを追加しました**
データ検証は、スプレッドシートデザイナーが特定のセルに無効な値を挿入するのを防ぐために使用する機能の一つです。Aspose.Cells for .NET 8.2.1では、セルにデータ検証が適用されているかどうかを特定するシンプルなメカニズムを公開しています。CellクラスのGetValidationメソッドを使用して適用された検証を取得できます。検証が適用されていない場合、nullが返されます。同様に、ValidationCollectionクラスのGetValidationInCellメソッドを使用して、行と列のインデックスを指定してセルに適用された検証を取得できます。

{{% alert color="primary" %}} 

詳細については、[セルに適用された検証を取得](/cells/ja/net/get-validation-applied-on-a-cell/)の詳細記事をご確認ください。

{{% /alert %}}
## **CellクラスにGetValidationValue()メソッドを追加しました**
適用された検証を確認するだけでなく、特定のセルのデータ検証ルールを満たす値かどうかも確認できます。この機能は、セルに入力された値がデータ検証ルールを満たすかどうかをリアルタイムで確認したい場合に役立ちます。Aspose.Cells APIは、CellクラスのGetValidationValueメソッドを公開しました。セルに入力された値がデータ検証ルールを満たさない場合、CellクラスのGetValidationValueメソッドはfalseを返します。

{{% alert color="primary" %}} 

詳細については、[セルの値がデータ検証ルールを満たすかどうかを確認](/cells/ja/net/verify-that-cell-value-satisfies-data-validation-rules/)の詳細記事をご確認ください。

{{% /alert %}}
## **WorkbookRenderクラスのToPrinter(PrinterSettings printerSettings)メソッドにオーバーロードが追加されました**
オーバーロードされたメソッドを使用して、PrinterSettingsを介してワークブックをプリンタにレンダリングすることが可能です。
{{< app/cells/assistant language="csharp" >}}
