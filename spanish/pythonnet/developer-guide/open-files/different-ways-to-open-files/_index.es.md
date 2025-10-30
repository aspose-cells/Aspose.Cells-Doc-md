---
title: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/python-net/different-ways-to-open-files/
description: Este artículo explica cómo abrir un archivo de Excel usando Aspose.Cells para Python via .NET API.
keywords: Cómo abrir un archivo de Excel sin Excel en Python, ¿Cómo abro un archivo de Excel?
---

{{% alert color="primary" %}}

Con Aspose.Cells para Python via .NET, es sencillo abrir archivos, por ejemplo, para recuperar datos, o para usar una plantilla de diseño para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Cómo abrir un archivo de Excel a través de una ruta**

Los desarrolladores pueden abrir un archivo de Microsoft Excel usando su ruta en el equipo local especificándolo en el constructor de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Solo pasa la ruta en el constructor como *cadena*. Aspose.Cells para Python via .NET detectará automáticamente el tipo de formato de archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Cómo abrir un archivo de Excel via un Stream**

También es sencillo abrir un archivo de Excel como un stream. Para hacerlo, use una versión sobrecargada del constructor que toma el objeto *Stream* que contiene el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Cómo abrir un archivo con solo datos**

Para abrir un archivo solo con datos, use las clases [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) y [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) para establecer el atributo y las opciones relacionadas de las clases para cargar el archivo de plantilla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
