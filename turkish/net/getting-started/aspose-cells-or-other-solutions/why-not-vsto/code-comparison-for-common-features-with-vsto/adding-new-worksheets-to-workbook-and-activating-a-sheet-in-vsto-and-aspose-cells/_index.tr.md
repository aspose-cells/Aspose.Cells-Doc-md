---
title: Çalışma Kitabına Yeni Çalışma Sayfaları Ekleme ve VSTO ve Aspose.Cells'de Bir Sayfayı Etkinleştirme
type: docs
weight: 30
url: /tr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Geçiş ipucu:**
1. Mevcut bir Microsoft Excel dosyasına yeni çalışma sayfaları ekleyin.
1. Verileri her yeni çalışma sayfasının hücrelerine doldurun.
1. Çalışma kitabında bir sayfayı etkinleştirin.
1. Microsoft Excel dosyası olarak kaydedin.

Aşağıda, bu görevlerin nasıl gerçekleştirileceğini gösteren VSTO (C#) ve Aspose.Cells for .NET (C#) için paralel kod parçacıkları bulunmaktadır.

**VSTO**

{{< highlight "csharp" >}}

//uygulama nesnesini başlat

Excel.Uygulama excelApp = Uygulama;

//Şablonun excel dosya yolunu belirtin.

string myPath = "Kitap1.xls";

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

 için (int ben = 1; ben< 6; i++){

                //Add a worksheet to the workbook.

                newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,

                Missing.Value, Missing.Value);

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + i.ToString();

                //Get the Cells collection.

                Excel.Range cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells.set_Item(i, i, "New_Sheet" + i.ToString());

            }

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**Aspose.Cells**

{{< highlight "csharp" >}}

 //Bir lisans örneği oluşturun ve lisans dosyasını ayarlayın

//yolu boyunca

Aspose.Cells.Lisans lisansı = yeni Aspose.Cells.License();

license.SetLicense("Aspose.Total.lic");

//Şablonun excel dosya yolunu belirtin.

string myPath = "Kitap1.xls";

//Yeni bir Çalışma Kitabı oluşturun.

//excel dosyasını açın.

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı(myPath);

//Bir Çalışma Sayfası nesnesi tanımlayın.

Çalışma sayfası yeniÇalışma sayfası;

//Çalışma kitabına 5 yeni çalışma sayfası ekleyin ve bazı verileri doldurun

//hücrelere.

 için (int ben = 0; ben< 5; i++){

                //Add a worksheet to the workbook.

                newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

                //Get the Cells collection.

                Cells cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());

            }

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [kaynak forge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/indir)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip)
