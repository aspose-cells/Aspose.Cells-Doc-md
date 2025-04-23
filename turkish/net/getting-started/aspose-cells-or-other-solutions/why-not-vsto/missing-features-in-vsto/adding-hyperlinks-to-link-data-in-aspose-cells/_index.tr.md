---
title: Aspose.Cells te Verileri Bağlamak İçin Bağlantıları Eklemek
type: docs
weight: 10
url: /tr/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

Bir bağlantı, iki varlık arasında bir bağlantı oluşturmak için kullanılır. Herkes, özellikle web sitelerinde bağlantıların kullanımı hakkında bilgilidir.

Aspose.Cells kullanarak, geliştiriciler Microsoft Excel dosyalarında farklı türde bağlantılar oluşturabilir. Bu konu, Aspose.Cells tarafından desteklenen bağlantı türlerini ve bunların Excel dosyalarımızda nasıl kullanılabileceğini tartışmaktadır.

{{% /alert %}}

## **Hyperlinkler Ekleme**

Aspose.Cells, üç farklı bağlantı türünü bir hücreye eklemek için kullanır:

- [URL'ye bağlantı eklemek](#adding-link-to-a-url).
- [Aynı dosyadaki başka bir hücreye bağlantı eklemek](#adding-a-link-to-a-cell-in-the-same-file).
- [Harici bir dosyaya bağlantı eklemek](#adding-a-link-to-an-external-file).

Aspose.Cells, geliştiricilere, Excel dosyalarına bağlantılar eklemelerini ya API ya da [tasarımcı elektronik tablolar](/cells/tr/net/what-is-a-designer-spreadsheet/) (bağlantıların manuel olarak oluşturulduğu elektronik tablolar ve Aspose.Cells'in bunları diğer elektronik tablolara içe aktarma amacıyla kullanıldığı elektronik tablolar) kullanarak sağlar.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir elektronik tabloya erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) içerir. Bir elektronik tablo, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, Excel dosyalarına farklı bağlantıları eklemek için farklı yöntemler sağlar.

### **URL'ye Bağlantı Ekleme**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir [**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) koleksiyonu içerir. Hyperlink koleksiyonundaki her öğe bir Hyperlink'i temsil eder. URL'lere bağlantı eklemek için Hyperlink koleksiyonunun Add yöntemini çağırarak bağlantılar ekleyin. Add yöntemi aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu bağlantı aralığındaki sütun sayısı
- URL, URL adresi.

**C#**

{{< highlight csharp >}}

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

### **Aynı Dosyadaki Bir Hücreye Bağlantı Ekleme**

Aynı Excel dosyasındaki hücrelere hyperlink eklemek için Hyperlink koleksiyonunun Add yöntemini çağırarak mümkündür. Add yöntemi, hem iç hem de dış hyperlink'ler için çalışır. Aşırı yüklenmiş yöntemin bir sürümü aşağıdaki parametreleri alır:

- Hücre adı, hyperlink'in eklenmesi gereken hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef hücrenin adresi.

**C#**

{{< highlight csharp >}}

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

### **Harici Bir Dosyaya Bağlantı Ekleme**

Harici Excel dosyalarına bağlantılar eklemek mümkündür. Bu, Hyperlink koleksiyonunun Add yöntemi çağrılarak yapılabilir. Add yöntemi aşağıdaki parametreleri alır:

- Hücre adı, bağlantı eklenecek hücrenin adı.
- Satır sayısı, bu hyperlink aralığındaki satır sayısı.
- Sütun sayısı, bu hyperlink aralığındaki sütun sayısı.
- URL, hedef harici Excel dosyasının adresi.

**C#**

{{< highlight csharp >}}

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

## **Örnek Kod İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
