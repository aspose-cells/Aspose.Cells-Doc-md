---
title: Dönen Cell Metin
type: docs
weight: 100
url: /tr/net/rotating-cell-text/
---
{{% alert color="primary" %}}

Bazen bir sütun başlığı, aşağıdaki hücrelerdeki verilerden çok daha geniştir. Bu, sayfada gereksiz boşluklara neden olabilir. Bir çözüm, daha az yatay alan kaplayacak şekilde metni dikey olarak döndürmektir. Microsoft Excel'de metni döndürmek kolaydır. Şans eseri, metni programlı olarak döndürmek de mümkündür, böylece geliştiriciler uygulamalarında oluşturdukları elektronik tablolardaki etiketleri döndürebilirler.

 Bu makale, kullanarak hücrelerdeki metnin nasıl döndürüleceğini ele almaktadır.[Aspose.Cells for .NET](/cells/tr/net/rotating-cell-text/) ile aynı şeyi yapmaya kıyasla[VSTO](/cells/tr/net/rotating-cell-text/).

{{% /alert %}}

## **Cells'de Metin Döndürme**

Çalışma sayfasındaki bir hücredeki metni döndürmek için aşağıdaki adımları izleyin:

1. Bir çalışma kitabı oluşturun ve bir çalışma sayfası alın.
1. Örnek metin ekleyin.
1. Metni biçimlendirin: döndürün, arka plan rengi ekleyin.
1. Dosya 'yı kaydet.

 Aşağıdaki kod örnekleri, ilk olarak bu adımların nasıl gerçekleştirileceğini gösterir.[VSTO](/cells/tr/net/rotating-cell-text/) C# veya Visual Basic kullanarak ve ardından[Aspose.Cells](/cells/tr/net/rotating-cell-text/), yine C# veya Visual Basic kullanarak.

Bu makaledeki kod örnekleri, aşağıda gösterilen çıktıyı verir.
**Döndürülmüş metne sahip bir hücre.**

![yapılacaklar:resim_alternatif_Metin](rotating-cell-text_1.png)

### **VSTO ile Metni Döndürme**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2]= "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Aspose.Cells for .NET ile Metin Döndürme**

**C#**

{{< highlight "csharp" >}}

 // Instantiate a new Workbook.
 
 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
