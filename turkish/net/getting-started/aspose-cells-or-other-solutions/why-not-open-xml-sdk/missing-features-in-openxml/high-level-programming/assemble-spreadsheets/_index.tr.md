---
title: Elektronik Tabloları Birleştirin
type: docs
weight: 10
url: /tr/net/assemble-spreadsheets/
---
Bu bölümde aşağıdakilerin nasıl yapılacağı açıklanmaktadır:

Sıfırdan yeni bir Excel dosyası oluşturun ve buna çalışma sayfası ekleyin.

- Tasarımcı elektronik tablolarına çalışma sayfaları ekleyin.
- Sayfa adını kullanarak çalışma sayfalarına erişin.
- Sayfa adını kullanarak bir çalışma sayfasını bir Excel dosyasından kaldırın.
- Sayfa dizinini kullanarak bir çalışma sayfasını bir Excel dosyasından kaldırın.
- Aspose.Cells, bir Excel dosyasını temsil eden bir Çalışma Kitabı sınıfı sağlar. Workbook sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir Worksheets koleksiyonu içerir.

Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar.
## **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**
Programlı olarak yeni bir Excel dosyası oluşturmak için:

- Workbook sınıfından bir nesne oluşturun.
- Worksheets koleksiyonunun Add yöntemini çağırın. Excel dosyasına * otomatik olarak boş bir çalışma sayfası eklenir. Yeni çalışma sayfasının sayfa dizini Worksheets koleksiyonuna geçirilerek başvurulabilir.
- Bir çalışma sayfası referansı edinin.
- Çalışma sayfaları üzerinde çalışma gerçekleştirin.
- Workbook sınıfının Save yöntemini çağırarak yeni Excel dosyasını yeni çalışma sayfalarıyla kaydedin.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Tasarımcı Elektronik Tablosuna Çalışma Sayfaları Ekleme**
Bir tasarımcı elektronik tablosuna çalışma sayfası ekleme işlemi, Excel dosyasının zaten mevcut olması ve çalışma sayfaları eklenmeden önce açılması gerektiği dışında, yeni bir çalışma sayfası ekleme işlemiyle aynıdır. Workbook sınıfı tarafından bir tasarımcı elektronik tablosu açılabilir.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Sayfa Adını Kullanarak Çalışma Sayfalarına Erişme**
Adını veya dizinini belirterek herhangi bir çalışma sayfasına erişin veya alın.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**
Çalışma sayfalarını bir dosyadan kaldırmak için Worksheets koleksiyonunun RemoveAt yöntemini çağırın. Belirli bir çalışma sayfasını kaldırmak için sayfa adını RemoveAt yöntemine iletin.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**
Çalışma sayfalarını ada göre kaldırmak, çalışma sayfasının adı bilindiğinde işe yarar. Çalışma sayfasının adını bilmiyorsanız, çalışma sayfasının sayfa adı yerine sayfa dizinini alan RemoveAt yönteminin aşırı yüklenmiş bir sürümünü kullanın.

{{< highlight "csharp" >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
