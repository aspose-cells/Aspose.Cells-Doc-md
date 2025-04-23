---
title: Aspose.Cells 16.11.0 daki Genel API Değişiklikleri
type: docs
weight: 350
url: /tr/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sindeki değişiklikleri 16.10.0'dan 16.11.0'a modül / uygulama geliştiricileri için ilginç olabilecek şekilde açıklar. Yeni ve güncellenmiş genel metotlar, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arkasındaki davranışta herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Küreselleşme Ayarları Desteği**
Aspose.Cells 16.11.0, Aspose.Cells API'larını custom etiketler kullanmaya zorlamak için GlobalizationSettings sınıfını ve WorkbookSettings.GlobalizationSettings özelliğini açığa çıkardı. GlobalizationSettings sınıfı, aşağıdaki yöntemleri içerir ve özelleştirilmiş uygulamasında istenilen adları **Toplam** ve **Genel Toplam** için döndürmek için bu şekilde üzerine yazılabilir.

- GlobalizationSettings.GetTotalName: Fonksiyonun toplam adını alır.
- GlobalizationSettings.GetGrandTotalName: Fonksiyonun büyük toplam adını alır.

Bu, GlobalizationSettings sınıfını genişleten ve konsolidasyon fonksiyonu Ortalama için özel etiketler döndürmek için yukarıdaki yöntemlerinin üzerine yazıldığı basit bir özel sınıfın kullanım senaryosudur.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



Aşağıdaki kod parçası, var olan bir elektronik tabloyu yükler ve çalışma sayfasında zaten mevcut olan verilere Subtotal ekler. Subtotal eklenirken CustomSettings sınıfı ve GetTotalName & GetGrandTotalName yöntemleri çağrılacaktır.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



GlobalizationSettings sınıfı aynı zamanda Pie grafikleri için "Diğer" etiketlerin adını almak için faydalı olan GetOtherName yöntemini sunar. İşte GlobalizationSettings.GetOtherName yönteminin basit bir kullanım senaryosu.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



Aşağıdaki kod parçacığı, yukarıda oluşturulan Özel Ayarlar sınıfını kullanarak bir Pasta grafik içeren mevcut bir elektronik tabloyu yükler ve grafikleri görüntüler.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **Eklenen CellsFactory Sınıfı**
Aspose.Cells 16.11.0, şu anda CreateStyle adında bir yöntemi olan CellsFactory sınıfını açığa çıkarmıştır. CellsFactory.CreateStyle yöntemi, Style sınıfının havuza eklenmeden bir örneğini oluşturmak için kullanılabilir.

İşte CellsFactory.CreateStyle yönteminin basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Eklenen Workbook.AbsolutePath Özelliği**
Aspose.Cells 16.11.0, Workbook.AbsolutePath özelliğini, depolanan workbook.xml dosyasında bulunan mutlak çalışma kitabı yolunu almak veya ayarlamak için kullanılmasını sağlar. Bu özellik, yalnızca dış bağlantıları güncellerken faydalıdır.
### **Eklenen GridHyperlinkCollection.GetHyperlink Yöntemi**
Aspose.Cells.GridWeb 16.11.0, GridHyperlinkCollection sınıfına GetHyperlink yöntemini açığa çıkarmıştır. Bu yöntemle GridCell örneği veya satır sütun dizinlerine karşılık gelen iki tam sayı çiftini geçirerek GridHyperlink örneğini alabilirsiniz.

{{% alert color="primary" %}} 

Belirtilen hücrede hiçbir bağlantı bulunmamışsa, GetHyperlink yöntemi null değer döndürecektir.

{{% /alert %}} 

İşte GetHyperlink yönteminin basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **Eskimiş API'lar**
### **Eski Style Constructor Obsoleted**
Alternatif olarak cellsFactory.CreateStyle yöntemini kullanınız.
## **Silinmiş API'lar**
### **Silinmiş Cell.GetConditionalStyle Yöntemi**
Yerine Cell.GetConditionalFormattingResult yöntemini kullanınız.
### **Silinmiş Cells.MaxDataRowInColumn(int column) Yöntemi**
Alternatif olarak Cells.GetLastDataRow(int) yöntemini kullanınız.
### **Silinen PageSetup.Draft Özelliği**
PageSetup.PrintDraft özelliğini kullanmanız önerilir.
### **Silinen AutoFilter.FilterColumnCollection Özelliği**
Aynı hedefi elde etmek için lütfen AutoFilter.FilterColumns özelliğini düşünün.
### **Silinen TickLabels.Rotation Özelliği**
Lütfen TickLabels.RotationAngle özelliğini kullanın.
{{< app/cells/assistant language="csharp" >}}
