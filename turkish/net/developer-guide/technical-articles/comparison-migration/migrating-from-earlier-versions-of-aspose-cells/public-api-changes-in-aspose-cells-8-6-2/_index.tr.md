---
title: Aspose.Cells 8.6.2 de Kamu API Değişiklikleri
type: docs
weight: 210
url: /tr/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sindeki 8.6.1'den 8.6.2'ye yapılan değişiklikleri modül/uygulama geliştiricileri için ilginç olabilecek değişiklikleri açıklar. Yeni ve güncellenmiş kamu metodları, eklenen sınıfların yanı sıra Aspose.Cells'in arka planda olan herhangi bir değişikliği de içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Akıllı İşaretçiler ile Geri Arama Desteği**
Bu Aspose.Cells for .NET API sürümü, WorkbookDesigner.CallBack özelliğini ve ISmartMarkerCallBack arabirimini açığa çıkarmıştır, bu da birlikte hücre referansı ve/veya smart marker işlenirken bildirim almayı sağlar. Aşağıdaki kod parçası, WorkbookDesigner.Process yöntemi için geri arama tanımlayan yeni bir sınıfı tanımlamak için ISmartMarkerCallBack arabirimini kullanımını gösterir.

**C#**

{{< highlight csharp >}}

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



İşlemin geri kalanı, tasarımcı elek ve veri kaynağını ayarlayarak içeren işlemi yüklemeyi içerir. Ancak bildirimleri etkinleştirmek için, WorkbookDesigner.Process yöntemi çağrılmadan önce WorkbookDesigner.CallBack özelliğini ayarlamak gereklidir.

**C#**

{{< highlight csharp >}}

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


### **Chart.ToPdf Yöntemi Eklendi**
Aspose.Cells for .NET 8.6.2, Chart.ToPdf yöntemini açığa çıkarmıştır, bu yöntem, Chart şeklini doğrudan PDF formatına dönüştürmek için kullanılabilir. Söz konusu yöntem şu anda sonuç dosyasını diske kaydetmek için dosya yolu konumunda bir string türünde parametre kabul eder.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Workbook.RemoveUnusedStyles Yöntemi Eklendi**
Aspose.Cells for .NET 8.6.2, Workbook.RemoveUnusedStyles yöntemini açığa çıkarmıştır, bu yöntem, stili temizlenmemiş Style nesnelerini kaldırmak için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Eklenen Cells.Style Özelliği**
Cells.Style özelliği, Varsayılan stilin temsil edildiği Çalışma Sayfasıiçin Stil'e erişmek için kullanılabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **GridWeb için Eklenen Olaylar**
Aspose.Cells.GridWeb for .NET 8.6.2, aşağıdaki iki yeni olayı açığa çıkarmıştır.

1. AjaxCallFinished: Denetimin AJAX güncellemesi tamamlandığında tetiklenir. (EnableAJAX true olarak ayarlanmalıdır).
1. CellModifiedOnAjax: Hücre AJAX çağrısı sırasında değiştirildiğinde tetiklenir.
{{< app/cells/assistant language="csharp" >}}
