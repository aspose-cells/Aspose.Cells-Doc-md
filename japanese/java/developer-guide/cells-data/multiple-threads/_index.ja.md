---
title: 複数のスレッドで同時に Cell の値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1100
url: /ja/java/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要があるのは、一般的な要件です。この記事では、この目的で Aspose.Cells を使用する方法について説明します。

{{% /alert %}}

複数のスレッドで同時にセル値を読み取るには、次のように設定します。[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)に**真実**.そうしないと、間違ったセル値が得られる可能性があります。マルチスレッドでは、セル値の書式設定などの一部の機能がサポートされていないことに注意してください。したがって、MultiThreadReading では、セルの元のデータのみにアクセスできます。マルチスレッド環境で、数値の Cell.getStringValue() などでセルの書式設定された値を取得しようとすると、予期しない結果または例外が発生する場合があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. ワークシートに文字列値を入力します。
1. 次に、ランダム セルから値を同時に読み取る 2 つのスレッドを作成します。
読み取った値が正しい場合、何も起こりません。読み取った値が正しくない場合は、メッセージが表示されます。

この行にコメントすると:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

次のメッセージが表示されます。

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

それ以外の場合、セルから読み取ったすべての値が正しいことを意味するメッセージを表示せずにプログラムが実行されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
