---
title: 複数のスレッドで同時に Cell 値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1100
url: /ja/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Java API を使用して、複数のスレッドで Cell の値を同時に読み取る方法を学習します。
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要があることは、一般的な要件です。この記事では、この目的で Aspose.Cells を使用する方法について説明します。

{{% /alert %}}

##  **Aspose.Cells for Java と同時に複数のスレッドで Cell の値を読み取る方法**

複数のスレッドで同時にセル値を読み取るには、次のように設定します。[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)*本当**に。そうしないと、間違ったセル値が取得される可能性があります。セル値の書式設定などの一部の機能はマルチスレッドではサポートされていないことに注意してください。したがって、MultiThreadReading では、セルの元のデータのみにアクセスできます。マルチスレッド環境では、数値の Cell.getStringValue() などによってセルの書式設定された値を取得しようとすると、予期しない結果または例外が発生する可能性があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. ワークシートに文字列値を入力します。
1. 次に、ランダムなセルから値を同時に読み取る 2 つのスレッドを作成します。
読み取られた値が正しい場合は、何も起こりません。読み取られた値が正しくない場合は、メッセージが表示されます。

この行をコメントすると:

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

それ以外の場合、プログラムはメッセージを表示せずに実行されます。これは、セルから読み取られたすべての値が正しいことを意味します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
