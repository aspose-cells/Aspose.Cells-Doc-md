---
title: Formülleri Dinamik Olarak Hesaplayın veya Yeniden Hesaplayın
type: docs
weight: 10
url: /tr/net/calculate-or-recalculate-formulas-dynamically/
---

**Formula Hesaplama** motoru **Aspose.Cells** içine gömülüdür. Sadece tasarımcı dosyasından alınan formülleri yeniden hesaplamakla kalmaz, aynı zamanda çalışma zamanında eklenen formüllerin sonuçlarını hesaplama desteği de sunar.
## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**
Aspose.Cells, Microsoft Excel'in büyük bir kısmını oluşturan formülleri veya işlevleri destekler. Geliştiriciler, bu formülleri API veya Tasarımcı Elektronik Tablolar kullanarak kullanabilirler. Aspose.Excel, Matematik, Dize, Boolean, Tarih/Saat, İstatistiksel, Veritabanı, Arama ve Referans formüllerinin geniş bir setini destekler.

Hücre sınıfının Formula özelliğini kullanarak bir hücreye formül eklemek için kullanın. Bir hücreye formül uygularken, her zaman bir Microsoft Excel formülü oluştururken olduğu gibi eşittir işareti (=) ile başlayın. Bir virgül (,) işlev parametrelerini ayırmak için kullanın.

Formüllerin sonuçlarını hesaplamak için Excel sınıfının CalculateFormula yöntemini çağırın, bu işlemle bir Excel dosyasına gömülü tüm formülleri işler. [url:CalculateFormula yöntemi tarafından desteklenen fonksiyonların listesi](/cells/tr/net/supported-formula-functions/)ni okuyun.

{{< highlight csharp >}}

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
## **Formülleri Yalnızca Bir Kez Hesaplayın**
Kullanıcı, Workbook.CalculateFormula() yöntemini çağırdığında, Aspose.Cells, bir hesaplama zinciri oluşturur. Formüller ikinci veya üçüncü kez hesaplandığında performansı artırır.
Ancak, kullanıcı şablonu çok çeşitli formüller içeriyorsa, formül hesaplamanın ilk kez CPU işlem süresi ve bellek kullanımı çok fazla olabilir.

Aspose.Cells, sadece dosyanızın formüllerini bir kez hesaplamak istediğiniz senaryolarda hesaplama zinciri oluşturmayı devre dışı bırakmanıza olanak tanır.

Aspose.Cells formül hesaplamalarının performansını iyileştirmeyi ve formül hesaplama zinciri oluşturmak istemiyorsanız, lütfen **FormulaSettings.EnableCalculationChain** özelliğini **false** olarak ayarlayın. Varsayılan olarak bu **true** olarak ayarlıdır.

{{< highlight csharp >}}

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
Aspose.Cells'e gömülü formül hesaplama motoru. Tasarımcı dosyasından alınan formülü yeniden hesaplamakla kalmaz, aynı zamanda formül sonuçlarını doğrudan hesaplama desteği de sunar.
Bazı durumlarda, hücrelerin değerleri zaten bir elektronik tabloda mevcut olup bir Ms-Excel formülüne dayalı olarak bu değerlerin sonucunu bulmak istersiniz, fakat formülü elektronik tabloya eklemek zorunda değilsiniz. Bu tür formüllerin sonuçlarını hesaplamak için Aspose.Cells Formula Calculation Engine API'sini yani  **worksheet.Calculate(string formula)** kullanabilirsiniz.

Aspose.Cells Formül Hesaplama Motoru API'sini, yani **worksheet.Calculate(string formül)**'ü bu tür formüllerin sonuçlarını çalışsayfaya gerçekten eklemeksizin hesaplamak için kullanabilirsiniz.

{{< highlight csharp >}}

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
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
