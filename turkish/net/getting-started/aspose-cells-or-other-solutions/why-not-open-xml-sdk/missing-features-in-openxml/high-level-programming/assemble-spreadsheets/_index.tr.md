---
title: Tabloları Birleştirme
type: docs
weight: 10
url: /tr/net/assemble-spreadsheets/
---

Bu bölümde aşağıdakiler açıklanmıştır:

Sıfırdan Yeni bir Excel Dosyası Oluşturma ve Buna Çalışsayfa Ekleme

- Tasarımcı çalışsayfalara çalışsayfa ekleme.
- Sayfa adını kullanarak çalışsayfalara erişme.
- Sayfa adını kullanarak bir Excel dosyasından bir çalışsayfa silme.
- Sayfa dizinini kullanarak bir Excel dosyasından bir çalışsayfa silme.
- Aspose.Cells, bir Excel dosyasını temsil eden Workbook sınıfını içeren bir sınıf sunmaktadır. Workbook sınıfı, Excel dosyasındaki her çalışsayfaya erişime olanak tanıyan Worksheets koleksiyonunu içerir.

Bir çalışsayfa, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, çalışsayfaları yönetmek için geniş bir özellik ve yöntem yelpazesi sunar.
## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**
Programlı olarak yeni bir Excel dosyası oluşturmak için:

- Workbook sınıfının bir nesnesini oluşturun.
- Worksheets koleksiyonunun Add yöntemini çağırın. * Otomatik olarak boş bir çalışsayfa Excel dosyasına eklenir. Yeni çalışsayfanın sayfa dizinini Worksheets koleksiyonuna geçirerek erişilebilir.
- Bir çalışsayfa referansı alın.
- Çalışsayfalarda işlem yapın.
- Yeni çalışsayfalarla birlikte yeni Excel dosyasını Workbook sınıfının Save yöntemini çağırarak kaydedin.

{{< highlight csharp >}}

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
## **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**
Tasarımcı çalışsayfalarına çalışsayfa eklemek, yeni bir çalışsayfa eklemekle aynıdır, fakat Excel dosyası zaten mevcut olduğu için önce açılmalı ve sonra çalışsayfalar eklenmelidir. Bir tasarımcı çalışsayfa, Workbook sınıfı tarafından açılabilir.

{{< highlight csharp >}}

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
## **Sayfa Adını Kullanarak Çalışsayfalara Erişme**
Belirli bir ad veya dizine göre herhangi bir çalışsayfaya erişme.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**
Dosyalardan çalışma sayfalarını kaldırmak için, ÇalışmaSayfaları koleksiyonunun RemoveAt yöntemini çağırın. Belirli bir çalışma sayfasını kaldırmak için RemoveAt yöntemine sayfa adını geçirin.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**
Çalışma sayfalarını ada göre kaldırmak, çalışma sayfasının adının bilindiği durumlarda iyi çalışır. Eğer çalışma sayfasının adını bilmiyorsanız, sayfa adının yerine sayfa dizinini alacak olan RemoveAt yönteminin aşırı yüklenmiş bir versiyonunu kullanın.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
