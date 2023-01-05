---
title: ワークブック内およびワークブック間でワークシートをコピーおよび移動する
type: docs
weight: 80
url: /ja/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

場合によっては、共通の書式設定とデータ入力を備えた多数のワークシートが必要になることがあります。たとえば、四半期ごとの予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成できます。これを行う方法があります: 1 つのシートを作成し、それを 3 回コピーします。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーまたは移動をサポートしています。データ、フォーマット、テーブル、マトリックス、チャート、画像、その他のオブジェクトを含むワークシートは、最高の精度でコピーされます。

{{% /alert %}}

## **ワークシートのコピーと移動**

### **ワークブック内でワークシートをコピーする**

最初の手順はすべての例で同じです。

1. Microsoft Excel でいくつかのデータを含む 2 つのワークブックを作成します。この例では、Microsoft Excel で 2 つの新しいワークブックを作成し、ワークシートにいくつかのデータを入力しました。

- FirstWorkbook.xlsx (3 つのワークシート)。
- SecondWorkbook.xlsx (1 ワークシート)。

1. Aspose.Cells をダウンロードしてインストールします。
   1. [ダウンロード Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. 開発用コンピューターにインストールします。
全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. プロジェクトを作成します。
 1. Visual Studio.Net を起動します。
 1. 新しいコンソール アプリケーションを作成します。
1. 参照を追加します。
 1. Aspose.Cells への参照をプロジェクトに追加します。
たとえば、...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。
1. ワークブック内でワークシートをコピーする
最初の例では、FirstWorkbook.xlsx 内の最初のワークシート (コピー) をコピーします。

コードを実行すると、Copy という名前のワークシートが Last Sheet という名前で FirstWorkbook.xlsx 内にコピーされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **ワークブック内でのワークシートの移動**

次のコードは、ブック内のある位置から別の位置にワークシートを移動する方法を示しています。コードを実行すると、Move という名前のワークシートが FirstWorkbook.xlsx のインデックス 1 からインデックス 2 に移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **ワークブック間でワークシートをコピーする**

コードを実行すると、Copy is という名前のワークシートが SecondWorkbook.xlsx に Sheet2 という名前でコピーされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **ワークブック間でワークシートを移動する**

コードを実行すると、Move という名前のワークシートが FirstWorkbook.xlsx から Sheet3 という名前の SecondWorkbook.xlsx に移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
