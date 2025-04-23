---
title: ワークブック内およびワークブック間でワークシートをコピーおよび移動する
type: docs
weight: 20
url: /ja/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

時には、共通の書式設定およびデータ入力の複数のワークシートが必要なことがあります。例えば、四半期予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを作成したいかもしれません。これを行う方法があります。1つのシートを作成し、それを3回コピーすることです。

Aspose.Cellsは、ワークブック内またはワークブック間でワークシートを最高の精度でコピーまたは移動する機能をサポートします。データ、書式設定、テーブル、行列、グラフ、画像、その他のオブジェクトを含むワークシートがコピーされます。

{{% /alert %}}

## **ワークシートのコピーおよび移動**

この記事では、Aspose.Cellsを使用して次の操作を行う方法について説明しています:

- ワークブック内でのワークシートのコピー[/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook]。
- ワークブック内でのワークシートの移動[/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook]。
- ワークブック間でのワークシートのコピー[/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks]。
- ワークブック間でのワークシートの移動[/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks]。

### **ワークブック内のワークシートのコピー**

すべての例で最初のステップは同じです。

1. Microsoft Excelにデータを含む2つのワークブックを作成します。この例では、Microsoft Excelで新しいワークブックを2つ作成し、ワークシートにデータを入力しました。

- FirstWorkbook.xls (3つのワークシート)
- SecondWorkbook.xls (1つのワークシート)

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Aspose.Cellsをダウンロードしてインストールします。
   1. [Aspose.Cells for Javaをダウンロード](https://downloads.aspose.com/cells/java)します。
   1. 開発コンピュータにそれを解凍します。
      すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。
1. プロジェクトを作成します。
   1. EclipseなどのJavaエディタを使用してプロジェクトを作成するか、テキストエディタを使用して簡単なプログラムを作成します。
1. クラスパスを追加します。
   1. Aspose.Cells.zipからAspose.Cells.jarとdom4j_1.6.1.jarを抽出します。
   1. Eclipseでプロジェクトのクラスパスを設定します。
      1. Eclipseでプロジェクトを選択し、**Project**、次に**Properties**をクリックします。
      1. ダイアログの左側で**Java Build Path**を選択し、Librariesタブを選択します。
      1. **Add JARs**または**Add External JARs**をクリックしてAspose.Cells.jarとdom4j_1.6.1.jarを選択し、ビルドパスに追加します。

{{% alert color="primary" %}}

または、WindowsのDOSプロンプトで実行時にクラスパスを設定できます。
例:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. ワークブック内でワークシートをコピーします。
   以下は、このタスクを達成するために使用されるコードです。これにより、ワークブックFirstWorkbook.xls内のワークシートCopyがコピーされます。

コードを実行すると、新しい名前のワークシートLast Sheetが付いたFirstWorkbook.xls内のワークシートCopyが移動します。

**出力ファイル**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **ワークブック内でワークシートを移動する**

以下は、このタスクを達成するために使用されるコードです。

コードを実行すると、FirstWorkbook.xls内のインデックス1からインデックス2にワークシートMoveが移動します。

**出力ファイル**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **ワークブック間でワークシートをコピーする**

コードを実行すると、ワークブックSecondWorkbook.xlsにワークシートCopyがSheet2という新しい名前でコピーされます。

**出力ファイル**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **ワークブック間でワークシートを移動する**

コードを実行すると、FirstWorkbook.xlsからSecondWorkbook.xlsにシートを移動し、新しい名前をSheet3に変更します。

**FirstWorkbook.xlsの出力**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**SecondWorkbook.xlsの出力**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **結論**

{{% alert color="primary" %}}

この記事では、Aspose.Cellsを使用してブック間およびブック内でワークシートをコピーおよび移動する方法について説明します。

Aspose.Cellsは、長年の研究、設計、丁寧なチューニングによって恩恵を受けています。[Aspose.Cellsフォーラム](https://forum.aspose.com/c/cells/9)でのお問い合わせ、コメント、提案を歓迎します。迅速な返信を保証します。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
