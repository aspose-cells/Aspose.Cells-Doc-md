---
title: Instalación de la licencia Aspose.Cells for SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

Una vez que esté satisfecho con la [evaluación](/cells/es/sharepoint/evaluate-aspose-cells/), [compre una licencia](https://purchase.aspose.com/buy).

Antes de comprar, asegúrese de entender y aceptar los términos de suscripción de la licencia.

{{% /alert %}}

La licencia se enviará por correo electrónico una vez que se haya pagado el pedido. La licencia es un archivo ZIP que contiene un paquete de solución regular de SharePoint.

El ZIP de licencia contiene:

- **Aspose.Cells.SharePoint.License.wsp** – Archivo de paquete de solución de SharePoint. La licencia Aspose.Cells for SharePoint está empaquetada como una solución de SharePoint para facilitar la implementación y retracción en todo el conjunto de servidores.
- **readme.txt** – Instrucciones de instalación de la licencia. La instalación de la licencia se realiza desde la consola del servidor a través de **stsadm.exe**. Los pasos necesarios para instalar la licencia se indican a continuación.

#### **Instalación de la Licencia**

{{% alert color="primary" %}}

Se omiten los caminos para mayor claridad. Agregue la ruta real a **stsadm.exe** y/o el archivo de solución al ejecutar los pasos a continuación.

{{% /alert %}}

1. Ejecute stsadm para agregar la solución a la tienda de soluciones de SharePoint:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Implemente la solución en todos los servidores de la granja:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Ejecute trabajos administrativos programados para completar la implementación inmediatamente:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

Recibirá una advertencia al ejecutar el paso de implementación si el servicio de administración de Windows SharePoint Services no se ha iniciado. ** Stsadm.exe ** depende de este servicio y del servicio de temporizador de Windows SharePoint para replicar datos de solución en toda la granja. Si estos servicios no se están ejecutando en su granja de servidores, es posible que necesite implementar la licencia por separado en cada servidor.

{{% /alert %}}
