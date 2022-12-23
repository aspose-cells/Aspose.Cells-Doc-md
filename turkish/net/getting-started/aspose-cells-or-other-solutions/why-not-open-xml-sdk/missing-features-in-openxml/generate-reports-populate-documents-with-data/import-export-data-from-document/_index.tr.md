---
title: Verileri belgeden içe aktar
type: docs
weight: 10
url: /tr/net/import-export-data-from-document/
---
## **Belgeden verileri içe aktar**

Veriler, ham gerçeklerin toplanmasıdır ve bu ham gerçekleri daha anlamlı bir şekilde sunmak için elektronik tablo belgeleri veya raporları oluştururuz. Normalde elektronik tablolara verileri kendimiz ekleriz, ancak bazen mevcut veri kaynaklarını yeniden kullanmamız gerekir ve burada farklı veri kaynaklarından elektronik tablolara veri aktarma ihtiyacı ortaya çıkar. Bu konuda, farklı veri kaynaklarından çalışma sayfalarına veri aktarmak için bazı teknikleri tartışacağız.

## **Aspose.Cells Kullanarak Verileri İçe Aktarma**

 kullandığınızda**Aspose.Cells** bir Excel dosyasını açmak için dosyadaki tüm veriler otomatik olarak içe aktarılır ancak Aspose.Cells farklı veri kaynaklarından veri içe aktarmayı da destekler. Bu veri kaynaklarından birkaçı aşağıda listelenmiştir:

- **Dizi**
- **Dizi Listesi**
- **Veri tablosu**
- **Veri Sütunu**
- **Veri görünümü**
- **Veri şebekesi**
- **Veri Okuyucu**
- **Izgara Görünümü**

 Aspose.Cells bir sınıf sağlar,**Çalışma kitabı** Bu bir Excel dosyasını temsil eder. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir Worksheets koleksiyonu içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı bir Cells koleksiyonu sağlar.

Cells koleksiyonu, farklı veri kaynaklarından veri almak için çok kullanışlı yöntemler sağlar.

### **Diziden İçe Aktarma**

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

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **ArrayList'ten içe aktarma**

 Geliştiriciler, ArrayList'i çağırarak çalışma sayfalarına veri aktarabilir.**ImportArrayList** Cells koleksiyonunun yöntemi. ImportArray yöntemi aşağıdaki parametreleri alır:**Dizi Listesi** , içeriğinin içe aktarılması gereken ArrayList nesnesini temsil eder

- Satır Numarası , verilerin içe aktarılacağı ilk hücrenin satır numarasını gösterir.
- Sütun Numarası , verilerin içe aktarılacağı ilk hücrenin sütun numarasını gösterir.
- Is Vertical , verilerin dikey veya yatay olarak içe aktarılacağını belirten bir boole değeri

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **Özel Nesnelerden İçe Aktarma**

 Geliştiriciler, nesneler koleksiyonundaki verileri kullanarak bir çalışma sayfasına aktarabilir.**Özel Nesneleri İçe Aktar**. İstediğiniz nesne listesini görüntülemek için yönteme bir sütun/özellikler listesi sağlayabilirsiniz.

{{< highlight "csharp" >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **DataTable'dan içe aktarma**

 Geliştiriciler, bir**Veri tablosu** arayarak çalışma sayfalarına**ImportDataTable** Cells koleksiyonunun yöntemi. Programın aşırı yüklenmiş birçok versiyonu vardır.**ImportDataTable** yöntem ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:**Veri tablosu** , temsil etmek**Veri tablosu** içeriğinin içe aktarılması gereken nesne

- **Alan Adı Gösteriliyor mu?**, DataTable sütunlarının adlarının çalışma sayfasına ilk satır olarak alınıp alınmayacağını belirtir.
- **Başlangıç Cell** DataTable içeriğinin içe aktarılacağı başlangıç hücresinin adını (yani "A1") temsil eder.

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Örnek Kodu İndir**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Verileri belgeden dışa aktar**

 Aspose.Cells, kullanıcılarının yalnızca harici veri kaynaklarından çalışma sayfalarına veri almalarını kolaylaştırmakla kalmaz, aynı zamanda çalışma sayfası verilerini bir**Veri tablosu** . bildiğimiz gibi**Veri tablosu** ADO.NET'in bir parçasıdır ve verileri tutmak için kullanılır. Veriler bir kez depolandığında**Veri tablosu**, kullanıcıların gereksinimlerine göre herhangi bir şekilde kullanılabilir.

## **Aspose.Cells Kullanarak Verileri DataTable'a (.NET) Aktarma**

Geliştiriciler, Cells sınıfının ExportDataTable veya ExportDataTableAsString yöntemini çağırarak çalışma sayfası verilerini kolayca bir DataTable nesnesine aktarabilir. Her iki yöntem de aşağıda daha ayrıntılı olarak tartışılan farklı senaryolarda kullanılmaktadır.

### **Kesinlikle Yazılmış Verileri İçeren Sütunlar**

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

### **Kesinlikle Yazılmamış Veriler İçeren Sütunlar**

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

## **Örnek Kodu İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
