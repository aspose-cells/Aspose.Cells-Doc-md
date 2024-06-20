---
title: Plantilla de Aspose.Cells y Marcadores Inteligentes
type: docs
weight: 30
url: /es/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Una plantilla de Aspose.Cells es un libro de Microsoft Excel que contiene Marcadores Inteligentes. Los Marcadores Inteligentes actúan como marcadores de datos para los elementos de informes y se reemplazan con los datos correspondientes en el momento de representación. Hay cinco tipos de marcadores inteligentes, enumerados a continuación. Todos los marcadores se pueden insertar en una plantilla mediante Aspose.Cells.Report.Designer. También se pueden editar manualmente. 

{{% /alert %}} 
### **Marcadores Inteligentes**
#### **Marcadores de Datos**
El formato de **marcadores de datos** es &=DataSetName.FieldName. Por ejemplo: &=SalesDetail.sales donde SalesDetail es el nombre de un conjunto de datos o consulta y sales es el nombre de uno de sus campos. En el momento de renderizado, los marcadores de datos se reemplazan por los valores del conjunto de datos proporcionado por Reporting Services.
#### **Marcadores de Fórmulas de Servicios de Informes**
El formato de **marcadores de fórmulas de Servicios de Informes** es &=expresión. Por ejemplo: &=sum(SalesDetail.sales)/100. La expresión consiste en función, campos del conjunto de datos, operador, etc. En el momento de renderizado, los marcadores de fórmulas de Servicios de Informes se reemplazan con valores calculados.
#### **Marcadores de Variables Globales de Servicios de Informes**
El formato de **marcadores de variables globales de Servicios de Informes** es &=Globals! Variable Name. Por ejemplo: &=Globals!ExecutionTime donde ExecutionTime es el nombre de una variable global. Los marcadores de variables globales se reemplazan con los valores de las variables globales en el momento de renderizado.
#### **Marcadores de Parámetros de Servicios de Informes**
Un parámetro de informe tiene dos atributos: valor y etiqueta. En consecuencia, los **marcadores de parámetros** tienen dos formatos: &= Parameters! ParamName.Value y &=Parameters! ParamName.Label. Indican el nombre y la etiqueta del parámetro respectivamente. Al renderizarse, los marcadores de parámetros se reemplazan con los valores de parámetros ingresados por el usuario.
#### **Fórmulas dinámicas**
Para realizar cálculos en filas insertadas, utilice fórmulas dinámicas. Las **fórmulas dinámicas** le permiten insertar fórmulas de Microsoft Excel en celdas incluso cuando una fórmula hace referencia a filas que se insertarán durante el proceso de exportación. Pueden repetirse para cada fila insertada o utilizarse solo con celdas donde se colocan marcadores de datos para ellos.

El formato de las fórmulas dinámicas es &=&=RepeatDynamicFormula.

Las fórmulas dinámicas permiten las siguientes opciones adicionales:

- {r} – Número de fila actual.
- {2}, {-1} – Desplazamiento al número de fila actual.

**Una fórmula dinámica repetitiva y la hoja de cálculo resultante de Excel** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
