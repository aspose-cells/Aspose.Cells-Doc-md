---
title: ワークブック内およびワークブック間でワークシートをコピーおよび移動する
type: docs
weight: 20
url: /ja/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

場合によっては、共通の書式設定とデータ入力を備えた多数のワークシートが必要になることがあります。たとえば、四半期ごとの予算を扱う場合、同じ列見出し、行見出し、および数式を含むシートを含むワークブックを作成できます。これを行う方法があります: 1 つのシートを作成し、それを 3 回コピーします。

Aspose.Cells は、ワークブック内またはワークブック間でのワークシートのコピーまたは移動をサポートしています。データ、フォーマット、テーブル、マトリックス、チャート、画像、その他のオブジェクトを含むワークシートは、最高の精度でコピーされます。

{{% /alert %}}

## **ワークシートのコピーと移動**

この記事では、Aspose.Cells を使用して次のことを行う方法について説明します。

- [ワークブック内でワークシートをコピーする](/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [ワークブック内でワークシートを移動する](/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [ワークブック間でワークシートをコピーする](/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [ワークブック間でワークシートを移動する](/cells/ja/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **ワークブック内でワークシートをコピーする**

最初の手順はすべての例で同じです。

1. Microsoft Excel でいくつかのデータを含む 2 つのワークブックを作成します。この例では、Microsoft Excel で 2 つの新しいワークブックを作成し、ワークシートにいくつかのデータを入力しました。

- FirstWorkbook.xls (3 つのワークシート)
- SecondWorkbook.xls (1 ワークシート)。

  **FirstWorkbook.xls**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Aspose.Cells をダウンロードしてインストールします。
   1. [ダウンロード Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 開発用コンピューターで解凍します。
全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. プロジェクトを作成します。
 1. Eclipse などの Java エディターを使用してプロジェクトを作成するか、テキスト エディターを使用して簡単なプログラムを作成します。
1. クラスパスを追加します。
1. Aspose.Cells.zip から Aspose.Cells.jar と dom4j_1.6.1.jar を抽出します。
 1. Eclipse でプロジェクトのクラスパスを設定します。
 1. Eclipse でプロジェクトを選択し、メニューをクリックします**計画**、 それから**プロパティ**.
1. 選択**Java ビルド パス**ダイアログの左側で、[ライブラリ] タブを選択します。
 1. クリック**JAR を追加する**また**外部 JAR を追加する**Aspose.Cells.jar と dom4j_1.6.1.jar を選択してビルド パスに追加します。

{{% alert color="primary" %}}

または、実行時に Windows の DOS プロンプトでクラスパスを設定できます。
例えば：

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. ワークブック内でワークシートをコピー:
以下は、タスクを実行するために によって使用されるコードです。ワークシート Copy を FirstWorkbook.xls 内にコピーします。

コードを実行すると、Copy という名前のワークシートが FirstWorkbook.xls 内に移動し、Last Sheet という新しい名前が付けられます。

**出力ファイル**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **ワークブック内でのワークシートの移動**

以下は、タスクを実行するために使用されるコードです。

コードを実行すると、ワークシート Move が FirstWorkbook.xls のインデックス 1 からインデックス 2 に移動します。

**出力ファイル**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **ワークブック間でワークシートをコピーする**

コードを実行すると、ワークシート Copy が新しい名前 Sheet2 で SecondWorkbook.xls にコピーされます。

**出力ファイル**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **ワークブック間でワークシートを移動する**

コードを実行すると、移動ワークシートが FirstWorkbook.xls から SecondWorkbook.xls に新しい名前 Sheet3 で移動します。

**FirstWorkbook.xls を出力**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**出力 SecondWorkbook.xls**

![todo:画像_代替_文章](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **結論**

{{% alert color="primary" %}}

この記事では、Aspose.Cells を使用して、ブック内およびブック間でワークシートをコピーおよび移動する方法について説明します。

 Aspose.Cells は、何年にもわたる研究、設計、慎重な調整の恩恵を受けてきました。ご質問、ご意見、ご提案は、[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9).迅速な返信を保証します。

{{% /alert %}}
