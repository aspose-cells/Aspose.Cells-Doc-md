---
title: Determinar si la licencia se cargó correctamente
type: docs
weight: 260
url: /es/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propiedad que puede utilizar para determinar si la licencia se carga correctamente o no. Si accede a esta propiedad antes de establecer la licencia, devolverá**falso** si llamará a esta propiedad después de establecer la licencia, devolverá**verdadero** indicando que la licencia se ha cargado con éxito.

{{% /alert %}}

## C# código para determinar si la Licencia se cargó correctamente

 El siguiente código accede a la[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) propiedad antes de establecer una licencia y vuelve**falso** . Luego carga la licencia y accede nuevamente a la propiedad que ahora regresa**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Salida de consola**

Aquí está la salida de la consola (depuración) del código de muestra anterior

{{< highlight "java" >}}

False

True

{{< /highlight >}}
