---
title: Detectar si la hoja de trabajo está protegida con contraseña
type: docs
weight: 360
url: /es/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Es posible proteger los libros y las hojas de trabajo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas de trabajo protegidas con contraseña; sin embargo, la hoja de cálculo en sí puede estar protegida o no. Aspose.Cells Las API proporcionan los medios para detectar si una hoja de trabajo determinada está protegida con contraseña o no. Este artículo demuestra el uso de Aspose.Cells for .NET API para lograr lo mismo.

{{% /alert %}}

 Aspose.Cells for .NET 8.7.0 ha expuesto el[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) propiedad para detectar si una hoja de trabajo está protegida con contraseña o no. tipo booleano[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) devoluciones de propiedad**verdadero** si[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) está protegido por contraseña y**falso** si no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
