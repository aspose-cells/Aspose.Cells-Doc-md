---
title: Configuración de números
type: docs
weight: 10
url: /es/net/cells-number-settings/
---
## **Configuración de formatos de visualización de Numbers y fechas**

Una característica muy fuerte de Microsoft Excel es que permite a los usuarios configurar los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos se pueden utilizar para representar diferentes valores, incluidos valores decimales, monetarios, porcentuales, fraccionarios o contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. Del mismo modo, existen muchos formatos en los que se puede mostrar una fecha o una hora.
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores configurar cualquier formato de visualización para un número o una fecha.

### **Configuración de formatos de visualización en Microsoft Excel**

Para establecer formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1.  Seleccione**Formato Cells**. Aparecerá un cuadro de diálogo que se utiliza para configurar los formatos de visualización de cualquier tipo de valor.

 En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como**General**, **Número**, **Divisa**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje,**etc. Aspose.Cells admite todos estos formatos de visualización.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona[**ObtenerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**EstablecerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos para el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase. Estos métodos se utilizan para obtener y establecer el formato de una celda. Él[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona algunas propiedades útiles para manejar los formatos de visualización de números y fechas.

### **Uso de formatos numéricos integrados**

 Aspose.Cells ofrece algunos formatos de números incorporados para configurar los formatos de visualización de los números y las fechas. Estos formatos numéricos integrados se pueden aplicar utilizando el[**Número**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) propiedad de la[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto. Todos los formatos de números incorporados reciben valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado al[**Número**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) propiedad de la[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto para aplicar el formato de visualización. Este enfoque es rápido. Los formatos de números incorporados admitidos por Aspose.Cells se enumeran a continuación.

|**Valor**|**Escribe**|**cadena de formato**|
|:- |:- |:- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Divisa|$#,##0;$-#,##0|
|6|Divisa|$#,##0;[Rojo]$-#,##0|
|7|Divisa|$#,##0.00;$-#,##0.00|
|8|Divisa|$#,##0.00;[Rojo]$-#,##0.00|
|9|Porcentaje|0%|
|10|Porcentaje|0.00%|
|11|Científico|0.00E+00|
|12|Fracción|# ?/?
|
|13|Fracción|# */*
|
|14|Fecha|m/d/aa|
|15|Fecha|d-mmm-aaa|
|16|Fecha|d-mmm|
|17|Fecha|mmm-aaa|
|18|Hora|h:mm AM/PM|
|19|Hora|h:mm:ss AM/PM|
|20|Hora|mmm|
|21|Hora|h: mm: ss|
|22|Hora|m/d/aa h:mm|
|37|Divisa|# ,##0;-#,##0
|
|38|Divisa|# ,##0;[Rojo]-#,##0
|
|39|Divisa|# ,##0.00;-#,##0.00
|
|40|Divisa|# ,##0.00;[Rojo]-#,##0.00
|
|41|Contabilidad|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Contabilidad|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Contabilidad|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Contabilidad|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Hora|mm: ss|
|46|Hora|h :mm:ss|
|47|Hora|mm:ss.0|
|48|Científico|## 0.0E+00
|
|49|Texto|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Uso de formatos de números personalizados**

Para definir su propia cadena de formato personalizado para configurar el formato de visualización, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Disfraz**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)propiedad. Este enfoque no es tan rápido como el uso de formatos preestablecidos, pero es más flexible.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Si usas el[**Disfraz**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propiedad para establecer el formato de número, cualquier formato anterior establecido con el[**Número**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)la propiedad se anula y viceversa.

{{% /alert %}}

## **Temas avanzados**
- [Compruebe el formato de número personalizado al configurar el estilo. Propiedad personalizada](/cells/es/net/check-custom-number-format-when-setting-style-custom-property/)
- [Lista de formatos de números admitidos](/cells/es/net/list-of-supported-number-formats/)
- [Render Formato de fecha personalizado Patrón g y ge mm dd](/cells/es/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Especificar separadores de grupos y decimales de números personalizados para el libro de trabajo](/cells/es/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación del formato de patrón personalizado de DBNum](/cells/es/net/specifying-dbnum-custom-pattern-formatting/)
