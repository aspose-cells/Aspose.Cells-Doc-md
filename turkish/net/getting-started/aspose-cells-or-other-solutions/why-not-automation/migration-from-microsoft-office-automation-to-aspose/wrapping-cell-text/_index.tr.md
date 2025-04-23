---
title: Hücre Metin Sarma
type: docs
weight: 130
url: /tr/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

Metni sarmak, okumayı kolaylaştırır: sarma metin içeren bir hücre, metni diğer hücrelerin üstüne görüntülemeden sığacak şekilde genişler.

Aspose.Cells for .NET ile, geliştiriciler Microsoft Excel'de kullanıcıların yaptığı çoğu görevi gerçekleştirebilir, bu da hücrelerde metin sarma işlemini içerir. Bu makale, bunu nasıl yapılacağını açıklar ve VSTO ve Aspose.Cells kullanarak karşılaştırır. Aspose.Cells, verimli kodlama için optimize edilmiştir ve Microsoft Automation olmadan çalışır.

{{% /alert %}}

## **Hücre Metin Sarma**

İki hücreli bir çalışma sayfası oluşturmak için, biri kaydırılmış metinle diğeri kaydırılmamış metinle:

1. Çalışma sayfasını kurun:
   1. Bir çalışma kitabı oluşturma.
   1. İlk çalışma sayfasına erişin.
1. Metin ekleyin:
   1. A1 hücresine metin ekleyin.
   1. A5 hücresine kaydırılmış metin ekleyin.
1. Elektronik tabloyu kaydedin.

Aşağıdaki kod örnekleri, bu adımları C# veya Visual Basic kullanarak [VSTO](/cells/tr/net/wrapping-cell-text/) ile nasıl gerçekleştireceğinizi gösterir. Aynı şeyi [Aspose.Cells for .NET](/cells/tr/net/wrapping-cell-text/) kullanarak yine C# veya Visual Basic kullanarak yapan kod örnekleri hemen arkasından gelir.

Kodun çalıştırılması sonucunda, kapsamı genişletilmemiş metin içeren bir hücre ve şunları içeren bir elektronik tablo oluşur:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **VSTO Kullanarak Hücre Metin Sarma**

**C#**

{{< highlight csharp >}}

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

### **Aspose.Cells for .NET Kullanarak Hücre Metin Sarma**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
