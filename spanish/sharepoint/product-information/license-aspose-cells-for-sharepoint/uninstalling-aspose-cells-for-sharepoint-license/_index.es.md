---
title: Desinstalar Aspose.Cells para la licencia de SharePoint
type: docs
weight: 30
url: /es/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 Para desinstalar Aspose.Cells para la licencia de SharePoint, siga los pasos a continuación desde la consola del servidor.

{{% /alert %}} 

1. Retire la solución de licencia de la granja:
stsadm.exe -o retractsolution -nombre Aspose.Cells.SharePoint.License.wsp -inmediato
1. Ejecute trabajos del temporizador administrativo para completar la retracción inmediatamente:
 stsadm.exe -o execadmsvcjobs
1. Espere a que se complete la retracción.
 Puede usar Administración central para verificar si la retractación se ha completado yendo a**Administración central** , después**Operaciones** y**Gestión de soluciones**.
1. Quite la solución del almacén de soluciones de SharePoint:
 stsadm.exe -o deletesolution -nombre Aspose.Cells.SharePoint.License.wsp
