---
title: Establecer borde de rango con Golang a través de C++
type: docs
weight: 600
url: /es/go-cpp/set-range-border/
description: Aprenda a establecer bordes de rango usando Aspose.Cells con Golang a través de C++.
---

## **Escenarios de uso posibles**
Cuando deseas establecer el borde para un rango, no necesitas configurar cada celda individualmente. Puedes establecer el borde en el rango completo. Aspose.Cells ofrece esta función. Este artículo proporciona un ejemplo de código que usa Aspose.Cells para establecer el borde del rango.

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
2. Agregar datos a las celdas en la primera hoja de trabajo.
3. Crear un [**Range**](https://reference.aspose.com/cells/go-cpp/range).
4. Establecer el borde interno del rango.
5. Establecer el borde externo del rango.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetBorder.go" >}}
