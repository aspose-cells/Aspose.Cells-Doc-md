---
title: ワークブック内およびワークブック間でワークシートをコピーおよび移動する
type: docs
weight: 80
url: /ja/python-net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

時には、共通の書式設定およびデータ入力の複数のワークシートが必要なことがあります。例えば、四半期予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを作成したいかもしれません。これを行う方法があります。1つのシートを作成し、それを3回コピーすることです。

Aspose.Cells for Python via .NETは、ワークブック内またはワークブック間でシートのコピーや移動をサポートします。シートにはデータ、書式設定、テーブル、行列、チャート、画像、およびその他のオブジェクトが含まれ、最大限の精度でコピーされます。

{{% /alert %}}

## **ワークシートのコピーおよび移動**

### **ワークブック内のワークシートのコピー**

すべての例で最初のステップは同じです。

1. Microsoft Excelにデータを含む2つのワークブックを作成します。この例では、Microsoft Excelで新しいワークブックを2つ作成し、ワークシートにデータを入力しました。

- FirstWorkbook.xlsx（3枚のワークシート）。
- SecondWorkbook.xlsx（1枚のワークシート）。

1. Aspose.Cells for Python via .NETをダウンロードしてインストールする：
   1.[Aspose.Cells for Python via .NETをダウンロード](https://downloads.aspose.com/cells/python-net)してください。
   1. 開発コンピュータにインストールします。
      すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。
1. プロジェクトを作成し、参照を追加する：   
1. ワークブック内のワークシートをコピーします。
   最初の例では、FirstWorkbook.xlsx の最初のワークシート（Copy）をコピーします。

このコードを実行すると、ワークシート「Copy」が「Last Sheet」としてFirstWorkbook.xlsx内にコピーされます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheets.py" >}}

### **ワークブック内のワークシートを移動**

以下のコードは、ワークブック内のワークシートを別の位置に移動する方法を示しています。このコードを実行すると、FirstWorkbook.xlsx内でインデックス1の「Move」という名前のワークシートがインデックス2に移動します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheets.py" >}}

### **ワークブック間でワークシートをコピーする**

このコードを実行すると、「Copy」という名前のワークシートがSecondWorkbook.xlsxに「Sheet2」としてコピーされます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.py" >}}

### **ワークブック間でワークシートを移動する**

このコードを実行すると、「Move」という名前のワークシートがFirstWorkbook.xlsx から「Sheet3」の名前でSecondWorkbook.xlsxに移動します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.py" >}}
{{< app/cells/assistant language="python-net" >}}
