---
title: Aspose.Cells'de Bağlantı Verilerine Köprüler Ekleme
type: docs
weight: 10
url: /tr/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

İki varlık arasında bir bağlantı oluşturmak için bir köprü kullanılır. Herkes, özellikle web sitelerinde, hiper bağlantıların kullanımına aşinadır.

Aspose.Cells'i kullanan geliştiriciler, Microsoft Excel dosyalarında farklı türden köprüler oluşturabilir. Bu konuda, Aspose.Cells tarafından hangi tür köprülerin desteklendiği ve bunların Excel dosyalarımızda nasıl kullanılabileceği açıklanmaktadır.

{{% /alert %}}

## **Köprü Ekleme**

Aspose.Cells kullanılarak bir hücreye üç tür köprü eklenebilir:

- [Bir URL'ye bağlantı ekleme](#adding-link-to-a-url).
- [Aynı dosyadaki başka bir hücreye bağlantı ekleme](#adding-a-link-to-a-cell-in-the-same-file).
- [Harici bir dosyaya bağlantı ekleme](#adding-a-link-to-an-external-file).

 Aspose.Cells, geliştiricilerin Excel dosyalarına API veya[tasarımcı elektronik tabloları](/cells/tr/net/what-is-a-designer-spreadsheet/)(köprülerin manuel olarak oluşturulduğu ve bunları diğer elektronik tablolara aktarmak için Aspose.Cells'in kullanıldığı elektronik tablolar).

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, Excel dosyalarına farklı köprüler eklemek için farklı yöntemler sağlar.

### **Bir URL'ye Bağlantı Ekleme**

 bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir içerir[**köprüler**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Toplamak. Köprüler koleksiyonundaki her öğe bir Köprüyü temsil eder. Hyperlinks koleksiyonunun Add yöntemini çağırarak URL'lere köprüler ekleyin. Add yöntemi aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı
- URL, URL adresi.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Aynı Dosyada Cell'e Bağlantı Ekleme**

Hyperlink koleksiyonunun Add yöntemini çağırarak aynı Excel dosyasındaki hücrelere köprü eklemek mümkündür. Add yöntemi hem iç hem de dış köprüler için çalışır. Aşırı yüklenmiş yöntemin bir sürümü aşağıdaki parametreleri alır:

- Cell ad, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Harici Dosyaya Bağlantı Ekleme**

Hyperlinks koleksiyonunun Add yöntemini çağırarak harici Excel dosyalarına köprüler eklemek mümkündür. Add yöntemi aşağıdaki parametreleri alır:

- Cell adı, köprünün ekleneceği hücrenin adı.
- Satır sayısı, bu köprü aralığındaki satır sayısı.
- Sütun sayısı, bu köprü aralığındaki sütun sayısı.
- URL, hedefin adresi, harici Excel dosyası.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Örnek Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
