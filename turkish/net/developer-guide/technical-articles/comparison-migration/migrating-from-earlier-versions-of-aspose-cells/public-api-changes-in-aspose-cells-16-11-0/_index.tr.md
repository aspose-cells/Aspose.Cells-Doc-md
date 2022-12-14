---
title: Genel API Aspose.Cells 16.11.0'daki değişiklikler
type: docs
weight: 350
url: /tr/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.10.0 sürümünden 16.11.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Küreselleştirme Ayarları Desteği**
Aspose.Cells 16.11.0, Aspose.Cells API'lerini Alt Toplamlar için özel etiketler kullanmaya zorlamak amacıyla WorkbookSettings.GlobalizationSettings özelliğiyle birlikte GlobalizationSettings sınıfını kullanıma sundu. GlobalizationSettings sınıfı, etiketlere istenen adları vermek için özel uygulamada geçersiz kılınabilen aşağıdaki yöntemlere sahiptir.**Toplam** & **Genel Toplam**.

- GlobalizationSettings.GetTotalName: Fonksiyonun toplam adını alır.
- GlobalizationSettings.GetGrandTotalName: İşlevin genel toplam adını alır.

İşte GlobalizationSettings sınıfını genişleten ve birleştirme işlevi Ortalama için özel etiketler döndürmek üzere yukarıda belirtilen yöntemlerini geçersiz kılan basit bir özel sınıf.

**C#**

{{< highlight "csharp" >}}

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



Aşağıdaki kod parçacığı, mevcut bir elektronik tabloyu yükler ve çalışma sayfasında zaten mevcut olan verilere Ortalama türündeki Alt Toplamı ekler. CustomSettings sınıfı ve onun GetTotalName & GetGrandTotalName yöntemleri, çalışma sayfasına Alt Toplam eklenirken çağrılır.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



GlobalizationSettings sınıfı, Pasta grafikleri için "Diğer" etiketlerinin adını almakta yararlı olan GetOtherName yöntemini de sunar. İşte GlobalizationSettings.GetOtherName yönteminin basit bir kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

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



Aşağıdaki kod parçacığı, Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve yukarıda oluşturulan CustomSettings sınıfını kullanırken grafiği resme dönüştürür.

**C#**

{{< highlight "csharp" >}}

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


### **CellsFactory Sınıfı Eklendi**
Aspose.Cells 16.11.0, şu anda bir yöntemi olan CellsFactory sınıfını kullanıma açtı, yani; Stil Oluştur. CellsFactory.CreateStyle yöntemi, çalışma kitabı stilleri havuzuna eklemeden bir Style sınıfı örneği oluşturmak için kullanılabilir.

İşte CellsFactory.CreateStyle yönteminin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Workbook.AbsolutePath Özelliği Eklendi**
Aspose.Cells 16.11.0, workbook.xml dosyasında saklanan mutlak çalışma kitabı yolunun alınmasına veya ayarlanmasına izin veren Workbook.AbsolutePath özelliğini kullanıma sundu. Bu özellik, yalnızca harici bağlantıları güncellerken kullanışlıdır.
### **GridHyperlinkCollection.GetHyperlink Yöntemi Eklendi**
Aspose.Cells.GridWeb 16.11.0, GetHyperlink yöntemini GridHyperlinkCollection sınıfına maruz bıraktı; bu sınıf, bir GridCell örneğini veya satır sütun indekslerine karşılık gelen bir çift tamsayı geçirerek GridHyperlink örneğini almaya olanak tanır.

{{% alert color="primary" %}} 

Belirtilen hücrede köprü bulunmaması durumunda GetHyperlink yöntemi null değerini döndürür.

{{% /alert %}} 

İşte GetHyperlink yönteminin basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **Eski API'ler**
### **Eski Stil Oluşturucu**
Lütfen alternatif olarak cellFactory.CreateStyle yöntemini kullanın.
## **Silinmiş API'ler**
### **Cell.GetConditionalStyle Yöntemi Silindi**
Lütfen bunun yerine Cell.GetConditionalFormattingResult yöntemini kullanın.
### **Cells.MaxDataRowInColumn(int sütunu) Yöntem Silindi**
Lütfen alternatif olarak Cells.GetLastDataRow(int) yöntemini kullanın.
### **PageSetup.Draft Özelliği Silindi**
Bunun yerine PageSetup.PrintDraft özelliğinin kullanılması önerilir.
### **Silinmiş AutoFilter.FilterColumnCollection Özelliği**
Aynı hedefe ulaşmak için lütfen AutoFilter.FilterColumns özelliğini kullanmayı düşünün.
### **TickLabels.Rotation Özelliği Silindi**
Lütfen bunun yerine TickLabels.RotationAngle özelliğini kullanın.
