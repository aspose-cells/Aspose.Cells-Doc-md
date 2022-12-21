---
title: データ検証
type: docs
weight: 70
url: /ja/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel には、ワークシート データを自動フィルター処理または検証するための優れた機能がいくつか用意されています。

[データ検証](/cells/ja/java/data-validation/)ワークシートに入力されたデータに関するルールを設定する機能です。たとえば、検証を使用して、DATE というラベルの付いた列に日付のみが含まれていること、または別の列に数値のみが含まれていることを確認します。 DATE というラベルの付いた列に、特定の範囲内の日付のみが含まれるようにすることもできます。データ検証を使用すると、ワークシートのセルに入力される内容を制御できます。 Aspose.Cells は、Microsoft Excel のデータ検証およびオートフィルター機能を完全にサポートします。この記事では、Microsoft Excel の機能の使用方法と、Aspose.Cells を使用してそれらをコーディングする方法について説明します。

{{% /alert %}} 
## **データ検証の種類と実行**
Microsoft Excel は、さまざまな種類のデータ検証をサポートしています。各タイプは、セルまたはセル範囲に入力されるデータのタイプを制御するために使用されます。以下のコード スニペットは、それを検証する方法を示しています。

- [数字は整数です](/cells/ja/java/data-validation/)、つまり、小数部分がありません。
- [10 進数は正しい構造に従います](/cells/ja/java/data-validation/).コード例では、セルの範囲に 2 つの小数点以下のスペースが必要であることを定義しています。
- [値は値のリストに制限されています](/cells/ja/java/data-validation/).リストの検証では、セルまたはセル範囲に適用できる個別の値のリストを定義します。
- [日付が特定の範囲内にある](/cells/ja/java/data-validation/).
- [時間は特定の範囲内です](/cells/ja/java/data-validation/).
- [テキストは指定された文字長以内です](/cells/ja/java/data-validation/).
### **Microsoft Excel によるデータ検証**
Microsoft Excel を使用して検証を作成するには:

1. ワークシートで、検証を適用するセルを選択します。
1. から**データ**メニュー、選択**検証**.
検証ダイアログが表示されます。
1. クリック**設定**タブを開き、以下に示すように設定を入力します。

   **データ検証設定** 

