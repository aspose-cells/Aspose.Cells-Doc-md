---
title: 複数のスレッドで同時にセル値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1800
url: /ja/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Node.js via C++ APIを使用して複数スレッドでセル値を読み取る方法を学ぶ。
keywords: C++経由でNode.jsで複数スレッドにおいてセル値を読み取る、Aspose.Cells C++の複数スレッド利用、複数スレッドでのデータ読込。
---

{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要がある場合がよくあります。この記事ではその目的で Aspose.Cells の使用方法を説明します。

{{% /alert %}}

複数のスレッドでセル値を同時に読み取るには、[**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-)を**true**に設定します。そうしないと、誤ったセル値を取得する可能性があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. 文字列値でワークシートを埋めます。
1. 次に、ランダムなセルから同時に値を読み取る2つのスレッドを作成します。
   読み取った値が正しい場合、何も起こりません。読み取った値が間違っている場合は、メッセージが表示されます。

この行をコメントアウトすると、次のメッセージが表示されます:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

それ以外の場合、すべてのセルから読み取った値が正しいことを意味するメッセージが表示されずにプログラムが実行されます。

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

それ以外の場合、セルから読み取ったすべての値が正しい場合、プログラムはメッセージを表示せずに実行されます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
