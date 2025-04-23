---
title: Configuraciones avanzadas de protección desde Excel XP con C++
linktitle: Configuraciones de protección avanzada desde Excel XP
type: docs
weight: 30
url: /es/cpp/advanced-protection-settings-since-excel-xp/
description: Aprende cómo aplicar configuraciones avanzadas de protección en archivos de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Desde el lanzamiento de Excel 2002 o XP, Microsoft ha añadido muchas configuraciones avanzadas de protección.

{{% /alert %}}

## **Introducción**

Estas configuraciones de protección restringen o permiten a los usuarios:

- Eliminar filas o columnas.
- Editar contenidos, objetos o escenarios.
- Formatear celdas, filas o columnas.
- Insertar filas, columnas o hipervínculos.
- Seleccionar celdas bloqueadas o desbloqueadas.
- Utilizar tablas dinámicas y mucho más.

Aspose.Cells admite todas las configuraciones de protección avanzada ofrecidas por Excel XP o versiones posteriores.

### **Configuraciones de protección avanzada utilizando Excel XP y versiones posteriores**

Para ver las configuraciones de protección disponibles en Excel XP:

1. Desde el menú **Herramientas**, selecciona **Protección** seguido de **Proteger hoja**. Se mostrará un cuadro de diálogo.

Para ver la configuración de protección disponible en Excel 2016:

1. Desde el menú **Archivo**, selecciona **Proteger libro** seguido de **Proteger hoja actual**.
1. Selecciona **Proteger hoja** en el menú **Revisar**.

Los pasos mencionados anteriormente mostrarán un cuadro de diálogo donde puede permitir o restringir funciones de la hoja de trabajo o aplicar una contraseña a la hoja.

### **Configuraciones de protección avanzada utilizando Aspose.Cells**

Aspose.Cells admite todas las configuraciones de protección avanzada.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona la propiedad [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) que se utiliza para aplicar estas configuraciones de protección avanzada. La propiedad [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) es de hecho un objeto de la clase [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra un pequeño ejemplo de aplicación. Abre un archivo de Excel y utiliza la mayoría de los ajustes de protección avanzados admitidos por Excel XP y versiones posteriores.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Por favor, no llame al método [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) al usar la propiedad [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/). Además, guarda el archivo en formato Excel97To2003 o Xlsx porque las configuraciones avanzadas de protección solo son compatibles con Excel XP y versiones posteriores.

{{% /alert %}}

### **Problema de bloqueo de celdas**

Si desea restringir a los usuarios de editar celdas, las celdas deben estar bloqueadas antes de aplicar cualquier configuración de protección. De lo contrario, las celdas pueden editarse incluso si la hoja de cálculo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

|**Cuadro de diálogo para bloquear celdas en Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

También es posible bloquear celdas usando la API Aspose.Cells. Cada celda puede obtener un formato [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) que contiene una propiedad Booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Establezca la propiedad [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) en **true** o **false** para bloquear o desbloquear la celda.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
