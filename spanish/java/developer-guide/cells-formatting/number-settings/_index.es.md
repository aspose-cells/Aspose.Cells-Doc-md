---
title: Configuración de números
type: docs
weight: 10
url: /es/java/cells-number-settings/
---
## **Configuración de formatos de visualización de números y fechas**

Una característica muy fuerte de Microsoft Excel es que permite a los usuarios configurar los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos se pueden utilizar para representar diferentes valores, incluidos valores decimales, monetarios, porcentuales, fraccionarios o contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. Del mismo modo, existen muchos formatos en los que se puede mostrar una fecha o una hora.
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores configurar cualquier formato de visualización para un número o una fecha.

## **Configuración de formatos de visualización en Microsoft Excel**

Para establecer formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1.  Seleccione**Formato Cells**. Aparecerá un cuadro de diálogo que se utiliza para configurar los formatos de visualización de cualquier tipo de valor.

 En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como**General**, **Número**, **Divisa**, **Contabilidad**, **Fecha**, **Tiempo**, **Porcentaje,**etc. Aspose.Cells admite todos estos formatos de visualización.

## **Uso de formatos numéricos integrados**

 Aspose.Cells ofrece algunos formatos de números incorporados para configurar los formatos de visualización de los números y las fechas. Todos los formatos de números incorporados reciben valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado al[**Número**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) metodo de la[**Estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/style) objeto para aplicar el formato de visualización. Este enfoque es rápido. Los formatos de números incorporados admitidos por Aspose.Cells se enumeran a continuación.

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
|18|Tiempo|h:mm AM/PM|
|19|Tiempo|h:mm:ss AM/PM|
|20|Tiempo|mmm|
|21|Tiempo|h: mm: ss|
|22|Tiempo|m/d/aa h:mm|
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
|45|Tiempo|mm: ss|
|46|Tiempo|h :mm:ss|
|47|Tiempo|mm:ss.0|
|48|Científico|## 0.0E+00
|
|49|Texto|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Uso de formatos de números personalizados**

Para definir su propia cadena de formato personalizado para configurar el formato de visualización, utilice el[**Disfraz**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Este enfoque no es tan rápido como el uso de formatos preestablecidos, pero es más flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Si usas el[**Disfraz**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) para configurar el formato de número, cualquier formato anterior configurado usando el[**Número**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Especificar separadores de grupos y decimales de números personalizados para el libro de trabajo](/cells/es/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación del formato de patrón personalizado de DBNum](/cells/es/java/specifying-dbnum-custom-pattern-formatting/)
