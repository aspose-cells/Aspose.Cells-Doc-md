---
title: Genel API Aspose.Cells 8.6.2'deki değişiklikler
type: docs
weight: 220
url: /tr/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.6.1'den 8.6.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen sınıfları değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Akıllı İşaretleyicilerle Geri Arama Desteği**
Aspose.Cells for Java API'in bu sürümü, WorkbookDesigner.CallBack alanını ve ISmartMarkerCallBack arabirimini kullanıma sunmuştur.[işlenmekte olan hücre referansı ve/veya akıllı işaretleyici hakkında bildirimleri alın](/cells/tr/java/getting-notifications-while-merging-data-with-smart-markers/) . Aşağıdaki kod parçası, WorkbookDesigner.process yöntemi için geri aramayı işleyen yeni bir sınıf tanımlamak için ISmartMarkerCallBack arabiriminin kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

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

Sürecin geri kalanı, Smart Marker'ları içeren tasarımcı elektronik tablosunu WorkbookDesigner ile yüklemeyi veya sıfırdan bir tane oluşturmayı ve veri kaynağını ayarlayarak işlemeyi içerir. Ancak bildirimleri etkinleştirmek için aşağıda gösterildiği gibi WorkbookDesigner.process yöntemini çağırmadan önce WorkbookDesigner.CallBack özelliğini ayarlamak gerekir.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Yöntem Chart.toPdf Eklendi**
Aspose.Cells for Java 8.6.2, Chart şeklini doğrudan PDF formatına dönüştürmek için kullanılabilecek Chart.toPdf yöntemini ortaya çıkardı. Bahsedilen yöntem şu anda, ortaya çıkan dosyayı diskte depolamak için dosya yolu konumu olarak String türünde bir parametre kabul etmektedir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Yöntem Workbook.removeUnusedStyles Eklendi**
 Aspose.Cells for Java 8.6.2, Workbook.removeUnusedStyles için kullanılabilecek yöntemi kullanıma sundu.[kullanılmayan tüm Stil nesnelerini stil havuzundan kaldırın](/cells/tr/java/remove-unused-styles-inside-the-workbook/). 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Özellik Cells.Stil Eklendi**
Cells.Style özelliği, varsayılan stili temsil eden Çalışma Sayfasının Stiline erişmek için kullanılabilir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **GridWeb İçin Eklenen Etkinlikler**
Aspose.Cells.GridWeb for Java 8.6.2, aşağıdaki iki yeni olayı ortaya çıkardı.

1. AjaxCallFinished: Denetimin AJAX güncellemesi bittiğinde tetiklenir. (EnableAJAX, true olarak ayarlanmalıdır).
1. CellModifiedOnAjax: AJAX çağrısında hücre değiştirildiğinde tetiklenir.
