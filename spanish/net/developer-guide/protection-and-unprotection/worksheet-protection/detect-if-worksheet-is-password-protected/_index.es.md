---
title: Detectar si la hoja de cálculo está protegida con contraseña
type: docs
weight: 360
url: /es/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Es posible proteger los libros de trabajo y las hojas de cálculo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas de cálculo que están protegidas con contraseña, sin embargo, la hoja de cálculo en sí puede estar protegida o no. Las API de Aspose.Cells proporcionan los medios para detectar si una determinada hoja de cálculo está protegida con contraseña o no. Este artículo demuestra el uso de la API Aspose.Cells for .NET para lograr lo mismo.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 ha expuesto la propiedad [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) para detectar si una hoja de cálculo está protegida con contraseña o no. La propiedad [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) de tipo booleano retorna **true** si [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) está protegida con contraseña y **false** si no lo está.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
