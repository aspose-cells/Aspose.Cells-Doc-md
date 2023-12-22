---
title: 複数のスレッドで同時に Cell 値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1800
url: /ja/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for .NET API を通じて、複数のスレッドで Cell の値を同時に読み取る方法を学びます。
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要があることは、一般的な要件です。この記事では、この目的で Aspose.Cells を使用する方法について説明します。

{{% /alert %}}

複数のスレッドで同時にセル値を読み取るには、次のように設定します。[**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)*本当**に。そうしないと、間違ったセル値が取得される可能性があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. ワークシートに文字列値を入力します。
1. 次に、ランダムなセルから値を同時に読み取る 2 つのスレッドを作成します。
読み取られた値が正しい場合は、何も起こりません。読み取られた値が正しくない場合は、メッセージが表示されます。

この行をコメントすると:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

次のメッセージが表示されます。

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

それ以外の場合、プログラムはメッセージを表示せずに実行されます。これは、セルから読み取られたすべての値が正しいことを意味します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
