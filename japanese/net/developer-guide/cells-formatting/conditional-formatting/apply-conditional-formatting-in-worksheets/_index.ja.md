---
title: ワークシートに条件付き書式設定を適用する
description: C#でAspose.Cellsライブラリを使用して、ワークシートに条件付き書式を適用する方法について説明します。これらの基準を調整することで、セルの外観と表示に対するより多くの制御が可能です。
keywords: Aspose.Cells, 条件付き書式, C#, ワークシート, 書式
type: docs
weight: 130
url: /ja/net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

この記事では、ワークシートのセル範囲に条件付き書式設定を追加する方法について詳しく説明しています。

条件付き書式設定は、Microsoft Excelの高度な機能であり、セルの値や数式の値に応じて書式を適用し、その書式を変更することを可能にします。たとえば、セルの背景が赤くなるとマイナスの値が強調表示されたり、テキストの色が緑色になるとプラスの値が強調表示されます。セルの値が条件を満たしている場合、書式が適用されます。セルの値が条件を満たしていない場合、セルのデフォルトの書式が使用されます。

Microsoft Office Automationで条件付き書式設定を適用することは可能ですが、その欠点があります。たとえば、セキュリティ、安定性、拡張性、速度などの理由や問題が存在します。他のソリューションを探す主な理由は、Microsoft自体がソフトウェアソリューション向けにOffice Automationを強く推奨していないことです。

この記事では、Aspose.Cells APIを使用して、わずか数行のコードでセルに条件付き書式設定を追加するコンソールアプリケーションを作成する方法を示しています。

{{% /alert %}}

## **セルの値に基づいた条件付き書式を適用するためのAspose.Cellsの使用**

1. **Aspose.Cellsをダウンロードしてインストールします。**
   1. Aspose.Cells for .NETをダウンロードします。
1. 開発コンピュータにインストールします。
   すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。
1. **プロジェクトを作成します**。
   Visual Studio.NETを起動し、新しいコンソールアプリケーションを作成します。この例ではC#のコンソールアプリケーションを作成しますが、VB.NETも使用できます。
1. **参照を追加します。**
   プロジェクトにAspose.Cellsへの参照を追加します。たとえば、….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dllへの参照を追加します。
1. *セルの値に基づいて条件付き書式を適用します。
   以下はそのタスクを達成するために使用されるコードです。セルに条件付き書式を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのセル“A1”に条件付き書式が適用されます。A1のセル値に応じて条件付き書式が適用されます。A1のセル値が50から100の間の場合、条件付き書式が適用されて背景色が赤になります。

## **Aspose.Cellsを使用してセルの値に基づいた条件付き書式を適用する**

1. 数式に応じて条件付き書式を適用する（コードスニペット）
   以下はそのタスクを達成するためのコードです。B3に条件付き書式を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのセル“B3”に条件付き書式が適用されます。適用された条件付き書式は、B1とB2の値を合計する数式に依存します。
