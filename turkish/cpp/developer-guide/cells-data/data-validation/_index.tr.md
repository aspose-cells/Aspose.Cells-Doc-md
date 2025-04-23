---
title: C++ ile Veri Doğrulama
linktitle: Veri Doğrulama
type: docs
weight: 90
url: /tr/cpp/data-validation/
description: Aspose.Cells for C++ API kullanarak veri doğrulama nasıl eklenir öğrenin.
keywords: Veri Doğrulama Ekle, Doğrulama Değerini Alma, Tamsayı Veri Doğrulama Ekle, Liste Veri Doğrulama Ekle, Tarih Veri Doğrulama Ekle, Zaman Veri Doğrulama Ekle, Metin Uzunluğu Veri Doğrulama Ekle, Varolan Doğrulamaya Hücre Alanı Ekle, Hücredeki doğrulama açılır menü mü, Özel Doğrulama Ekle  
---

{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerini otomatik filtreleme veya doğrulama için iyi özellikler sağlar. Aspose.Cells, Microsoft Excel'in veri doğrulama ve Otomatik Filtre özelliklerini tam olarak destekler. Bu makalede, bu özelliklerin Microsoft Excel'de nasıl kullanılacağı ve Aspose.Cells kullanılarak nasıl kodlanacağı anlatılmaktadır.

{{% /alert %}}

## **Veri Doğrulama Türleri ve Uygulama**

Veri doğrulama, çalışsayadaki girilen verilere ilişkin kuralların ayarlanabilme yeteneğidir. Örneğin, bir sütunun TARIH olarak etiketlendiğinden emin olmak için doğrulamayı kullanın ve yalnızca tarihlerin bulunduğu veya başka bir sütunda yalnızca sayıların bulunduğundan emin olun. Aynı zamanda BELİRLİ bir tarih aralığında yalnızca tarihlerin bulunduğundan emin olabilirsiniz. Veri doğrulama ile çalışarak, çalışsayadaki hücrelere neyin girileceğini kontrol edebilirsiniz.

Microsoft Excel, çeşitli farklı veri doğrulama türlerini desteklemektedir. Her tür, bir hücre veya hücre aralığına hangi veri türünün girileceğini kontrol etmek için kullanılır. Aşağıda, aşağıdaki durumların doğrulanma şeklini gösteren kod örnekleri bulunmaktadır:

- Sayıların tam olduğunu, yani onların ondalık kısmının olmadığını doğrulama.
- Ondalık sayıların doğru yapısı takip edildiğini doğrulama. Kod örneği, bir hücre aralığının iki ondalık alanı olması gerektiğini tanımlar.
- Değerlerin belirli bir değer listesine sınırlı olduğunu doğrulama. Liste doğrulama, bir hücre veya hücre aralığına uygulanabilen ayrı bir değer listesi tanımlar.
- Tarihlerin belirli bir aralıkta olmasını sağlama.
- Zamanın belirli bir aralıkta olup olmadığını kontrol etme.
- Bir metnin belirli bir karakter uzunluğunda olup olmadığını kontrol etme.

### **Microsoft Excel ile Veri Doğrulama**

Microsoft Excel kullanarak doğrulamalar oluşturmak için:

1. Bir çalışsayfada, doğrulama uygulamak istediğiniz hücreleri seçin.
1. **Data** menüsünden **Doğrulama** seçeneğini seçin. Doğrulama iletişim kutusu görüntülenecektir.
1. **Ayarlar** sekmesine tıklayın ve ayarları girin.

### **Aspose.Cells ile Veri Doğrulama**

Veri doğrulaması, çalışma tablolarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulaması ile geliştiriciler, kullanıcılara bir liste seçeneği sunabilir, veri girişlerini belirli bir tür veya boyuta sınırlayabilir, vb.
Aspose.Cells'de, her [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının bir [**GetValidations()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getvalidations/) özelliği vardır. Bu özellik, bir [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) koleksiyonunu temsil eder. Doğrulamayı kurmak için, [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) sınıfının bazı özelliklerini aşağıdaki gibi ayarlayın:

- Tip - [**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) numaralı sayısal değerlerden birini kullanarak belirtilebilen doğrulama tipini temsil eder.
- Operatör - doğrulamada kullanılacak operatörü temsil eder, bu, [**OperatorType**](https://reference.aspose.com/cells/cpp/aspose.cells/operatortype/) numaralandırmasındaki önceden tanımlanmış değerlerden birini kullanarak belirtilebilir.
- Formül1 - Doğrulamanın ilk parçasıyla ilişkilendirilen değeri veya ifadeyi temsil eder.
- Formül2 - Doğrulamanın ikinci parçası ile ilişkilendirilen değeri veya ifadeyi temsil eder.

[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) nesnesinin özellikleri yapılandırıldığında, geliştiriciler oluşturulan doğrulamayı kullanarak doğrulanacak hücre aralığı hakkında bilgileri depolamak için [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) yapısını kullanabilir.

#### **Veri Doğrulama Türleri**

[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) numaralandırmasının aşağıdaki üyeleri bulunmaktadır:

|**Üye Adı**|**Açıklama**|
| :- | :- |
|AnyValue|Herhangi bir türün bir değeri olarak belirtilir.
|WholeNumber|Tamsayılar için doğrulama türünü belirtir.
|Decimal|Ondalık sayılar için doğrulama türünü belirtir.
|List|Açılır kutu listesi için doğrulama türünü belirtir.
|Date|Tarihler için doğrulama türünü belirtir.
|Time|Zamanlar için doğrulama türünü belirtir.
|TextLength|Metnin uzunluğu için doğrulama türünü belirtir.
|Custom|Özel doğrulama türünü belirtir.

##### **Tamsayı Veri Doğrulaması**

Bu tür doğrulama ile kullanıcılar doğrulanmış hücrelere yalnızca belirli bir aralık içinde tam sayılar girebilirler. Aşağıdaki örnek kodlar, WholeNumber doğrulama türünü uygulamanın nasıl yapılacağını göstermektedir. Örnek, Aspose.Cells kullanılarak Microsoft Excel ile yukarıda oluşturduğumuz aynı veri doğrulamasını oluşturur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Create a worksheet and get the first worksheet
    Worksheet ExcelWorkSheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Creating a Validation object
    Validation validation = validations.Get(validations.Add(ca));

    // Setting the validation type to whole number
    validation.SetType(ValidationType::WholeNumber);

    // Setting the operator for validation to Between
    validation.SetOperator(OperatorType::Between);

    // Setting the minimum value for the validation
    validation.SetFormula1(u"10");

    // Setting the maximum value for the validation
    validation.SetFormula2(u"1000");

    // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 1;
    area.StartColumn = 0;
    area.EndColumn = 1;

    // Adding the cell area to Validation
    validation.AddArea(area);

    // Save the workbook
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Validation applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Liste Veri Doğrulaması**

Bu tür doğrulama, kullanıcının bir açılır kutu listesinden değerler girmesine izin verir. Bu, veri içeren bir dizi satırın bir listesini sağlar. Örnekte, listedeki kaynağı tutmak için ikinci bir çalışma tablosu eklenir. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, birinci çalışma tablosundaki A1:A5 hücre aralığıdır.

Burada önemli olan nokta, [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) özelliğini **true** olarak ayarlamanızdır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Add a new worksheet and access it
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet2 = workbook.GetWorksheets().Get(i);

    // Create a range in the second worksheet
    Range range = worksheet2.GetCells().CreateRange(u"E1", u"E4");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"Blue");
    range.Get(1, 0).PutValue(u"Red");
    range.Get(2, 0).PutValue(u"Green");
    range.Get(3, 0).PutValue(u"Yellow");

    // Get the validations collection
    ValidationCollection validations = worksheet1.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Create a new validation to the validations list
    Validation validation = validations.Get(validations.Add(ca));

    // Set the validation type
    validation.SetType(ValidationType::List);

    // Set the operator
    validation.SetOperator(OperatorType::None);

    // Set the in cell drop down
    validation.SetInCellDropDown(true);

    // Set the formula1
    validation.SetFormula1(u"=MyRange");

    // Enable it to show error
    validation.SetShowError(true);

    // Set the alert type severity level
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the error title
    validation.SetErrorTitle(u"Error");

    // Set the error message
    validation.SetErrorMessage(u"Please select a color from the list");

    // Specify the validation area
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 4;
    area.StartColumn = 0;
    area.EndColumn = 0;

    // Add the validation area
    validation.AddArea(area);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Tarih Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan tarih değerlerini doğrulanmış hücrelere girerler. Örnekte, kullanıcının 1970 ila 1999 arasında tarih girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into the A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Date b/w 1/1/1970 and 12/31/1999");

    // Set row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::Date);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"1/1/1970");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"12/31/1999");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Date Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Date");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Date Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Zaman Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan saatleri doğrulanmış hücrelere girebilirler. Örnekte, kullanıcının 09:00 ile 11:30 arasında zaman girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Time b/w 09:00 and 11:30 'o Clock");

    // Set the row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    Validation validation = validations.Get(validations.Add(ca));

    // Set the data validation type
    validation.SetType(ValidationType::Time);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"09:00");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"11:30");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Information);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Time Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Time");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Time Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Metin Uzunluğu Veri Doğrulaması**

