---
title: VSTO ve Aspose.Cells'de Adlandırılmış Aralık Oluşturma
type: docs
weight: 90
url: /tr/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
Adlandırılmış bir aralık oluşturmak için:

1.  Çalışma sayfasını ayarlayın:
 1. Bir Uygulama nesnesinin örneğini oluşturun. (Yalnızca VSTO.)
 1. Bir Çalışma Kitabı ekleyin.
 1. İlk sayfayı alın.
1.  Adlandırılmış bir aralık oluşturun:
 1. Bir aralık tanımlayın.
 1. Aralığı adlandırın.
 1. Dosyayı kaydedin.

Aşağıdaki kod örnekleri, C# ile VSTO kullanarak bu adımların nasıl gerçekleştirileceğini gösterir. Aşağıdaki kod örnekleri, Aspose.Cells for .NET kullanılarak, yine C# ile aynı şeyin nasıl yapılacağını gösterir.
## **VSTO**
{{< highlight "csharp" >}}

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
{{< highlight "csharp" >}}

 //Çalışma Kitabı nesnesinin somutlaştırılması

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı();

//Excel dosyasındaki ilk çalışma sayfasına erişim

Çalışma sayfası çalışma sayfası = çalışma kitabı.Çalışma Sayfaları[0];

//Adlandırılmış bir aralık oluşturma

Aralık aralığı = worksheet.Cells.CreateRange("A1", "B4");

//Adlandırılmış aralığın adını ayarlıyoruz

range.Name = "Test_Aralığı";

 için (int satır = 0; satır< range.RowCount; row++)

{

	for (int column = 0; column < range.ColumnCount; column++)

	{

		range[row, column].PutValue("Test");

	}

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [kaynak forge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/indir)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip)
