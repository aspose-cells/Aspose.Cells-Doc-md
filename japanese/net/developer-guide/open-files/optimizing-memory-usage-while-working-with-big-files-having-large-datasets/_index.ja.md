---
title: 大規模なデータセットを含む大きなファイルを操作する際のメモリ使用量の最適化
type: docs
weight: 180
url: /ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

大規模なデータ セットを含むワークブックを作成する場合、または大きな Microsoft Excel ファイルを読み取る場合、プロセスが使用する RAM の総量が常に懸念されます。課題に対処するために適応できる対策があります。 Aspose.Cells は、いくつかの関連するオプションと API 呼び出しを提供して、メモリ使用量を削減、削減、および最適化します。また、プロセスがより効率的に機能し、より速く実行するのに役立ちます。

使用[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)セル データのメモリ使用を最適化し、全体的なメモリ コストを削減するオプション。セルの大きなデータ セットを構築する場合、既定の設定を使用する場合と比較して、一定量のメモリを節約できます ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **メモリの最適化**

### **大きな Excel ファイルの読み取り**

次の例は、最適化モードで大きな Microsoft Excel ファイルを読み取る方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **大きな Excel ファイルの書き込み**

次の例は、大規模なデータセットを最適化モードでワークシートに書き込む方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **注意**

デフォルトのオプション、[**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)すべてのバージョンに適用されます。セルの大きなデータ セットを含むワークブックを作成するなど、状況によっては、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)オプションにより、メモリの使用が最適化され、アプリケーションのメモリ コストが削減される場合があります。ただし、このオプションは、次のような特殊なケースではパフォーマンスを低下させる可能性があります。

1. **Cells にランダムに繰り返しアクセスする**注: セル コレクションにアクセスするための最も効率的な順序は、1 つの行でセルごとにアクセスし、次に行ごとに実行することです。特に、Enumerator から取得した行/セルにアクセスする場合[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**行コレクション**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection)と[**行**](https://reference.aspose.com/cells/net/aspose.cells/row)、パフォーマンスは最大化されます[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Cells & 行の挿入と削除** Cells/Rows の挿入/削除操作が多い場合、パフォーマンスの低下が顕著になることに注意してください。*メモリ設定*モードと比較して*普通*モード。
1. **異なる Cell タイプでの操作** ほとんどのセルに文字列値または数式が含まれている場合、メモリ コストは*普通*モードですが、空のセルがたくさんある場合、またはセルの値が数値、bool などの場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)オプションを使用すると、パフォーマンスが向上します。
