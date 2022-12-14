---
title: Satır veya Sütun Ekleme veya Silme
type: docs
weight: 20
url: /tr/net/insert-or-delete-rows-or-columns/
---
İster sıfırdan yeni bir çalışma sayfası oluşturuyor olun, ister mevcut bir çalışma sayfası üzerinde çalışıyor olun, daha fazla veriyi barındırmak için veya başka bir nedenle çalışma sayfasına fazladan satırlar veya sütunlar eklememiz gerekebilir. Tersine, çalışma sayfasının belirtilen konumlarından satır veya sütunların silinmesi de gerekebilir.
## **Satırları/Sütunları Yönetme**
**Aspose.Cells** bir Excel dosyasını temsil eden bir çalışma kitabı sınıfı sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir Worksheets koleksiyonu içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir Cells koleksiyonu sağlar.

**Cells**koleksiyon, bir çalışma sayfasındaki satırları veya sütunları yönetmek için çeşitli yöntemler sağlar; bunlardan birkaçı aşağıda daha ayrıntılı olarak ele alınmıştır.
## **Satır Ekleme**
 Geliştiriciler, Cells koleksiyonunun InsertRow yöntemini çağırarak çalışma sayfasına herhangi bir konumda bir satır ekleyebilir.**Satır Ekle** method yeni satırın ekleneceği satırın indeksini alır.

{{< highlight "csharp" >}}

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
## **Birden Çok Satır Ekleme**
Bazen, geliştiricilerin çalışma sayfasına birden çok satır eklemesi gerekebilir. Cells koleksiyonunun InsertRows yöntemi çağrılarak yapılabilir. InsertRows yöntemi iki parametre alır:

- **Satır Dizini**, yeni satırların ekleneceği satırın dizini
- **Satır sayısı**, eklenmesi gereken toplam satır sayısı

{{< highlight "csharp" >}}

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
## **Satır Silme**
 Geliştiriciler, herhangi bir konumdaki çalışma sayfasındaki bir satırı şunu çağırarak silebilir:**Sırayı sil** Cells koleksiyonunun yöntemi.**Sırayı sil** method silinmesi gereken satırın indeksini alır.

{{< highlight "csharp" >}}

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
## **Birden Çok Satırı Silme**
Geliştiricilerin çalışma sayfasından birden çok satırı silmeleri gerekiyorsa, bu, Cells koleksiyonunun DeleteRows yöntemi çağrılarak da yapılabilir. DeleteRows yöntemi iki parametre alır:

- **Satır Dizini**, satırların silineceği satırın dizini.
- **Satır sayısı**, silinmesi gereken toplam satır sayısı.

{{< highlight "csharp" >}}

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
## **Sütun Ekleme**
Geliştiriciler ayrıca Cells koleksiyonunun InsertColumn yöntemini çağırarak çalışma sayfasına herhangi bir konumda bir sütun ekleyebilir. InsertColumn yöntemi, yeni sütunun ekleneceği sütunun dizinini alır.

{{< highlight "csharp" >}}

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
## **Sütun Silme**
Herhangi bir konumdaki çalışma sayfasından bir sütunu silmek için geliştiriciler, Cells koleksiyonunun DeleteColumn yöntemini çağırabilir. DeleteColumn yöntemi, silinecek sütunun dizinini alır.

{{< highlight "csharp" >}}

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
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
