---
title: 空のワークシートの検出
type: docs
weight: 410
url: /ja/net/detecting-empty-worksheets/
description: この記事では、C# API ライブラリと .NET を使用して、Excel ブックの空のワークシートをプログラムで検出する方法を説明するコードを示します。
keywords: detect empty worksheet c#, find empty excel worksheet c#
---
##  **入力済みの Cells を確認してください**

ワークシートには、値を入力した 1 つ以上のセルを含めることができます。値は、単純な値 (テキスト、数値、日付/時刻)、または数式または数式ベースの値にすることができます。このような場合、特定のワークシートが空かどうかを簡単に検出できます。私たちが確認しなければならないのは、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)また[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)プロパティ。前述のプロパティが 0 または正の値を返す場合は、1 つ以上のセルが設定されていることを意味しますが、これらのプロパティのいずれかが -1 を返す場合は、指定されたワークシートにどのセルも設定されていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションには 0 から始まるインデックスがあるため、行 0 と列 0 のセルはワークシートの最初のセル (A1) を意味します。

{{% /alert %}}

##  **空の初期化済みを確認 Cells**

値を持つすべてのセルは自動的に初期化されますが、ワークシートには書式設定のみが適用されたセルが含まれる可能性があります。このようなシナリオでは、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)また[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)プロパティは、値が設定されていないことを示す -1 を返しますが、セルの書式設定が原因で初期化されたセルは、このアプローチでは検出できません。ワークシートに空の初期化されたセルがあるかどうかを確認するには、から取得した列挙子に対して IEnumerator.MoveNext メソッドを使用することをお勧めします。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。 IEnumerator.MoveNext メソッドが返った場合**真実**これは、指定されたワークシートに 1 つ以上の初期化されたセルがあることを意味します。

##  **形状の確認**

特定のワークシートにデータが入力されたセルがない可能性もありますが、コントロール、グラフ、画像などの図形やオブジェクトが含まれている可能性があります。ワークシートに何らかの形状が含まれているかどうかを確認する必要がある場合は、[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)財産。正の値は、ワークシート内に形状が存在することを示します。

##  **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
