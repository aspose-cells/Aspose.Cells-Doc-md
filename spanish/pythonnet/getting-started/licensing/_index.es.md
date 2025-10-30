---
title: Licencias
type: docs
weight: 21
url: /es/python-net/licensing/
---

{{% alert color="primary" %}}

Puedes descargar fácilmente una versión de evaluación de Aspose.Cells Python a través de .Net desde su [página de descarga] (https://pypi.org/project/aspose-cells-python/) en repositorios Pypi. La versión de evaluación ofrece absolutamente las mismas capacidades que la versión con licencia del componente. Además, la versión de evaluación simplemente se licencia cuando compras una licencia y agregas un par de líneas de código para aplicar la licencia.

{{% /alert %}}

## **Limitaciones de la versión de evaluación**

La versión de evaluación del producto Aspose.Cells Python a través de .Net (sin una licencia especificada) proporciona la funcionalidad completa del producto, pero está limitada a abrir 100 archivos en un programa y una hoja de cálculo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

- **Número de archivos abiertos** (Aspose.Cells Python via .Net)
  Al ejecutar su programa, solo puede abrir 100 archivos de Excel usando Aspose.Cells Python a través de la biblioteca .Net. Si su aplicación excede este número, se lanzará una excepción.


Además, una hoja de cálculo con marca de agua de evaluación siempre se mostrará como la hoja de cálculo activa en el archivo de Excel generado usando Aspose.Cells Python a través de la biblioteca. Solo en la versión con licencia, puede establecer la hoja de cálculo activa en otras hojas de cálculo. En el archivo PDF de salida o en el archivo de imagen con Aspose.Cells Python a través de la biblioteca, se pegará una marca de agua de evaluación en la parte superior del documento/imagen.

{{% alert color="primary" %}}

Si desea probar Aspose.Cells Python a través de la versión de evaluación sin limitaciones, también puede solicitar una [Licencia Temporal de 30 Días](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Aplicar una Licencia en Aspose.Cells Python a través del Componente**

La licencia es un archivo XML de texto plano que contiene detalles como el nombre del producto, el número de desarrolladores a los que se les otorga licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique. Incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará. Debe establecer una licencia antes de utilizar Aspose.Cells Python a través de la biblioteca si desea evitar sus limitaciones de evaluación. Solo es necesario establecer una licencia una vez por aplicación (o proceso). La licencia se puede cargar desde un archivo.

Aspose.Cells Python a través de la biblioteca intenta encontrar la licencia en ubicaciones de ruta explícitas.

Hay dos métodos comunes para aplicar una licencia desde un archivo.

### **Aplicar una Licencia desde Disco**

La forma más sencilla de establecer una licencia es colocar el archivo de licencia en la ruta explícita.

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llame al método set_license, el nombre de la licencia debe ser el mismo que el de su archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia a **Aspose.Cells.lic.xml**. Luego, en su código, debe usar el nombre de licencia modificado (**Aspose.Cells.lic.xml**) para el método set_license.

{{% /alert %}}


{{< app/cells/assistant language="python-net" >}}
