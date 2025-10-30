---
title: Verificar número de versión
type: docs
weight: 80
url: /es/python-net/check-version-number/
---

{{% alert color="primary" %}}

¿Te gustaría saber qué versión de Aspose.Cells estás usando? Publicamos nuevas versiones de Aspose.Cells, tanto para introducir nuevas funciones como para solucionar problemas, de forma regular. El número de versión consta de un número de versión principal, un número de versión secundaria y un número de versión de corrección. Cada número debe ser un entero de 0 hacia arriba. El formato es el siguiente:

mayor.menor.corrección

Cuando lanzamos una nueva compilación de Aspose.Cells, actualizamos el número de versión.

Este artículo explica cómo comprobar manualmente qué versión de Aspose.Cells está instalada en el sistema y cómo hacerlo utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Verificar número de versión manualmente**

Para averiguar qué versión de Aspose.Cells estás utilizando manualmente:

1. Haz clic con el botón derecho en el archivo Aspose.Cells.dll y selecciona **Propiedades**.
1. Haz clic en la pestaña Versión (o Detalles) para comprobar el número de versión.

## **Verificar número de versión utilizando la API de Aspose.Cells**

Para averiguar qué versión de Aspose.Cells estás utilizando a través de la API, utiliza el método estático GetVersion de la clase CellsHelper para obtener el número de versión de Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}
