---
title: ワークシート データのエクスポート中に重複する列の名前を自動的に変更する
type: docs
weight: 250
url: /ja/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Aspose.Cells for .NET API を通じてワークシート データをエクスポートする際に、重複する列の名前を自動的に変更する方法を学びます。
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **考えられる使用シナリオ**

ワークシートからデータテーブルにデータをエクスポートするときに、ユーザーは重複列の問題に直面することがあります。 DataTable には重複した列を含めることはできないため、ワークシート データをデータ テーブルにエクスポートする前に、重複した列の名前を変更する必要があります。 Aspose.Cells は、指定した戦略に従って重複列の名前を自動的に変更できます。[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy)財産。指定する場合[**名前の変更戦略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit を指定すると、列の名前が column1、column2、column3 などのように変更されます。[**名前の変更戦略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter の場合、列の名前は、columnA、columnB、columnC などのように変更されます。

##  **ワークシート データのエクスポート中に重複する列の名前を自動的に変更する**

次のサンプル コードでは、ワークシートの最初の 3 列にデータを追加しますが、すべての列の名前は *People* と同じです。次に、次のように指定して、ワークシートからデータテーブルにデータをエクスポートします。[**名前の変更戦略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).レター戦略。次に、Aspose.Cells によって生成されたデータ テーブルの列名を出力します。次のスクリーンショットは、ビジュアライザーにエクスポートされたデータを含むデータ テーブルを示しています。ご覧のとおり、重複した列の名前は PeopleA、PeopleB などに変更されています。

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **コンソール出力**

参考までに、上記のサンプル コードのコンソール出力を示します。

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
