---
title: Smart Markerパラメータ
type: docs
weight: 30
url: /ja/net/smart-marker-parameters/
---

## **デザイナースプレッドシートとスマートマーカー**
デザイナースプレッドシートは、視覚的な書式、数式、スマートマーカーを含む標準のExcelファイルです。プロジェクトからの情報や関連連絡先の情報など、1つ以上のデータソースを参照するスマートマーカーを含めることができます。スマートマーカーは、情報を配置したいセルに書き込まれます。

すべてのスマートマーカーは、&=で始まります。データマーカーの例として、&=Party.FullNameがあります。データマーカーが1つ以上のアイテム（例：完全な行）の結果を得る場合、新しい情報に対応するために自動的に次の行が移動されます。したがって、サブトータルや合計は、挿入されたデータに基づいて計算を行うために、データマーカーの直後の行に配置することができます。挿入された行で計算を行うには、**動的な数式**を使用します。

スマートマーカーには、ほとんどの情報の**データソース**と**フィールド名**から成るものがあります。特別な情報は変数や変数配列を伴ったスマートマーカーにも渡される場合があります。変数は常に1つのセルのみに入り、変数配列は複数のセルに入ることがあります。セルごとに1つのデータマーカーしか使用しないでください。未使用のスマートマーカーは削除されます。

スマートマーカーにはパラメータも含めることができます。パラメータを使用すると、情報のレイアウト方法を変更することができます。パラメータは、カンマで区切られたリストとしてスマートマーカーの末尾に追加されます。

## **スマートマーカーオプション**

```csharp
&=DataSource.FieldName 
&=[Data Source].[Field Name] 
&=$VariableName 
&=$VariableArray 
&==DynamicFormula 
&=&=RepeatDynamicFormula
```
## **Smart Markerパラメータ**
以下のパラメータが許可されています:

- **noadd** - データに合わせて追加の行を追加しません。
- **skip:n** - 各データ行ごとにn行をスキップします。
- **ascending:n**または**descending:n** - スマートマーカーのデータをソートします。nが1の場合、列はソーターの最初のキーです。データはデータソースの処理後に並べ替えられます。例えば：&=Table1.Field3(ascending:1)。
- **horizontal** - 上下ではなく左から右にデータを書き込みます。
- **numeric** - 可能であればテキストを数値に変換します。
- **shift** - 下方向または右方向にシフトし、データに合わせて余分な行または列を作成します。シフトパラメーターはMicrosoft Excelと同じ方法で機能します。たとえば、Microsoft Excelではセルの範囲を選択して、右クリックして**挿入**を選択し、**セルを下にシフト**、**セルを右にシフト**などを指定します。 簡単に言うと、**shift**パラメーターは垂直／通常（上から下へ）または水平（左から右へ）のスマートマーカーのために同じ機能を果たします。
- **copystyle** - ベースセルのスタイルをその列のすべてのセルにコピーします。

パラメーターnoaddとskipを組み合わせることで、交互に行にデータを挿入できます。テンプレートは上から下に処理されるため、交互の行の前に余分な行が挿入されるのを避けるために、最初の行にnoaddを追加するべきです。

複数のパラメータを持つ場合は、コンマで区切りますが、スペースは入れません：parameterA,parameterB,parameterC。

次のスクリーンショットは、交互の行にデータを挿入する方法を示しています。

|**テンプレートファイル**|**出力ファイル**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|

## **動的な式**
動的な式を使用すると、エクスポートプロセス中に挿入される行を参照する式をセルに挿入できます。 動的な式は、挿入された行ごとに繰り返すことができるか、データマーカーが配置されたセルのみを使用できます。

動的な式には、次の追加のオプションがあります:

- r - 現在の行番号。
- 2, -1 - 現在の行番号へのオフセット。

例:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

