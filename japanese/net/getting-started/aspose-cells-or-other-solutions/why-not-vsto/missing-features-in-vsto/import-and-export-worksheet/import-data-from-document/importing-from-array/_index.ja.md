---
title: 配列からのインポート
type: docs
weight: 10
url: /ja/net/importing-from-array/
---

開発者は、Cells コレクションの **ImportArray** メソッドを呼び出すことで、配列からデータをワークシートにインポートできます。ImportArray メソッドには多くのオーバーロードされたバージョンがありますが、典型的なオーバーロードは次のパラメーターを取ります：

- 配列、インポートする内容の配列オブジェクトを表します
- 行番号、データをインポートする最初のセルの行番号を表します
- 列番号、データをインポートする最初のセルの列番号を表します
- 垂直かどうかを指定するブール値、データを縦方向または横方向にインポートするかどうかを指定します

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array.xls");

{{< /highlight >}}
