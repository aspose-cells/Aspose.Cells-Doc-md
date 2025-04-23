---
title: Verifique si el proyecto VBA en un Libro de Trabajo está firmado
type: docs
weight: 70
url: /es/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Puede verificar si su proyecto VBA está firmado o no usando Microsoft Excel a través del comando de menú **Herramientas > Firmas digitales...**. De manera similar, puede verificarlo programáticamente usando Aspose.Cells para Python via .NET propiedad [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed).

{{% /alert %}}

## **Verificar si el proyecto VBA en un Libro de Excel está firmado en Python**

El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado utilizando la propiedad [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed). La propiedad devolverá **verdadero** si el proyecto está firmado, de lo contrario devolverá **falso**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