![todo:画像_代替_文章](data-validation_1.png)
### **Aspose.Cells によるデータ検証**
データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データ エントリを特定のタイプやサイズに制限したりできます。
 Aspose.Cellsで、それぞれ[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには[検証](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)のコレクションを表すオブジェクト[検証](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)オブジェクト。検証を設定するには、いくつかの[検証](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)クラスのプロパティ:

- [タイプ](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): 検証タイプを表します。これは、[検証タイプ](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)列挙。
- [オペレーター](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator)検証で使用される演算子を表します。これは、[OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)列挙。
- [式1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): データ検証の最初の部分に関連付けられた値または式を表します。
- [フォーミュラ2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): データ検証の 2 番目の部分に関連付けられた値または式を表します。

とき[検証](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)オブジェクトのプロパティが構成されているため、開発者は[セルエリア](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)作成された検証を使用して検証されるセル範囲に関する情報を格納する構造。
#### **データ検証の種類**
データ検証を使用すると、各セルにビジネス ルールを組み込むことができるため、入力が正しくないとエラー メッセージが表示されます。ビジネス ルールは、ビジネスの運営方法を管理するポリシーと手順です。 Aspose.Cells は、重要な種類のデータ検証をすべてサポートしています。

の[検証タイプ](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)列挙には次のメンバーがあります。

|**メンバー名**|**説明**|
|:- |:- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|任意の型の値を示します。|
|[整数](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|整数の検証タイプを示します。|
|[小数](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|10 進数の検証タイプを示します。|
|[リスト](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|ドロップダウン リストの検証タイプを示します。|
|[日にち](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|日付の検証タイプを示します。|
|[時間](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Time の検証タイプを示します。|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|テキストの長さの検証タイプを示します。|
|[習慣](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|カスタム検証タイプを示します。|
#### **プログラミング サンプル: 整数データの検証**
このタイプの検証では、ユーザーは指定された範囲内の整数のみを検証済みのセルに入力できます。以下のコード例は、[整数](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)検証タイプ。この例では、上記の Microsoft Excel を使用して作成したものと同じデータ検証を Aspose.Cells を使用して作成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **プログラミング サンプル: 10 進数データの検証**
このタイプの検証では、ユーザーは検証済みのセルに 10 進数を入力できます。この例では、ユーザーは 10 進数値のみを入力するように制限されており、検証領域は A1:A10 です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **プログラミング サンプル: リスト データの検証**
このタイプの検証では、ユーザーはドロップダウン リストから値を入力できます。データを含む一連の行であるリストを提供します。ユーザーはリストからのみ値を選択できます。検証領域は、最初のワークシートのセル範囲 A1:A5 です。

ここで重要なのは、[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown)プロパティへ**真実**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **プログラミング サンプル: 日付データの検証**
このタイプの検証では、ユーザーは指定された範囲内の日付値、または特定の基準を満たす日付値を検証済みセルに入力します。この例では、ユーザーは 1970 年から 1999 年までの日付を入力するように制限されています。ここでは、検証領域は B1 セルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **プログラミング サンプル: 時間データの検証**
このタイプの検証では、ユーザーは、指定された範囲内の時間を入力するか、いくつかの条件を満たす時間を検証済みのセルに入力できます。この例では、ユーザーは午前 9 時から午前 11 時 30 分までの時間を入力するように制限されています。ここでは、検証領域は B1 セルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **プログラミング サンプル: テキスト長データの検証**
このタイプの検証では、ユーザーは指定された長さのテキスト値を検証済みのセルに入力できます。この例では、ユーザーは 5 文字以下の文字列値を入力するように制限されています。検証領域は B1 セルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **データ検証規則**
データ検証が実装されている場合、セルに異なる値を割り当てることで検証を確認できます。[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) を使用して検証結果を取得できます。次の例は、この機能をさまざまな値で示しています。サンプル ファイルは、テスト用に次のリンクからダウンロードできます。

[SampleDataValidationRules.xlsx](77987849.xlsx)

**サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **セル内の検証がドロップダウンかどうかを確認する**
これまで見てきたように、セル内に実装できる検証には多くの種類があります。バリデーションがドロップダウンかどうかを確認したい場合は、[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown)プロパティを使用してこれをテストできます。次のサンプル コードは、このプロパティの使用方法を示しています。テスト用のサンプル ファイルは、次のリンクからダウンロードできます。

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **CellArea を既存の Validation に追加**
追加したくなるケースもあるかもしれません[セルエリア](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)既存へ[検証](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).追加すると[セルエリア](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)使用して[Validation.AddArea(CellArea セルエリア)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\))、Aspose.Cells は、既存のすべてのエリアをチェックして、新しいエリアが既に存在するかどうかを確認します。ファイルに多数の検証がある場合、パフォーマンスが低下します。これを克服するために、API は[Validation.AddAreaCellArea cellArea、bool checkIntersection、bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)） 方法。の*チェック交差点*パラメータは、特定の領域と既存の検証領域との交差をチェックするかどうかを示します。に設定する**間違い**他の領域のチェックを無効にします。の*チェックエッジ*パラメータは、適用された領域をチェックするかどうかを示します。新しい領域が左上の領域になると、内部設定が再構築されます。新しい領域が左上の領域でないことが確実な場合は、このパラメータを次のように設定できます。**間違い**.

次のコード スニペットは、[Validation.AddAreaCellArea cellArea、bool checkIntersection、bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) 新規追加するメソッド[セルエリア](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)既存へ[検証](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

参照用にソースと出力の Excel ファイルが添付されています。

[ソースファイル](PivotTableHideAndSortSample.xlsx)

[出力ファイル](ValidationsSample_out.xlsx)


## **先行トピック**
- [ODS ファイルで Cell 検証を取得](/cells/ja/java/get-cell-validation-in-ods-files/)
- [Cell に検証を適用する](/cells/ja/java/get-validation-applied-on-a-cell/)
- [Cell 値がデータ検証ルールを満たしていることを確認する](/cells/ja/java/verify-that-cell-value-satisfies-data-validation-rules/)
