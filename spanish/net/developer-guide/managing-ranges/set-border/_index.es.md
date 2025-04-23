---
title: Establecer Borde de Rango
type: docs
weight: 600
url: /es/net/set-range-border/
---

## **Escenarios de uso posibles**
Cuando desee establecer el borde para un Rango, no es necesario establecer cada celda individualmente. Puede establecer el borde en el rango. Aspose.Cells ofrece esta función.
Este artículo proporciona un código de ejemplo que utiliza Aspose.Cells para establecer el borde de un rango.

## **Establecer borde de rango en Excel**
Para establecer el borde de un rango en Excel, puedes seguir estos pasos:
1. Selecciona el rango de celdas al que deseas aplicarle el borde.
2. En la pestaña "Inicio" de la cinta, busca el grupo "Fuente".
3. Dentro del grupo "Fuente", haz clic en el botón desplegable "Bordes".
<br>
<img src="border.png" />
4. Elige el tipo de borde que deseas aplicar de las opciones en el menú desplegable. Puedes elegir entre estilos de borde preestablecidos o personalizar tu propio borde.
5. Una vez que hayas seleccionado el estilo de borde deseado, el borde se aplicará al rango seleccionado de celdas.

## **Configurar borde de rango usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Crear un [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Establecer el borde interno del rango.
1. Establecer el borde externo del rango.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-set-border.cs" >}}
{{< app/cells/assistant language="csharp" >}}
