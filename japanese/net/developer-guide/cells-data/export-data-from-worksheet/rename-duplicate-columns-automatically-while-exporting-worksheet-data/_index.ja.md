---
title: ワークシート データのエクスポート中に重複する列の名前を自動的に変更する
type: docs
weight: 250
url: /ja/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **考えられる使用シナリオ**

ワークシートからデータ テーブルにデータをエクスポートしているときに、列が重複するという問題に直面することがあります。 DataTable は重複する列を持つことができないため、ワークシート データをデータ テーブルにエクスポートする前に、重複する列の名前を変更する必要があります。 Aspose.Cells は、指定した戦略に従って、重複する列の名前を自動的に変更できます[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy)財産。指定すれば[**Rename戦略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit、列は、column1、column2、column3 などのように名前が変更されます。[**Rename戦略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter の場合、列は columnA、columnB、columnC などのように名前が変更されます。

## **ワークシート データのエクスポート中に重複する列の名前を自動的に変更する**

次のサンプル コードは、ワークシートの最初の 3 つの列にいくつかのデータを追加しますが、すべての列の名前は同じです。*人々* .次に、指定してワークシートからデータテーブルにデータをエクスポートします[**Rename戦略**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).レター戦略。次に、Aspose.Cells によって生成されたデータ テーブルの列名を出力します。次のスクリーンショットは、ビジュアライザーでデータがエクスポートされたデータ テーブルを示しています。ご覧のとおり、重複した列の名前が PeopleA、PeopleB などに変更されました。

![todo:画像_代替_文章](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **コンソール出力**

参考までに、上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
