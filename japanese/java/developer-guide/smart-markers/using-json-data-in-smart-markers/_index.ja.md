---
title: スマートマーカーでのJSONデータの使用方法
type: docs
weight: 30
url: /ja/java/using-json-data-in-smart-markers/
---

## **なぜスマートマーカーにJSONデータを使用するのか**
なぜスマートマーカーの元データとしてJSONデータを使用するのか？
JSON（JavaScript Object Notation）は、階層構造のデータを構築するのに理想的な軽量で人間に読みやすいデータ交換フォーマットです。これがスマートマーカー（スプレッドシート、ドキュメント、ダッシュボードを自動入力する動的プレースホルダー）の元データとして適している理由です：

1. 構造化・階層的データのサポート
JSONはネストされたオブジェクトや配列（例：{ "user": { "name": "Alice", "orders": [ ... ] } }）をネイティブにサポートします。スマートマーカーはこの階層をたどることができ（例：{{user.orders[0].price}}）、複雑なデータをテンプレートに簡単にマッピングできます。

2. 言語・プラットフォームに依存しない
ほぼすべてのプログラミング言語（Python、JavaScript、Javaなど）にJSONパーサがあります。ExcelのPower Query、Google Apps Script、またはノーコードプラットフォーム（例：Airtable）はJSONをシームレスに取り込みます。

3. APIに親和性あり
ほとんどの最新API（例：REST、GraphQL）はJSONフォーマットでデータを返します。スマートマーカーはこれらのWebサービスからライブのJSONを直接取り込み、リアルタイムでデータを更新できます（例：株価、天気情報）。

4. 人間に読みやすく、デバッグしやすい
JSONのプレーンテキスト構造は、簡単に検証（例：JSONLintの使用）、手動やスクリプトでの編集、データをマーカーにマッピングするときのデバッグを容易にします。

5. 拡張性と柔軟性
JSON内のフィールドを追加・削除しても既存のスマートマーカーを壊さずに済みます（オプションのフィールドが適切に扱われる場合）。文字列、数字、ブール値、配列、オブジェクトなど、多様なデータタイプをサポートします。

6. エコシステムとの互換性
最新のデータツールと互換性があります。データベース：MongoDB、PostgreSQL（JSONB）など。自動化ツール：Zapier、Integromat。データパイプライン：Apache NiFi、Talend。

## **JSONデータを使用したExcelネストテンプレートの利用例**
Aspose.Cells for JavaはスマートマーカーでのJSONデータをサポートしており、JSONデータは階層的にネスト可能です。 [テンプレートファイル](smartmarker.xlsx)、[JSONファイル](smartmarker.json)、および以下のコードで生成されたExcel出力のスクリーンショットをご確認ください。

|**smartmarker.xlsxファイルの最初のワークシートにスマートマーカーを表示**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**出力Excelファイルのスクリーンショット**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

以下はJSONデータです：
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **ExcelのサブトータルテンプレートでのJSONデータの使用例**
Aspose.Cells for JavaはスマートマーカーでのJSONデータをサポートしており、JSONデータは階層的にネスト可能です。サブトータルはExcelテンプレートでデータ統計に使用されました。[テンプレートファイル](jsonExcelTemplate.xlsx)、[JSONファイル](jsonData.json)、および以下のコードで生成されたExcel出力のスクリーンショットをご確認ください。

|**jsonExcelTemplate.xlsxファイルの最初のワークシートにスマートマーカーを表示。**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**出力Excelファイルのスクリーンショット**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

以下はJSONデータです：
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
以下の例は、これがどのように動作するかを示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
