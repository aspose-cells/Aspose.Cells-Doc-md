---
title: Licencias
type: docs
weight: 50
url: /es/python-java/licensing/
---

{{% alert color="primary" %}} 

Puedes instalar una versión de evaluación de **Aspose.Cells** para Python via Java con `pip install aspose-cells`. La versión de evaluación proporciona exactamente las mismas capacidades que la versión con licencia del producto. Además, la versión de evaluación simplemente se licencia cuando compras una licencia y añades un par de líneas de código para aplicar la licencia.

Una vez que estés satisfecho con tu evaluación de **Aspose.Cells**, puedes [comprar una licencia](https://purchase.aspose.com) en el sitio web de Aspose. Familiarízate con los distintos tipos de suscripción ofrecidos. Si tienes alguna pregunta, no dudes en contactar al equipo de ventas de Aspose.

Cada licencia de Aspose lleva una suscripción de un año para actualizaciones gratuitas a cualquier nueva versión o correcciones que salgan durante este tiempo. El soporte técnico es gratuito e ilimitado y se proporciona tanto a usuarios con licencia como de evaluación.

{{% /alert %}} {{% alert color="primary" %}} 

Si desea probar **Aspose.Cells** sin limitaciones de la versión de evaluación, solicite una licencia temporal de 30 días. Consulte [Cómo obtener una licencia temporal?](https://purchase.aspose.com/temporary-license) para más información.

{{% /alert %}}

## **Limitaciones de la versión de evaluación**

La versión de evaluación del producto **Aspose.Cells** (sin una licencia especificada) proporciona funcionalidad completa del producto, pero está limitada a abrir 100 archivos en un programa y una hoja de cálculo adicional con marca de agua de evaluación.

Las limitaciones se muestran a continuación:

### **1ª Limitación: Número de archivos abiertos**

Al ejecutar su programa, solo puede abrir 100 archivos de Excel. Si su aplicación supera este número, se generará una excepción.

### **2ª Limitación: Hoja de cálculo con marca de agua de evaluación**

![todo:image_alt_text](licensing_1.png)

Esta hoja de cálculo siempre se mostrará como la hoja de cálculo activa. Solo en la versión con licencia, puede establecer la hoja de cálculo activa en otras hojas de cálculo.

## **Configuración de una licencia**

La licencia es un archivo XML de texto sin formato que contiene detalles como el nombre del producto, el número de desarrolladores con licencia, la fecha de vencimiento de la suscripción, etc. El archivo está firmado digitalmente, por lo que no debe modificarlo; incluso la adición inadvertida de un salto de línea adicional en el archivo lo invalidará.

Debe configurar una licencia antes de utilizar Aspose.Cells si desea evitar sus limitaciones de evaluación. Solo es necesario configurar una licencia una vez por aplicación o proceso.

La licencia se puede cargar desde un archivo en las siguientes ubicaciones:

1. Ruta explícita.
2. Carpeta de trabajo.

Utilice el método [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) para licenciar el componente. A menudo, la forma más sencilla de establecer una licencia es colocar el archivo de licencia en la misma carpeta que Aspose.Cells.jar y especificar solo el nombre de archivo sin ruta, como se muestra en el siguiente ejemplo:

### **Ejemplo**

En este ejemplo, **Aspose.Cells** intentará encontrar el archivo de licencia en su carpeta de trabajo.

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
