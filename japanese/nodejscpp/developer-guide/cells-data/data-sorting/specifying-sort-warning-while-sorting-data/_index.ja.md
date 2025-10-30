---
title: データをソートする際のソート警告の指定
type: docs
weight: 140
url: /ja/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: ソート時に警告を指定する方法を、Aspose.Cells for Node.js via C++ APIを使用して学習します。
keywords: データをソートする際にソート警告を追加する、データをソートする際にソート警告を設定する、データをソートする際にソート警告を選択する。
---

## **可能な使用シナリオ**

このテキストデータ、例：{11, 111, 22}は、文字列としてソートされると111が22より前に来ますが、数値としてソートしたい場合は{11, 22, 111}となります。Aspose.Cells for Node.js via C++は{0}プロパティを提供しており、これをtrueに設定することで、文字列としてのデータも数値としてソートされるようになります。Microsoft Excelで数値のように見える文字列データのソート時に表示されるソート警告もスクリーンショットで示しています。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **サンプルコード**

次のサンプルコードは、上記で説明した[**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-)プロパティの使用方法を説明しています。詳細については、サンプルExcelファイル（43352075.xlsx）とそれに対応する出力Excelファイル（43352076.xlsx）を確認してください。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
