---
title: Aspose.Cells for Java 7.3.0 Notas de la versión
type: docs
weight: 50
url: /es/java/aspose-cells-for-java-7-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Esta página contiene notas de la versión para[Aspose.Cells for Java 7.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.0/)

{{% /alert %}} 

Estamos
 feliz de anunciar Aspose.Cells for Java v7.3.0!

 Qué hay de nuevo

- Leer
 y escribir archivos MHT
- Soporta
 mapas XML
- Aplicar
 Temas de MS Excel 2007/2010 para gráficos



Otras características notables, mejoras y correcciones se dan a continuación.

 Nuevas características

 – Admite configuraciones para la evaluación de la fórmula de transición

 Mejoras

- Dar formato a los valores de las celdas con la configuración regional especificada por el usuario

 Excepciones

- Los archivos de fuentes no admitidos pueden provocar errores al guardar en PDF con una excepción

 Insectos

- Cell. El método setR1C1Formula() no funcionó correctamente sin el desplazamiento de columna
- El rango con nombre se creó dos veces
- El método sortNames() provocó una excepción al guardar un archivo XLSM
- El número no se formateó correctamente para la fracción
- PDF en blanco generado para PrintOrderType.OVER_DESPUÉS_ABAJO
- El color de fondo y las cuadrículas son incorrectos en el PDF generado
- Las funciones de intersección y pendiente no se calcularon correctamente
- Elimine el límite de 33k de los elementos del campo Pivot para los formatos de archivo de Excel 2007
- La notación 1:1 no es compatible con la función IF
- La fórmula DATEDIF se calculó incorrectamente
- Búsqueda incorrecta de celdas en caso de fila nombrada
