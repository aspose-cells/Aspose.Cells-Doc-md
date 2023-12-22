---
title: Precedentes y dependientes
type: docs
weight: 100
url: /es/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Las hojas de cálculo financieras complejas, especialmente las desarrolladas en colaboración, pueden ocultar los errores más embarazosos. Verificar la precisión de las fórmulas y encontrar la fuente de un error puede resultar difícil cuando la fórmula utiliza celdas precedentes y celdas dependientes.

{{% /alert %}} 
##  **Introducción**
- **Celdas precedentes** son celdas a las que se hace referencia mediante una fórmula en otra celda. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda B5 es un precedente de la celda D10.
- **Células dependientes** contienen fórmulas que hacen referencia a otras celdas. Por ejemplo, si la celda D10 contiene la fórmula =B5, la celda D10 depende de la celda B5.

Para que la hoja de cálculo sea fácil de leer, es posible que desees mostrar claramente qué celdas de una hoja de cálculo se utilizan en una fórmula. De manera similar, es posible que desees extraer las células dependientes de otras células.

Aspose.Cells le permite rastrear celdas y descubrir cuáles están vinculadas.
##  **Seguimiento de precedentes y dependientes Cells: Microsoft Excel**
Las fórmulas pueden cambiar según las modificaciones realizadas por un cliente. Por ejemplo, si la celda C1 depende de que C3 y C4 contengan una fórmula, y se cambia C1 (por lo que se anula la fórmula), es necesario cambiar C3 y C4, u otras celdas, para equilibrar la hoja de cálculo según las reglas comerciales.

De manera similar, supongamos que C1 contiene la fórmula "=(B1*22)/(M2*N32)". Quiero encontrar las celdas de las que depende C1, es decir, las celdas precedentes B1, M2 y N32.

Es posible que necesites rastrear la dependencia de una celda en particular con respecto a otras celdas. Si las reglas comerciales están integradas en fórmulas, nos gustaría descubrir la dependencia y ejecutar algunas reglas basadas en ella. De manera similar, si se modifica el valor de una celda en particular, ¿qué celdas de la hoja de trabajo se ven afectadas por ese cambio?

Microsoft Excel permite a los usuarios rastrear precedentes y dependientes.

1.  Sobre el**Ver barra de herramientas**, seleccione **Auditoría de fórmulas**
1. Seguimiento de precedentes:
 1. Seleccione la celda que contiene la fórmula para la que desea buscar celdas precedentes.
 1. Para mostrar una flecha trazadora en cada celda que proporciona datos directamente a la celda activa, haga clic en**Seguimiento de precedentes** sobre el**Auditoría de fórmulas** barra de herramientas.
1. Rastrear fórmulas que hacen referencia a una celda en particular (dependientes)
 1. Seleccione la celda para la cual desea identificar las celdas dependientes.
1. Para mostrar una flecha de seguimiento en cada celda que depende de la celda activa, haga clic en Seguimiento de dependientes en la barra de herramientas Auditoría de fórmulas.
##  **Seguimiento de precedente y dependiente Cells: Aspose.Cells**
###  **Seguimiento de precedentes**
Aspose.Cells facilita la obtención de celdas precedentes. No sólo puede recuperar celdas que proporcionan datos para precedentes de fórmulas simples, sino también encontrar celdas que proporcionan datos para precedentes de fórmulas complejas con rangos con nombre.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
###  **Seguimiento de dependientes**
Aspose.Cells te permite obtener celdas dependientes en hojas de cálculo. Aspose.Cells no sólo puede recuperar celdas que proporcionan datos sobre una fórmula simple, sino también encontrar celdas que proporcionan datos sobre fórmulas complejas dependientes con rangos con nombre.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
