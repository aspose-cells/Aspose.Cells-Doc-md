---
title: Aspose.Cells'de Kılavuz Çizgilerini Görüntüleyin veya Gizle
type: docs
weight: 50
url: /tr/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Tüm Excel çalışma sayfalarında varsayılan olarak kılavuz çizgileri bulunur. Belirli hücrelere veri girmenin kolay olması için hücrelerin tanımlanmasına yardımcı olurlar. Kılavuz çizgileri, bir çalışma sayfasını, her hücrenin kolayca tanımlanabildiği bir hücreler koleksiyonu olarak görmemizi sağlar.

{{% /alert %}}

## **Kılavuz Çizgilerin Görünürlüğünü Kontrol Etme**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class, bir çalışma sayfasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Kılavuz çizgilerinin görünürlüğünü kontrol etmek için[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf'[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Emlak.[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) bir Boolean özelliğidir, yani yalnızca bir**doğru** veya**yanlış** değer.

 kullanımını gösteren tam bir örnek aşağıda verilmiştir.[**Izgara Çizgileri Görünür mü**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) mülkiyeti[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Excel dosyasının ilk çalışma sayfasının kılavuz çizgilerini gizlemek için sınıf.

Aşağıdaki ekran görüntüsünde, Book1.xls dosyasının üç çalışma sayfası içerdiğini görebilirsiniz: Sayfa1, Sayfa2 ve Sayfa3. Tüm çalışma sayfalarının kılavuz çizgileri vardır.

**Book1.xls: değişiklikten önce çalışma sayfası görünümü** 

![yapılacaklar:resim_alternatif_Metin](display-or-hide-gridlines-in-aspose-cells_1.png)

Book1.xls dosyası Workbook sınıfı kullanılarak açılır ve ilk çalışma sayfasındaki kılavuz çizgileri gizlenir. Değiştirilen dosya output.xls olarak kaydedilir.

**Output.xls: değişiklikten sonra çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Örnek Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
