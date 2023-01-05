---
title: アレイからのインポート
type: docs
weight: 10
url: /ja/net/importing-from-array/
---
開発者は、配列からワークシートにデータをインポートするには、**ImportArray** Cells コレクションのメソッド。 ImportArray メソッドにはオーバーロードされたバージョンが多数ありますが、典型的なオーバーロードは次のパラメーターを取ります。

- 配列は、内容をインポートする必要がある配列オブジェクトを表します
- 行番号は、データがインポートされる最初のセルの行番号を表します
- 列番号は、データがインポートされる最初のセルの列番号を表します
- データを垂直方向または水平方向にインポートするように指定するブール値です。

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array.xls");

{{< /highlight >}}
