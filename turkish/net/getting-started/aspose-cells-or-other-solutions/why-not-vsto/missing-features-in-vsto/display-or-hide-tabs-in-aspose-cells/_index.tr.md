---
title: Aspose.Cells'de Sekmeleri Görüntüle veya Gizle
type: docs
weight: 80
url: /tr/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel dosyasının en altına yakından bakarsanız, bir dizi kontrol görürsünüz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Söz konusu çalışma sayfasına geçmek için herhangi bir sekmeye tıklayın. Çalışma kitabında ne kadar çok çalışma sayfası varsa, o kadar çok sayfa sekmesi vardır. Excel dosyasında çok sayıda çalışma sayfası varsa, bunlar arasında gezinmek için düğmelere ihtiyacınız vardır. Bu nedenle, Microsoft Excel, sayfa sekmeleri arasında gezinmek için sekme kaydırma düğmeleri sağlar.

**Sayfa sekmeleri ve sekme kaydırma düğmeleri** 

![yapılacaklar:resim_alternatif_Metin](display-or-hide-tabs-in-aspose-cells_1.png)

Geliştiriciler, Aspose.Cells'i kullanarak Excel dosyalarındaki sayfa sekmelerinin ve sekme kaydırma düğmelerinin görünürlüğünü kontrol edebilir.

{{% /alert %}} 

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilen dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır.

Book1.xls dosyasının aşağıdaki şekilde sekmeler içerdiğini görebilirsiniz. Örnek kod yürütüldükten sonra, aşağıdaki output.xls dosyasının ekran görüntüsünden de görebileceğiniz gibi sekmeler gizlenir.

**book1.xls: Herhangi bir değişiklikten önceki Excel dosyası** 

![yapılacaklar:resim_alternatif_Metin](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Değişiklikten sonra Excel dosyası** 

![yapılacaklar:resim_alternatif_Metin](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Sekme Çubuğu Genişliğini Kontrol Etme**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
