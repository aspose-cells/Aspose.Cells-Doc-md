---
title: Determinar si la licencia se cargó correctamente
type: docs
weight: 260
url: /es/net/determining-if-the-license-is-loaded-successfully/
description: Aprenda cómo Detectar si la Licencia se cargó correctamente a través de las API Aspose.Cells for NET.
keywords: Cómo Detectar si la Licencia se cargó correctamente en C#, Determinar si la Licencia se cargó correctamente usando C#, Verificar si la Licencia se cargó correctamente a través de C#, comprobar el estado de la licencia.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la propiedad [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) que puede usar para determinar si la licencia se cargó correctamente o no. Si accede a esta propiedad antes de establecer la licencia, devolverá **falso**, y si llama a esta propiedad después de establecer la licencia, devolverá **verdadero**, lo que indica que la licencia se ha cargado correctamente.

{{% /alert %}}

## Código de C# para determinar si la Licencia se cargó correctamente

El siguiente código accede a la propiedad [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) antes de establecer una licencia y devuelve **falso**. Luego carga la licencia y accede a la propiedad nuevamente, que ahora devuelve **verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Salida de la consola**

Aquí está la salida de consola (depuración) del código de ejemplo anterior

{{< highlight java >}}

False

True

{{< /highlight >}}
