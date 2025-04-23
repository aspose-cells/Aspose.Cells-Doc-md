---
title: Precedentes y Dependientes
type: docs
weight: 230
url: /es/net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente aquellas desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula utiliza celdas precedentes y celdas dependientes.

{{% /alert %}} 
## **Introducción**
- **Celdas precedentes** son celdas a las que hace referencia una fórmula en otra celda. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es precedente a la celda D10.
- **Celdas dependientes**: contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 es dependiente de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desees mostrar claramente qué celdas en una hoja de cálculo se utilizan en una fórmula. Del mismo modo, es posible que desees extraer las celdas dependientes de otras celdas.

Aspose.Cells te permite rastrear celdas y averiguar cuáles están vinculadas.
## **Rastreo de celdas precedentes y dependientes: Microsoft Excel**
Las fórmulas pueden cambiar en función de las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de C3 y C4 que contienen una fórmula, y se cambia C1 (por lo que se anula la fórmula), C3 y C4, u otras celdas, necesitan cambiar para equilibrar la hoja de cálculo según las reglas empresariales.

De manera similar, suponga que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que necesite rastrear la dependencia de una celda particular respecto a otras celdas. Si las reglas empresariales están incrustadas en fórmulas, nos gustaría averiguar la dependencia y ejecutar algunas reglas basadas en ella. De manera similar, si se modifica el valor de una celda en particular, ¿qué celdas en la hoja de cálculo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear las celdas precedentes y dependientes.

1. En la **Barra de herramientas Ver**, seleccione **Revisión de Fórmulas**. Se mostrará el cuadro de diálogo Revisión de Fórmulas.
1. Rastrear precedentes:
   1. Selecciona la celda que contiene la fórmula de la cual deseas encontrar las celdas precedentes.
   1. Para mostrar una flecha rastreadora a cada celda que proporciona datos directamente a la celda activa, haz clic en **Rastrear precedentes** en la barra de herramientas **Auditoría de fórmulas**.
1. Rastrear fórmulas que hacen referencia a una celda en particular (dependientes)
   1. Selecciona la celda de la que deseas identificar las celdas dependientes.
   1. Para mostrar una flecha rastreadora a cada celda que depende de la celda activa, haz clic en Rastrear dependientes en la barra de herramientas Auditoría de fórmulas.
## **Rastreo de celdas precedentes y dependientes: Aspose.Cells**
### **Rastreo de Precedentes**
Aspose.Cells facilita obtener celdas precedentes. No solo puede recuperar celdas que proporcionan datos a predecesores de fórmulas simples, sino que también puede encontrar celdas que proporcionan datos a predecesores de fórmulas complejas con rangos nombrados.

En el ejemplo a continuación, se utiliza un archivo de plantilla de Excel, Book1.xls. La hoja de cálculo tiene datos y fórmulas en la primera hoja de trabajo.

Aspose.Cells proporciona el método [GetPrecedents](https://reference.aspose.com/cells/net/aspose.cells/cell) de la clase [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) utilizado para rastrear los predecesores de una celda. Devuelve un [ReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection). Como se puede ver en el ejemplo anterior, en Book1.xls, la celda B7 contiene la fórmula "=SUM(A1:A3)". Por lo tanto, las celdas A1:A3 son las celdas precedentes de la celda B7. El siguiente ejemplo demuestra la característica de rastreo de predecesores utilizando el archivo de plantilla Book1.xls.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Rastreo de Dependientes**
Aspose.Cells le permite obtener celdas dependientes en hojas de cálculo. Aspose.Cells no solo puede recuperar celdas que proporcionan datos respecto a una fórmula simple, sino que también puede encontrar celdas que proporcionan datos a dependientes de fórmulas complejas con rangos nombrados.

Aspose.Cells proporciona el método [GetDependents](https://reference.aspose.com/cells/net/aspose.cells/cell) de la clase [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) utilizado para rastrear los dependientes de una celda. Por ejemplo, en Book1.xlsx hay fórmulas: "=A1+20" y "=A1+30" en las celdas B2 y C2 respectivamente. El siguiente ejemplo demuestra cómo rastrear los dependientes de la celda A1 utilizando el archivo de plantilla Book1.xlsx.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **Rastreo de celdas precedentes y dependientes según la cadena de cálculo**
Las API anteriores de rastreo de predecesores y dependientes están de acuerdo con la expresión de fórmula en sí. Simplemente proporcionan una forma conveniente para que el usuario rastree las interdependencias de unas pocas fórmulas. Si hay un gran cantidad de fórmulas en el libro de trabajo y el usuario necesita rastrear predecesores y dependientes para cada celda, tendrán un mal rendimiento. Para tal situación, el usuario debería considerar usar los métodos [GetPrecedentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) y [GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/). Estos dos métodos rastrean dependencias de acuerdo con la cadena de cálculo. Por lo tanto, para usarlos, primero debe habilitar la cadena de cálculo con [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/). Luego, debe realizar el cálculo completo para el libro de trabajo con [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1). Después de eso, puede rastrear predecesores o dependientes para todas esas celdas que necesite.

Para algunas fórmulas, los predecesores resultantes pueden ser diferentes para GetPrecedents y GetPrecedentsInCalculation, y los dependientes resultantes pueden ser diferentes para GetDependents y GetDependentsInCalculation. Por ejemplo, si la fórmula de la celda A1 es "=IF(TRUE,B2,C3)", GetPrecedents proporcionará B2 y C3 como predecesores de A1. En consecuencia, B2 y C3 tienen a la dependiente A1 al verificar con GetDependents. Sin embargo, para el cálculo de esta fórmula, es obvio que solo B2 puede afectar el resultado calculado. Así que GetPrecedentsInCalculation no proporcionará C3 para A1, y GetDependentsInCalculation no proporcionará A1 para C3. A veces el usuario solo puede tener el requisito de rastrear aquellas interdependencias que realmente afectan el resultado calculado de las fórmulas basadas en los datos actuales del libro de trabajo, en ese caso también necesitarán usar GetDependentsInCalculation/GetPrecedentsInCalculation en lugar de GetDependents/GetPrecedents.

El siguiente ejemplo muestra cómo rastrear los predecesores y dependientes según la cadena de cálculo para las celdas:


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
{{< app/cells/assistant language="csharp" >}}
