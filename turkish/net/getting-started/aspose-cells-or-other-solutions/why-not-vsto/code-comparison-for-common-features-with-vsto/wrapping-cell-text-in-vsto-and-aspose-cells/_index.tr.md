---
title: VSTO ve Aspose.Cells te Hücre Metnini Kaydırma
type: docs
weight: 250
url: /tr/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---

İki hücreli bir çalışma sayfası oluşturmak için, biri kaydırılmış metinle diğeri kaydırılmamış metinle:

1. Çalışma sayfasını kurun: 
   1. Bir çalışma kitabı oluşturma.
   1. İlk çalışma sayfasına erişin.
1. Metin ekleyin: 
   1. A1 hücresine metin ekleyin.
   1. A5 hücresine kaydırılmış metin ekleyin.
1. Elektronik tabloyu kaydedin.
   Aşağıdaki kod örnekleri, VSTO kullanarak bu adımları C# ile nasıl gerçekleştireceğimizi göstermektedir. Aynı şeyi yapmak için Aspose.Cells for .NET'yi kullanan kod örnekleri, yine C# kullanılarak hemen aşağıda bulunmaktadır.

Kodun çalıştırılması sonucunda, kapsamı genişletilmemiş metin içeren bir hücre ve şunları içeren bir elektronik tablo oluşur:

## **VSTO Excel Kullanarak Çıktı**

![todo:image_alt_text](picture1.png)

## **Aspose.Cells for .NET Kullanarak Çıktı**

![todo:image_alt_text](picture2.png)

## **VSTO**

{{< highlight csharp >}}

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

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 private static void WrappingCellText()

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

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Örnek Kod İndir**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
