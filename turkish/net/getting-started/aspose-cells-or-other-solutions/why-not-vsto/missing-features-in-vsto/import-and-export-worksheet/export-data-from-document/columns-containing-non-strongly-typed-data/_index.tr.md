---
title: Kesinlikle Yazılmamış Veriler İçeren Sütunlar
type: docs
weight: 10
url: /tr/net/columns-containing-non-strongly-typed-data/
---
 Bir çalışma sayfasının sütunlarındaki tüm değerler kesin olarak yazılmamışsa (bu, bir sütundaki değerlerin farklı veri türlerine sahip olabileceği anlamına gelir), o zaman çalışma sayfasının içeriğini çağırarak dışarı aktarabiliriz.**ExportDataTableAsString** Cells sınıfının yöntemi.**ExportDataTableAsString** yöntemi ile aynı parametre kümesini alır.**ExportDataTable** çalışma sayfası verilerini dışa aktarma yöntemi**Veri tablosu** nesne.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

Ekran görüntüleri aşağıdadır:

![yapılacaklar:resim_alternatif_Metin](picture1.png)

![yapılacaklar:resim_alternatif_Metin](picture2.png)

## **Örnek Kodu İndir**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
