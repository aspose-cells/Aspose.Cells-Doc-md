---
title: Çalışma Sayfalarını Çalışma Kitapları Arasında Kopyalama
type: docs
weight: 10
url: /tr/net/copy-worksheets-between-workbooks/
---
Aspose.Cells, çalışma kitapları içinde veya arasında bir kaynak çalışma sayfasından başka bir çalışma sayfasına verileri ve biçimlendirmeyi kopyalamak için kullanılan Aspose.Cells.Worksheet.Copy() adlı bir yöntem sağlar. Yöntem, kaynak çalışma sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, çalışma sayfasının bir çalışma kitabından başka bir çalışma kitabına nasıl kopyalanacağını gösterir.

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Örnek Dosyalar\";

string FileName = FilePath + "Workbook.xlsx arasında Sayfayı Kopyala";

//Yeni bir Çalışma Kitabı oluştur.

Çalışma kitabı excelWorkbook0 = new Çalışma Kitabı();

//Kitaptaki ilk çalışma sayfasını alın.

Çalışma sayfası ws0 = excelWorkbook0.Worksheets[0];

//Bazı verileri başlık satırlarına koyun (A1:A4)

 için (int ben = 0; ben< 5; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save(FileName);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

Aşağıdaki örnek, çalışma sayfasının bir çalışma kitabından başka bir çalışma kitabına nasıl kopyalanacağını gösterir.

{{< highlight "csharp" >}}

 //Yeni bir Çalışma Kitabı oluştur.

Çalışma kitabı excelWorkbook0 = new Çalışma Kitabı();

//Kitaptaki ilk çalışma sayfasını alın.

Çalışma sayfası ws0 = excelWorkbook0.Worksheets[0];

//Bazı verileri başlık satırlarına koyun (A1:A4)

 için (int ben = 0; ben< 5; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save("copyworksheet.xls");


{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)
