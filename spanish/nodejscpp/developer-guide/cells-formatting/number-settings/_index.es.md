---  
title: Configuraciones numéricas
linktitle: Configuraciones numéricas  
description: Aspose.Cells es una biblioteca de Node.js para trabajar con archivos de hoja de cálculo que soporta muchas configuraciones diferentes de números en las celdas. Este artículo presenta cómo usar la biblioteca Aspose.Cells para gestionar las configuraciones numéricas de las celdas para ajustar los formatos de números en las hojas de cálculo.  
keywords: Aspose.Cells, biblioteca Node.js, hoja de cálculo electrónica, configuraciones de números en celdas, formato, gestión, formatos de números y fechas  
type: docs  
weight: 10  
url: /es/nodejs-cpp/cells-number-settings/  
---  

## **Cómo establecer formatos de visualización de números y fechas**  

Una función muy potente de Microsoft Excel es que permite a los usuarios establecer los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos pueden usarse para representar diferentes valores incluyendo decimal, moneda, porcentaje, fracción o valores de contabilidad, etc. Todos estos valores numéricos se muestran en diferentes formatos dependiendo del tipo de información que representan. De manera similar, existen muchos formatos en los que se puede mostrar una fecha o hora.  
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores establecer cualquier formato de visualización para un número o fecha.  

### **Cómo establecer formatos de visualización en Microsoft Excel**  

Para establecer formatos de visualización en Microsoft Excel:  

1. Haga clic derecho en cualquier celda.  
2. Seleccione **Formato de celdas**. Aparecerá un cuadro de diálogo que se usa para establecer los formatos de visualización de cualquier valor.  

En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como **General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje**, etc. Aspose.Cells soporta todos estos formatos de visualización.  

Aspose.Cells proporciona un módulo, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Excel. El módulo [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja en el archivo de Excel. Una hoja de cálculo está representada por el módulo [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). El módulo [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) representa un objeto del módulo [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells ofrece métodos [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) y [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) para el módulo [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Estos métodos se usan para obtener y establecer el formato de una celda. El módulo [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) proporciona algunas propiedades útiles para tratar los formatos de visualización de números y fechas.  

### **Cómo utilizar los formatos de números integrados**  

Aspose.Cells ofrece algunos formatos de números incorporados para configurar los formatos de visualización de los números y fechas. Estos formatos pueden aplicarse usando el método [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Todos los formatos de números incorporados tienen valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado al método [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) para aplicar el formato de visualización. Este método es rápido. Los formatos de números incorporados soportados por Aspose.Cells se listan a continuación.  

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
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Cómo utilizar formatos de números personalizados**  

Para definir tu propia cadena de formato personalizada para establecer el formato de visualización, usa el método [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Este método no es tan rápido como usar formatos predefinidos, pero es más flexible.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Si usas el método [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) para establecer el formato numérico, cualquier formato anterior establecido con el método [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) será sobreescrito y viceversa.  

{{% /alert %}}  

## **Temas avanzados**  
- [Consulte el formato de número personalizado al configurar la propiedad Style.Custom](/cells/es/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Lista de formatos de número admitidos](/cells/es/nodejs-cpp/list-of-supported-number-formats/)  
- [Renderizar formato personalizado de fecha del patrón g y ge mm dd](/cells/es/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Especificar separadores de números decimales y de grupo personalizados para el libro de trabajo](/cells/es/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Especificación de formato de patrón personalizado DBNum](/cells/es/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
