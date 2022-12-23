---
title: 大規模なデータセットを含む大きなファイルを操作する際のメモリ使用量の最適化
type: docs
weight: 110
url: /ja/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

大規模なデータ セットを含むワークブックを作成する場合、または大きな Microsoft Excel ファイルを読み取る場合、プロセスが使用する RAM の総量が常に懸念されます。課題に対処するために適応できる対策があります。 Aspose.Cells は、いくつかの関連するオプションと API 呼び出しを提供して、メモリ使用量を削減、削減、および最適化します。また、プロセスがより効率的に機能し、より速く実行するのに役立ちます.

使用[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)セル データに使用されるメモリを最適化して、全体的なメモリ コストを削減するオプション。セルの大きなデータ セットを構築する場合、既定の設定を使用する場合と比較して、一定量のメモリを節約できます。[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **メモリの最適化**

次の例は、Aspose.Cells for Node.js via Java の大きなデータを操作しながらメモリ使用量を最適化する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **注意**

デフォルトのオプション、[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)すべてのバージョンに適用されます。セルの大きなデータ セットを含むワークブックを作成するなど、状況によっては、[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)オプションにより、メモリの使用が最適化され、アプリケーションのメモリ コストが削減される場合があります。ただし、このオプションは、次のような特殊なケースではパフォーマンスを低下させる可能性があります。

1. **Cells にランダムに繰り返しアクセスする**注: セル コレクションにアクセスするための最も効率的な順序は、1 つの行でセルごとにアクセスし、次に行ごとに実行することです。特に、Enumerator から取得した行/セルにアクセスする場合[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**行コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection)と[**行**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)、パフォーマンスは最大化されます[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Cells & 行の挿入と削除** Cells/Rows の挿入/削除操作が多い場合、パフォーマンスの低下が顕著になることに注意してください。[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)モードと比較して[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)モード。
1. **異なる Cell タイプでの操作** ほとんどのセルに文字列値または数式が含まれている場合、メモリ コストは[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)モードですが、空のセルがたくさんある場合、またはセルの値が数値、bool などの場合、[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)オプションを使用すると、パフォーマンスが向上します。

