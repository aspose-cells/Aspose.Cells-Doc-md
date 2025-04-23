---
title: Aspose.Cells 16.11.0 daki Genel API Değişiklikleri
type: docs
weight: 360
url: /tr/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sindeki değişiklikleri 16.10.0'dan 16.11.0'a modül / uygulama geliştiricileri için ilginç olabilecek şekilde açıklar. Yeni ve güncellenmiş genel metotlar, eklenen ve kaldırılan sınıflar vb. yanı sıra Aspose.Cells'in arkasındaki davranışta herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Küreselleşme Ayarları Desteği**
Aspose.Cells 16.11.0, Aspose.Cells API'larını custom etiketler kullanmaya zorlamak için GlobalizationSettings sınıfını ve WorkbookSettings.GlobalizationSettings özelliğini açığa çıkardı. GlobalizationSettings sınıfı, aşağıdaki yöntemleri içerir ve özelleştirilmiş uygulamasında istenilen adları **Toplam** ve **Genel Toplam** için döndürmek için bu şekilde üzerine yazılabilir.

- GlobalizationSettings.getTotalName: Fonksiyonun toplam adını alır.
- GlobalizationSettings.getGrandTotalName: Fonksiyonun genel toplam adını alır.

Bu, GlobalizationSettings sınıfını genişleten ve konsolidasyon fonksiyonu Ortalama için özel etiketler döndürmek için yukarıdaki yöntemlerinin üzerine yazıldığı basit bir özel sınıfın kullanım senaryosudur.

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

Aşağıdaki kod parçacığı, mevcut bir elektronik tabloyu yükler ve çalışma sayfasında zaten mevcut verilere Ortalama türünde bir Öz-toplam ekler. Özelleştirilmiş Ayarlar sınıfı ve getTotalName & getGrandTotalName yöntemleri, çalışma sayfasına Öz-toplam eklerken çağrılacaktır.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

GlobalizationSettings sınıfı, ayrıca, Pasta grafikleri için "Diğer" etiketlerinin adını almak için faydalı olan getOtherName yöntemini sunar. Burada, GlobalizationSettings.getOtherName yönteminin basit kullanım senaryosu bulunmaktadır.

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

Aşağıdaki kod parçacığı, yukarıda oluşturulan Özel Ayarlar sınıfını kullanarak bir Pasta grafik içeren mevcut bir elektronik tabloyu yükler ve grafikleri görüntüler.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **Eklenen CellsFactory Sınıfı**
Aspose.Cells 16.11.0, şu anda yalnızca bir yönteme sahip olan CellsFactory sınıfını açığa çıkardı, yani; createStyle. CellsFactory.createStyle yöntemi, bunu çalışma kitabı stiller havuzuna eklemeksizin Style sınıfından bir örnek oluşturmak için kullanılabilir.

CellsFactory.createStyle yönteminin basit kullanım senaryosu burada.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Eklenen Workbook.AbsolutePath Özelliği**
Aspose.Cells 16.11.0, Workbook.AbsolutePath özelliğini, depolanan workbook.xml dosyasında bulunan mutlak çalışma kitabı yolunu almak veya ayarlamak için kullanılmasını sağlar. Bu özellik, yalnızca dış bağlantıları güncellerken faydalıdır.
### **Eklenen GridHyperlinkCollection.getHyperlink Yöntemi**
Aspose.Cells.GridWeb 16.11.0, GridHyperlinkCollection sınıfına getHyperlink yöntemini açıkladı. Bu, bir GridCell örneğini geçerek GridHyperlink örneğini veya satır sütun dizinlerine karşılık gelen bir çift geçerek almak için kullanılır.

{{% alert color="primary" %}} 

Belirtilen hücrede hiçbir hyperlink bulunamadıysa, getHyperlink yöntemi null değer döndürecektir.

{{% /alert %}} 

getHyperlink yönteminin basit kullanım senaryosu burada.

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **Eskimiş API'lar**
### **Eski Style Constructor Obsoleted**
Alternatif olarak cellsFactory.createStyle yöntemini kullanınız.
## **Silinmiş API'lar**
### **Silinen Cell.getConditionalStyle Yöntemi**
Lütfen Cell.getConditionalFormattingResult yöntemini kullanın.
### **Silinen Cells.getMaxDataRowInColumn(int column) Yöntemi**
Lütfen alternatif olarak Cells.getLastDataRow(int) yöntemini kullanın.
### **Silinen PageSetup.Draft Özelliği**
PageSetup.PrintDraft özelliğini kullanmanız önerilir.
### **Silinen AutoFilter.FilterColumnCollection Özelliği**
Aynı hedefi elde etmek için lütfen AutoFilter.FilterColumns özelliğini düşünün.
### **Silinen TickLabels.Rotation Özelliği**
Lütfen TickLabels.RotationAngle özelliğini kullanın.
{{< app/cells/assistant language="java" >}}
