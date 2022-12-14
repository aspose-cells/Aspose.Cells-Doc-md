---
title: Precedentes y dependientes
type: docs
weight: 100
url: /es/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente las desarrolladas en colaboración, pueden ocultar los errores más vergonzosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede ser difícil cuando la fórmula usa celdas precedentes y celdas dependientes.

{{% /alert %}} 
## **Introducción**
- **Células precedentes** son celdas a las que se hace referencia mediante una fórmula en otra celda. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es un precedente de la celda D10.
- **células dependientes** contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 depende de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desee mostrar claramente qué celdas de una hoja de cálculo se utilizan en una fórmula. De manera similar, es posible que desee extraer las celdas dependientes de otras celdas.

Aspose.Cells le permite rastrear celdas y averiguar cuáles están vinculadas.
## **Seguimiento de precedentes y dependientes Cells: Microsoft Excel**
Las fórmulas pueden cambiar según las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de que C3 y C4 contengan una fórmula, y se cambia C1 (por lo que se anula la fórmula), C3 y C4, u otras celdas, deben cambiar para equilibrar la hoja de cálculo en función de las reglas comerciales.

De manera similar, suponga que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que deba rastrear la dependencia de una celda en particular con otras celdas. Si las reglas comerciales están incrustadas en fórmulas, nos gustaría averiguar la dependencia y ejecutar algunas reglas basadas en ella. De manera similar, si se modifica el valor de una celda en particular, ¿qué celdas de la hoja de trabajo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear precedentes y dependientes.

1.  Sobre el**Ver barra de herramientas** , Seleccione**Auditoría de fórmulas**
1. Rastrear precedentes:
 1. Seleccione la celda que contiene la fórmula para la que desea buscar celdas precedentes.
 1. Para mostrar una flecha de seguimiento a cada celda que proporciona datos directamente a la celda activa, haga clic en**Rastrear precedentes** sobre el**Auditoría de fórmulas** barra de herramientas.
1. Seguimiento de fórmulas que hacen referencia a una celda en particular (dependientes)
 1. Seleccione la celda para la que desea identificar las celdas dependientes.
1. Para mostrar una flecha de rastreo para cada celda que depende de la celda activa, haga clic en Rastrear dependientes en la barra de herramientas Auditoría de fórmulas.
## **Seguimiento de precedentes y dependientes Cells: Aspose.Cells**
### **Rastreando precedentes**
Aspose.Cells facilita la obtención de celdas precedentes. No solo puede recuperar celdas que brindan datos a fórmulas precedentes simples, sino que también puede encontrar celdas que brindan datos a fórmulas precedentes complejas con rangos con nombre.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents.cpp" >}}
### **Seguimiento de dependientes**
Aspose.Cells le permite obtener celdas dependientes en hojas de cálculo. Aspose.Cells no solo puede recuperar celdas que brindan datos con respecto a una fórmula simple, sino que también puede encontrar celdas que brindan datos a dependientes de fórmulas complejas con rangos con nombre.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents.cpp" >}}
