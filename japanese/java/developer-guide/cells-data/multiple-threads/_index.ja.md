---
title: 複数のスレッドで同時にセル値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1100
url: /ja/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for Java API を使用して複数スレッドでセル値を同時に読み込む方法を学ぶ。
keywords: Java で複数スレッドでセル値を同時に読み取り、Aspose.Cells for Java API 用の複数スレッド。
---

{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要がある場合がよくあります。この記事ではその目的で Aspose.Cells の使用方法を説明します。

{{% /alert %}}

## **Aspose.Cells for Java と共に複数スレッドでセル値を同時に読み取る方法**

複数のスレッドでセル値を同時に読む場合、[**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) を **true** に設定します。そうしないと、誤ったセル値を取得する可能性があります。注意: 複数スレッドではセル値の書式設定などの一部の機能はサポートされていません。したがって、MultiThreadReading はセルの元のデータにアクセスするだけを有効にします。複数スレッド環境では、数値セルの場合に Cell.getStringValue() などでセルの書式設定された値を取得しようとすると、予期しない結果または例外が発生する場合があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. 文字列値でワークシートを埋めます。
1. 次に、ランダムなセルから同時に値を読み取る2つのスレッドを作成します。
   読み取った値が正しい場合、何も起こりません。読み取った値が間違っている場合は、メッセージが表示されます。

この行をコメントアウトすると、次のメッセージが表示されます:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

それ以外の場合、すべてのセルから読み取った値が正しいことを意味するメッセージが表示されずにプログラムが実行されます。

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

それ以外の場合、セルから読み取ったすべての値が正しい場合、プログラムはメッセージを表示せずに実行されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
{{< app/cells/assistant language="java" >}}
