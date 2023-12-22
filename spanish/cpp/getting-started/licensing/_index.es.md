---
title: Licensing
type: docs
weight: 50
url: /es/cpp/licensing/
---
##  **Limitaciones de la versión de evaluación**
 Se puede descargar una versión de evaluación gratuita de Aspose.Cells for C++ desde la sección de descargas del sitio web de Aspose en:<https://downloads.aspose.com/cells/cpp>.
##  **Aplicar licencia utilizando un archivo o un objeto de transmisión**
La licencia se puede cargar desde un archivo u objeto de flujo. Aspose.Cells for C++ intentará encontrar la licencia en las siguientes ubicaciones:

1. Camino explícito.
1. La carpeta que contiene Aspose.Cells.dll.
1. La carpeta que contiene el ensamblado que llamó Aspose.Cells.dll.
1. La carpeta que contiene el ensamblado de entrada (su .exe).
1. Un recurso incrustado en el ensamblado que llamó Aspose.Cells.dll.

La forma más sencilla de configurar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.Cells.dll y especificar el nombre del archivo, sin una ruta, como se muestra en el siguiente ejemplo.
###  **Cargando una licencia desde un archivo**
La forma más sencilla de aplicar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.Cells.dll y especificar solo el nombre del archivo sin una ruta.

{{% alert color="primary" %}} 

Cuando llama al método SetLicense, el nombre de la licencia que pasa debe ser el del archivo de licencia. Por ejemplo, si cambia el nombre del archivo de licencia a "Aspose.Cells.lic.xml", pase ese nombre de archivo al método Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **Cargando una licencia desde un objeto Stream**
El siguiente ejemplo muestra cómo cargar una licencia desde una secuencia.

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
