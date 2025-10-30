---
title: Este formato de archivo no es compatible o no ha especificado un formato correcto
type: docs
weight: 10
url: /es/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Este formato de archivo no es compatible o no ha especificado un formato correcto**
Si el usuario ha especificado el formato de archivo al crear un libro desde una plantilla, comúnmente este error ocurre porque el formato de archivo especificado no es el formato real de la plantilla. Si el usuario no ha especificado el formato, generalmente es porque la extensión del nombre del archivo no representa el formato real del archivo y el formato no puede ser detectado automáticamente, como en el caso de archivos CSV/TSV que no tienen identificadores especiales. Por supuesto, los formatos de archivo no compatibles por Cells también reportarán este error.
{{< app/cells/assistant language="java" >}}
