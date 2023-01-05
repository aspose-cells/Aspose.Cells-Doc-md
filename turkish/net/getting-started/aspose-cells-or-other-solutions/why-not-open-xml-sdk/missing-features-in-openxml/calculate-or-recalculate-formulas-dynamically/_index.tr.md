---
title: Formülleri dinamik olarak hesaplayın veya yeniden hesaplayın
type: docs
weight: 10
url: /tr/net/calculate-or-recalculate-formulas-dynamically/
---
**formül hesaplama** motor gömülü**Aspose.Cells**. Yalnızca tasarımcı dosyasından içe aktarılan formülü yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarını hesaplamayı da destekler.
## **Formül Ekleme ve Sonuçları Hesaplama**
Aspose.Cells, Microsoft Excel'in parçası olan formüllerin veya işlevlerin çoğunu destekler. Geliştiriciler, bu formülleri API veya Tasarımcı Elektronik Tablolarını kullanarak kullanabilir. Aspose.Excel, çok sayıda Matematiksel, Dize, Boolean, Tarih/Saat, İstatistiksel, Veritabanı, Arama ve Referans formüllerini destekler.

Bir hücreye formül eklemek için Cell sınıfının Formula özelliğini kullanın. Bir hücreye formül uygularken, Microsoft Excel'de formül oluştururken yaptığınız gibi dizeye her zaman eşittir işaretiyle (=) başlayın. İşlev parametrelerini ayırmak için virgül (,) kullanın.

 Formüllerin sonuçlarını hesaplamak için Excel sınıfının bir Excel dosyasına katıştırılmış tüm formülleri işleyen CalculateFormula yöntemini çağırın. Okumak[url:CalculateFormula yöntemi tarafından desteklenen işlevlerin listesi](/cells/tr/net/supported-formula-functions/).

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **Formülleri Yalnızca Bir Kez Hesaplama**
Kullanıcı, çalışma kitabı şablonu içindeki formüllerin değerlerini hesaplamak için Workbook.CalculateFormula() öğesini çağırdığında, Aspose.Cells bir hesaplama zinciri oluşturur. Formüller ikinci, üçüncü kez vb. hesaplandığında performansı artırır.
Bununla birlikte, kullanıcı şablonu çok sayıda farklı formül içeriyorsa, ilk kez formül hesaplaması çok fazla CPU işlem süresi ve bellek tüketebilir.

Aspose.Cells, dosyanızın formüllerini yalnızca bir kez hesaplamak istediğiniz senaryolarda yararlı olan hesaplama zinciri oluşturmayı kapatmanıza olanak tanır.

 Aspose.Cells ile formül hesaplamalarının performansını artırmak istiyor ve formül hesaplama zinciri oluşturmak istemiyorsanız, lütfen**FormulaSettings.EnableCalculationChain** olarak**YANLIŞ** . Varsayılan olarak, şu şekilde ayarlanmıştır:**doğru**.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **Formülün Doğrudan Hesaplanması**
Formül hesaplama motoru Aspose.Cells içine gömülüdür. Ayrıca, tasarımcı dosyasından içe aktarılan formülün yeniden hesaplanmasının yanı sıra, Aspose.Cells, formül sonuçlarının doğrudan hesaplanmasını da destekler.
Bazen formül sonuçlarını bir çalışma sayfasına eklemeden doğrudan hesaplamanız gerekir. Formülde kullanılan hücrelerin değerleri bir çalışma sayfasında zaten var ve ihtiyacınız olan tek şey, formülü bir çalışma sayfasına eklemeden bazı Ms-Excel formüllerine dayalı olarak bu değerlerin sonucunu bulmak.

 Aspose.Cells Formül Hesaplama Motorunu kullanabilirsiniz API yani**worksheet.Calculate(dize formülü)**bu tür formüllerin sonuçlarını çalışma sayfasına fiilen eklemeden hesaplamak için.

{{< highlight "csharp" >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
