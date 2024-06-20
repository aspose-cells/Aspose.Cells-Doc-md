---
title: ArrayList ten alma
type: docs
weight: 20
url: /tr/net/importing-from-arraylist/
---

Geliştiriciler, Hücreler koleksiyonunun **ImportArrayList** yöntemini çağırarak verileri ArrayList'ten çalışma sayfalarına alabilirler. ImportArray yöntemi aşağıdaki parametreleri alır: **ArrayList** , içeriği alınması gereken ArrayList nesnesini temsil eder

- Satır Numarası , verinin alınacağı ilk hücrenin satır numarasını temsil eder
- Sütun Numarası , verinin alınacağı ilk hücrenin sütun numarasını temsil eder
- Dikey, verinin dikey veya yatay olarak alınmasını belirten boolean bir değerdir

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
