---  
title: データ検証
type: docs  
weight: 90  
url: /ja/nodejs-cpp/data-validation/  
description: データ检証をAspose.Cells for Node.js via C++ APIを通じて追加する方法を学びます。  
keywords: データ検証を追加（Node.js via C++）、検証値を取得（Node.js via C++）、整数データ検証を追加（Node.js via C++）、リストデータ検証を追加（Node.js via C++）、日付データ検証を追加（Node.js via C++）、時間データ検証を追加（Node.js via C++）、テキスト長さデータ検証を追加（Node.js via C++）、既存のValidationにセルエリアを追加（Node.js via C++）、セルの検証がドロップダウンかどうかを確認（Node.js via C++）、カスタム検証を追加（Node.js via C++）  
---  

{{% alert color="primary" %}}  
Microsoft Excelはワークシートの自動フィルタや検証の良い機能を提供しています。Aspose.CellsはMicrosoft Excelのデータ検証と自動フィルタの機能を完全にサポートしています。この記事では、Microsoft Excelでのこれらの機能の使用方法と、それらをAspose.Cells for Node.js via C++を使用してコーディングする方法を説明します。  
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

### **Aspose.Cells for Node.js via C++を用いたデータ検証**  

データ検証は、ワークシートに入力された情報を検証するための強力な機能です。データ検証を使用すると、開発者はユーザーに選択肢のリストを提供したり、データの入力を特定のタイプやサイズに制限したりすることができます。  
Aspose.Cells for Node.js via C++の各[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスには、[**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--)メソッドがあり、これは[**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)オブジェクトのコレクションを表します。検証を設定するには、[**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)クラスのいくつかのプロパティを次のように設定します。  

- 種類 – 検証タイプを表し、[**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype)列挙体の事前定義された値の1つを使用して指定できます。  
- オペレーター – 検証で使用されるオペレーターを表し、[**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype)列挙体の事前定義された値のいずれかを使用して指定できます。  
- Formula1：データ検証の最初の部分に関連付けられた値または式を表します。  
- Formula2：データ検証の2番目の部分に関連付けられた値または式を表します。  

[**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)オブジェクトのプロパティが設定されたら、開発者は[**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)構造体を使用して、作成された検証を使用して検証されるセル範囲に関する情報を格納できます。  

#### **データ検証の種類**  

[**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype)列挙体には次のメンバーがあります：  

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

このタイプの検証では、ユーザーは指定された範囲内の整数のみを検証されたセルに入力できます。以下のコード例では、WholeNumber検証タイプの実装方法を示しています。例は、上記のMicrosoft Excelを使用して作成したのと同じデータ検証をAspose.Cells for Node.js via C++で作成します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **リストデータの検証**  

この種類の検証では、ユーザーはドロップダウンリストから値を入力できます。リストにはデータを含む一連の行があります。この例では、リストのソースを保持するために2番目のワークシートが追加されます。ユーザーはリストからのみ値を選択できます。検証エリアは最初のワークシートのセル範囲 A1:A5 です。  

ここで重要なのは、[**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-)プロパティを**true**に設定することです。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **日付データの検証**  

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の日付値、または特定の条件を満たす日付値を入力できます。例では、ユーザーは1970年から1999年の間の日付を入力することに制限されます。ここでは、検証領域はB1セルです。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **時間データの検証**  

このタイプの検証では、ユーザーは検証済みのセルに特定の範囲内の時刻、または特定の条件を満たす時刻を入力できます。例では、ユーザーは午前09:00から11:30の間の時間のみを入力するように制限されます。ここでは、検証領域はB1セルです。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **テキスト長のデータ検証**  

このタイプの検証を使用すると、ユーザーは検証されたセルに指定された長さのテキスト値を入力できます。例では、ユーザーは5文字を超えない文字列値を入力することが制限されています。検証エリアはB1セルです。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **データ検証ルール**  

データ検証が実装されると、セルに異なる値を割り当てて検証を確認できます。[**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--)を使用して検証結果を取得できます。以下の例では、異なる値を使用してこの機能を示しています。テスト用のサンプルファイルは以下のリンクからダウンロードできます：  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **セルの検証がドロップダウンであるかどうかをチェック**  

セルに実装できる検証の種類はさまざまです。検証がドロップダウンかどうかを確認したい場合は、[**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--)メソッドを使用してこれをテストできます。以下のサンプルコードはこのプロパティの使用例を示しています。テスト用のサンプルファイルは以下のリンクからダウンロードできます：  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **既存の検証にCellAreaを追加**  

既存の[**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)に[**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)を追加したい場合があります。[**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-)を使用して[**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)を追加すると、Aspose.Cellsは既存のすべての範囲を確認し、新しい範囲が既に存在しているかどうかを判断します。検証が多いファイルでは、パフォーマンスに影響を及ぼす可能性があります。これを回避するために、APIは[**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-)メソッドを提供しています。*checkIntersection*パラメータは、指定された範囲と既存の検証範囲の交差を確認するかどうかを示します。これを**false**に設定すると、他の範囲のチェックが無効になります。*checkEdge*パラメータは、適用された範囲をチェックするかどうかを示します。新しい範囲が左上の範囲になる場合、内部設定が再構築されます。新しい範囲が左上の範囲でないことが確実な場合、このパラメータを**false**に設定できます。  

以下のコードスニペットは、[**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-)メソッドを使用して既存の[**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)に新しい[**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)を追加する例を示しています。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

ソースエクセルファイルと出力エクセルファイルが添付されています。  

[ソースファイル](96928093.xlsx)  

[出力ファイル](96928220.xlsx)  

## **高度なトピック**  
- [ODS ファイルでのセル検証を取得](/cells/ja/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [セルに適用された検証を取得する](/cells/ja/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [セルの値がデータ検証ルールを満たすかどうかを確認する](/cells/ja/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
