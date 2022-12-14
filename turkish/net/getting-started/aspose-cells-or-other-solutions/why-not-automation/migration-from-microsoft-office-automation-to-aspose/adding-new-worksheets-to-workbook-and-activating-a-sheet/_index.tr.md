---
title: Çalışma Kitabına Yeni Çalışma Sayfaları Ekleme ve Bir Sayfayı Etkinleştirme
type: docs
weight: 10
url: /tr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

Bir şablon dosyasıyla çalışırken, bazen veri toplamak için çalışma kitabına fazladan çalışma sayfaları eklemeniz gerekebilir. Yeni hücreler, her çalışma sayfasında belirtilen konum ve konumlardaki verilerle doldurulacaktır.

Benzer şekilde, belirli bir çalışma sayfasının etkin olması ve dosya Microsoft Excel'de açıldığında ilk olarak görüntülenmesi gerekebilir. "Etkin sayfa", bir çalışma kitabında üzerinde çalıştığınız sayfadır. Etkin sayfanın sekmesindeki ad varsayılan olarak kalındır.

 Çalışma sayfaları eklemek ve hangi sayfanın etkin olduğunu ayarlamak, geliştiricilerin nasıl gerçekleştireceklerini bilmesi gereken yaygın ve basit görevlerdir. Bu yazıda, bu görevleri kullanarak gerçekleştiriyoruz.[VSTO](/cells/tr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) ve[Aspose.Cells for .NET](/cells/tr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Çalışma Sayfaları Ekleme ve Bir Sayfayı Etkinleştirme**
Bu geçiş ipucunun amaçları doğrultusunda:

1. Mevcut bir Microsoft Excel dosyasına yeni çalışma sayfaları ekleyin.
1. Verileri her yeni çalışma sayfasının hücrelerine doldurun.
1. Çalışma kitabında bir sayfayı etkinleştirin.
1. Microsoft Excel dosyası olarak kaydedin.

Aşağıda, bu görevlerin nasıl gerçekleştirileceğini gösteren VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) için paralel kod parçacıkları bulunmaktadır.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

Microsoft.VisualStudio.Tools.Applications.Runtime kullanarak;

Excel kullanarak = Microsoft.Office.Interop.Excel;

Office = Microsoft.Office.Core kullanılarak;

System.Reflection kullanarak;

.......

//Uygulama nesnesini örneklendirin.

Excel.Application excelApp = yeni Excel.ApplicationClass();

//Şablonun excel dosya yolunu belirtin.

string myPath = @"d:\test\My_Book1.xls";

//excel dosyasını açın.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Eksik.Değer, Eksik.Değer,

Eksik.Değer, Eksik.Değer,

Eksik.Değer, Eksik.Değer,

Eksik.Değer, Eksik.Değer,

Eksik.Değer, Eksik.Değer,

Eksik.Değer, Eksik.Değer);

//Bir Çalışma Sayfası nesnesi tanımlayın.

Excel.Çalışma sayfası yeniÇalışma sayfası;

//Çalışma kitabına 5 yeni çalışma sayfası ekleyin ve bazı verileri doldurun

//hücrelere.

 için (int ben = 1; ben< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

Aspose.Cells kullanarak;

.......

//Bir lisans örneği oluşturun ve lisans dosyasını ayarlayın

//yolu boyunca

Aspose.Cells.Lisans lisansı = yeni Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

//Şablonun excel dosya yolunu belirtin.

string myPath =@"d:\test\My_Book1.xls";

//Yeni bir Çalışma Kitabı oluşturun.

//excel dosyasını açın.

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı(myPath);

//Bir Çalışma Sayfası nesnesi tanımlayın.

Çalışma sayfası yeniÇalışma sayfası;

//Çalışma kitabına 5 yeni çalışma sayfası ekleyin ve bazı verileri doldurun

//hücrelere.

 için (int ben = 0; ben< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
