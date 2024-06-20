---
title: Belgeden Veri İçe ve Dışa Aktar
type: docs
weight: 10
url: /tr/net/import-export-data-from-document/
---

## **Belgeden veri içe aktarma**

Veri, ham gerçeklerin bir koleksiyonudur ve bu ham gerçekleri daha anlamlı bir şekilde sunmak için elektronik tablo belgeleri veya raporlar oluştururuz. Genellikle veri ekleriz ancak bazen mevcut veri kaynaklarını yeniden kullanmamız gerekebilir ve burada farklı veri kaynaklarından çalışsayılara veri almanın ihtiyacı ortaya çıkar.

## **Aspose.Cells Kullanarak Veri İçe Aktarma**

**Aspose.Cells**’i bir Excel dosyasını açmak için kullandığınızda, dosyadaki tüm veriler otomatik olarak alınır ancak Aspose.Cells, farklı veri kaynaklarından veri almayı da destekler. Bu veri kaynaklarından bazıları aşağıda listelenmiştir:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells, bir Excel dosyasını temsil eden **Workbook** adlı bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışsayıya erişime izin veren bir Worksheets koleksiyonunu içerir. Bir çalışsayı, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, bir Hücreler koleksiyonu sağlar.

Hücreler koleksiyonu, farklı veri kaynaklarından veri almak için çok kullanışlı yöntemler sağlar.

### **Diziden Alınan Veri**

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

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **ArrayList'ten Alınan Veri**

Geliştiriciler, Hücreler koleksiyonunun **ImportArrayList** yöntemini çağırarak verileri ArrayList'ten çalışma sayfalarına alabilirler. ImportArray yöntemi aşağıdaki parametreleri alır: **ArrayList** , içeriği alınması gereken ArrayList nesnesini temsil eder

- Satır Numarası , verinin alınacağı ilk hücrenin satır numarasını temsil eder
- Sütun Numarası , verinin alınacağı ilk hücrenin sütun numarasını temsil eder
- Dikey, verinin dikey veya yatay olarak alınmasını belirten boolean bir değerdir

{{< highlight csharp >}}

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

### **Özel Nesnelerden Alınan Veri**

Geliştiriciler, istenen nesne listesini göstermek için **ImportCustomObjects** yöntemini kullanarak bir çalışma sayfasına nesne koleksiyonundan veri alabilirler.

{{< highlight csharp >}}

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

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

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

### **DataTable'dan Alınan Veri**

Geliştiriciler, Hücreler koleksiyonunun **ImportDataTable** yöntemini çağırarak **DataTable**'den veri alabilirler. **ImportDataTable** yönteminin çok sayıda aşırı yüklenmiş sürümü olsa da, tipik bir aşırı yüklemenin aşağıdaki parametreleri alır: **DataTable** , içeriği alınması gereken **DataTable** nesnesini temsil eder

- **Alan Adı Gösterilsin Mi**, DataTable sütunlarının çalışma sayfasına ilk satır olarak alınıp alınmayacağını belirtir
- **Başlangıç Hücresi** , DataTable içeriğinin nereden alınacağını temsil eden başlangıç hücresinin adını (örn. "A1") temsil eder

{{< highlight csharp >}}

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

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Örnek Kod İndir**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Belgeden Veri Aktar**

Aspose.Cells, kullanıcılarının yalnızca dış veri kaynaklarından çalışsayılarına veri almasına olanak tanımakla kalmaz, aynı zamanda çalışsayı verilerini bir **DataTable**'a aktarmalarına da izin verir.

## **Aspose.Cells Kullanarak Veriyi DataTable (.NET)’e Aktarma**

Geliştiriciler, Cells sınıfının ExportDataTable veya ExportDataTableAsString yöntemini çağırarak çalışsayı verilerini bir DataTable nesnesine kolayca dışa aktarabilirler. Her iki yöntem de farklı senaryolarda kullanılır ve daha ayrıntılı olarak aşağıda tartışılmaktadır.

### **Güçlü-Tiplendirilmiş Veri İçeren Sütunlar**

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

### **Güçlü-Tiplendirilmemiş Veri İçeren Sütunlar**

Bir çalışma sayfasının sütunlarının tüm değerleri güçlü bir şekilde türde değilse (bu, bir sütundaki değerlerin farklı veri tiplerine sahip olabileceği anlamına gelir) o zaman **Cells** sınıfının **ExportDataTableAsString** yöntemini çağırarak çalışma sayfası içeriğini dışa aktarabiliriz. **ExportDataTableAsString** yöntemi, çalışma sayfasındaki verileri **DataTable** nesnesi olarak dışa aktarmak için **ExportDataTable** yönteminin aldığı parametre setini alır

{{< highlight csharp >}}

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

## **Örnek Kod İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
