---
title: Detectar si la hoja de cálculo está protegida con contraseña
type: docs
weight: 280
url: /es/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Es posible proteger los libros y las hojas de cálculo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas de cálculo protegidas por contraseña, sin embargo, la hoja de cálculo en sí puede o no estar protegida. Las API de Aspose.Cells proporcionan los medios para detectar si una hoja de cálculo dada está protegida por contraseña o no. Este artículo demuestra el uso de la API Aspose.Cells for Java para lograr lo mismo.

{{% /alert %}}

## **Detectar si la hoja de cálculo está protegida con contraseña**

Aspose.Cells for Java 8.7.0 ha expuesto la propiedad [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) para detectar si una hoja de cálculo está protegida por contraseña o no. El campo de tipo Boolean [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) devuelve **verdadero** si [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) está protegida por contraseña y **falso** si no lo está.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
{{< app/cells/assistant language="java" >}}
