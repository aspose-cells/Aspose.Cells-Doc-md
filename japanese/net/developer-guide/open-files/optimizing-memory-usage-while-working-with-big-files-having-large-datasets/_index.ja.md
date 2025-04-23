---
title: 大規模なデータセットを扱う場合のメモリ使用量を最適化する
type: docs
weight: 180
url: /ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを構築したり、大きなMicrosoft Excelファイルを読み込んだりする際に、プロセスが使用する合計RAM量は常に懸念事項です。Aspose.Cellsは、メモリ使用量を低減、削減、最適化するための関連するオプションやAPI呼び出しを提供します。これにより、プロセスが効率的に動作し、高速に動作するようにすることができます。

セルのデータのメモリ使用を最適化し、総合的なメモリコストを減らすために [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) オプションを使用してください。大規模なセルデータセットを構築する際、デフォルトの設定（[**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)）に比べて一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

### **大きなExcelファイルの読み取り**

以下の例は、最適化モードで大きなMicrosoft Excelファイルを読み取る方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **大きなExcelファイルの書き込み**

以下の例は、大規模なデータセットをワークシートに書き込む方法を最適化モードで示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **注意**

デフォルトオプションである [**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) はすべてのバージョンで適用されます。セルの大規模なデータセットを使用するなど、アプリケーションのメモリ使用を最適化し、メモリコストを減らすためには [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) オプションを使用することができます。ただし、このオプションは次のような特殊なケースにおいてパフォーマンスが低下する可能性があります。

1. **ランダムで繰り返しセルにアクセス**: セルのコレクションにアクセスする最も効率的なシーケンスは、行ごとに1つずつセルにアクセスし、その後行ごとにアクセスすることです。特に、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)、[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection)および[**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)から取得したEnumeratorで行/セルにアクセスする場合、パフォーマンスは[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)で最適化されます。
1. **セルや行の挿入・削除**: セル/行の挿入/削除が多い場合、*MemoryPreference*モードのパフォーマンス劣化が*Normal*モードと比較して顕著になります。
1. **異なるセルタイプ間での操作**: ほとんどのセルが文字列値や数式を含む場合、メモリコストは*Normal*モードと同じになりますが、空のセルが多い場合やセルの値が数値、ブール値などの場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) オプションの方がパフォーマンスが向上します。
{{< app/cells/assistant language="csharp" >}}
