---
title: Aspose.Cells for Java 7.2.1 Notas de la versión
type: docs
weight: 70
url: /es/java/aspose-cells-for-java-7-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Esta página contiene notas de la versión para[Aspose.Cells for Java 7.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.1/)

{{% /alert %}} 

Estamos
 feliz de anunciar Aspose.Cells for Java v7.2.1!

 Nuevas características

- Dar formato a la tabla dinámica con estilos personalizados para diferentes categorías (Modificar el estilo rápido de la tabla dinámica)

 Mejoras

- Cells.findString()/find() admite la búsqueda de RegExand en un rango específico
- Soporte Imagen.setTitle()/getTitle()
- Guarde los gráficos de MS Excel en el archivo ODS
- Hacer que el archivo XLS creado Aspose.Cells sea compatible con POI

 Excepciones

- La lectura del archivo XLSX produce: "java.lang.ClassCastException:org.dom4j.Namespace"

 Insectos

- El archivo XLSX guardado da error: "Puede que se hayan perdido los datos"
- El número formateado era incorrecto en el PDF generado (se perdieron mil caracteres de grupo)
- El gráfico de barras no aparecía en el PDF generado para la versión JDK6
- Las referencias no se actualizan al expandir un rango
