---
title: Validación de datos con C++
linktitle: Validación de datos
type: docs
weight: 90
url: /es/cpp/data-validation/
description: Aprende cómo agregar validación de datos a través de la API Aspose.Cells for C++.
keywords: Agregar validación de datos, obtener valor de validación, agregar validación de número entero, agregar validación de lista, agregar validación de fecha, agregar validación de hora, agregar validación de longitud de texto, agregar CellArea a la validación existente, verificar si la validación en la celda es un desplegable, agregar validación personalizada  
---

{{% alert color="primary" %}}

Microsoft Excel ofrece algunas funciones útiles para autofiltar o validar datos en hojas de cálculo. Aspose.Cells soporta completamente las funciones de validación de datos y AutoFilter de Microsoft Excel. Este artículo explica cómo usar esas funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}}

## **Tipos de Validación de Datos y Ejecución**

La validación de datos es la capacidad de establecer reglas relacionadas con los datos ingresados en una hoja de cálculo. Por ejemplo, use la validación para asegurarse de que una columna etiquetada como FECHA contenga solo fechas, o que otra columna contenga solo números. Incluso puede asegurarse de que una columna etiquetada como FECHA contenga solo fechas dentro de un cierto rango. Con la validación de datos, puede controlar lo que se ingresa en las celdas de la hoja de cálculo.

Microsoft Excel admite varios tipos diferentes de validación de datos. Cada tipo se usa para controlar qué tipo de datos se ingresa en una celda o rango de celdas. A continuación, se muestran fragmentos de código que ilustran cómo validar que:

- Los números son enteros, es decir, que no tienen parte decimal.
- Los números decimales siguen la estructura correcta. El ejemplo de código define que un rango de celdas debe tener dos espacios decimales.
- Los valores están restringidos a una lista de valores. La validación de lista define una lista separada de valores que se pueden aplicar a una celda o rango de celdas.
- Las fechas se encuentran dentro de un rango específico.
- Una hora está dentro de un rango específico.
- Un texto está dentro de una longitud de caracteres dada.

### **Validación de datos con Microsoft Excel**

Para crear validaciones usando Microsoft Excel:

1. En una hoja de cálculo, seleccione las celdas a las que desea aplicar la validación.
1. Desde el menú **Datos**, seleccione **Validación**. Se mostrará el diálogo de validación.
1. Haga clic en la pestaña **Configuración** e ingrese la configuración.

### **Validación de datos con Aspose.Cells**

La validación de datos es una función poderosa para validar la información ingresada en las hojas de cálculo. Con la validación de datos, los desarrolladores pueden proporcionar a los usuarios una lista de opciones, restringir las entradas de datos a un tipo o tamaño específico, etc.
En Aspose.Cells, cada clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tiene una propiedad [**GetValidations()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getvalidations/) que representa una colección de objetos [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/). Para configurar la validación, configura algunas de las propiedades de la clase [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) de la siguiente manera:

