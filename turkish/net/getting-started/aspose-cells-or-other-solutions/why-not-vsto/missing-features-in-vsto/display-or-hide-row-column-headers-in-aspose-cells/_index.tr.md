---
title: Aspose.Cells da Satır ve Sütun Başlıklarını Göster veya Gizle
type: docs
weight: 60
url: /tr/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Bir Excel dosyasındaki tüm çalışma sayfaları, satır ve sütunlarda düzenlenen hücrelerden oluşur. Tüm satırlar ve sütunlar, bunları tanımlamak ve tek hücreleri tanımlamak için kullanılan benzersiz değerlere sahiptir. Örneğin, satırlar - 1, 2, 3, 4, vb. - numaralandırılır ve sütunlar alfabetik olarak sıralanır - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda gösterilir. Aspose.Cells kullanarak geliştiriciler, bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

{{% /alert %}}

## **Çalışma sayfalarının görünürlüğünü kontrol etmek**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) özelliğini kullanın. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) sadece **true** veya **false** değerini saklayabilen bir Boolean özelliğidir.

Aşağıda, bir dosyanın ilk çalışma sayfasındaki satır ve sütun başlıklarını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) özelliğini nasıl kullanacağını gösteren tam bir örnek verilmiştir.

Ekran görüntüsü Book1.xls'i, giriş dosyasını gösteriyor. Sheet1, Sheet2 ve Sheet3 olmak üzere üç çalışma sayfası içeriyor. Her çalışma sayfası satır ve sütun başlıklarını gösteriyor.

**Book1.xls: herhangi bir değişiklik yapılmadan önce çalışma sayfası**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls, Workbook sınıfı'nın Open yöntemi çağrılarak açılır ve ilk çalışma sayfasındaki satır ve sütun başlıkları gizlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

**Output.xls: düzenlemeden sonra çalışma sayfası** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
