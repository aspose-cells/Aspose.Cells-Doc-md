---
title: Fuente de encabezado y cuerpo del tema con Golang a través de C++
linktitle: Fuente de tema para encabezados y cuerpo
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta establecer fuentes de tema para encabezados y cuerpo en documentos de Excel, permitiendo a los usuarios personalizar la apariencia y estilo del documento. Este artículo mostrará cómo usar la biblioteca Aspose.Cells para trabajar con fuentes de tema en encabezados y cuerpo en documentos de Excel.
keywords: Aspose.Cells, Documento de Excel, Encabezado, Cuerpo, Fuente de tema, Apariencia, Estilo
type: docs
weight: 120
url: /es/go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La fuente predeterminada cambiará automáticamente cuando se modifique la configuración regional.

Si se cambia la fuente predeterminada, también se cambiará la altura de la fila y el ancho de la columna e incluso puede desconfigurar el diseño de la página.

¿Qué causó el cambio de la fuente predeterminada?

Si se establece una fuente de tema de Excel, Excel cambiará automáticamente entre fuentes diferentes según el entorno de idioma actual.

{{% /alert %}}

## **Fuente de tema para encabezados y cuerpo en Excel**

En Excel, selecciona la pestaña Inicio, haz clic en la caja desplegable de fuente, verás "Fuentes de tema" con dos fuentes de tema: Calibri Light (Encabezados) y Calibri (Cuerpo) en la parte superior con la configuración regional en inglés.

**![Fuentes del tema](Theme-Fonts.png)**

Si se selecciona Fuente de tema, el nombre de la fuente se mostrará de manera diferente en diferentes regiones.
Si no deseas que la fuente cambie automáticamente en diferentes regiones, no selecciones las dos Fuentes de tema.

## **Cambiar fuentes de encabezados y cuerpo de forma programática**
Con Aspose.Cells for C++, podemos verificar si la fuente predeterminada es una fuente de tema o establecer la fuente de tema con la propiedad [**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/).

El siguiente código de muestra muestra cómo manipular la fuente del tema de forma programática.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}
## **Obtiene dinámicamente la fuente del tema local de forma programática**
A veces, nuestros servidores y las máquinas de los usuarios no están en la misma región. ¿Cómo podemos obtener la misma fuente que los usuarios desean para el procesamiento de archivos?

Debemos configurar las configuraciones regionales del sistema antes de cargar el archivo con la propiedad [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/).

El siguiente ejemplo de código muestra cómo obtener la fuente de tema local.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}
