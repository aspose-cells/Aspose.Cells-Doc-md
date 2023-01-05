---
title: ワークシートに条件付き書式を適用する
type: docs
weight: 130
url: /ja/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

この記事は、ワークシートのセル範囲に条件付き書式を追加する方法を詳しく説明することを目的としています。

条件付き書式は Microsoft Excel の高度な機能で、セルの範囲に書式を適用し、セルの値または数式の値に応じて書式を変更できます。たとえば、セルの背景を赤色にして負の値を強調したり、テキストの色を緑色にして正の値にしたりすることができます。セルの値がフォーマット条件を満たしている場合、フォーマットが適用されます。セルの値がフォーマット条件を満たさない場合、セルのデフォルトのフォーマットが使用されます。

Microsoft Office Automation で条件付き書式を適用することは可能ですが、これには欠点があります。関連する理由と問題はいくつかあります。たとえば、セキュリティ、安定性、スケーラビリティ、速度などです。別のソリューションを見つける主な理由は、Microsoft 自身がソフトウェア ソリューションに Office Automation を使用しないことを強く推奨しているためです。

この記事では、コンソール アプリケーションを作成し、Aspose.Cells API.

{{% /alert %}}

## **Aspose.Cells を使用して、Cell 値に基づいて条件付き書式を適用する**

1. **Aspose.Cells をダウンロードしてインストールします**.
1. Aspose.Cells for .NET をダウンロードします。
1. 開発用コンピューターにインストールします。
Aspose コンポーネントはすべて、インストールすると評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. **プロジェクトを作成する**.
 Visual Studio.NET を起動し、新しいコンソール アプリケーションを作成します。この例では、C# コンソール アプリケーションを作成しますが、VB.NET も使用できます。
1. **参照を追加する**.
プロジェクトに Aspose.Cells への参照を追加します。たとえば、….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。
1. *セルの値に基づいて条件付き書式を適用します。
以下は、タスクを実行するために使用されるコードです。セルに条件付き書式を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

上記のコードを実行すると、出力ファイル (output.xls) の最初のワークシートのセル「A1」に条件付き書式が適用されます。 A1 に適用される条件付き書式は、セルの値によって異なります。 A1 のセル値が 50 ～ 100 の場合、条件付き書式が適用されているため、背景色は赤になります。

## **Aspose.Cells を使用して数式に基づく条件付き書式を適用する**

1. 数式に応じた条件付き書式の適用 (コード スニペット)
以下は、タスクを実行するためのコードです。 B3 に条件付き書式を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのセル「B3」に条件付き書式が適用されます。適用される条件付き書式は、「B3」の値を B1 と B2 の合計として計算する式によって異なります。
