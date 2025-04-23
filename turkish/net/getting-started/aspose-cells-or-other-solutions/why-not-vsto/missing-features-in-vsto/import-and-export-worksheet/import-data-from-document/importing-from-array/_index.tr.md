---
title: Diziden İçe Aktarma
type: docs
weight: 10
url: /tr/net/importing-from-array/
---

Geliştiriciler, hücreler koleksiyonunun **ImportArray** yöntemini çağırarak verileri diziden çalışma sayfalarına aktarabilirler. **ImportArray** yönteminin birçok aşırı yüklenmiş versiyonu bulunmaktadır ancak tipik bir aşırı yüklenme aşağıdaki parametreleri alır:

- Dizi, içeri aktarılacak dizi nesnesini temsil eder
- Satır Numarası, verilerin içeri aktarılacağı ilk hücrenin satır numarasını temsil eder
- Sütun Numarası, verilerin içeri aktarılacağı ilk hücrenin sütun numarasını temsil eder
- Dikey, verinin dikey veya yatay olarak alınmasını belirten boolean bir değerdir.

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
{{< app/cells/assistant language="csharp" >}}
