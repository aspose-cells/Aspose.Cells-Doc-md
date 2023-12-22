---
title: Cellのテキストを回転する方法
type: docs
weight: 80
url: /ja/net/how-to-rotate-text-of-cell/
description: C# Cell のテキストを Aspose.Cells for .NET API で回転するコード
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Cell のテキストを Aspose.Cells で回転**

Aspose.Cells は、開発者がプログラムで Excel スプレッドシートを操作できるようにする強力な .NET および Java コンポーネントです。 Aspose.Cells が提供する機能の 1 つはセルを回転する機能で、これによりテキストの向きをカスタマイズし、データの視覚的な表示を改善できます。このドキュメントでは、Aspose.Cells を使用してセルを回転する方法を説明します。

##  **ExcelでCellのテキストを回転する方法**
Excel でセルを回転するには、次の手順を実行できます。
1. Excel を開き、回転するセルまたはセル範囲を選択します。
1. 選択したセルを右クリックし、コンテキスト メニューから「Cells の書式設定」を選択します。または、Excel リボンの [ホーム] タブに移動し、[Cells] グループの [書式] ドロップダウンをクリックして、[Cells の書式設定] を選択することもできます。
1. 「Cellsの形式」ダイアログボックスで、「配置」タブに移動します。
1. 「方向」セクションの下に、テキストを回転するオプションが表示されます。 「度」ボックスに希望の回転角度を度単位で直接入力できます。正の値を指定するとテキストが反時計回りに回転し、負の値を指定すると時計回りに回転します。
<br>
![todo:image_alt_text](alignment.png)
1. 希望の回転を選択したら、「OK」をクリックして変更を適用します。選択したセルが、選択した回転角度または方向に基づいて回転されます。

##  **Aspose.Cells API を使用して Cell のテキストを回転する方法**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/)プロパティを使用すると、セルを回転するのに便利です。 Aspose.Cells のセルを回転するには、次の手順に従う必要があります。
1. Excel ワークブックをロードする
<br>
まず、Aspose.Cells を使用して Excel ワークブックをロードする必要があります。Workbook クラスを使用して、既存の Excel ファイルを開いたり、新しい Excel ファイルを作成したりできます。

1. ワークシートにアクセスする
<br>
ワークブックが読み込まれたら、セルを回転するワークシートにアクセスする必要があります。ワークシートにはインデックスまたは名前でアクセスできます。

1. Cellのテキストを回転します
<br>
ワークシートにアクセスできるようになったので、目的のセルの Style オブジェクトを変更してセルを回転できます。 Style オブジェクトを使用すると、回転などのさまざまな書式設定オプションを設定できます。

1. ワークブックを保存する
<br>
セルを回転した後、Save メソッドを使用して、変更したワークブックをファイルまたはストリームに保存し直すことができます。

##  **C# サンプルコード**

次のコードを参照してください。ワークブック オブジェクトを作成し、複数のセルに異なる回転角度を設定します。スクリーンショットは、サンプル コードの実行後の結果を示しています。
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
