---
title: よくある質問
type: docs
weight: 100
url: /ja/net/faq/
---
## **Workbook.CalculateFormula で System.StackOverFlowException を修正する方法は?**
Workbook.CalculateFormula メソッドで System.StackOverFlowException が発生することがあります。この例外は通常、IIS の既定のスタック サイズが小さすぎる (265k のみ) ために発生します。このエラーを修正するには、スタック サイズを増やした別のスレッドを作成し、その中に Workbook.CalculateFormula 関連のコードを移動します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Excel を PDF にレンダリングする際の線の太さの問題**
Excel ファイルを PDF に変換すると、出力 PDF の線の太さが異なる場合があります。この問題は Aspose.Cells が原因ではありません。**アドビリーダー**その設定時に**「滑らかな線画」**と**「細い線を強調」**チェックされます。これらのオプションをオフにすると、PDF が表示されます。

チェックする場合**「滑らかな線画」**と**「細い線を強調」**、線の太さが違います。次の手順を参照してください。

- 後藤**編集**
- 選択する**環境設定**
- の中に**ページ表示**カテゴリー チェック**「滑らかな線画」**と**「細い線を強調」**

チェックを外した場合**「滑らかな線画」**と**「細い線を強調」**、線の太さは同じです。これを実現するには、以下の手順に従ってください。

- 後藤**編集**
- 選択する**環境設定**
- の中に**ページ表示**カテゴリのチェックを外します**「滑らかな線画」**と**「細い線を強調」**
## **大きなスプレッドシートのロード中に System.OutOfMemoryException を修正する方法は?**
大規模なスプレッドシートのロード中に Workbook コンストラクターが System.OutOfMemoryException をスローする可能性はかなりあります。この例外は、スプレッドシートをメモリに完全にロードするには使用可能なメモリが不足していることを示唆しています。[メモリ設定](/cells/ja/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells API は、スプレッドシートのロードおよび処理中のメモリ消費を最適化するためのメモリ設定を提供します。これらのオプションは、以下に示すように Workbook オブジェクトに巨大なデータ セットを含む大きなスプレッドシートを効率的に読み込むのにも役立ちます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **特定のワークブックに必要なスタック サイズを決定する**
ただし、Aspose.Cells 数式計算エンジンが強化されており、ほとんどの場合、スタック サイズを小さく指定しなくても、特定のテンプレート ファイルに対して正常に計算されたすべての数式を取得できるはずです。それでも、Workbook.CalculateFormula メソッドで StackOverFlowException が発生することは避けられない場合があります。ユーザーが数式の計算を追跡するための新しい API を提供します。 「AbstractCalculationMonitor」という名前のクラスを追加し、プロパティを提供しました。*CalculationOptions.CalculationMonitor*問題に対処/追跡します。

ユーザーは、API を使用して自分でスタック サイズをトレースできます。すべてのセルのスタックをチェックすると、確実にパフォーマンスが大幅に低下することに注意してください。参照用にサンプル コード セグメントを参照してください。

`     `public class MyCalculationMonitor : AbstractCalculationMonitor
" StackOverflowException のリスクがあるため、式の計算を停止します");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

実行時に使用されるスタック サイズを取得するより良い方法はありません。提供した上記のコードは単なる例です。性能は確実に大幅に低下します。そのため、ユーザー (実際に使用したいユーザー) は、さまざまなシナリオや要件に応じてコードを最適化できると考えています。再帰セルの数が一定数に達したときにスタックをチェックする、1 つの再帰セルのスタックの平均増加率を収集し、スタックをチェックする頻度を決定する、など。

{{% /alert %}}

