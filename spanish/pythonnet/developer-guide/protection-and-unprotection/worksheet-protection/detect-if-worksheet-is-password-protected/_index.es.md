---
title: Detectar si la hoja de cálculo está protegida con contraseña
type: docs
weight: 360
url: /es/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Es posible proteger los libros y las hojas de cálculo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas protegidas por contraseña, sin embargo, el libro en sí puede estar protegido o no. Las APIs de Aspose.Cells para Python via .NET proporcionan los medios para detectar si una hoja de cálculo dada está protegida por contraseña o no. Este artículo demuestra el uso de la API Aspose.Cells para Python via .NET para lograr lo mismo.

{{% /alert %}}

Aspose.Cells para Python via .NET ha expuesto la propiedad [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) para detectar si una hoja de cálculo está protegida por contraseña o no. La propiedad booleana [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) devuelve **true** si [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) está protegida por contraseña y **false** si no.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

