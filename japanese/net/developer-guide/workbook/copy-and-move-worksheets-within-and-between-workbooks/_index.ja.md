---
title: ワークブック内およびワークブック間でワークシートをコピーおよび移動する
type: docs
weight: 80
url: /ja/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

時には、共通の書式設定およびデータ入力の複数のワークシートが必要なことがあります。例えば、四半期予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを作成したいかもしれません。これを行う方法があります。1つのシートを作成し、それを3回コピーすることです。

Aspose.Cellsは、ワークブック内またはワークブック間でワークシートを最高の精度でコピーまたは移動する機能をサポートします。データ、書式設定、テーブル、行列、グラフ、画像、その他のオブジェクトを含むワークシートがコピーされます。

{{% /alert %}}

## **ワークシートのコピーおよび移動**

### **ワークブック内のワークシートのコピー**

すべての例で最初のステップは同じです。

1. Microsoft Excelにデータを含む2つのワークブックを作成します。この例では、Microsoft Excelで新しいワークブックを2つ作成し、ワークシートにデータを入力しました。

- FirstWorkbook.xlsx（3枚のワークシート）。
- SecondWorkbook.xlsx（1枚のワークシート）。

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [ダウンロード Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
   1. 開発コンピュータにインストールします。
      すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。
1. プロジェクトを作成します。
   1. Visual Studio.Net を起動します。
   1. 新しいコンソールアプリケーションを作成します。
1. 参照を追加します。
   1. Aspose.Cells をプロジェクトに追加します。
      例えば、...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll に参照を追加します。
1. ワークブック内のワークシートをコピーします。
   最初の例では、FirstWorkbook.xlsx の最初のワークシート（Copy）をコピーします。

このコードを実行すると、ワークシート「Copy」が「Last Sheet」としてFirstWorkbook.xlsx内にコピーされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **ワークブック内のワークシートを移動**

以下のコードは、ワークブック内のワークシートを別の位置に移動する方法を示しています。このコードを実行すると、FirstWorkbook.xlsx内でインデックス1の「Move」という名前のワークシートがインデックス2に移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **ワークブック間でワークシートをコピーする**

このコードを実行すると、「Copy」という名前のワークシートがSecondWorkbook.xlsxに「Sheet2」としてコピーされます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **ワークブック間でワークシートを移動する**

このコードを実行すると、「Move」という名前のワークシートがFirstWorkbook.xlsx から「Sheet3」の名前でSecondWorkbook.xlsxに移動します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}
{{< app/cells/assistant language="csharp" >}}
