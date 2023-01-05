---
title: ArrayList からのインポート
type: docs
weight: 20
url: /ja/net/importing-from-arraylist/
---
開発者は、ArrayList からワークシートにデータをインポートするには、**ImportArrayList** Cells コレクションのメソッド。 ImportArray メソッドは、次のパラメーターを取ります。**配列リスト** 、内容をインポートする必要がある ArrayList オブジェクトを表します

- Row Number は、データがインポートされる最初のセルの行番号を表します
- 列番号 は、データがインポートされる最初のセルの列番号を表します
- Vertical 、データを垂直または水平にインポートするように指定するブール値

{{< highlight "csharp" >}}

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
