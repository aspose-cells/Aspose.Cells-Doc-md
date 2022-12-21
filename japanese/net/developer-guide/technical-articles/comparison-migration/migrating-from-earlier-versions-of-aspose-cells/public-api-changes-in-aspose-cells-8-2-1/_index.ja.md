---
title: パブリック API Aspose.Cells の変更点 8.2.1
type: docs
weight: 80
url: /ja/net/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.2.0 から 8.2.1 への Aspose.Cells API の変更について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **Cell クラスに GetValidation() メソッドを追加**
データ検証は、ユーザーが特定のセルに無効な値を挿入するのを防ぐためにスプレッドシートの設計者が使用する機能の 1 つです。 Aspose.Cells for .NET 8.2.1 で、API は、データ検証がセルに適用されているかどうかを識別する単純なメカニズムを公開しました。適用された検証を取得するには、Cell クラスの GetValidation メソッドを使用します。検証がない場合、メソッドは null を返します。同様に、ValidationCollection クラスの GetValidationInCell メソッドを使用して、行と列のインデックスを指定することにより、任意のセルに適用される検証を取得できます。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[Cell に検証を適用する](/cells/ja/net/get-validation-applied-on-a-cell/)詳細については。

{{% /alert %}}
## **Cell クラスに GetValidationValue() メソッドを追加**
検証が適用されているかどうかを判断するだけでなく、特定の値が特定のセルのデータ検証規則を満たしているかどうかを検証することもできます。この機能は、セルに入力された値がその場でデータ検証ルールを満たしているかどうかを確認する場合に役立ちます。 Aspose.Cells API は、Cell クラスの GetValidationValue メソッドを公開しました。セルに入力された値がデータ検証規則を満たさない場合、Cell クラスの GetValidationValue メソッドは false を返します。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[Cell 値がデータ検証ルールを満たしていることを確認する](/cells/ja/net/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **WorkbookRender クラスのオーバーロード ToPrinter(PrinterSettings printerSettings) メソッドを追加しました**
オーバーロードされたメソッドを使用して、PrinterSettings を介してワークブックをプリンターにレンダリングできます。
