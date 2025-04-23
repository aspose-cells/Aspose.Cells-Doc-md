---
title: Aspose.Cells 8.2.1でのパブリックAPIの変更
type: docs
weight: 90
url: /ja/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.2.0から8.2.1へのAPIの変更について説明しており、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの内部の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **CellクラスのgetValidation()メソッドが追加されました**
データ検証は、スプレッドシートの設計者が特定のセルに無効な値を挿入するのを止めるために使用する機能の一つです。Aspose.Cells for Java 8.2.1では、CellクラスのgetValidationメソッドを使用して、セルに適用されたデータ検証を取得する簡単なメカニズムが公開されました。検証が適用されていない場合、メソッドはnullを返します。同様に、ValidationCollectionクラスのgetValidationInCellメソッドを使用して、行と列のインデックスを指定して任意のセルに適用された検証を取得することが可能です。

{{% alert color="primary" %}} 

詳細な記事は[セルに適用された検証を取得](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/)をご確認ください。

{{% /alert %}}
## **CellクラスのgetValidationValue()メソッドが追加されました**
適用されている検証があるかどうかを確認するだけでなく、特定のセルのデータ検証ルールを満たすかどうかを検証することも可能です。Aspose.Cells APIでは、CellクラスのgetValidationValueメソッドが公開されています。セルに入力された値がデータ検証ルールを満たさない場合、CellクラスのgetValidationValueメソッドはfalseを返します。

{{% alert color="primary" %}} 

詳細な記事は[セルの値がデータ検証ルールを満たすかを確認する](/cells/ja/java/verify-that-cell-value-satisfies-data-validation-rules/)をご確認ください。

{{% /alert %}}
## **WorkbookRenderクラスのtoPrinter(PrinterSettings printerSettings)メソッドにオーバーロードが追加されました**
オーバーロードされたメソッドを使用して、PrinterSettingsを介してワークブックをプリンタにレンダリングすることが可能です。
{{< app/cells/assistant language="java" >}}
