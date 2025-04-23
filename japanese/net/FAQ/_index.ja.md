---
title: よくある質問
type: docs
weight: 100
url: /ja/net/faq/
---

## **Workbook.CalculateFormulaでSystem.StackOverFlowExceptionを修正する方法**
ユーザーは、Workbook.CalculateFormulaメソッドでSystem.StackOverFlowExceptionに遭遇することがあります。この例外は通常、IISのデフォルトのスタックサイズが小さすぎる（265kのみ）ために発生します。スタックサイズを増やした別のスレッドを作成し、それに関連するコードを移動することでこのエラーを修正できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **ExcelをPDFに変換する際の線の太さの問題**
ExcelファイルをPDFに変換すると、出力されるPDFの線の太さが異なることがあります。この問題はAspose.Cellsによるものではなく、Adobe Readerの設定の"スムースラインアート"と"細い線を強調する"のチェックによるものです。これらのオプションをオフにすると、PDFが正常に表示されます。

"スムースラインアート"と"細い線を強調する"のチェックを外すと、線の太さが異なります。次の手順を参照してください:

- "編集"に移動
- "設定"を選択
- "ページ表示"カテゴリで"スムースラインアート"と"細い線を強調する"をチェック

"スムースラインアート"と"細い線を強調する"のチェックを外すと、線の太さが同じになります。次の手順に従ってください:

- "編集"に移動
- "設定"を選択
- "ページ表示"カテゴリで"スムースラインアート"と"細い線を強調する"のチェックを外す
## **大規模なスプレッドシートを読み込む際のSystem.OutOfMemoryExceptionの修正方法**
大規模なスプレッドシートを読み込む際にWorkbookコンストラクタがSystem.OutOfMemoryExceptionをスローする可能性があります。この例外は、利用可能なメモリがスプレッドシートを完全に読み込むのに十分でないことを示唆しています。したがって、[メモリ設定](/cells/ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)を有効にしてスプレッドシートを読み込む必要があります。

Aspose.Cells APIは、大規模なスプレッドシートを効率的に読み込むためのメモリ設定を提供しています。以下に示すように、これらのオプションは、大量のデータセットを含む大規模なスプレッドシートを効率的にWorkbookオブジェクトに読み込むのに役立ちます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **特定のワークブックに必要なスタックサイズを決定する**
Aspose.Cellsの数式計算エンジンを強化していますが、ほとんどの場合、より小さなスタックサイズを指定せずに与えられたテンプレートファイルのすべての数式を正常に計算できるはずです。ただし、Workbook.CalculateFormulaメソッドでStackOverFlowExceptionが発生することがあります。この問題に対処するために、ユーザー向けに数式計算をトラッキングする新しいAPIを提供しています。"AbstractCalculationMonitor"というクラスを追加し、*CalculationOptions.CalculationMonitor*プロパティを提供しています。

ユーザーはAPIを使用してスタックサイズを自分でトレースすることができます。ただし、すべてのセルのスタックを確認すると、パフォーマンスが著しく低下します。参考のためにサンプルコードセグメントをご覧ください:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

実行時に使用されるスタックサイズを取得するよりよい方法はありません。上記のコードはあくまで参考例です。パフォーマンスは確実に著しく低下します。したがって、スタックを確認するユーザー（本当に使用したいユーザー）によるコードの最適化が必要と考えられます。たとえば、再帰セルの数がある数値に達したときにスタックを確認し、1つの再帰セルの平均増加率を収集し、スタックを確認する頻度を決定することなどがあります。

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
