---
title: 大規模なデータセットを扱う場合のメモリ使用量を最適化する
type: docs
weight: 110
url: /ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

大規模なデータセットを含むワークブックを構築したり、大きなMicrosoft Excelファイルを読み込んだりする際、プロセスが必要とするRAMの総量は常に懸念事項です。Aspose.Cellsは、メモリ使用量を最適化するための関連するオプションとAPI呼び出しを提供します。これにより、プロセスがより効率的に動作し、より速く実行されるようになります。

セルデータのメモリ使用量を最適化するために、[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)よりもメモリ使用量を減らすために使用します。大規模なデータセットを扱う際、デフォルトの設定を使用するよりも一定量のメモリを節約することができます。

{{% /alert %}}

## **メモリの最適化**

### **大きなExcelファイルの読み取り**

以下の例は、最適化モードで大きなMicrosoft Excelファイルを読み取る方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **大きなExcelファイルの書き込み**

大きなデータセットを最適モードでワークシートに書き込む方法を示す例が以下に示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **注意**

デフォルトオプション[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)はすべてのバージョンで適用されます。大量のセルデータセットを持つワークブックを構築するなどの一部の状況では、メモリ使用を最適化し、アプリケーションのメモリコストを減らすことができるかもしれませんが、このオプションは特定の状況ではパフォーマンスを低下させる可能性があります。

1. **ランダムで繰り返しセルにアクセス**: セルのコレクションにアクセスする最も効率的なシーケンスは、行ごとに1つずつセルにアクセスし、その後行ごとにアクセスすることです。特に、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)、[**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection)および[**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)から取得したEnumeratorで行/セルにアクセスする場合、パフォーマンスは[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE)で最適化されます。
1. **セルや行の挿入および削除**：多くの挿入/削除操作がセル/行にある場合、[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE)モードでは、[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)モードと比較してパフォーマンスの低下が顕著になります。
1. **異なるセルタイプでの操作**：ほとんどのセルが文字列値や数式を含む場合、メモリコストは[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)モードと同じになりますが、空のセルが多いか、セルの値が数値、ブール値などの場合、[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE)オプションはパフォーマンスが向上します。
{{< app/cells/assistant language="java" >}}