Bu tür doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcıya en fazla 5 karakter içeren dize değerlerini girmesi engellenir. Doğrulama alanı B1 hücresidir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter a string not more than 5 chars");

    // Set row height and column width for the cell
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::TextLength);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::LessOrEqual);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"5");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Warning);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Text Length Error");

    // Set the data validation error message
    validation.SetErrorMessage(u" Enter a Valid String");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"TextLength Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Veri Doğrulama Kuralları**

Veri doğrulamaları uygulandığında, doğrulamanın farklı hücrelere farklı değerler atayarak kontrol edilebilir. Doğrulama sonucunu almak için [**Cell.GetValidationValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) kullanılabilir. Aşağıdaki örnek bu özelliği farklı değerlerle göstermektedir. Test için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Hücrede doğrulamanın açılır menü olup olmadığını kontrol et**

Gördüğümüz gibi bir hücre içinde uygulanabilecek birçok doğrulama türü bulunmaktadır. Doğrulamanın açılır menü olup olmadığını kontrol etmek istiyorsanız, [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) özelliği bunu test etmek için kullanılabilir. Aşağıdaki örnek kod, bu özelliğin kullanımını göstermektedir. Test için örnek bir dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleValidation.xlsx](79527947.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleValidation.xlsx";

    // Create workbook
    Workbook book(inputFilePath);

    // Get worksheet
    Worksheet sheet = book.GetWorksheets().Get(u"Sheet1");

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Check validation for cell A2
    Cell a2 = cells.Get(u"A2");
    Validation va2 = a2.GetValidation();
    if (va2.GetInCellDropDown())
    {
        std::cout << "A2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "A2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell B2
    Cell b2 = cells.Get(u"B2");
    Validation vb2 = b2.GetValidation();
    if (vb2.GetInCellDropDown())
    {
        std::cout << "B2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "B2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell C2
    Cell c2 = cells.Get(u"C2");
    Validation vc2 = c2.GetValidation();
    if (vc2.GetInCellDropDown())
    {
        std::cout << "C2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "C2 is NOT a dropdown" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Mevcut Doğrulama Alanına Hücre Alanı Ekle**

Mevcut [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)'e [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) eklemek isteyebileceğiniz durumlar olabilir. Yeni alanı eklerken [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) kullanarak [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) eklerseniz, Aspose.Cells, yeni alanın zaten var olup olmadığını kontrol etmek için tüm mevcut alanları kontrol eder. Dosyada çok sayıda doğrulama varsa, bu performansı olumsuz etkiler. Bunu aşmak için API, [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) yöntemini sağlar. *checkIntersection* parametresi, verilen alanın mevcut doğrulama alanlarıyla kesişimini kontrol edip etmeyeceğini belirtir. **false** ayarlamak diğer alanların kontrolünü devre dışı bırakır. *checkEdge* parametresi, uygulanan alanların kontrol edilip edilmeyeceğini belirtir. Yeni alanın sol üst alan olması durumunda iç ayarlar yeniden oluşturulur. Yeni alanın sol üst alan olmadığından eminseniz, bu parametreyi **false** olarak ayarlayabilirsiniz.

Aşağıdaki kod örneği, mevcut [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)'e yeni [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) eklemek için [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) yönteminin kullanımını göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ValidationsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    Validation validation = worksheet.GetValidations().Get(0);

    // Create cell area
    CellArea cellArea = CellArea::CreateCellArea(u"D5", u"E7");

    // Adding the cell area to Validation
    validation.AddArea(cellArea, false, false);

    // Save the output workbook
    workbook.Save(outDir + u"ValidationsSample_out.xlsx");

    std::cout << "Validation added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Kaynak ve çıktı excel dosyaları referans için ekte sunulmuştur.

[Kaynak Dosyası](96928093.xlsx)

[Çıkış Dosyası](96928220.xlsx)

## **Gelişmiş Konular**
- [ODS Dosyalarında Hücre Doğrulamasını Al](/cells/tr/cpp/get-cell-validation-in-ods-files/)
- [Bir Hücreye Uygulanan Doğrulamayı Al](/cells/tr/cpp/get-validation-applied-on-a-cell/)
- [Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulama](/cells/tr/cpp/verify-that-cell-value-satisfies-data-validation-rules/)
