---
title: Diziden İçe Aktarma
type: docs
weight: 10
url: /tr/net/importing-from-array/
---
 Geliştiriciler, çağırarak bir diziden çalışma sayfalarına veri aktarabilir.**İçe Aktarma Dizisi** Cells koleksiyonunun yöntemi. ImportArray yönteminin birçok aşırı yüklenmiş sürümü vardır, ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:

- Dizi, içeriğinin içe aktarılması gereken dizi nesnesini temsil eder
- Satır Numarası, verilerin içe aktarılacağı ilk hücrenin satır numarasını gösterir.
- Sütun Numarası, verilerin içe aktarılacağı ilk hücrenin sütun numarasını gösterir.
- Is Vertical, verilerin dikey veya yatay olarak içe aktarılacağını belirten bir boole değeri

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
