---
title: Aplicar una licencia
type: docs
weight: 40
url: /es/java/applying-a-license/
---
{{% alert color="primary" %}}

 Una vez que esté satisfecho con su evaluación de Aspose.Cells,[comprar una licencia](https://purchase.aspose.com/buy) en el sitio web Aspose. Familiarícese con los diferentes[tipos de licencia](https://purchase.aspose.com/policies/license-types/) Ofrecido. Si tiene alguna pregunta, no dude en[póngase en contacto con el equipo de ventas Aspose](https://about.aspose.com/contact).

Cada licencia Aspose incluye una suscripción de un año para actualizaciones gratuitas a cualquier nueva versión o corrección que surja durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como a usuarios de evaluación.

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, la cantidad de desarrolladores con licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no lo modifique: incluso agregar un salto de línea adicional en el archivo lo invalidará.

Debe configurar una licencia antes de realizar cualquier operación con documentos. Asegúrese de hacer esto antes de crear un objeto Documento. Solo debe establecer una licencia una vez por aplicación o proceso.

{{% /alert %}}

## **Cargando el archivo de licencia**

 En Aspose.Cells para Android a través de Java, la licencia puede ser[incrustado como un recurso](/cells/es/java/applying-a-license/#applying-a-license-from-an-embedded-resource), o cargado desde una secuencia:

1.  Coloque el archivo de licencia en cualquier ubicación en**/mnt/tarjeta sd/**.
1. Cree una secuencia que haga referencia al archivo.
1. Pase la transmisión (que contiene el archivo de licencia) al método SetLicense.

**Java**

{{< highlight "java" >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Aplicación de una licencia desde un recurso integrado**

Para acceder a la licencia como un recurso por nombre desde un archivo de paquete de Android:

1.  Agregue el archivo de licencia como un recurso a su aplicación**res/crudo** carpeta.
 El archivo de licencia debe estar visible en el**res/crudo** carpeta.
1. Acceda o cargue la licencia desde el recurso con el siguiente ejemplo de código.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
