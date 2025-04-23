---
title: Verifique si el proyecto VBA en un Libro de Trabajo está firmado
type: docs
weight: 70
url: /es/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Puedes verificar si tu proyecto VBA está firmado o no utilizando Microsoft Excel a través del menú **Herramientas > Firmas Digitales...**. Del mismo modo, puedes verificarlo programáticamente utilizando la propiedad [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) de Aspose.Cells.

{{% /alert %}}

## **Verifica si el proyecto VBA en un libro está firmado en C#**

El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado utilizando la propiedad [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned). La propiedad devolverá **verdadero** si el proyecto está firmado, de lo contrario devolverá **falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
