---
title: Precedentes y Dependientes
type: docs
weight: 230
url: /es/python-net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente aquellas desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula utiliza celdas precedentes y celdas dependientes.

{{% /alert %}} 
## **Introducción**
- **Celdas precedentes** son celdas a las que hace referencia una fórmula en otra celda. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es precedente a la celda D10.
- **Celdas dependientes**: contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 es dependiente de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desees mostrar claramente qué celdas en una hoja de cálculo se utilizan en una fórmula. Del mismo modo, es posible que desees extraer las celdas dependientes de otras celdas.

Aspose.Cells para Python via .NET te permite rastrear celdas y descubrir cuáles están vinculadas.
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
## **Seguimiento de celdas predecedentes y dependientes: Aspose.Cells para Python via .NET**
### **Rastreo de Precedentes**
Aspose.Cells para Python via .NET facilita obtener celdas predecedentes. No solo puede recuperar celdas que proporcionan datos a precedentes de fórmulas simples, sino también encontrar celdas que proporcionan datos a precedentes de fórmulas complejas con rangos con nombre.

En el ejemplo a continuación, se utiliza un archivo de plantilla de Excel, Book1.xls. La hoja de cálculo tiene datos y fórmulas en la primera hoja de trabajo.

Aspose.Cells para Python via .NET ofrece el método [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) de la clase [**get_precedents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents/#) usado para rastrear los predecedentes de una celda. Devuelve un [**ReferredAreaCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/referredareacollection). Como puedes ver arriba, en Book1.xls, la celda B7 contiene la fórmula "=SUMA(A1:A3)". Entonces, las celdas A1:A3 son las predecedentes de la celda B7. El siguiente ejemplo demuestra la función de rastreo de precedentes usando el archivo de plantilla Book1.xls.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingPrecedents-1.py" >}}
### **Rastreo de Dependientes**
Aspose.Cells para Python via .NET te permite obtener las celdas dependientes en las hojas de cálculo. Aspose.Cells para Python via .NET no solo puede recuperar celdas que proporcionan datos respecto a una fórmula simple, sino también encontrar celdas que proporcionan datos a dependientes de fórmulas complejas con rangos nombrados.

Aspose.Cells para Python via .NET proporciona el método [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) de la clase [**get_dependents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents/#bool) usado para rastrear los dependientes de una celda. Por ejemplo, en Book1.xlsx hay fórmulas: "=A1+20" y "=A1+30" en las celdas B2 y C2 respectivamente. El siguiente ejemplo demuestra cómo rastrear los dependientes de la celda A1 usando el archivo de plantilla Book1.xlsx.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependents-1.py" >}}

### **Rastreo de celdas precedentes y dependientes según la cadena de cálculo**
Las API anteriores de rastreo de precedentes y dependientes funcionan según la expresión de fórmula misma. Simplemente ofrecen una forma conveniente para que el usuario rastree las dependencias entre fórmulas. Si hay una gran cantidad de fórmulas en el libro y el usuario necesita rastrear precedentes y dependientes en cada celda, el rendimiento será deficiente. Para esas situaciones, el usuario debería considerar usar los métodos [**get_precedents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents_in_calculation/#) y [**get_dependents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents_in_calculation/#bool). Estos rastrean las dependencias según la cadena de cálculo. Por lo tanto, para usarlos, primero necesitas habilitar la cadena de cálculo con [**Workbook.settings.formula_settings.enable_calculation_chain**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/enable_calculation_chain/). Luego debes realizar un cálculo completo del libro con [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#). Después de eso, puedes rastrear precedentes o dependientes de todas esas celdas que necesitas.

Para algunas fórmulas, los predecesores resultantes pueden ser diferentes para GetPrecedents y GetPrecedentsInCalculation, y los dependientes resultantes pueden ser diferentes para GetDependents y GetDependentsInCalculation. Por ejemplo, si la fórmula de la celda A1 es "=IF(TRUE,B2,C3)", GetPrecedents proporcionará B2 y C3 como predecesores de A1. En consecuencia, B2 y C3 tienen a la dependiente A1 al verificar con GetDependents. Sin embargo, para el cálculo de esta fórmula, es obvio que solo B2 puede afectar el resultado calculado. Así que GetPrecedentsInCalculation no proporcionará C3 para A1, y GetDependentsInCalculation no proporcionará A1 para C3. A veces el usuario solo puede tener el requisito de rastrear aquellas interdependencias que realmente afectan el resultado calculado de las fórmulas basadas en los datos actuales del libro de trabajo, en ese caso también necesitarán usar GetDependentsInCalculation/GetPrecedentsInCalculation en lugar de GetDependents/GetPrecedents.

El siguiente ejemplo muestra cómo rastrear los predecesores y dependientes según la cadena de cálculo para las celdas:


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependenciesInCalculation.py" >}}

