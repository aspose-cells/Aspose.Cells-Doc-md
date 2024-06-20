---
title: Aspose.Cells te Izgaraları Gösterme veya Gizleme
type: docs
weight: 50
url: /tr/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

Tüm Excel çalışsayılarının varsayılan olarak ızgaraları bulunmaktadır. Bunlar hücreleri belirginleştirmeye yardımcı olur, bu sayede belirli hücrelere veri girmek kolay olur. Izgaralar, bir çalışsayıyı hücrelerin bir koleksiyonu olarak görüntülememizi sağlar, her hücre kolayca tanımlanabilir hale gelir.

{{% /alert %}}

## **Izgaraların Görünürlüğünü Kontrol Etme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)'ı sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışsayıya erişime izin veren bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir.

Bir çalışsayı, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışsayıyı yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Izgaraların görünürlüğünü kontrol etmek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) özelliğini kullanın. [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible), yalnızca **true** veya **false** bir değer saklayabilen bir Boolean özelliğidir .

Aşağıda kullanımını gösteren tam bir örnek verilmiştir. Excel dosyasının ilk çalışma sayfasının ızgaralarını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfının [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) özelliği kullanılır.

Aşağıdaki ekran görüntüsünde Book1.xls dosyasının üç çalışma sayfası: Sheet1, Sheet2 ve Sheet3 bulunmaktadır. Tüm çalışma sayfalarının ızgaraları bulunmaktadır.

**Book1.xls: düzenlemeden önce çalışma sayfası görünümü** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Book1.xls dosyası Workbook sınıfı kullanılarak açılır ve ilk çalışma sayfasındaki ızgaralar gizlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

**Output.xls: düzenlemeden sonra çalışma sayfası** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Örnek Kod İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
