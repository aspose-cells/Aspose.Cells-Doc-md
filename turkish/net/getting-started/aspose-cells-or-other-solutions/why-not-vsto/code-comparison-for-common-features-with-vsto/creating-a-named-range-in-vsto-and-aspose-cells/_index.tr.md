---
title: VSTO ve Aspose.Cells te Adlandırılmış Aralık Oluşturma
type: docs
weight: 90
url: /tr/net/creating-a-named-range-in-vsto-and-aspose-cells/
---

Bir adlandırılmış aralık oluşturmak için:

1. Çalışma sayfasını kurun: 
   1. Bir Uygulama nesnesi örneği oluşturun.(Sadece VSTO.)
   1. Bir çalışma kitabı ekleyin.
   1. İlk sayfayı alın.
1. Adlandırılmış bir aralık oluşturun: 
   1. Bir aralık tanımlayın.
   1. Aralığa isim verin.
   1. Dosyayı kaydedin.

Aşağıdaki kod örnekleri, bu adımları VSTO kullanarak C# ile gerçekleştirmenin nasıl yapıldığını göstermektedir. Aynı işlemi Aspose.Cells for .NET kullanarak, yine C# ile nasıl yapıldığını gösteren kod örnekleri aşağıdadır
## **VSTO**
{{< highlight csharp >}}

 //Create Excel Object

Excel.Application xl = Application;

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

	cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

	for (int column = 0; column < range.ColumnCount; column++)

	{

		range[row, column].PutValue("Test");

	}

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
