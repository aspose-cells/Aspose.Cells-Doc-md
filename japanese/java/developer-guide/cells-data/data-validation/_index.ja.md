---
title: データ検証
type: docs
weight: 70
url: /ja/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel はワークシートデータの自動フィルタリングや検証に役立つ機能を提供しています。

[データ検証](/cells/ja/java/data-validation/) は、ワークシートに入力されたデータに関するルールを設定する機能です。たとえば、DATE という列には日付のみが含まれるようにし、別の列には数字のみが含まれるようにするなど、検証を使用してできることがあります。特定の範囲内の日付のみを含むようにすることもできます。データ検証を使用すると、ワークシート内のセルに入力される内容を制御できます。Aspose.Cells は、Microsoft Excel のデータ検証と自動フィルター機能を完全にサポートしています。この記事では、Microsoft Excel の機能の使用方法と、Aspose.Cells を使用したコードについて説明します。

{{% /alert %}} 
## **データ検証の種類と実行**
Microsoft Excel はさまざまな種類のデータ検証をサポートしています。それぞれの種類は、セルまたはセル範囲に入力されるデータの種類を制御するために使用されます。以下は、それぞれの種類を確認するためのコードスニペットの例です。

- [整数であること](/cells/ja/java/data-validation/)、つまり、小数部がないことを検証します。
- [小数点数が正しい構造に従うこと](/cells/ja/java/data-validation)を検証します。コード例で、セル範囲に対して小数部が 2 つあることを定義します。
- [値が特定の値のリストに制限されること](/cells/ja/java/data-validation)を検証します。リスト検証では、セルまたはセル範囲に適用できる別々の値リストを定義します。
- [日付が特定の範囲内にあること](/cells/ja/java/data-validation)を検証します。
- [時間が特定の範囲内にあること](/cells/ja/java/data-validation)を検証します。
- [テキストが指定の文字数範囲内にあること](/cells/ja/java/data-validation)を検証します。
### **Microsoft Excel でデータ検証**
Microsoft Excel を使用して検証を作成するには:

1. ワークシートで、検証を適用したいセルを選択します。
1. **データ** メニューから **検証** を選択します。
   検証のダイアログが表示されます。
1. **設定** タブをクリックして、以下に示すように設定を入力します。 

   **データ検証の設定** 

![todo:image_alt_text](data-validation_1.png)
### **Aspose.Cells を使用したデータ検証**
データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データの入力を特定のタイプやサイズに制限したりすることができます。
Aspose.Cellsでは、各[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、[Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)オブジェクトがあり、これは[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)オブジェクトのコレクションを表します。検証を設定するには、いくつかの[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)クラスのプロパティを設定します:

- [Type](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): 検証タイプを表し、[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)列挙型の事前定義された値の1つを使用して指定できます。
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): 検証で使用する演算子を表し、[OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)列挙型の事前定義された値の1つを使用して指定できます。
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): データ検証の最初の部分に関連付けられた値や式を表します。
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): データ検証の2番目の部分に関連付けられた値や式を表します。

[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)オブジェクトのプロパティが構成されたら、開発者は作成した検証を使用して検証されるセル範囲に関する情報を保存するために[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)構造を使用できます。
#### **データ検証の種類**
データ検証を使用すると、各セルにビジネスルールを組み込み、不正確なエントリがエラーメッセージを引き起こすようにすることができます。ビジネスルールとは、ビジネスが運営される方法を規定する方針と手順です。Aspose.Cellsはすべての重要なデータ検証の種類をサポートしています。

[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)列挙型には、次のメンバーがあります:

