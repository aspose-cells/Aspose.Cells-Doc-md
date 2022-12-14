---
title: Instalación de Aspose.Cells para la licencia de SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 Una vez que esté satisfecho con su[evaluación](/cells/es/sharepoint/evaluate-aspose-cells/), [comprar una licencia](https://purchase.aspose.com/buy).

Antes de comprar, asegúrese de comprender y aceptar los términos de suscripción de la licencia.

{{% /alert %}}

La licencia se le envía por correo electrónico cuando se ha pagado el pedido. La licencia es un archivo ZIP que contiene un paquete de solución de SharePoint regular.

El ZIP de la licencia contiene:

- **Aspose.Cells.SharePoint.License.wsp** – Archivo de paquete de solución de SharePoint. La licencia Aspose.Cells para SharePoint está empaquetada como una solución de SharePoint para facilitar la implementación y la retirada en toda la granja de servidores.
- **Léame.txt** – Instrucciones de instalación de la licencia. La instalación de la licencia se realiza desde la consola del servidor a través del**stsadm.exe**. Los pasos necesarios para instalar la licencia se indican a continuación.

#### **Instalación de la licencia**

{{% alert color="primary" %}}

 Las rutas se omiten para mayor claridad. Agregue la ruta real a**stsadm.exe** y/o archivo de solución al ejecutar los pasos a continuación.

{{% /alert %}}

1. Ejecute stsadm para agregar la solución al almacén de soluciones de SharePoint:
 stsadm.exe -o addsolution -nombre de archivo Aspose.Cells.SharePoint.License.wsp
1. Implemente la solución en todos los servidores de la granja:
stsadm.exe -o deploymentsolution -name Aspose.Cells.SharePoint.License.wsp -inmediate -force
1. Ejecute trabajos del temporizador administrativo para completar la implementación de inmediato:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Recibirá una advertencia cuando ejecute el paso de implementación si el servicio de administración de SharePoint Services Windows no se ha iniciado.**Stsadm.exe** depende de este servicio y del servicio de temporizador de SharePoint Windows para replicar los datos de la solución en toda la granja. Si estos servicios no se ejecutan en su conjunto de servidores, es posible que deba implementar la licencia por separado en cada servidor.

{{% /alert %}}
