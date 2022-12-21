---
title: 空のワークシートの検出
type: docs
weight: 410
url: /ja/net/detecting-empty-worksheets/
---
## **設定済みの Cells を確認します**

ワークシートには、値が単純な値 (テキスト、数値、日付/時刻)、数式、または数式ベースの値である値が入力された 1 つ以上のセルを含めることができます。このような場合、特定のワークシートが空かどうかは簡単に検出できます。私たちがチェックしなければならないのは、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)また[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)プロパティ。前述のプロパティが 0 または正の値を返す場合は、1 つ以上のセルが入力されていることを意味しますが、これらのプロパティのいずれかが -1 を返す場合は、指定されたワークシートにセルが入力されていないことを示します。

{{% alert color="primary" %}}

行と列のコレクションにはゼロベースのインデックスがあるため、行 0 と列 0 のセルは、ワークシートの最初のセルである A1 を意味します。

{{% /alert %}}

## **空の初期化済み Cells を確認します**

値を持つすべてのセルは自動的に初期化されますが、ワークシートに書式設定のみが適用されたセルが含まれる可能性があります。このようなシナリオでは、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)また[**Cells.MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn)プロパティは、入力された値がないことを示す -1 を返しますが、セルの書式設定のために初期化されたセルは、この方法では検出できません。ワークシートに空の初期化セルがあるかどうかを確認するには、取得した列挙子で IEnumerator.MoveNext メソッドを使用することをお勧めします。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。 IEnumerator.MoveNext メソッドが返す場合**真実**これは、指定されたワークシートに 1 つ以上の初期化されたセルがあることを意味します。

## **形状の確認**

特定のワークシートにセルが入力されていない可能性がありますが、コントロール、チャート、画像などの図形やオブジェクトが含まれている可能性があります。ワークシートに形状が含まれているかどうかを確認する必要がある場合は、[**ShapeCollection.Count**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)財産。正の値は、ワークシートに図形が存在することを示します。

## **プログラミングサンプル**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectEmptyWorksheets-DetectEmptyWorksheets.cs" >}}
