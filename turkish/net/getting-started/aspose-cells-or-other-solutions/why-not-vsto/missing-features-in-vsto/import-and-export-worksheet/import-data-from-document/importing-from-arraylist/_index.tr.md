---
title: ArrayList'ten içe aktarma
type: docs
weight: 20
url: /tr/net/importing-from-arraylist/
---
 Geliştiriciler, ArrayList'i çağırarak çalışma sayfalarına veri aktarabilir.**ImportArrayList** Cells koleksiyonunun yöntemi. ImportArray yöntemi aşağıdaki parametreleri alır:**Dizi Listesi** , içeriğinin içe aktarılması gereken ArrayList nesnesini temsil eder

- Satır Numarası , verilerin içe aktarılacağı ilk hücrenin satır numarasını gösterir.
- Sütun Numarası , verilerin içe aktarılacağı ilk hücrenin sütun numarasını gösterir.
- Is Vertical , verilerin dikey veya yatay olarak içe aktarılacağını belirten bir boole değeri

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