動的な数式のマーカーでは、「-1」は、除算操作に設定されるB列とC列への現在の行へのオフセットを示し、スキップパラメーターは1行です。さらに、以下の文字を指定する必要があります:

{{< highlight java >}}

 "~"

{{< /highlight >}}

動的な数式で追加のパラメーターを適用するための区切り文字。

次のスクリーンショットは、繰り返しの動的な数式とその結果のExcelワークシートを示しています。

|**テンプレートファイル**|**出力ファイル**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
セル"C1"には、式**= A1*B1**が含まれ、セル"C2"には**= A2*B2**、セル"C3"には**= A3*B3**が含まれています。

スマートマーカーの処理は非常に簡単です。 次の例コードは、スマートマーカーで動的式を使用する方法を示しています。 [テンプレートファイル](templateDynamicFormulas.xlsx)を読み込んでテストデータを作成し、マーカーを処理してセルにデータを埋めます。 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **SmartMarkersで動的数式や変数を使用する方法**
時には、SmartMarkersで動的数式や変数を使用する必要があります。動的数式には、区切り文字（~）を追加してください。Aspose.Cellsでは、SmartMarkersで動的数式や変数を使用することが可能です。以下のファイルとコード例を参照してください： [テンプレートファイル](template.xlsx)、 [従業員データjson](employees-data.json)、および生成されたExcelファイルのスクリーンショット。

|**変数を示すtemplate.xlsxファイルの最初のシート**|
| :- |
|![todo:image_alt_text](template_variables.png)|

|**SmartMarkersを示すtemplate.xlsxファイルの2番目のシート**|
| :- |
|![todo:image_alt_text](template_data.png)|

|**出力Excelファイルのスクリーンショット**|
| :- |
|![todo:image_alt_text](template_result.png)|

以下はJSONデータです：
```json data
{
  "RootData": {
    "Directors": [
      {
        "FirstName": "director first 1",
        "id": "director id 1",
        "LastName": "director last 1",
        "MiddleName": "director middle 1",
        "Reportees": [
          {
            "City": "aaa city",
            "Department": "aaa department",
            "FirstName": "first aaa",
            "GST": "Yes",
            "id": "aaa",
            "ITR": "No",
            "LastName": "last aaa",
            "MiddleName": "middle aaa"
          },
          {
            "City": "bbb city",
            "Department": "bbb department",
            "FirstName": "first bbb",
            "GST": "Yes",
            "id": "bbb",
            "ITR": "Yes",
            "LastName": "last bbb",
            "MiddleName": "middle bbb"
          },
          {
            "City": "ccc city",
            "Department": "ccc department",
            "FirstName": "first ccc",
            "GST": "No",
            "id": "ccc",
            "ITR": "No",
            "LastName": "last ccc",
            "MiddleName": "middle ccc"
          },
          {
            "City": "ddd city",
            "Department": "ddd department",
            "FirstName": "first ddd",
            "GST": "No",
            "id": "ddd",
            "ITR": "No",
            "LastName": "last ddd",
            "MiddleName": "middle ddd"
          },
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "No",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          }
        ]
      },
      {
        "FirstName": "director first 2",
        "id": "director id 2",
        "LastName": "director last 2",
        "MiddleName": "director middle 2",
        "Reportees": [
          {
            "City": "eee city",
            "Department": "eee department",
            "FirstName": "first eee",
            "GST": "Yes",
            "id": "eee",
            "ITR": "No",
            "LastName": "last eee",
            "MiddleName": "middle eee"
          },
          {
            "City": "fff city",
            "Department": "fff department",
            "FirstName": "first fff",
            "GST": "No",
            "id": "fff",
            "ITR": "No",
            "LastName": "last fff",
            "MiddleName": "middle fff"
          }
        ]
      }
    ],
    "DOB": "2025-02-28",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111",
	"CtcPerEmployee": 100000,
	"CountOfEmployees": 132
  }
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-DynamicFormula-And-Variables.cs" >}}
