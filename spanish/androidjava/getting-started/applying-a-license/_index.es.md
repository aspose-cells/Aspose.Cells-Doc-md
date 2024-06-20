---
title: Aplicar una licencia
type: docs
weight: 40
url: /es/java/applying-a-license/
---

{{% alert color="primary" %}}

Una vez que esté satisfecho con su evaluación de Aspose.Cells, [adquiera una licencia](https://purchase.aspose.com/buy) en el sitio web de Aspose. Familiarícese con los diferentes [tipos de licencias](https://purchase.aspose.com/policies/license-types/) que se ofrecen. Si tiene alguna pregunta, no dude en [contactar al equipo de ventas de Aspose](https://about.aspose.com/contact).

Cada licencia de Aspose lleva una suscripción de un año para actualizaciones gratuitas a cualquier nueva versión o correcciones que salgan durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como de evaluación.

La licencia es un archivo XML de texto plano que contiene detalles como el nombre del producto, el número de desarrolladores con licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, así que no modifique el archivo: incluso agregar un salto de línea adicional lo invalidará.

Debe establecer una licencia antes de realizar cualquier operación con documentos. Asegúrese de hacer esto antes de crear un objeto Document. Solo se requiere establecer una licencia una vez por aplicación o proceso.

{{% /alert %}}

## **Cargando el archivo de licencia**

En Aspose.Cells para Android via Java, la licencia puede ser [incrustada como un recurso](/cells/es/java/applying-a-license/#applying-a-license-from-an-embedded-resource), o cargada desde un flujo:

1. Coloque el archivo de licencia en cualquier ubicación en **/mnt/sdcard/**.
1. Cree un flujo que haga referencia al archivo.
1. Pase el flujo (que contiene el archivo de licencia) al método SetLicense.

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **Aplicando una licencia desde un recurso incrustado**

Para acceder a la licencia como un recurso por nombre desde un archivo de paquete de Android:

1. Agregue el archivo de licencia como un recurso a la carpeta **res/raw** de su aplicación.
   El archivo de licencia debe ser visible en la carpeta **res/raw**.
1. Acceda/cargue la licencia desde el recurso con el siguiente ejemplo de código.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
