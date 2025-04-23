---
title: Aspose.Cells 8.6.2 de Kamu API Değişiklikleri
type: docs
weight: 220
url: /tr/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sindeki 8.6.1'den 8.6.2'ye yapılan değişiklikleri modül/uygulama geliştiricileri için ilginç olabilecek değişiklikleri açıklar. Yeni ve güncellenmiş kamu metodları, eklenen sınıfların yanı sıra Aspose.Cells'in arka planda olan herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Akıllı İşaretçiler ile Geri Arama Desteği**
Bu sürümde, Aspose.Cells for Java API, WorkbookDesigner.CallBack alanını ve ISmartMarkerCallBack arayüzünü ortaya çıkardı ve bu ikisi, WorkbookDesigner.process yöntemi tarafından işlenen hücre referansı ve/veya akıllı işaretçi hakkında bildirim almayı sağlar. Aşağıdaki kod parçası, ISmartMarkerCallBack arayüzünün kullanımını gösterir. 

**Java**

{{< highlight csharp >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

İşlem geri kalan kısmı, tasarım spreadsheet'inin yüklenmesini WorkbookDesigner ile veya sıfırdan bir tane oluşturularak ve veri kaynağının ayarlanarak işlenmesini içerir. Ancak, bildirimleri etkinleştirmek için, WorkbookDesigner.process yönetmeden önce WorkbookDesigner.CallBack özelliğini ayarlamak gereklidir.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Eklenen Chart.toPdf Metodu**
Aspose.Cells for Java 8.6.2, Chart.toPdf methodunu doğrudan Grafik şeklini PDF biçimine dönüştürmek için kullanılabilir hale getirdi. Söz konusu method, şu anda diskte sonuç dosyasını saklamak için dosya yol konumunda tür String parametresini kabul eder.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Eklenen Workbook.removeUnusedStyles Metodu**
Aspose.Cells for Java 8.6.2, Workbook.removeUnusedStyles metodunu kullanarak kullanılmayan Tüm Stil nesnelerini kaldırabilirsiniz. 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Eklenen Cells.Style Özelliği**
Cells.Style özelliği, Varsayılan stilin temsil edildiği Çalışma Sayfasıiçin Stil'e erişmek için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **GridWeb için Eklenen Olaylar**
Aspose.Cells.GridWeb for Java 8.6.2, aşağıda verilen iki yeni olayı ortaya çıkardı.

1. AjaxCallFinished: Kontrolün AJAX güncellemesi tamamlandığında tetiklenir. (EnableAJAX true olarak ayarlanmalıdır).
1. CellModifiedOnAjax: Hücre AJAX çağrısı sırasında değiştirildiğinde tetiklenir.
{{< app/cells/assistant language="java" >}}
