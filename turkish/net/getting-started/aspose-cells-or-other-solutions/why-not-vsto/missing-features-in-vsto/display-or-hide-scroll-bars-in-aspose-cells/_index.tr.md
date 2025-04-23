---
title: Aspose.Cells da Kaydırma Çubuklarını Göster veya Gizle
type: docs
weight: 70
url: /tr/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunmaktadır:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel ayrıca yatay ve dikey kaydırma çubukları sağlar böylece kullanıcılar çalışma sayfası içeriğinde kaydırma yapabilirler. Aspose.Cells kullanarak geliştiriciler Excel dosyalarında her iki türde de kaydırma çubuklarının görünürlüğünü kontrol edebilirler.

{{% /alert %}}

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Kaydırma çubuklarının görünürlüğünü kontrol etmek için [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) sınıfının [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) özelliklerini kullanın. [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Boolean özelliklerdir, bu da bu özelliklerin yalnızca **true** veya **false** değerlerini saklayabileceği anlamına gelir.

Aşağıda, bir Excel dosyasını açan, hem dikey hem yatay kaydırma çubuklarını gizleyen ve sonra değiştirilmiş dosyayı output.xls olarak kaydeden tam bir kod bulunmaktadır.

Aşağıdaki ekran görüntüsü, her iki kaydırma çubuğunu da içeren Book1.xls dosyasını göstermektedir. Değiştirilmiş dosya output.xls olarak gösterilmektedir.

**Book1.xls: herhangi bir değişiklik yapılmadan önce Excel dosyası**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Değişiklik sonrası Excel dosyası**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Örnek Kod İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
