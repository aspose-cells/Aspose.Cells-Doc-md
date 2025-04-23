---
title: データ検証
type: docs
weight: 90
url: /ja/net/data-validation/
description: Aspose.Cells for .NETのAPIを通じてデータ検証の追加方法を学ぶ。
keywords: データ検証を追加し、検証値を取得する、整数データ検証を追加する、リストデータ検証を追加する、日付データ検証を追加する、時間データ検証を追加する、テキスト長データ検証を追加する、既存の検証にCellAreaを追加する、セルの検証がドロップダウンかどうかをチェックする、カスタム検証を追加する。  
---

{{% alert color="primary" %}}

Microsoft Excelは、ワークシートデータの自動フィルタリングや検証に関する優れた機能を提供しています。Aspose.CellsはMicrosoft Excelのデータ検証と自動フィルタリング機能を完全にサポートしています。この記事では、Microsoft Excelの機能の使用方法と、Aspose.Cellsを使用したコーディング方法について説明しています。

{{% /alert %}}

## **データ検証の種類と実行**

データ検証は、ワークシートに入力されたデータに関するルールを設定する機能です。たとえば、「日付」と記載された列には日付のみが含まれるようにし、他の列には数字のみが含まれるようにすることができます。あるいは、「日付」と記載された列には特定の範囲内の日付のみが含まれるようにすることもできます。データ検証を使用すると、ワークシートのセルに入力される内容を制御することができます。

Microsoft Excel はさまざまな種類のデータ検証をサポートしています。それぞれの種類は、セルまたはセル範囲に入力されるデータの種類を制御するために使用されます。以下は、それぞれの種類を確認するためのコードスニペットの例です。

- 数値が整数で、つまり小数部を持たないこと。
- 小数点以下の桁に構造が正しいこと。コード例では、セルの範囲に2つの小数点以下があることを定義しています。
- 一覧からの値に制限されていること。一覧の検証では、セルやセル範囲に適用する別々の値の一覧が定義されます。
- 特定の範囲内の日付であること。
- 特定の範囲内の時間であること。
- 指定された文字長内のテキストであること。

### **Microsoft Excel でデータ検証**

Microsoft Excel を使用して検証を作成するには:

1. ワークシートで、検証を適用したいセルを選択します。
2. **データ** メニューから **検証** を選択します。 検証のダイアログが表示されます。
3. **設定** タブをクリックし、設定を入力します。

### **Aspose.Cells を使用したデータ検証**

データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データの入力を特定のタイプやサイズに制限したりすることができます。
Aspose.Cellsでは、各[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには[**Validations**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)プロパティがあり、[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)オブジェクトのコレクションを表します。検証を設定するには、[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)クラスのいくつかのプロパティを以下のように設定します:

- Type：[**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)列挙型の定義された値のいずれかを使用して指定された検証タイプを表します。
- Operator – 検証で使用される演算子を表し、[**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype) 列挙型で定義された事前定義の値のいずれかを使用して指定できます。
- Formula1：データ検証の最初の部分に関連付けられた値または式を表します。
- Formula2：データ検証の2番目の部分に関連付けられた値または式を表します。

{0} オブジェクトのプロパティが構成されたら、開発者は作成された検証を使用して、{@1} 構造を使用して検証を行う予定のセル範囲に関する情報を保存できます。

#### **データ検証の種類**

[**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype) 列挙型には、次のメンバーがあります:

|**メンバー名**|**説明**|
| :- | :- |
|AnyValue|任意の型の値を示します。
|WholeNumber|整数の検証タイプを示します。
|Decimal|10進数の検証タイプを示します。 |
|List|ドロップダウンリストの検証タイプを示します。 |
|Date|日付の検証タイプを示します。 |
|Time|時刻の検証タイプを示します。 |
|TextLength|テキストの長さの検証タイプを示します。 |
|Custom|カスタム検証タイプを示します。 |

##### **整数データの検証**

この種類の検証を使用すると、検証されたセルに指定された範囲内の整数のみを入力できます。以下のコード例では、WholeNumber検証タイプを実装する方法が示されています。例では、Microsoft Excelで作成したデータ検証と同じデータ検証をAspose.Cellsを使用して作成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **リストデータの検証**

この種類の検証では、ユーザーはドロップダウンリストから値を入力できます。リストにはデータを含む一連の行があります。この例では、リストのソースを保持するために2番目のワークシートが追加されます。ユーザーはリストからのみ値を選択できます。検証エリアは最初のワークシートのセル範囲 A1:A5 です。

ここで重要な点は、[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)プロパティを **true** に設定することです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **日付データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の日付値、または特定の条件を満たす日付値を入力できます。例では、ユーザーは1970年から1999年の間の日付を入力することに制限されます。ここでは、検証領域はB1セルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **時間データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の時刻、または特定の条件を満たす時刻を入力できます。例では、ユーザーは午前09:00から11:30の間の時間のみを入力するように制限されます。ここでは、検証領域はB1セルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **テキスト長のデータ検証**

このタイプの検証を使用すると、ユーザーは検証されたセルに指定された長さのテキスト値を入力できます。例では、ユーザーは5文字を超えない文字列値を入力することが制限されています。検証エリアはB1セルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **データ検証ルール**

データ検証が実装されている場合、セルに異なる値を割り当てて検証を確認できます。 [**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) は検証結果を取得するために使用できます。次の例では、異なる値を使用してこの機能をデモンストレーションしています。テスト用のサンプルファイルは、次のリンクからダウンロードできます。

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **セルの検証がドロップダウンであるかどうかをチェック**

検証がドロップダウンかどうかを確認する

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **既存の検証にCellAreaを追加**

既存の検証に [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) を追加する場合があります。[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea) を使用して [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) を追加する場合、Aspose.Cells は新しいエリアがすでに存在するかどうかをチェックします。ファイルに検証が多数ある場合は、これにパフォーマンスの影響があります。これを克服するために、APIは [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) メソッドを提供します。 *checkIntersection* パラメーターは、指定されたエリアと既存の検証エリアとの交差をチェックするかどうかを示します。これを **false** に設定すると、他のエリアをチェックしないようになります。 *checkEdge* パラメーターは、適用エリアをチェックするかどうかを示します。新しいエリアが左上のエリアになる場合、内部設定が再構築されます。新しいエリアが左上のエリアでないことを確信している場合、このパラメーターを **false** に設定できます。

新しい[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)を既存の[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)に追加する[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1)メソッドの使用を示すコードスニペット。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

ソースエクセルファイルと出力エクセルファイルが添付されています。

[ソースファイル](96928093.xlsx)

[出力ファイル](96928220.xlsx)


## **高度なトピック**
- [ODS ファイルでのセル検証を取得](/cells/ja/net/get-cell-validation-in-ods-files/)
- [セルに適用された検証を取得する](/cells/ja/net/get-validation-applied-on-a-cell/)
- [セルの値がデータ検証ルールを満たすかどうかを確認する](/cells/ja/net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="csharp" >}}
