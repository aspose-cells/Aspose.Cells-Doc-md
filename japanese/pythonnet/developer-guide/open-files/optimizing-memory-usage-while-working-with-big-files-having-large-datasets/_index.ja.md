---
title: 大規模なデータセットを扱う場合のメモリ使用量を最適化する
type: docs
weight: 180
url: /ja/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを構築したり、大きなMicrosoft Excelファイルを読み取ると、必要なRAMの合計量が常に懸念されます。これに対処するための措置がいくつかあります。Aspose.Cells for Python via .NETは、メモリ使用量を削減、最適化するための関連するオプションやAPI呼び出しを提供します。また、処理をより効率的にし、より高速に実行させることも可能です。

セルのデータのメモリ使用を最適化し、総合的なメモリコストを減らすために [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) オプションを使用してください。大規模なセルデータセットを構築する際、デフォルトの設定（[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)）に比べて一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

### **大きなExcelファイルの読み取り**

以下の例は、最適化モードで大きなMicrosoft Excelファイルを読み取る方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **大きなExcelファイルの書き込み**

以下の例は、大規模なデータセットをワークシートに書き込む方法を最適化モードで示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **注意**

デフォルトオプションである [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) はすべてのバージョンで適用されます。セルの大規模なデータセットを使用するなど、アプリケーションのメモリ使用を最適化し、メモリコストを減らすためには [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) オプションを使用することができます。ただし、このオプションは次のような特殊なケースにおいてパフォーマンスが低下する可能性があります。

1. **ランダムで繰り返しセルにアクセス**: セルのコレクションにアクセスする最も効率的なシーケンスは、行ごとに1つずつセルにアクセスし、その後行ごとにアクセスすることです。特に、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)、[**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection)および[**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)から取得したEnumeratorで行/セルにアクセスする場合、パフォーマンスは[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)で最適化されます。
1. **セルや行の挿入・削除**: セル/行の挿入/削除が多い場合、*MemoryPreference*モードのパフォーマンス劣化が*Normal*モードと比較して顕著になります。
1. **異なるセルタイプ間での操作**: ほとんどのセルが文字列値や数式を含む場合、メモリコストは*Normal*モードと同じになりますが、空のセルが多い場合やセルの値が数値、ブール値などの場合、[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) オプションの方がパフォーマンスが向上します。

{{< app/cells/assistant language="python-net" >}}