|**メンバー名**|**説明**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY-VALUE)|任意の型の値を示します。|
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE-NUMBER)|整数値の検証タイプを示します。|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|：10進数の検証タイプを示します。
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|：ドロップダウンリストの検証タイプを示します。
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|：日付の検証タイプを示します。
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|：時間の検証タイプを示します。
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT-LENGTH)|テキストの長さの検証タイプを示します。|
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|：カスタム検証のタイプを示します。
#### **プログラミングサンプル: 整数のデータ検証**
この種類の検証により、ユーザーは指定された範囲内の整数のみを入力可能にできます。以下の例は [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE-NUMBER) 検証タイプの実装例です。この例では Microsoft Excel で作成したのと同じデータ検証を Aspose.Cells を使用して作成しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **プログラミングサンプル: 10進数のデータ検証**
このタイプの検証では、ユーザーは検証済みのセルに10進数を入力できます。例では、ユーザーは10進数の値のみを入力するように制限され、検証領域はA1:A10です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **プログラミングサンプル: リストのデータ検証**
このタイプの検証では、ユーザーはドロップダウンリストから値を入力できます。一連のデータを含む行のリストが提供されます。ユーザーはリストからの値のみを選択できます。検証領域は、最初のワークシートのセル範囲A1:A5です。

ここで重要なのは、[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown)プロパティを**true**に設定することです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **プログラミングサンプル: 日付のデータ検証**
このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の日付値、または特定の条件を満たす日付値を入力できます。例では、ユーザーは1970年から1999年の間の日付を入力することに制限されます。ここでは、検証領域はB1セルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **プログラミングサンプル: 時間のデータ検証**
このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の時刻、または特定の条件を満たす時刻を入力できます。例では、ユーザーは午前09:00から11:30の間の時間のみを入力するように制限されます。ここでは、検証領域はB1セルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **プログラミングサンプル：テキスト長データ検証**
このタイプの検証を使用すると、ユーザーは検証されたセルに指定された長さのテキスト値を入力できます。例では、ユーザーは5文字を超えない文字列値を入力することが制限されています。検証エリアはB1セルです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **データ検証ルール**
データバリデーションが実装されている場合、セルに異なる値を割り当てて検証を確認できます。[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)を使用して検証結果を取得できます。以下の例は、異なる値を使ったこの機能のデモです。テスト用のサンプルファイルは以下のリンクからダウンロード可能です。

[SampleDataValidationRules.xlsx](77987849.xlsx)

**サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **セルの検証がドロップダウンかどうかをチェックする**
セル内に実装できる検証の多くの種類があることが分かりました。検証がドロップダウンかどうかをチェックしたい場合は、[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) プロパティを使用してテストできます。次のサンプルコードは、このプロパティの使用法を実証しています。テスト用のサンプルファイルを以下のリンクからダウンロードできます:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **既存の検証にCellAreaを追加**
既存の[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)に[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)を追加したい場合があります。[Validation.AddArea(CellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-)を使用すると、Aspose.Cellsは既存のエリアをすべて確認して、新しいエリアが既に存在しているかどうかを確認します。ファイルに大量のバリデーションがある場合、パフォーマンスに影響します。これを回避するために、APIは[Validation.AddAreaCellArea(cellArea, checkIntersection, checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-boolean-boolean-)メソッドを提供します。*checkIntersection* パラメータは、指定したエリアと既存のバリデーションエリアの交差を確認するかどうかを示します。`false`に設定すると、他のエリアの確認が無効になります。 *checkEdge* パラメータは、適用済みのエリアを確認するかどうかを示します。新しいエリアが左上のエリアになる場合、内部設定が再構築されます。新しいエリアが左上のエリアでないと確信している場合は、このパラメータを *false* に設定できます。

以下のコードスニペットは、[Validation.AddAreaCellArea](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-boolean-boolean-) メソッドを使用して、既存の[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)に新しい[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)を追加する例です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

ソースエクセルファイルと出力エクセルファイルが添付されています。

[ソースファイル](PivotTableHideAndSortSample.xlsx)

[出力ファイル](ValidationsSample_out.xlsx)


## **高度なトピック**
- [ODS ファイルでのセル検証を取得](/cells/ja/java/get-cell-validation-in-ods-files/)
- [セルに適用された検証を取得する](/cells/ja/java/get-validation-applied-on-a-cell/)
- [セルの値がデータ検証ルールを満たすかどうかを確認する](/cells/ja/java/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="java" >}}
