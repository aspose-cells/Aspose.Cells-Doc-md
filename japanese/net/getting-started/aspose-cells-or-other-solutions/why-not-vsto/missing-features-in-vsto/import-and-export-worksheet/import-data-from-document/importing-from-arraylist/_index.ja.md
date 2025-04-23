---
title: ArrayList からのインポート
type: docs
weight: 20
url: /ja/net/importing-from-arraylist/
---

開発者は、Cells コレクションの **ImportArrayList** メソッドを呼び出すことで、ArrayList からデータをワークシートにインポートできます。ImportArray メソッドには次のパラメーターがあります：**ArrayList**、インポートする内容の ArrayList オブジェクトを表します

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

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array List.xls");


{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
