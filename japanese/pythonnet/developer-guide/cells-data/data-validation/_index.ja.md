---
title: データ検証
type: docs
weight: 90
url: /ja/python-net/data-validation/
description: Aspose.Cells for Python via .NET API を使用してデータ検証を追加する方法を学ぶ。
keywords: Python Excel ライブラリ、Python データ検証の追加、Python 検証値の取得、Python 整数のデータ検証の追加、Python リストのデータ検証の追加、Python 日付のデータ検証の追加、Python 時間のデータ検証の追加、Python テキスト長のデータ検証の追加、既存の検証に CellArea を追加する方法、セルの検証がドロップダウンかどうかを確認する方法、カスタム検証の追加  
---

{{% alert color="primary" %}}

Microsoft Excel はワークシートデータの自動フィルタリングや検証に関する優れた機能を提供します。Aspose.Cells for Python via .NET は Microsoft Excel のデータ検証と自動フィルター機能を完全にサポートしています。この記事では、Microsoft Excel の機能の使用方法と、Aspose.Cells for Python via .NET を使用してこれらの機能をコーディングする方法について説明します。

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

### **Aspose.Cells for Python Excel Library でのデータ検証**

データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データの入力を特定のタイプやサイズに制限したりすることができます。
Aspose.Cells for Python via .NET では、各 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスには [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) プロパティがあり、これは [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) オブジェクトのコレクションを表します。検証を設定するには、[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) クラスのいくつかのプロパティを次のように設定します:

- type – 検証のタイプを表し、[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) 列挙型で定義された事前定義の値のいずれかを使用して指定できます。
- Operator – 検証で使用される演算子を表し、[**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype) 列挙型で定義された事前定義の値のいずれかを使用して指定できます。
- formula1 – データ検証の最初の部分に関連付けられた値または式を表します。
- formula2 – データ検証の2番目の部分に関連付けられた値または式を表します。

{0} オブジェクトのプロパティが構成されたら、開発者は作成された検証を使用して、{@1} 構造を使用して検証を行う予定のセル範囲に関する情報を保存できます。

#### **データ検証の種類**

[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) 列挙型には、次のメンバーがあります:

|**メンバー名**|**説明**|
| :- | :- |
|ANY_VALUE|任意のタイプの値を示します。
|WHOLE_NUMBER|整数の検証タイプを示します。
DECIMAL数値の検証タイプを示します。
LISTドロップダウンリストの検証タイプを示します。
|DATE|日付の検証タイプを示します。
TIME時間の検証タイプを示します。
|TEXT_LENGTH|テキストの長さの検証タイプを示します。
CUSTOMカスタム検証タイプを示します。

##### **整数データの検証**

この種類の検証では、ユーザーは検証されたセルに指定された範囲内の整数のみを入力できます。以下のコード例では、WholeNumber検証タイプを実装する方法が示されます。この例では、マイクロソフトエクセルで作成したものと同じデータ検証を Aspose.Cells for Python via .NET を使用して作成します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **リストデータの検証**

この種類の検証では、ユーザーはドロップダウンリストから値を入力できます。リストにはデータを含む一連の行があります。この例では、リストのソースを保持するために2番目のワークシートが追加されます。ユーザーはリストからのみ値を選択できます。検証エリアは最初のワークシートのセル範囲 A1:A5 です。

ここで重要な点は、[**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/)プロパティを **true** に設定することです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **日付データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の日付値、または特定の条件を満たす日付値を入力できます。例では、ユーザーは1970年から1999年の間の日付を入力することに制限されます。ここでは、検証領域はB1セルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **時間データの検証**

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の時刻、または特定の条件を満たす時刻を入力できます。例では、ユーザーは午前09:00から11:30の間の時間のみを入力するように制限されます。ここでは、検証領域はB1セルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **テキスト長のデータ検証**

このタイプの検証を使用すると、ユーザーは検証されたセルに指定された長さのテキスト値を入力できます。例では、ユーザーは5文字を超えない文字列値を入力することが制限されています。検証エリアはB1セルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **データ検証ルール**

データ検証が実装されている場合、検証はセルに異なる値を割り当てて確認できます。[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) を使用して検証結果を取得できます。次の例は、異なる値を使用してこの機能をカバーしています。テスト用のサンプルファイルは次のリンクからダウンロードできます。

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **セルの検証がドロップダウンであるかどうかをチェック**

検証がドロップダウンかどうかを確認する

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **既存の検証にCellAreaを追加**

既存の検証に [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) を追加する場合があります。[**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea) を使用して [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) を追加する場合、Aspose.Cells は新しいエリアがすでに存在するかどうかをチェックします。ファイルに検証が多数ある場合は、これにパフォーマンスの影響があります。これを克服するために、APIは [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) メソッドを提供します。 *checkIntersection* パラメーターは、指定されたエリアと既存の検証エリアとの交差をチェックするかどうかを示します。これを **false** に設定すると、他のエリアをチェックしないようになります。 *checkEdge* パラメーターは、適用エリアをチェックするかどうかを示します。新しいエリアが左上のエリアになる場合、内部設定が再構築されます。新しいエリアが左上のエリアでないことを確信している場合、このパラメーターを **false** に設定できます。

新しい[**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)を既存の[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)に追加する[**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool)メソッドの使用を示すコードスニペット。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

ソースエクセルファイルと出力エクセルファイルが添付されています。

[ソースファイル](96928093.xlsx)

[出力ファイル](96928220.xlsx)


## **高度なトピック**
- [ODS ファイルでのセル検証を取得](/cells/ja/python-net/get-cell-validation-in-ods-files/)
- [セルに適用された検証を取得する](/cells/ja/python-net/get-validation-applied-on-a-cell/)
- [セルの値がデータ検証ルールを満たすかどうかを確認する](/cells/ja/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
