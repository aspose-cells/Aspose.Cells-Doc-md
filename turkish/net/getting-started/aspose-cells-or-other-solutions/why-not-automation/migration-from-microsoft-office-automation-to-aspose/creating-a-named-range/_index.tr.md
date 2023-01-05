---
title: Adlandırılmış Aralık Oluşturma
type: docs
weight: 70
url: /tr/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET, geliştiricilerin, kullanıcıların uygulamaları aracılığıyla Microsoft Excel'de gerçekleştirebilecekleri görevlerin çoğunu gerçekleştirmesine olanak tanır. Bu makalede, adlandırılmış bir aralığın programlı olarak nasıl uygulanacağı açıklanmaktadır.

Adlandırılmış aralık, bir Excel elektronik tablosunda bir hücreye veya bir hücre aralığına ad atamanıza izin veren bir Excel özelliğidir. Daha sonra hücreye (veya aralığa) başvurmak için adı formüllerde kullanabilirsiniz. Mantıklı bir şekilde adlandırılmış aralıklar, formüllerin anlaşılmasını kolaylaştırır.

Adlandırılmış bir aralığın kapsamı içinde benzersiz olması gerekir, bu nedenle bir çalışma sayfasındaki birkaç aralık için aynı adı kullanmayın. Açıklayıcı aralık adları, bundan kaçınmaya yardımcı olur: örneğin, OrderSubTotal, SubTotal'dan daha açıklayıcıdır ve aynı zamanda bir sayfada yinelenme olasılığı daha düşüktür.

{{% /alert %}}

## **Adlandırılmış Aralık Oluşturma**

Adlandırılmış bir aralık oluşturmak için:

1. Çalışma sayfasını ayarlayın:
 1. Bir Uygulama nesnesi oluşturun.
 (Yalnızca VSTO.)
 1. Bir Çalışma Kitabı ekleyin.
 1. İlk sayfayı alın.
1. Adlandırılmış bir aralık oluşturun:
 1. Bir aralık tanımlayın.
 1. Aralığı adlandırın.
1. Dosya 'yı kaydet.

 Aşağıdaki kod örnekleri, kullanarak bu adımların nasıl gerçekleştirileceğini gösterir.[VSTO](/cells/tr/net/creating-a-named-range/) C# veya Visual Basic ile. Aşağıdaki kod örnekleri, kullanarak aynı şeyi nasıl yapacağınızı gösterir.[Aspose.Cells for .NET](/cells/tr/net/creating-a-named-range/), yine C# veya Visual Basic ile.
### **VSTO ile Adlandırılmış Aralık Oluşturma**

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

 .......

Aspose.Cells kullanarak;

.......


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

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
