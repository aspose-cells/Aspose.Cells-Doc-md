---
title: Genel API Aspose.Cells 16.11.0'daki değişiklikler
type: docs
weight: 360
url: /tr/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 16.10.0 sürümünden 16.11.0 sürümüne Aspose.Cells API değişikliklerini açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Küreselleştirme Ayarları Desteği**
Aspose.Cells 16.11.0, Aspose.Cells API'lerini Alt Toplamlar için özel etiketler kullanmaya zorlamak amacıyla WorkbookSettings.GlobalizationSettings özelliğiyle birlikte GlobalizationSettings sınıfını kullanıma sundu. GlobalizationSettings sınıfı, etiketlere istenen adları vermek için özel uygulamada geçersiz kılınabilen aşağıdaki yöntemlere sahiptir.**Toplam** & **Genel Toplam**.

- GlobalizationSettings.getTotalName: Fonksiyonun toplam adını alır.
- GlobalizationSettings.getGrandTotalName: İşlevin genel toplam adını alır.

İşte GlobalizationSettings sınıfını genişleten ve birleştirme işlevi Ortalama için özel etiketler döndürmek üzere yukarıda belirtilen yöntemlerini geçersiz kılan basit bir özel sınıf.

**Java**

{{< highlight "csharp" >}}

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

Aşağıdaki kod parçacığı, mevcut bir elektronik tabloyu yükler ve çalışma sayfasında zaten mevcut olan verilere Ortalama türündeki Alt Toplamı ekler. CustomSettings sınıfı ve onun getTotalName & getGrandTotalName yöntemleri, çalışma sayfasına Alt Toplam eklenirken çağrılır.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

GlobalizationSettings sınıfı ayrıca, Pasta grafikler için "Diğer" etiketlerinin adını almak için yararlı olan getOtherName yöntemini de sunar. İşte GlobalizationSettings.getOtherName yönteminin basit bir kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

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

Aşağıdaki kod parçacığı, Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve yukarıda oluşturulan CustomSettings sınıfını kullanırken grafiği resme dönüştürür.

**Java**

{{< highlight "csharp" >}}

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
### **CellsFactory Sınıfı Eklendi**
Aspose.Cells 16.11.0, şu anda bir yöntemi olan CellsFactory sınıfını kullanıma açtı, yani; CreateStyle. CellsFactory.createStyle yöntemi, çalışma kitabı stilleri havuzuna eklemeden bir Style sınıfı örneği oluşturmak için kullanılabilir.

İşte CellsFactory.createStyle yönteminin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Workbook.AbsolutePath Özelliği Eklendi**
Aspose.Cells 16.11.0, workbook.xml dosyasında saklanan mutlak çalışma kitabı yolunun alınmasına veya ayarlanmasına izin veren Workbook.AbsolutePath özelliğini kullanıma sundu. Bu özellik, yalnızca harici bağlantıları güncellerken kullanışlıdır.
### **GridHyperlinkCollection.getHyperlink Yöntemi Eklendi**
Aspose.Cells.GridWeb 16.11.0, getHyperlink yöntemini GridHyperlinkCollection sınıfına maruz bıraktı; bu sınıf, bir GridCell örneğini veya satır sütun indekslerine karşılık gelen bir tamsayı çiftini geçirerek GridHyperlink örneğini almaya olanak tanır.

{{% alert color="primary" %}} 

Belirtilen hücrede köprü bulunmaması durumunda getHyperlink yöntemi null değerini döndürür.

{{% /alert %}} 

İşte getHyperlink yönteminin basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **Eski API'ler**
### **Eski Stil Oluşturucu**
Lütfen alternatif olarak cellFactory.createStyle yöntemini kullanın.
## **Silinmiş API'ler**
### **Cell.getConditionalStyle Yöntemi Silindi**
Lütfen bunun yerine Cell.getConditionalFormattingResult yöntemini kullanın.
### **Cells.getMaxDataRowInColumn(int sütunu) Yöntem Silindi**
Lütfen alternatif olarak Cells.getLastDataRow(int) yöntemini kullanın.
### **PageSetup.Draft Özelliği Silindi**
Bunun yerine PageSetup.PrintDraft özelliğinin kullanılması önerilir.
### **Silinmiş AutoFilter.FilterColumnCollection Özelliği**
Aynı hedefe ulaşmak için lütfen AutoFilter.FilterColumns özelliğini kullanmayı düşünün.
### **TickLabels.Rotation Özelliği Silindi**
Lütfen bunun yerine TickLabels.RotationAngle özelliğini kullanın.
