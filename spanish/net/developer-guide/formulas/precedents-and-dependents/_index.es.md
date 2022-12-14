---
title: Precedentes y dependientes
type: docs
weight: 230
url: /es/net/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente las desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula usa celdas precedentes y celdas dependientes.

{{% /alert %}} 
## **Introducción**
- **Células precedentes** son celdas a las que se hace referencia mediante una fórmula en otro Cell. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es un precedente de la celda D10.
- **células dependientes** contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 depende de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desee mostrar claramente qué celdas de una hoja de cálculo se utilizan en una fórmula. De manera similar, es posible que desee extraer las celdas dependientes de otras celdas.

Aspose.Cells le permite rastrear celdas y averiguar cuáles están vinculadas.
## **Seguimiento de precedentes y dependientes Cells: Microsoft Excel**
Las fórmulas pueden cambiar según las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de que C3 y C4 contengan una fórmula, y se cambia C1 (por lo que se anula la fórmula), C3 y C4, u otras celdas, deben cambiar para equilibrar la hoja de cálculo en función de las reglas comerciales.

De manera similar, suponga que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que deba rastrear la dependencia de una celda en particular con otras celdas. Si las reglas comerciales están incrustadas en fórmulas, nos gustaría averiguar la dependencia y ejecutar algunas reglas basadas en ella. De manera similar, si se modifica el valor de una celda en particular, ¿qué celdas de la hoja de trabajo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear precedentes y dependientes.

1.  Sobre el**Ver barra de herramientas** , Seleccione**Auditoría de fórmulas**. Se mostrará el cuadro de diálogo Auditoría de fórmulas.
1. Rastrear precedentes:
 1. Seleccione la celda que contiene la fórmula para la que desea buscar celdas precedentes.
 1. Para mostrar una flecha de seguimiento a cada celda que proporciona datos directamente a la celda activa, haga clic en**Rastrear precedentes** sobre el**Auditoría de fórmulas** barra de herramientas.
1. Seguimiento de fórmulas que hacen referencia a una celda en particular (dependientes)
 1. Seleccione la celda para la que desea identificar las celdas dependientes.
1. Para mostrar una flecha de rastreo para cada celda que depende de la celda activa, haga clic en Rastrear dependientes en la barra de herramientas Auditoría de fórmulas.
## **Seguimiento de precedentes y dependientes Cells: Aspose.Cells**
### **Rastreando precedentes**
Aspose.Cells facilita la obtención de celdas precedentes. No solo puede recuperar celdas que brindan datos a fórmulas precedentes simples, sino que también puede encontrar celdas que brindan datos a fórmulas precedentes complejas con rangos con nombre.

En el siguiente ejemplo, se utiliza un archivo de plantilla de Excel, Book1.xls. La hoja de cálculo tiene datos y fórmulas en la primera hoja de cálculo.

 Aspose.Cells proporciona el[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[ObtenerPrecedentes](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedents) método utilizado para rastrear los precedentes de una celda. devuelve un[ReferredAreaCollectionReferredAreaCollectionReferredAreaCollection](https://reference.aspose.com/cells/net/aspose.cells/referredareacollection)Como puede ver arriba, en Book1.xls, la celda B7 contiene una fórmula "=SUM(A1:A3)". Entonces, las celdas A1:A3 son las celdas precedentes a la celda B7. El siguiente ejemplo demuestra la función de rastreo de precedentes utilizando el archivo de plantilla Book1.xls.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingPrecedents-1.cs" >}}
### **Seguimiento de dependientes**
Aspose.Cells le permite obtener celdas dependientes en hojas de cálculo. Aspose.Cells no solo puede recuperar celdas que brindan datos con respecto a una fórmula simple, sino que también puede encontrar celdas que brindan datos a una fórmula compleja dependiente con rangos con nombre.

 Aspose.Cells proporciona el[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[ObtenerDependientes](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependents)método utilizado para rastrear los dependientes de una celda. Por ejemplo, en Book1.xlsx hay fórmulas: "=A1+20" y "=A1+30" en las celdas B2 y C2 respectivamente. El siguiente ejemplo muestra cómo realizar un seguimiento de los dependientes de la celda A1 mediante el archivo de plantilla Book1.xlsx.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependents-1.cs" >}}
### **Seguimiento de celdas precedentes y dependientes según la cadena de cálculo**
Las apis anteriores de rastreo de precedentes y dependientes están de acuerdo con la expresión de la fórmula en sí. Simplemente proporcionan una manera conveniente para que el usuario rastree las interdependencias de algunas fórmulas. Si hay una gran cantidad de fórmulas en el libro de trabajo y el usuario necesita rastrear precedentes y dependientes para cada celda, tendrán un rendimiento deficiente. Para tal situación, el usuario debe considerar usar[ObtenerPrecedentesEnCálculo](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getprecedentsincalculation/) y[GetDependentsInCalculation](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getdependentsincalculation/) métodos. Estos dos métodos rastrean las dependencias según la cadena de cálculo. Entonces, para usarlos, primero debe habilitar la cadena de cálculo por[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/enablecalculationchain/) . Luego, debe realizar el cálculo completo para el Libro de trabajo al[Libro de trabajo. Calcular fórmula ()](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1). Después de eso, puede rastrear precedentes o dependientes para todas las celdas que necesita.

Para algunas fórmulas, los precedentes resultantes pueden ser diferentes para GetPrecedents y GetPrecedentsInCalculation, y los dependientes resultantes pueden ser diferentes para GetDependents y GetDependentsInCalculation. Por ejemplo, si la fórmula de la celda A1 es "=SI(VERDADERO,B2,C3)", ObtenerPrecedentes proporcionará B2 y C3 como precedente de A1. En consecuencia, B2 y C3 tienen el dependiente A1 cuando se verifican con GetDependents. Sin embargo, para el cálculo de esta fórmula, es obvio que solo B2 puede afectar el resultado calculado. Por lo tanto, GetPrecedentsInCalculation no proporcionará C3 para A1 y GetDependentsInCalculation no proporcionará A1 para C3. A veces, el usuario puede tener el requisito de rastrear esas interdependencias que realmente afectan el resultado calculado de las fórmulas basadas en los datos actuales del libro de trabajo, entonces también necesitan usar GetDependentsInCalculation/GetPrecedentsInCalculation en lugar de GetDependents/GetPrecedents.

El siguiente ejemplo demuestra cómo rastrear los precedentes y dependientes según la cadena de cálculo de las celdas:


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-TracingDependenciesInCalculation.cs" >}}