- Tipo – representa el tipo de validación, que puede especificarse utilizando uno de los valores predefinidos en la enumeración [**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/).
- Operator: representa el operador que se utilizará en la validación, que puede ser especificado utilizando uno de los valores predefinidos en la enumeración [**OperatorType**](https://reference.aspose.com/cells/cpp/aspose.cells/operatortype/).
- Fórmula1 – representa el valor o expresión asociado con la primera parte de la validación de datos.
- Fórmula2 – representa el valor o expresión asociado con la segunda parte de la validación de datos.

Cuando las propiedades del objeto [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) hayan sido configuradas, los desarrolladores pueden utilizar la estructura [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) para almacenar información sobre el rango de celdas que se validarán utilizando la validación creada.

#### **Tipos de validación de datos**

La enumeración [**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) tiene los siguientes miembros:

|**Nombre del miembro**|**Descripción**|
| :- | :- |
|AnyValue|Denota un valor de cualquier tipo.|
|WholeNumber|Denota tipo de validación para números enteros.|
|Decimal|Denota tipo de validación para números decimales.|
|List|Denota tipo de validación para lista desplegable.|
|Date|Denota tipo de validación para fechas.|
|Time|Denota tipo de validación para tiempo.|
|TextLength|Denota tipo de validación para longitud del texto.|
|Custom|Denota tipo de validación personalizado.|

##### **Validación de datos de números enteros**

Con este tipo de validación, los usuarios solo pueden ingresar números enteros dentro de un rango especificado en las celdas validadas. Los ejemplos de código que siguen muestran cómo implementar el tipo de validación de números enteros. El ejemplo crea la misma validación de datos utilizando Aspose.Cells que creamos utilizando Microsoft Excel anteriormente.

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

##### **Validación de datos de lista**

Este tipo de validación permite al usuario ingresar valores de una lista desplegable. Proporciona una lista: una serie de filas que contienen datos. En el ejemplo, se agrega una segunda hoja de cálculo para contener la fuente de la lista. Los usuarios solo pueden seleccionar valores de la lista. El área de validación es el rango de celdas A1:A5 en la primera hoja de cálculo.

Es importante aquí que establezca la propiedad [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) como **true**.

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

##### **Validación de datos de fechas**

Con este tipo de validación, los usuarios ingresan valores de fecha dentro de un rango especificado, o que cumplen criterios específicos, en las celdas validadas. En el ejemplo, el usuario está restringido a ingresar fechas entre 1970 y 1999. Aquí, el área de validación es la celda B1.

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

##### **Validación de datos de hora**

Con este tipo de validación, los usuarios pueden ingresar horas dentro de un rango especificado, o que cumplan con ciertos criterios, en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar horas entre las 09:00 y las 11:30 AM. Aquí, el área de validación es la celda B1.

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

##### **Validación de Datos de Longitud de Texto**

Con este tipo de validación, los usuarios pueden ingresar valores de texto de una longitud específica en las celdas validadas. En el ejemplo, al usuario se le restringe ingresar valores de cadena con no más de 5 caracteres. El área de validación es la celda B1.

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

### **Reglas de Validación de Datos**

Cuando se implementan validaciones de datos, entonces la validación se puede verificar asignando diferentes valores en las celdas. [**Cell.GetValidationValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) se puede utilizar para obtener el resultado de la validación. El siguiente ejemplo demuestra esta característica con diferentes valores. El archivo de ejemplo se puede descargar desde el siguiente enlace para fines de prueba:

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

## **Verificar si la validación en la celda es de lista desplegable**

Como hemos visto, existen muchos tipos de validaciones que se pueden implementar dentro de una celda. Si quieres verificar si la validación es de lista desplegable o no, se puede utilizar la propiedad [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) para probarlo. El siguiente código de ejemplo muestra el uso de esta propiedad. Se puede descargar un archivo de ejemplo para pruebas desde el siguiente enlace:

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

## **Agregar CellArea a la validación existente**

Puede haber casos en los que desees agregar [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) a la [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) existente. Cuando agregas [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) usando [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/), Aspose.Cells verifica todas las áreas existentes para ver si la nueva área ya está incluida. Si el archivo tiene un gran número de validaciones, esto afecta el rendimiento. Para superar esto, la API proporciona el método [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/). El parámetro *checkIntersection* indica si se debe verificar la intersección de una determinada área con áreas de validación existentes. Establecerlo en **falso** deshabilitará la verificación de otras áreas. El parámetro *checkEdge* indica si se deben verificar las áreas aplicadas. Si la nueva área se convierte en el área superior izquierda, se reconstruyen las configuraciones internas. Si estás seguro de que la nueva área no es el área superior izquierda, puedes establecer este parámetro en **falso**.

El siguiente fragmento de código muestra el uso del método [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) para agregar nuevas [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) a las [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) existentes.

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

Se adjuntan los archivos de Excel de origen y salida para referencia.

[Archivo de origen](96928093.xlsx)

[Archivo de Salida](96928220.xlsx)

## **Temas avanzados**
- [Obtener validación de celda en archivos ODS](/cells/es/cpp/get-cell-validation-in-ods-files/)
- [Obtener Validación Aplicada en una Celda](/cells/es/cpp/get-validation-applied-on-a-cell/)
- [Verificar que el Valor de la Celda Satisface las Reglas de Validación de Datos](/cells/es/cpp/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="cpp" >}}
