---
title: Este formato de archivo no es compatible o no ha especificado un formato correcto
type: docs
weight: 10
url: /es/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Este formato de archivo no es compatible o no ha especificado un formato correcto**
Si el usuario ha especificado el formato de archivo al crear un libro de trabajo a partir de un archivo de plantilla, comúnmente este error se debe a que el formato de archivo especificado no es el formato real del archivo de plantilla. Si el usuario no ha especificado el formato de archivo, comúnmente se debe a que la extensión del nombre de archivo no representa el formato real de este archivo y el formato de archivo no puede ser detectado automáticamente, como en el archivo csv/tsv que no tiene identificadores especiales.
{{< app/cells/assistant language="java" >}}
