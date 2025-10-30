---
title: スマートマーカーにJSONをスマートにインポートする方法
type: docs
weight: 30
url: /ja/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **なぜスマートマーカーにJSONデータを使用するのか**
なぜスマートマーカーの元データとしてJSONデータを使用するのか？
JSON（JavaScript Object Notation）は、階層型データの構造化に理想的な軽量で人間が読みやすいデータ交換フォーマットです。これは、スマートマーカーの元データとして適している理由です（スプレッドシート、ドキュメント、ダッシュボードに自動入力される動的プレースホルダー）：

1. 構造化および階層型データのサポート
JSONはネストされたオブジェクトや配列（例：{ "user": { "name": "Alice", "orders": [ ... ] } }）をネイティブにサポートします。スマートマーカーはこの階層をたどることができ（例：{{user.orders[0].price}}）、複雑なデータをテンプレートに簡単にマッピングできます。

2. 言語およびプラットフォームに依存しない
JSONパーサはほぼすべてのプログラミング言語（Python、JavaScript、Javaなど）に存在します。ExcelのPower Query、Google Apps Script、またはno-codeプラットフォーム（例：Airtable）などのツールがシームレスにJSONを取り込みます。

3. API対応
ほとんどの最新API（例：REST、GraphQL）はJSONフォーマットでデータを返します。スマートマーカーはWebサービスのライブJSONを直接取り込み、リアルタイムのデータ更新（例：株価、天気）を可能にします。

4. 人間に読みやすくデバッグしやすい
JSONのプレーンテキスト構造は以下に便利です：検証（例：JSONLintを使用）、手動またはスクリプトによる編集、データをマーカーにマッピングするときのデバッグ。

5. スケーラビリティと柔軟性
JSON内のフィールドの追加/削除は、既存のスマートマーカーを壊さずに行えます（オプションのフィールドを適切に処理すれば）。文字列、数値、ブール値、配列、オブジェクトなど多様なデータタイプをサポートします。

6. エコシステムとの互換性
最新のデータツールと連携：データベース（例：MongoDB、PostgreSQL（JSONB））、自動化ツール（例：Zapier、Integromat）、データパイプライン（例：Apache NiFi、Talend）。

## **ExcelのネストしたテンプレートとJSONデータの使用**
Aspose.Cells for .NETはスマートマーカーでJSONデータをサポートしており、JSONデータは階層的にネスト可能です。 [テンプレートファイル](smartmarker.xlsx)、[JSONファイル](smartmarker.json)、および以下のコードで生成された出力Excelファイルのスクリーンショットを確認してください。

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **ExcelサブトータルテンプレートをJSONデータと共に使用する**
Aspose.Cells for .NETはスマートマーカーでJSONデータをサポートしており、JSONデータは階層的にネスト可能です。サブトータルはExcelテンプレートでデータ統計に使用されました。 [テンプレートファイル](jsonExcelTemplate.xlsx)、[JSONデータ](jsonData.json)、および以下のコードで生成された出力Excelファイルのスクリーンショットを確認してください。

|**jsonExcelTemplate.xlsxファイルの最初のワークシートにスマートマーカーが表示されている部分。**|
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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
