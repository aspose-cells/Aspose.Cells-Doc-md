---
title: Aspose.Cells te Sekmelerin Görüntülenmesi veya Gizlenmesi
type: docs
weight: 80
url: /tr/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:

- Sayfa sekmeleri.
- Sekme kaydırma düğmeleri.

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.

**Sayfa sekmeleri & sekme kaydırma düğmeleri** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

Aspose.Cells kullanarak geliştiriciler Excel dosyalarında sayfa sekmelerinin ve sekmelerin kaydırma düğmelerinin görünürlüğünü kontrol edebilirler. 

{{% /alert %}} 

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmesini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır.

Book1.xls dosyasının aşağıdaki şekilde sekmeler içerdiğini görebilirsiniz. Örnek kod çalıştırıldıktan sonra, sekmeler gizlenir ve output.xls dosyasının ekran görüntüsünde gördüğünüz gibi görünür.

**book1.xls: Herhangi bir değişiklik öncesi Excel dosyası** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Değişiklik sonrası Excel dosyası** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
