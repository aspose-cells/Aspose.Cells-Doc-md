---
title: Configuración de números
type: docs
weight: 10
url: /es/java/cells-number-settings/
---
##  **Configuración de formatos de visualización de Numbers y fechas**

Una característica muy importante de Microsoft Excel es que permite a los usuarios configurar los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos se pueden utilizar para representar diferentes valores, incluidos decimales, moneda, porcentaje, fracción o valores contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. De igual forma, existen muchos formatos en los que se puede mostrar una fecha u hora.
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores configurar cualquier formato de visualización para un número o fecha.

##  **Configuración de formatos de visualización en Microsoft Excel**

Para configurar formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1. Seleccione *Formato Cells**. Aparecerá un cuadro de diálogo que se utiliza para configurar los formatos de visualización de cualquier tipo de valor.

 En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como**General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje,**etc. Aspose.Cells admite todos estos formatos de visualización.

##  **Uso de formatos numéricos integrados**

Aspose.Cells ofrece algunos formatos de números integrados para configurar los formatos de visualización de números y fechas. Todos los formatos numéricos integrados reciben valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado al[**Número**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) método de la[**Estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/style) objeto para aplicar el formato de visualización. Este enfoque es rápido. Los formatos de números integrados admitidos por Aspose.Cells se enumeran a continuación.

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
|14|Date|m/d/aaaa|
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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **Usar formatos de números personalizados**

 Para definir su propia cadena de formato personalizada para configurar el formato de visualización, utilice el[**Costumbre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Este enfoque no es tan rápido como utilizar formatos preestablecidos, pero es más flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Si usas el[**Costumbre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) para configurar el formato del número, cualquier formato anterior configurado usando el[**Número**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Especificar números decimales personalizados y separadores de grupo para el libro de trabajo](/cells/es/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación del formato de patrón personalizado DBNum](/cells/es/java/specifying-dbnum-custom-pattern-formatting/)
