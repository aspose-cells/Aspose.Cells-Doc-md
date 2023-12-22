---
title: Configuración de números
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo que admite muchas configuraciones de números de celda diferentes. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para administrar la configuración numérica de las celdas para que los usuarios puedan ajustar el formato numérico en la hoja de cálculo según sea necesario.
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /es/net/cells-number-settings/
---
##  **Cómo configurar formatos de visualización de Numbers y fechas**

Una característica muy importante de Microsoft Excel es que permite a los usuarios configurar los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos se pueden utilizar para representar diferentes valores, incluidos decimales, moneda, porcentaje, fracción o valores contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. De igual forma, existen muchos formatos en los que se puede mostrar una fecha u hora.
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores configurar cualquier formato de visualización para un número o fecha.

###  **Cómo configurar formatos de visualización en Microsoft Excel**

Para configurar formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1. Seleccione *Formato Cells**. Aparecerá un cuadro de diálogo que se utiliza para configurar los formatos de visualización de cualquier tipo de valor.

 En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como**General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje,**etc. Aspose.Cells admite todos estos formatos de visualización.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada elemento en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona[**Obtener estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**Establecer estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos para el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase. Estos métodos se utilizan para obtener y configurar el formato de una celda. El[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona algunas propiedades útiles para tratar con los formatos de visualización de números y fechas.

###  **Cómo utilizar formatos numéricos integrados**

 Aspose.Cells ofrece algunos formatos de números integrados para configurar los formatos de visualización de números y fechas. Estos formatos de números integrados se pueden aplicar utilizando el[**Número**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) propiedad de la[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto. Todos los formatos numéricos integrados reciben valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado al[**Número**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) propiedad de la[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto para aplicar el formato de visualización. Este enfoque es rápido. Los formatos de números integrados admitidos por Aspose.Cells se enumeran a continuación.

|**Valor**|**Tipo**|**Cadena de formato**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Rojo]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Rojo]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|m/d/aa|
|15|Date|d-mmm-aa|
|16|Date|Mmmmm|
|17|Date|mmm-aa|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|Mmm|
|21|Time|h:mm:ss|
|22|Time|m/d/aa h:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Rojo]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[Rojo]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **Cómo utilizar formatos de números personalizados**

 Para definir su propia cadena de formato personalizada para configurar el formato de visualización, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Costumbre**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)propiedad. Este enfoque no es tan rápido como utilizar formatos preestablecidos, pero es más flexible.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Si usas el[**Costumbre**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propiedad para establecer el formato del número, cualquier formato anterior establecido usando el[**Número**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)La propiedad se anula y viceversa.

{{% /alert %}}

##  **Temas avanzados**
- [Verifique el formato de número personalizado al configurar el estilo. Propiedad personalizada](/cells/es/net/check-custom-number-format-when-setting-style-custom-property/)
- [Lista de formatos de números admitidos](/cells/es/net/list-of-supported-number-formats/)
- [Renderizar patrón de formato de fecha personalizado g y ge mm dd](/cells/es/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Especificar números decimales personalizados y separadores de grupo para el libro de trabajo](/cells/es/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación del formato de patrón personalizado DBNum](/cells/es/net/specifying-dbnum-custom-pattern-formatting/)
