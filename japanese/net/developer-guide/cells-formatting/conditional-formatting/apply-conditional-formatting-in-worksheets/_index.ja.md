---
title: ワークシートに条件付き書式を適用する
description: C# の Aspose.Cells ライブラリを使用してワークシートに条件付き書式を適用する方法。これらの基準を調整することで、セルの外観をより詳細に制御できるようになります。
keywords: Aspose.Cells, Conditional Formatting, C#, Worksheet, Formatting
type: docs
weight: 130
url: /ja/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

この記事は、ワークシート内のセル範囲に条件付き書式を追加する方法を詳しく理解することを目的としています。

条件付き書式設定は、Microsoft Excel の高度な機能で、セル範囲に書式を適用し、セルの値または数式の値に応じてその書式を変更できます。たとえば、セルの背景を赤にして負の値を強調したり、テキストの色を緑にして正の値を強調したりすることができます。セルの値が書式条件を満たしている場合、書式が適用されます。セルの値が書式条件を満たさない場合は、セルのデフォルトの書式設定が使用されます。

Microsoft Office Automation では条件付き書式を適用できますが、これには欠点があります。セキュリティ、安定性、スケーラビリティ、速度など、いくつかの理由と問題が関係しています。別の解決策を探す主な理由は、Microsoft 自体がソフトウェア ソリューションとして Office Automation を強く推奨していないためです。

この記事では、コンソール アプリケーションを作成し、Aspose.Cells API を使用した最も単純な数行のコードでセルに条件付き書式を追加する方法を説明します。

{{% /alert %}}

##  **Aspose.Cells を使用して Cell の値に基づいて条件付き書式設定を適用する**

1. *Aspose.Cells** をダウンロードしてインストールします。
 1. Aspose.Cells for .NET をダウンロードします。
1. 開発用コンピューターにインストールします。
すべての Aspose コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、作成されたドキュメントにウォーターマークが挿入されるだけです。
1. *プロジェクトを作成します**。
 Visual Studio.NET を起動し、新しいコンソール アプリケーションを作成します。この例では C# コンソール アプリケーションを作成しますが、VB.NET も使用できます。
1. *参考文献を追加**。
 Aspose.Cells への参照をプロジェクトに追加します。たとえば、….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。
1. *セルの値に基づいて条件付き書式を適用します。
以下は、タスクを実行するために使用されるコードです。セルに条件付き書式を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのセル「A1」に条件付き書式が適用されます。 A1 に適用される条件付き書式は、セルの値によって異なります。 A1 のセル値が 50 ～ 100 の場合、条件付き書式設定が適用されているため、背景色は赤になります。

##  **Aspose.Cells を使用して数式に基づいて条件付き書式を適用する**

1. 数式に応じて条件付き書式を適用する (コード スニペット)
以下は、タスクを実行するためのコードです。 B3に条件付き書式を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのセル「B3」に条件付き書式が適用されます。適用される条件付き書式は、B1 と B2 の合計として「B3」の値を計算する数式によって異なります。
