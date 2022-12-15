---
title: Licencia
type: docs
weight: 21
url: /es/python-net/licensing/
---
{{% alert color="primary" %}}

 Puede descargar fácilmente una versión de evaluación de Aspose.Cells Python a través de .Net desde su[página de descarga](https://pypi.org/project/aspose-cells-python/)@Repos Pypi. La versión de evaluación proporciona absolutamente las mismas capacidades que la versión con licencia del componente. Además, la versión de evaluación simplemente obtiene la licencia cuando compra una licencia y agrega un par de líneas de código para aplicar la licencia.

{{% /alert %}}

## **Limitaciones de la versión de evaluación**

La versión de evaluación de Aspose.Cells Python a través del producto .Net (sin una licencia especificada) proporciona una funcionalidad completa del producto, pero está limitada a abrir 100 archivos en un programa y una hoja de trabajo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

- **Número de archivos abiertos** (Aspose.Cells Python vía .Net)
 Al ejecutar su programa, solo puede abrir 100 archivos de Excel usando Aspose.Cells Python a través de la biblioteca .Net. Si su aplicación excede este número, se lanzará una excepción.


Además, una hoja de trabajo con marca de agua de evaluación siempre se mostrará como la hoja de trabajo activa en el archivo de Excel generado usando Aspose.Cells Python a través de la biblioteca. Solo en la versión con licencia, puede configurar la hoja de trabajo activa en otras hojas de trabajo. En el PDF de salida o el archivo de imagen por Aspose.Cells Python vía, se pegaría una marca de agua de evaluación en la parte superior del documento/imagen.

{{% alert color="primary" %}}

 Si desea probar Aspose.Cells Python sin limitaciones de versión de evaluación, también puede solicitar un[Licencia temporal de 30 días](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Solicitud de una licencia en Aspose.Cells Python a través de un componente**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores para los que tiene licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique. Incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará. Debe configurar una licencia antes de utilizar Aspose.Cells Python si desea evitar su limitación de evaluación. Solo se requiere establecer una licencia una vez por aplicación (o proceso). La licencia se puede cargar desde un archivo.

Aspose.Cells Python vía intenta encontrar la licencia en ubicaciones de rutas explícitas.

Hay dos métodos comunes para aplicar una licencia desde un archivo.

### **Aplicar una licencia desde el disco**

La forma más fácil de configurar una licencia es colocar el archivo de licencia en la ruta explícita.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Cuando llamas al set_método de licencia, el nombre de la licencia debe ser el mismo que el nombre de su archivo de licencia. Por ejemplo, puede cambiar el nombre del archivo de licencia a **Aspose.Cells.lic.xml**. Luego, en su código, debe usar el nombre de licencia modificado (**Aspose.Cells.lic.xml**) para el conjunto_método de licencia

{{% /alert %}}


