---
title: Satır veya Sütun Ekleme veya Silme
type: docs
weight: 20
url: /tr/net/insert-or-delete-rows-or-columns/
---

Sıfırdan yeni bir çalışma sayfası oluşturuyor olsak da mevcut bir çalışma sayfası üzerinde çalışıyor olsak da, çalışma sayfasına daha fazla veri sığdırmak veya başka bir nedenle ekstra satır veya sütun eklememiz gerekebilir. Tersi durumda, belirli konumlardan satır veya sütun silinmesi de gerekebilir.
## **Satır/Sütun Yönetimi**
**Aspose.Cells**, bir Excel dosyasını temsil eden bir Workbook sınıfını sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan bir Worksheets koleksiyonunu içerir. Bir çalışma sayfası Worksheet sınıfı ile temsil edilir. Worksheet sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir Cells koleksiyonunu sağlar.

**Cells** koleksiyonu, çalışma sayfasındaki satır veya sütunları yönetmek için birçok yöntem sağlar, bunlardan bazıları burada daha detaylı olarak tartışılmaktadır.
## **Satır Ekleme**
Geliştiriciler, Cells koleksiyonunun InsertRow yöntemini çağırarak çalışma sayfasına istenilen konuma bir satır ekleyebilir. **InsertRow** yöntemi, yeni satırın ekleneceği satırın dizinini alır.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Birden Fazla Satır Ekleme**
Geliştiriciler bazen çalışma sayfasına birden çok satır eklemeleri gerekebilir. Bu, Cells koleksiyonunun InsertRows yöntemini çağırarak yapılabilir. InsertRows yöntemi iki parametre alır:

- **Satır İndeksi**, yeni satırların nereden ekleneceği satırın endeksi
- **Satır Sayısı**, eklenmesi gereken toplam satır sayısı

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Bir Satırı Silme**
Geliştiriciler, çalışma sayfasından herhangi bir konumdaki bir satırı silmek için Cells koleksiyonunun **DeleteRow** yöntemini çağırabilir. **DeleteRow** yöntemi silinmesi gereken satırın endeksini alır.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Birden Fazla Satırı Silme**
Geliştiriciler, çalışma sayfasından birden fazla satır silmek istediklerinde, bu da Cells koleksiyonunun DeleteRows yöntemi çağırılarak yapılabilir. DeleteRows yöntemi iki parametre alır:

- **Satır İndeksi**, silinecek satırların başlangıç endeksi
- **Satır Sayısı**, silinmesi gereken toplam satır sayısı

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Bir Sütun Ekleme**
Geliştiriciler, çalışma sayfasına herhangi bir konumda sütun eklemek için Cells koleksiyonunun InsertColumn yöntemini de çağırabilir. InsertColumn yöntemi yeni sütunun ekleneceği sütunun endeksini alır.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Bir Sütunu Silme**
Herhangi bir konumdan çalışma sayfasından bir sütunu silmek için geliştiriciler, Cells koleksiyonunun DeleteColumn yöntemini çağırabilir. DeleteColumn yöntemi silinecek sütunun endeksini alır.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
