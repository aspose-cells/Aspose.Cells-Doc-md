---
title: データをソートする際のソート警告の指定
type: docs
weight: 100
url: /ja/java/specifying-sort-warning-while-sorting-data/
---

## **可能な使用シナリオ**
{11, 111, 22}というテキストデータを考慮してください。このようなテキストデータは、111が22よりも前に来るため、このように並び替えられます。しかし、このデータを数値としてソートしたい場合、{11, 22, 111}となります。なぜなら数値的には111は22の後に来るからです。Aspose.Cellsは、この問題に対処するために[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)プロパティを提供しています。このプロパティを**true**に設定すると、テキストデータが数値データとして並べ替えられます。次のスクリーンショットは、テキストデータが数値データとして並べ替えられる際にMicrosoft Excelによって表示されるソート警告を示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **サンプルコード**
次のサンプルコードは、先ほど説明したように[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)プロパティの使用方法を示しています。詳細は[sample Excel file](43352077.xlsx)と[output Excel file](43352078.xlsx)をご覧ください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
