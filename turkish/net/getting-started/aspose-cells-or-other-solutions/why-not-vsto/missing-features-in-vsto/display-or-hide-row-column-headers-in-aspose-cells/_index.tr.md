---
title: Aspose.Cells'de Satır Sütun Başlıklarını Görüntüleyin veya Gizle
type: docs
weight: 60
url: /tr/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlar halinde düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar, onları ve tek tek hücreleri tanımlamak için kullanılan benzersiz değerlere sahiptir. Örneğin, satırlar – 1, 2, 3, 4, vb. – numaralandırılır ve sütunlar alfabetik olarak sıralanır – A, B, C, D, vb. Başlıklarda satır ve sütun değerleri görüntülenir. Geliştiriciler, Aspose.Cells'i kullanarak bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.

{{% /alert %}}

## **Çalışma Sayfalarının Görünürlüğünü Kontrol Etme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) Emlak.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya**YANLIŞ** değer.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) dosyadaki ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleme özelliği.

Ekran görüntüsü, giriş dosyası olan Book1.xls'yi gösterir. Üç çalışma sayfası içerir: Sayfa1, Sayfa2 ve Sayfa3. Her çalışma sayfası satır ve sütun başlıklarını gösteriyor.

**Book1.xls: değişiklikten önceki çalışma sayfası**

![yapılacaklar:resim_alternatif_metin](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls, Workbook sınıfının Open yöntemi çağrılarak açılır ve ilk çalışma sayfasındaki satır ve sütun başlıkları gizlenir. Değiştirilen dosya output.xls olarak kaydedilir.

**Output.xls: değişiklikten sonra çalışma sayfası** 

![yapılacaklar:resim_alternatif_metin](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
