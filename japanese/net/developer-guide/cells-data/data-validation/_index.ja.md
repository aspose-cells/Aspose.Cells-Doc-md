---
title: データ検証
type: docs
weight: 90
url: /ja/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel には、ワークシートのデータを自動フィルター処理または検証するための優れた機能がいくつか用意されています。この記事では、Microsoft Excel の機能を使用する方法と、Aspose.Cells を使用してそれらをコーディングする方法について説明します。

{{% /alert %}}

## **データ検証の種類と実行**

データ検証は、ワークシートに入力されたデータに関するルールを設定する機能です。たとえば、検証を使用して、DATE というラベルの付いた列に日付のみが含まれていること、または別の列に数値のみが含まれていることを確認します。 DATE というラベルの付いた列に、特定の範囲内の日付のみが含まれるようにすることもできます。データ検証を使用すると、ワークシートのセルに入力される内容を制御できます。

Microsoft Excel は、さまざまな種類のデータ検証をサポートしています。各タイプは、セルまたはセル範囲に入力されるデータのタイプを制御するために使用されます。以下のコード スニペットは、それを検証する方法を示しています。

- Numbers は整数です。つまり、小数部分がありません。
- 10 進数は正しい構造に従います。コード例では、セルの範囲に 2 つの小数点以下のスペースが必要であることを定義しています。
- 値は値のリストに制限されています。リストの検証では、セルまたはセル範囲に適用できる個別の値のリストを定義します。
- 日付は特定の範囲内にあります。
- 時間は特定の範囲内です。
- テキストは指定された文字長以内です。

### **Microsoft Excel によるデータ検証**

Microsoft Excel を使用して検証を作成するには:

1. ワークシートで、検証を適用するセルを選択します。
1. から**データ**メニュー、選択**検証**.検証ダイアログが表示されます。
1. クリック**設定**タブを開き、設定を入力します。

### **Aspose.Cells によるデータ検証**

データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データ エントリを特定のタイプやサイズに制限したりできます。
 Aspose.Cellsで、それぞれ[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[**検証**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)のコレクションを表すプロパティ[**検証**](https://reference.aspose.com/cells/net/aspose.cells/validation)オブジェクト。検証を設定するには、いくつかの[**検証**](https://reference.aspose.com/cells/net/aspose.cells/validation)クラスのプロパティは次のとおりです。

- Type – 検証タイプを表します。これは、[**検証タイプ**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)列挙。
- 演算子 – 検証で使用される演算子を表します。これは、[**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)列挙。
- Formula1 – データ検証の最初の部分に関連付けられた値または式を表します。
- Formula2 – データ検証の 2 番目の部分に関連付けられた値または式を表します。

とき[**検証**](https://reference.aspose.com/cells/net/aspose.cells/validation)オブジェクトのプロパティが構成されているため、開発者は[**セルエリア**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)作成された検証を使用して検証されるセル範囲に関する情報を格納する構造。

#### **データ検証の種類**

の[**検証タイプ**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)列挙には次のメンバーがあります。

|**メンバー名**|**説明**|
|:- |:- |
|AnyValue|任意の型の値を示します。|
|整数|整数の検証タイプを示します。|
|小数|10 進数の検証タイプを示します。|
|リスト|ドロップダウン リストの検証タイプを示します。|
|日にち|日付の検証タイプを示します。|
|時間|時間の検証タイプを示します。|
|テキストの長さ|テキストの長さの検証タイプを示します。|
|カスタム|カスタム検証タイプを示します。|

##### **整数データの検証**

このタイプの検証では、ユーザーは指定された範囲内の整数のみを検証済みのセルに入力できます。以下のコード例は、WholeNumber 検証タイプを実装する方法を示しています。この例では、上記の Microsoft Excel を使用して作成したものと同じデータ検証を Aspose.Cells を使用して作成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **リスト データの検証**

このタイプの検証では、ユーザーはドロップダウン リストから値を入力できます。データを含む一連の行であるリストを提供します。この例では、リスト ソースを保持するために 2 番目のワークシートが追加されます。ユーザーはリストからのみ値を選択できます。検証領域は、最初のワークシートのセル範囲 A1:A5 です。

ここで重要なのは、[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **日付データの検証**

このタイプの検証では、ユーザーは指定された範囲内の日付値、または特定の基準を満たす日付値を検証済みセルに入力します。この例では、ユーザーは 1970 年から 1999 年までの日付を入力するように制限されています。ここでは、検証領域は B1 セルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **時間データの検証**

このタイプの検証では、ユーザーは、指定された範囲内の時間を入力するか、いくつかの条件を満たす時間を検証済みのセルに入力できます。この例では、ユーザーは午前 9 時から午前 11 時 30 分までの時間を入力するように制限されています。ここでは、検証領域は B1 セルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **テキスト長データの検証**

このタイプの検証では、ユーザーは指定された長さのテキスト値を検証済みのセルに入力できます。この例では、ユーザーは 5 文字以下の文字列値を入力するように制限されています。検証領域は B1 セルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **データ検証規則**

データ検証が実装されている場合、セルに異なる値を割り当てることで検証を確認できます。[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)検証結果を取得するために使用できます。次の例は、この機能をさまざまな値で示しています。サンプル ファイルは、テスト用に次のリンクからダウンロードできます。

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **セルの検証がドロップダウンかどうかを確認します**

これまで見てきたように、セル内に実装できる検証には多くの種類があります。バリデーションがドロップダウンかどうかを確認したい場合は、[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)プロパティを使用してこれをテストできます。次のサンプル コードは、このプロパティの使用方法を示しています。テスト用のサンプル ファイルは、次のリンクからダウンロードできます。

[サンプル検証.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **CellArea を既存の Validation に追加**

追加したくなるケースもあるかもしれません[**セルエリア**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)既存へ[**検証**](https://reference.aspose.com/cells/net/aspose.cells/validation).追加すると[**セルエリア**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)使用して[**Validation.AddArea(CellArea セルエリア)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea)、Aspose.Cells は、すべての既存のエリアをチェックして、新しいエリアが既に存在するかどうかを確認します。ファイルに多数の検証がある場合、パフォーマンスが低下します。これを克服するために、API は[**Validation.AddAreaCellArea cellArea、bool checkIntersection、bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1)方法。の*チェック交差点*パラメータは、特定の領域と既存の検証領域との交差をチェックするかどうかを示します。に設定する**間違い**他の領域のチェックを無効にします。の*チェックエッジ*パラメータは、適用された領域をチェックするかどうかを示します。新しい領域が左上の領域になると、内部設定が再構築されます。新しい領域が左上の領域でないことが確実な場合は、このパラメータを次のように設定できます。**間違い**.

次のコード スニペットは、[**Validation.AddAreaCellArea cellArea、bool checkIntersection、bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1)新規追加方法[**セルエリア**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)既存へ[**検証**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

参照用にソースと出力の Excel ファイルが添付されています。

[ソースファイル](96928093.xlsx)

[出力ファイル](96928220.xlsx)


## **先行トピック**
- [ODS ファイルで Cell 検証を取得する](/cells/ja/net/get-cell-validation-in-ods-files/)
- [Cell に検証を適用する](/cells/ja/net/get-validation-applied-on-a-cell/)
- [Cell 値がデータ検証ルールを満たしていることを確認する](/cells/ja/net/verify-that-cell-value-satisfies-data-validation-rules/)
