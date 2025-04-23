---
title: Configuraciones numéricas
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo que soporta muchas configuraciones diferentes del número en las celdas. Este artículo introducirá cómo usar la biblioteca Aspose.Cells para gestionar la configuración del número en las celdas para que los usuarios puedan ajustar el formato en la hoja de cálculo según sus necesidades.
keywords: Aspose.Cells, biblioteca Python, hoja de cálculo electrónica, configuraciones de números en celdas, formato, gestión, formatos de números y fechas
type: docs
weight: 10
url: /es/python-net/cells-number-settings/
---

## **Cómo establecer formatos de visualización de números y fechas**

Una característica muy fuerte de Microsoft Excel es que permite a los usuarios establecer los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos pueden utilizarse para representar diferentes valores, incluidos decimales, moneda, porcentaje, fracción o valores contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. De manera similar, hay muchos formatos en los que se puede mostrar una fecha u hora.
Aspose.Cells para Python via .NET soporta esta funcionalidad y permite a los desarrolladores establecer cualquier formato de visualización para un número o fecha.

### **Cómo establecer formatos de visualización en Microsoft Excel**

Para establecer formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1. Seleccione **Formato de celdas**. Aparecerá un cuadro de diálogo que se usa para establecer los formatos de visualización de cualquier tipo de valor.

En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como **General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje**, etc. Aspose.Cells para Python via .NET soporta todos estos formatos de visualización.

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo del archivo Excel. Una hoja de cálculo se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells para Python via .NET proporciona métodos [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) y [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) para la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Estos métodos se usan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) proporciona algunas propiedades útiles para tratar los formatos de visualización de números y fechas.

### **Cómo utilizar los formatos de números integrados**

Aspose.Cells para Python via .NET ofrece algunos formatos numéricos integrados para configurar los formatos de visualización de números y fechas. Estos formatos numéricos integrados pueden aplicarse usando la propiedad [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Todos los formatos numéricos integrados tienen valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado a la propiedad [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) para aplicar el formato de visualización. Este enfoque es rápido. Los formatos numéricos integrados soportados por Aspose.Cells se enumeran a continuación.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Cómo utilizar formatos de números personalizados**

Para definir su propia cadena de formato personalizada para establecer el formato de visualización, utilice la propiedad [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) del objeto [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Este enfoque no es tan rápido como usar formatos preestablecidos, pero es más flexible.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

Si utiliza la propiedad [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) para configurar el formato de número, cualquier formato anterior establecido usando la propiedad [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) se anulará y viceversa.

{{% /alert %}}

## **Temas avanzados**
- [Consulte el formato de número personalizado al configurar la propiedad Style.Custom](/cells/es/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Lista de formatos de número admitidos](/cells/es/python-net/list-of-supported-number-formats/)
- [Renderizar formato personalizado de fecha del patrón g y ge mm dd](/cells/es/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Especificar separadores de números decimales y de grupo personalizados para el libro de trabajo](/cells/es/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación de formato de patrón personalizado DBNum](/cells/es/python-net/specifying-dbnum-custom-pattern-formatting/)

