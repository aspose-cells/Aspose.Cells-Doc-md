---
title: Determinar si la licencia se cargó correctamente
type: docs
weight: 260
url: /es/net/determining-if-the-license-is-loaded-successfully/
description: Aprenda a detectar si la licencia se cargó correctamente a través de Aspose.Cells para las API NET.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**Libro de trabajo. Tiene licencia**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propiedad que puede utilizar para determinar si la licencia se cargó correctamente o no. Si accede a esta propiedad antes de configurar la licencia, le devolverá**FALSO** y si llama a esta propiedad después de configurar la licencia, volverá**verdadero** indicando que la licencia se ha cargado exitosamente.

{{% /alert %}}

##  Código C# para determinar si la licencia se cargó correctamente

 El siguiente código accede al[**Libro de trabajo. Tiene licencia**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)propiedad antes de establecer una licencia y devuelve *falso**. Luego carga la licencia y accede nuevamente a la propiedad, que ahora devuelve *verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Salida de consola**

Aquí está el resultado de la consola (depuración) del código de muestra anterior.

{{< highlight "java" >}}

False

True

{{< /highlight >}}
