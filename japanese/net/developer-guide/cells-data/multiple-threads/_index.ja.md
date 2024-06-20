---
title: 複数のスレッドで同時にセル値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1800
url: /ja/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for .NET APIを使用して複数のスレッドでセル値を読み取る方法を学びます。
keywords: 複数のスレッドで同時にセル値を読み取る、Aspose.Cells C# 複数スレッドでの読み取り、複数のスレッドでデータを読み取る
---

{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要がある場合がよくあります。この記事ではその目的で Aspose.Cells の使用方法を説明します。

{{% /alert %}}

複数のスレッドで同時にセル値を読み取るために、[**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) を **true** に設定します。そうしないと、間違ったセル値を取得する可能性があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. 文字列値でワークシートを埋めます。
1. 次に、ランダムなセルから同時に値を読み取る2つのスレッドを作成します。
   読み取った値が正しい場合、何も起こりません。読み取った値が間違っている場合は、メッセージが表示されます。

この行をコメントアウトすると、次のメッセージが表示されます:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

それ以外の場合、すべてのセルから読み取った値が正しいことを意味するメッセージが表示されずにプログラムが実行されます。

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

それ以外の場合、セルから読み取ったすべての値が正しい場合、プログラムはメッセージを表示せずに実行されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
