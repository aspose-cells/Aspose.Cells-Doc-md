---
title: Configuración de números con C++
linktitle: Configuraciones numéricas
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo que admite muchas configuraciones diferentes de números en las celdas. Este artículo presentará cómo usar la biblioteca Aspose.Cells para gestionar las configuraciones numéricas de las celdas, permitiendo a los usuarios ajustar el formato de números en la hoja según sea necesario.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo electrónica, configuración de números en celdas, formato, gestión, formatos de números y fechas
type: docs
weight: 10
url: /es/cpp/cells-number-settings/
---

## **Cómo establecer formatos de visualización de números y fechas**

Una característica muy fuerte de Microsoft Excel es que permite a los usuarios establecer los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos pueden utilizarse para representar diferentes valores, incluidos decimales, moneda, porcentaje, fracción o valores contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. De manera similar, hay muchos formatos en los que se puede mostrar una fecha u hora.
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores establecer cualquier formato de visualización para un número o fecha.

### **Cómo establecer formatos de visualización en Microsoft Excel**

Para establecer formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1. Seleccione **Formato de celdas**. Aparecerá un cuadro de diálogo que se usa para establecer los formatos de visualización de cualquier tipo de valor.

En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como **General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje**, etc. Aspose.Cells admite todos estos formatos de visualización.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells proporciona métodos [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) y [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) para la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Estos métodos se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) proporciona algunas propiedades útiles para tratar con los formatos de visualización de números y fechas.

### **Cómo utilizar los formatos de números integrados**

Aspose.Cells ofrece algunos formatos de números integrados para configurar los formatos de visualización de los números y fechas. Estos formatos de números integrados se pueden aplicar utilizando la propiedad [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Todos los formatos de números integrados tienen valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado a la propiedad [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) para aplicar el formato de visualización. Este enfoque es rápido. Los formatos de números integrados admitidos por Aspose.Cells se enumeran a continuación.

|**Valor**|**Tipo**|**Cadena de formato**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo utilizar formatos de números personalizados**

Para definir su propia cadena de formato personalizada para establecer el formato de visualización, utilice la propiedad [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) del objeto [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Este enfoque no es tan rápido como usar formatos preestablecidos, pero es más flexible.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si utiliza la propiedad [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) para configurar el formato de número, cualquier formato anterior establecido usando la propiedad [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) se anulará y viceversa.

{{% /alert %}}

## **Temas avanzados**
- [Consulte el formato de número personalizado al configurar la propiedad Style.Custom](/cells/es/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Lista de formatos de número admitidos](/cells/es/cpp/list-of-supported-number-formats/)
- [Renderizar formato personalizado de fecha del patrón g y ge mm dd](/cells/es/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Especificar separadores de números decimales y de grupo personalizados para el libro de trabajo](/cells/es/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación de formato de patrón personalizado DBNum](/cells/es/cpp/specifying-dbnum-custom-pattern-formatting/)
