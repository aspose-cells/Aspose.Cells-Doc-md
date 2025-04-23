---
title: 大規模なデータセットを扱う場合のメモリ使用量を最適化する
type: docs
weight: 110
url: /ja/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを構築したり、大きなMicrosoft Excelファイルを読み込んだりする際、プロセスが必要とするRAMの総量は常に懸念事項です。Aspose.Cellsは、メモリ使用量を最適化するための関連するオプションとAPI呼び出しを提供します。これにより、プロセスがより効率的に動作し、より速く実行されるようになります。

セルデータのメモリ使用量を最適化するために、[**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)よりもメモリ使用量を減らすために使用します。大規模なデータセットを扱う際、デフォルトの設定を使用するよりも一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

以下の例は、大規模なデータを扱う際にメモリ使用量を最適化する方法を示しています Aspose.Cells for Node.js via C++。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "OptimizingMemory.js" >}}

## **注意**

デフォルトオプション[**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)はすべてのバージョンで適用されます。大量のセルデータセットを持つワークブックを構築するなどの一部の状況では、メモリ使用を最適化し、アプリケーションのメモリコストを減らすことができるかもしれませんが、このオプションは特定の状況ではパフォーマンスを低下させる可能性があります。

1. **ランダムで繰り返しセルにアクセス**: セルのコレクションにアクセスする最も効率的なシーケンスは、行ごとに1つずつセルにアクセスし、その後行ごとにアクセスすることです。特に、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/)、[**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)および[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)から取得したEnumeratorで行/セルにアクセスする場合、パフォーマンスは[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)で最適化されます。
1. **セルや行の挿入および削除**：多くの挿入/削除操作がセル/行にある場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)モードでは、[**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)モードと比較してパフォーマンスの低下が顕著になります。
1. **異なるセルタイプでの操作**：ほとんどのセルが文字列値や数式を含む場合、メモリコストは[**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)モードと同じになりますが、空のセルが多いか、セルの値が数値、ブール値などの場合、[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)オプションはパフォーマンスが向上します。

