---
title: Licencias
type: docs
weight: 50
url: /es/cpp/licensing/
---

## **Limitaciones de la versión de evaluación**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Aplicar la licencia usando un archivo o un objeto de flujo**
La licencia se puede cargar desde un archivo o un objeto de flujo. Aspose.Cells for C++ tratará de encontrar la licencia en las siguientes ubicaciones:

1. Ruta explícita.
1. La carpeta que contiene Aspose.Cells.dll.
1. La carpeta que contiene la ensambladura que llamó a Aspose.Cells.dll.
1. La carpeta que contiene la ensambladura de entrada (su .exe).
1. Un recurso incrustado en la ensambladura que llamó a Aspose.Cells.dll.

La forma más sencilla de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.Cells.dll y especificar el nombre del archivo, sin una ruta, como se muestra en el ejemplo a continuación.
### **Cargando una Licencia desde un Archivo**
La forma más sencilla de aplicar una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.Cells.dll y especificar solo el nombre del archivo sin una ruta.

{{% alert color="primary" %}} 

Cuando llame al método SetLicense, el nombre de la licencia que pase debe ser el del archivo de licencia. Por ejemplo, si cambia el nombre del archivo de licencia a "Aspose.Cells.lic.xml", pase ese nombre de archivo al método Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Cargando una Licencia desde un Objeto Stream**
El siguiente ejemplo muestra cómo cargar una licencia desde un flujo.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
