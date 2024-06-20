---
title: Güçlü Türde Veri İçeren Sütunlar
type: docs
weight: 20
url: /tr/net/columns-containing-strongly-typed-data/
---

Bir elektronik tablo, verileri bir dizi satır ve sütun olarak depolar. Bir çalışma sayfasının sütunlarının tüm değerleri güçlü bir şekilde türdeyse (bu, bir sütundaki tüm değerlerin aynı veri tipine sahip olması gerektiği anlamına gelir) o zaman **Cells** sınıfının **ExportDataTable** yöntemini çağırarak çalışma sayfası içeriğini dışa aktarabiliriz. **ExportDataTable** yöntemi, çalışma sayfasındaki verileri **DataTable** nesnesi olarak dışa aktarmak için aşağıdaki parametreleri alır: **Satır Numarası** , verilerin dışa aktarılacağı ilk hücrenin satır numarasını temsil eder

- **Sütun Numarası** , verilerin dışa aktarılacağı ilk hücrenin sütun numarasını temsil eder
- **Satır Sayısı** , dışa aktarılacak satır sayısını temsil eder
- **Sütun Sayısı** , dışa aktarılacak sütun sayısını temsil eder
- **Sütun İsimlerini Dışa Aktar** , çalışma sayfasının ilk satırındaki verilerin **DataTable** sütun isimleri olarak dışa aktarılıp aktarılmayacağını gösteren bir boolean özelliği

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
