---
title: Establecer borde de rango
type: docs
weight: 600
url: /es/java/set-range-border/
---
##  **Posibles escenarios de uso**
Cuando desee establecer el borde para Rango, no necesita establecer cada celda individualmente. Puede establecer el borde en el rango. Aspose.Cells ofrece esta función.
Este artículo proporciona un código de muestra que usa Aspose.Cells para establecer el borde del rango.

##  **Establecer borde de rango en Excel**
Para establecer el borde de un rango en Excel, puede seguir estos pasos:
1. Seleccione el rango de celdas al que desea aplicar el borde.
2. En la pestaña "Inicio" de la cinta, busque el grupo "Fuente".
3. Dentro del grupo "Fuente", haga clic en el botón desplegable "Bordes".
<br>
<img src="border.png" />
4. Elija el tipo de borde que desea aplicar de las opciones en el menú desplegable. Puede elegir entre estilos de borde preestablecidos o personalizar su propio borde.
5. Una vez que haya seleccionado el estilo de borde deseado, el borde se aplicará al rango de celdas seleccionado.

##  **Establecer borde de rango usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregue datos a las celdas en la primera hoja de trabajo.
1.  Crear un[**Rango**](https://reference.aspose.com/cells/java/com.aspose.cells/range/).
1. Establezca el borde interior del Rango.
1. Establezca el borde exterior de Rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Range-set-border.java" >}}