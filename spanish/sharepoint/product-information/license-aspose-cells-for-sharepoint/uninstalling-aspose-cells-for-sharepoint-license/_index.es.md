---
title: Desinstalación de la licencia Aspose.Cells for SharePoint
type: docs
weight: 30
url: /es/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Para desinstalar la licencia Aspose.Cells for SharePoint, utilice los siguientes pasos desde la consola del servidor. 

{{% /alert %}} 

1. Retraiga la solución de la licencia de la granja:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Ejecute trabajos administrativos programados para completar la retracción inmediatamente:
   stsadm.exe -o execadmsvcjobs
1. Espere a que se complete la retracción.
   Puede usar la Administración Central para verificar si la retracción ha sido completada yendo a **Administración Central**, luego **Operaciones** y **Administración de soluciones**.
1. Elimine la solución de la tienda de soluciones de SharePoint:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
