---
title: Cell Metni VSTO ve Aspose.Cells'de kaydırma
type: docs
weight: 250
url: /tr/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---
Biri kaydırılmış metin içeren ve diğeri içermeyen iki hücreli bir çalışma sayfası oluşturmak için:

1.  Çalışma sayfasını ayarlayın:
 1. Bir çalışma kitabı oluşturun.
 1. İlk çalışma sayfasına erişin.
1.  Yazı ekle:
 1. A1 hücresine metin ekleyin.
 1. Kaydırılmış metni A5 hücresine ekleyin.
1. Elektronik tabloyu kaydedin.
 Aşağıdaki kod örnekleri, C# ile VSTO kullanarak bu adımların nasıl gerçekleştirileceğini gösterir. Aynı şeyi Aspose.Cells for .NET kullanarak, tekrar C# kullanarak nasıl yapacağınızı gösteren kod örnekleri hemen ardından gelir.

Kodun çalıştırılması, biri sarmalanmamış metin ve diğeri aşağıdakileri içeren iki hücreli bir elektronik tabloyla sonuçlanır:

## **VSTO Excel kullanarak çıktı alın**

![yapılacaklar:resim_alternatif_metin](picture1.png)

## **Aspose.Cells for .NET kullanılarak çıktı**

![yapılacaklar:resim_alternatif_metin](picture2.png)

## **VSTO**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

## **Örnek Kodu İndir**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [kaynak forge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/indir)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
