---
title: ワークシートからデータをエクスポートする際に重複する列を自動的にリネーム
type: docs
weight: 250
url: /ja/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Aspose.Cells for .NET API を介してワークシートのデータをエクスポートする際に重複する列を自動的にリネームする方法を学びます。
keywords: データテーブルへのワークシートデータのエクスポート時に重複する列のリネーム, DataTable へデータをエクスポートする際に重複する列を自動的にリネーム
---

## **可能な使用シナリオ**

ユーザーは、ワークシートからデータをデータテーブルにエクスポートする際に重複する列の問題に直面することがあります。データテーブルには重複する列を持つことはできないため、ワークシートデータをデータテーブルにエクスポートする前に重複列をリネームする必要があります。Aspose.Cells では、[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy)プロパティを使用して、指定された戦略に従って重複列を自動的にリネームできます。[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digitを指定すると列名がcolumn1、column2、column3などのようにリネームされ、[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letterを指定するとcolumnA、columnB、columnCなどのようにリネームされます。

## **ワークシートデータをエクスポートする際に重複する列の名前を自動的に変更する**

次のサンプルコードでは、ワークシートの最初の3列にいくつかのデータを追加しますが、すべての列の名前が*People*です。次に、[**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter戦略を指定してワークシートからデータをデータテーブルにエクスポートします。その後、Aspose.Cells によって生成されたデータテーブルの列名を印刷します。次のスクリーンショットは、ビジュアライザ内でエクスポートされたデータを持つデータテーブルを示しています。重複する列がPeopleA、PeopleBなどにリネームされていることがわかります。

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **コンソール出力**

上記サンプルコードのコンソール出力は次のとおりです。

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
