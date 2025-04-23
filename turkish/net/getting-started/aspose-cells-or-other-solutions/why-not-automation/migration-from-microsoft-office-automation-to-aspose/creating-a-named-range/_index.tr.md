---
title: Bir Adlandırılmış Aralık Oluşturma
type: docs
weight: 70
url: /tr/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET, geliştiricilere uygulamaları aracılığıyla Microsoft Excel'de kullanıcıların gerçekleştirebileceği çoğu görevi yapabilme imkanı sağlar. Bu makale, bir adlandırılmış aralığı programlı bir şekilde uygulamanın nasıl yapıldığını açıklar.

Bir adlandırılmış aralık, bir Excel özelliğidir ve bir hücreye veya hücrelerin bir aralığına bir isim atamanızı sağlar. Bu ismi daha sonra formüllerde hücreye (veya aralığa) başvurmak için kullanabilirsiniz. Mantıklı adlandırılmış aralıklar, formülleri anlaşılır hale getirir.

Bir adlandırılmış aralığın kapsamı içinde benzersiz olması gerekir, bu nedenle aynı adı bir çalışma sayfasındaki birkaç aralık için kullanmayın. Betimleyici aralık isimleri, bunun önlenmesine yardımcı olur: örneğin, SiparişAltToplamı, SiparişAltToplamı'ndan daha açıklayıcıdır ve aynı zamanda bir sayfada tekrarlanması daha olası değildir.

{{% /alert %}}

## **Bir Adlandırılmış Aralık Oluşturma**

Bir adlandırılmış aralık oluşturmak için:

1. Çalışma sayfasını kurun:
   1. Bir Uygulama nesnesi örnekleyin.
      (Sadece VSTO.)
   1. Bir çalışma kitabı ekleyin.
   1. İlk sayfayı alın.
1. Adlandırılmış bir aralık oluşturun:
   1. Bir aralık tanımlayın.
   1. Aralığa isim verin.
1. Dosyayı kaydedin.

[VSTO ile](/cells/tr/net/creating-a-named-range/) C# veya Visual Basic kullanarak bu adımları nasıl gerçekleştireceğinizi gösteren kod örnekleri aşağıda verilmiştir. Aşağıdaki kod örnekleri, aynı şeyi [Aspose.Cells for .NET ile](/cells/tr/net/creating-a-named-range/) yine C# veya Visual Basic kullanarak nasıl yapılacağını göstermektedir.
### **VSTO ile Adlandırılmış Aralık Oluşturma**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

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

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET ile Adlandırılmış Aralık Oluşturma**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


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

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
