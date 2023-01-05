---
title: Paketleme Cell Metin
type: docs
weight: 130
url: /tr/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

Metni kaydırmak, okumayı kolaylaştırır: Sarılmış metne sahip bir hücre, metne sığacak şekilde genişler, böylece metin diğer hücrelerin üzerinde görüntülenmez.

Aspose.Cells for .NET ile geliştiriciler, uygulamalarında, kullanıcıların Microsoft Excel ile gerçekleştirebildiği görevlerin çoğunu, hücrelerdeki metni kaydırma dahil gerçekleştirebilir. Bu makale, VSTO ve Aspose.Cells'in nasıl kullanıldığını açıklar ve görevi karşılaştırır. Aspose.Cells, verimli kodlama için optimize edilmiştir ve Microsoft Otomasyonu olmadan çalışır.

{{% /alert %}}

## **Paketleme Cell Metin**

Biri kaydırılmış metin içeren ve diğeri içermeyen iki hücreli bir çalışma sayfası oluşturmak için:

1. Çalışma sayfasını ayarlayın:
 1. Bir çalışma kitabı oluşturun.
 1. İlk çalışma sayfasına erişin.
1. Yazı ekle:
 1. A1 hücresine metin ekleyin.
 1. Kaydırılmış metni A5 hücresine ekleyin.
1. Elektronik tabloyu kaydedin.

 Aşağıdaki kod örnekleri, kullanarak bu adımların nasıl gerçekleştirileceğini gösterir.[VSTO](/cells/tr/net/wrapping-cell-text/) C# veya Visual Basic ile. kullanarak aynı şeyi nasıl yapacağınızı gösteren kod örnekleri[Aspose.Cells for .NET](/cells/tr/net/wrapping-cell-text/), yine C# veya Visual Basic kullanarak hemen ardından izleyin.

Kodun çalıştırılması, biri sarmalanmamış metin ve diğeri aşağıdakileri içeren iki hücreli bir elektronik tabloyla sonuçlanır:

|<p>**VSTO ile çıktı sarma hücre metni** </p><p>![yapılacaklar:resim_alternatif_metin](wrapping-cell-text_1.png)</p>|<p>**Aspose.Cells for .NET ile çıktı sarma hücre metni** </p><p>![yapılacaklar:resim_alternatif_metin](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **Cell Metni VSTO Kullanarak Kaydırma**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

    //Access vsto application

    Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

    //Access workbook 

    Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

    //Access worksheet 

    Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

    //Access vsto worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

    //Place some text in cell A1 without wrapping

    Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

    cellA1.Value = "Sample Text Unwrapped";

    //Place some text in cell A5 with wrapping

    Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

    cellA5.Value = "Sample Text Wrapped";

    cellA5.WrapText = true;

    //Save the workbook

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Sarma Cell Metin Kullanılıyor Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

{

    //Create workbook

    Workbook workbook = new Workbook();

    //Access worksheet

    Worksheet worksheet = workbook.Worksheets[0];

    //Place some text in cell A1 without wrapping

    Cell cellA1 = worksheet.Cells["A1"];

    cellA1.PutValue("Some Text Unwrapped");

    //Place some text in cell A5 wrapping

    Cell cellA5 = worksheet.Cells["A5"];

    cellA5.PutValue("Some Text Wrapped");

    Style style = cellA5.GetStyle();

    style.IsTextWrapped = true;

    cellA5.SetStyle(style);

    //Autofit rows

    worksheet.AutoFitRows();

    //Save the workbook

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
