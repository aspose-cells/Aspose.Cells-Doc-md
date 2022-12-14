---
title: Genel API Aspose.Cells 8.6.2'deki değişiklikler
type: docs
weight: 210
url: /tr/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.6.1'den 8.6.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen sınıfları değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **Akıllı İşaretleyicilerle Geri Arama Desteği**
 Aspose.Cells for .NET API'in bu sürümü, WorkbookDesigner.CallBack özelliğini ve ISmartMarkerCallBack arabirimini kullanıma sunmuştur.[işlenmekte olan hücre referansı ve/veya akıllı işaretleyici hakkında bildirimleri alın](/cells/tr/net/getting-notifications-while-merging-data-with-smart-markers/). Aşağıdaki kod parçası, WorkbookDesigner.Process yöntemi için geri aramayı işleyen yeni bir sınıf tanımlamak için ISmartMarkerCallBack arabiriminin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



Sürecin geri kalanı, Smart Marker'ları içeren tasarımcı elektronik tablosunu WorkbookDesigner ile yüklemeyi ve veri kaynağını ayarlayarak işlemeyi içerir. Ancak bildirimleri etkinleştirmek için WorkbookDesigner.CallBack özelliği aşağıda gösterildiği gibi WorkbookDesigner.Process yöntemini çağırmadan önce ayarlamak gerekir.

**C#**

{{< highlight "csharp" >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Yöntem Chart.ToPdf Eklendi**
 Aspose.Cells for .NET 8.6.2, Chart.ToPdf yöntemini kullanıma sundu.[Grafik şeklini doğrudan PDF formatına dönüştürün](/cells/tr/net/convert-an-excel-chart-to-image/). Bahsedilen yöntem şu anda sonuçtaki dosyayı diskte depolamak için dosya yolu konumu olarak string türünde bir parametre kabul etmektedir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Yöntem Workbook.RemoveUnusedStyles Eklendi**
 Aspose.Cells for .NET 8.6.2, Workbook.RemoveUnusedStyles için kullanılabilecek yöntemi kullanıma sundu.[kullanılmayan tüm Stil nesnelerini stil havuzundan kaldırın](/cells/tr/net/remove-unused-styles-inside-the-workbook/).

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Özellik Cells.Stil Eklendi**
Cells.Style özelliği, varsayılan stili temsil eden Çalışma Sayfasının Stiline erişmek için kullanılabilir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **GridWeb İçin Eklenen Etkinlikler**
Aspose.Cells.GridWeb for .NET 8.6.2, aşağıdaki iki yeni olayı ortaya çıkardı.

1. AjaxCallFinished: Denetimin AJAX güncellemesi bittiğinde tetiklenir. (EnableAJAX, true olarak ayarlanacaktır).
1. CellModifiedOnAjax: AJAX çağrısında hücre değiştirildiğinde tetiklenir.
