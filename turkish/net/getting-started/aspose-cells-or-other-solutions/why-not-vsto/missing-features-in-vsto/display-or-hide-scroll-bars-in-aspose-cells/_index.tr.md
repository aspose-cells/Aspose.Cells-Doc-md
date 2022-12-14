---
title: Aspose.Cells'de Kaydırma Çubuklarını Görüntüleyin veya Gizle
type: docs
weight: 70
url: /tr/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Kaydırma çubukları, herhangi bir dosyanın içeriğinde gezinmek için çok kullanılır. Normalde iki tür kaydırma çubuğu vardır:

- Dikey kaydırma çubukları
- Yatay kaydırma çubukları

Microsoft Excel, kullanıcıların çalışma sayfası içeriklerinde gezinebilmeleri için yatay ve dikey kaydırma çubukları da sağlar. Geliştiriciler, Aspose.Cells'i kullanarak Excel dosyalarındaki her iki kaydırma çubuğunun da görünürlüğünü kontrol edebilir.

{{% /alert %}}

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Bu bir Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Kaydırma çubuklarının görünürlüğünü kontrol etmek için,[**Çalışma Kitabı Ayarları**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) sınıf'[**IsVScrollBarGörünür**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve[**IsHScrollBarGörünür**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) özellikleri.[**IsVScrollBarGörünür**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ve[**IsHScrollBarGörünür**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Boole özellikleridir; bu, bu özelliklerin yalnızca depolayabileceği anlamına gelir.**doğru** veya**yanlış** değerler.

Aşağıda, book1.xls adlı bir Excel dosyasını açan, her iki kaydırma çubuğunu da gizleyen ve ardından değiştirilen dosyayı output.xls olarak kaydeden eksiksiz bir kod bulunmaktadır.

Aşağıdaki ekran görüntüsü, her iki kaydırma çubuğunu da içeren Book1.xls dosyasını göstermektedir. Değiştirilen dosya, aşağıda da gösterilen output.xls dosyası olarak kaydedilir.

**Book1.xls: Herhangi bir değişiklik yapılmadan önceki Excel dosyası**

![yapılacaklar:resim_alternatif_Metin](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Değişiklikten sonra Excel dosyası**

![yapılacaklar:resim_alternatif_Metin](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Örnek Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
