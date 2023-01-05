---
title: Kesinlikle Yazılmış Verileri İçeren Sütunlar
type: docs
weight: 20
url: /tr/net/columns-containing-strongly-typed-data/
---
Bir elektronik tablonun verileri bir dizi satır ve sütun olarak sakladığını biliyoruz. Bir çalışma sayfasının sütunlarındaki tüm değerler kesin olarak yazılmışsa (bu, bir sütundaki tüm değerlerin aynı veri türüne sahip olması gerektiği anlamına gelir), o zaman çalışma sayfasının içeriğini çağırarak dışa aktarabiliriz.**ExportDataTable** Cells sınıfının yöntemi.**ExportDataTable** yöntem, çalışma sayfası verilerini şu şekilde dışa aktarmak için aşağıdaki parametreleri alır:**Veri tablosu** nesne:**Satır numarası** , verilerin dışa aktarılacağı ilk hücrenin satır numarasını temsil eder

- **Sütun Numarası** , verilerin dışa aktarılacağı ilk hücrenin sütun numarasını temsil eder
- **Satır sayısı** , dışa aktarılacak satır sayısını temsil eder
- **Sütun sayısı** dışa aktarılacak sütun sayısını temsil eder
- **Sütun Adlarını Dışa Aktar** , çalışma sayfasının ilk satırındaki verilerin DataTable'ın sütun adları olarak dışa aktarılıp aktarılmayacağını belirten bir boole özelliği

{{< highlight "csharp" >}}

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
