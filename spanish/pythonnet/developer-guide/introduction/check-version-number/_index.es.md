---
title: Comprobar el número de versión
type: docs
weight: 80
url: /es/python-net/check-version-number/
---
{{% alert color="primary" %}}

¿Se pregunta qué versión de Aspose.Cells está utilizando? Publicamos nuevas versiones de Aspose.Cells, tanto para presentar nuevas funciones como para solucionar problemas, de forma regular. El número de versión consta del número de versión principal, el número de versión secundaria y el número de versión de revisión. Cada número debe ser un número entero de 0 en adelante. El formato es el siguiente:

mayor.menor.revisión

Cuando lanzamos una nueva compilación de Aspose.Cells, actualizamos el número de versión.

Este artículo explica cómo verificar qué versión de Aspose.Cells está instalada en el sistema manualmente y usando el Aspose.Cells API.

{{% /alert %}}

## **Comprobar el número de versión manualmente**

Para averiguar qué versión de Aspose.Cells está utilizando manualmente:

1.  Haga clic derecho en el archivo Aspose.Cells.dll y seleccione**Propiedades**.
1. Haga clic en la pestaña Versión (o Detalles) para comprobar el número de versión.

## **Verifique el número de versión usando el Aspose.Cells API**

Para averiguar qué versión de Aspose.Cells está usando a través de API, use el método estático GetVersion de la clase CellsHelper para obtener el número de versión de Aspose.Cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
