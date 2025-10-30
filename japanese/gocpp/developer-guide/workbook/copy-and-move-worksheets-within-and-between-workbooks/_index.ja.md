---
title: GolangとC++を使ってワークブック内およびワークブック間でシートをコピー・移動する
linktitle: シートのコピーと移動
type: docs
weight: 80
url: /ja/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aspose.Cells for C++を使用してExcelのワークシート内および間でのコピーと移動方法を学習します。
---

{{% alert color="primary" %}}

複数のシートに共通のフォーマットやデータ入力を持たせる必要がある場合があります。例えば、四半期予算の作成において、同じ列見出し、行見出し、数式を含むシートを複数作成したい場合です。これには、1つのシートを作成し、それを複数コピーする方法があります。

Aspose.Cellsは、ワークブック内またはワークブック間でワークシートを最高の精度でコピーまたは移動する機能をサポートします。データ、書式設定、テーブル、行列、グラフ、画像、その他のオブジェクトを含むワークシートがコピーされます。

{{% /alert %}}

## **ワークシートのコピーおよび移動**

### **ワークブック内のワークシートのコピー**

すべての例の最初のステップは次の通りです：

1. Microsoft Excelでいくつかのデータを入力した2つのワークブックを作成します。この例では、新たに2つのワークブックを作成し、シートにデータを入力しました：
   - FirstWorkbook.xlsx（3つのシート）
   - SecondWorkbook.xlsx（1つのシート）

1. Aspose.Cellsをダウンロードしてインストールします。
    1. [ダウンロード Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. 開発コンピュータにインストールする

1. プロジェクトを作成します。
   1. 好みのIDEで新しいC++プロジェクトを作成します

1. 参照を追加します。
   1. プロジェクトにAspose.Cells for C++ライブラリを追加します

1. ワークブック内のワークシートをコピーします。
   最初の例では、FirstWorkbook.xlsx の最初のワークシート（Copy）をコピーします。

このコードを実行すると、ワークシート「Copy」が「Last Sheet」としてFirstWorkbook.xlsx内にコピーされます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **ワークブック内のワークシートを移動**

以下のコードは、ワークブック内のワークシートを別の位置に移動する方法を示しています。このコードを実行すると、FirstWorkbook.xlsx内でインデックス1の「Move」という名前のワークシートがインデックス2に移動します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **ワークブック間でワークシートをコピーする**

コードを実行すると、「Copy」という名前のシートを持つワークシートが、SecondWorkbook.xlsxにコピーされます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **ワークブック間でワークシートを移動する**

このコードを実行すると、「Move」という名前のワークシートがFirstWorkbook.xlsx から「Sheet3」の名前でSecondWorkbook.xlsxに移動します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
