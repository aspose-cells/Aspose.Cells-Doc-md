---
title: Aspose.Cells Plantilla y marcadores inteligentes
type: docs
weight: 30
url: /es/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

Una plantilla Aspose.Cells es un libro de Excel Microsoft que contiene marcadores inteligentes. Los marcadores inteligentes actúan como marcadores de posición de datos para los elementos del informe y se reemplazan con los datos correspondientes en el momento de la representación. Hay cinco tipos de marcadores inteligentes, enumerados a continuación. Todos los marcadores se pueden insertar en una plantilla mediante Aspose.Cells.Report.Designer. También se pueden editar manualmente.

{{% /alert %}} 
### **Marcadores inteligentes**
#### **Marcadores de datos**
 el formato de**marcadores de datos** es &=NombreConjuntoDatos.NombreCampo. Por ejemplo: &=SalesDetail.sales donde SalesDetail es el nombre de un conjunto de datos o consulta y sales es el nombre de uno de sus campos. En el momento de la representación, los marcadores de datos se reemplazan con los valores del conjunto de datos proporcionado por Reporting Services.
#### **Marcadores de fórmulas de Reporting Services**
 El formato de Reporting Services'**marcadores de fórmulas**es &=expresión. Por ejemplo: &=suma(DetalleVentas.ventas)/100. La expresión consta de función, campos de conjunto de datos, operador, etc. En tiempo de renderizado. Los marcadores de fórmulas de Reporting Services se reemplazan con valores calculados.
#### **Marcadores de variables globales de Reporting Services**
 El formato de Reporting Services'**marcadores de variables globales** es &=Globales! Nombre de la variable. Por ejemplo: &=Globals!ExecutionTime donde ExecutionTime es el nombre de una variable global. Los marcadores de variables globales se reemplazan con valores de variables globales en el momento de la representación.
#### **Marcadores de parámetros de Reporting Services**
 Un parámetro de informe tiene dos atributos: valor y etiqueta. Como consecuencia,**marcadores de parámetros** tienen dos formatos: &= Parámetros! ParamName.Value y &=Parámetros! ParamName.Etiqueta. Indican el nombre y la etiqueta del parámetro respectivamente. En el momento del renderizado, los marcadores de parámetros se reemplazan con los valores de parámetros ingresados por el usuario.
#### **Fórmulas dinámicas**
 Para realizar cálculos en filas insertadas, utilice fórmulas dinámicas.**fórmulas dinámicas** le permite insertar Microsoft fórmulas de Excel en celdas incluso cuando una fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Se pueden repetir para cada fila insertada o usarse solo con celdas donde se colocan marcadores de datos para ellos.

El formato de las fórmulas dinámicas es &=&=RepeatDynamicFormula.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- {r}: número de fila actual.
- {2}, {-1}: desplazamiento al número de fila actual.

**Una fórmula dinámica repetitiva y la hoja de cálculo de Excel resultante** 

![todo:imagen_alternativa_texto](aspose-cells-template-and-smart-markers_1.png)
