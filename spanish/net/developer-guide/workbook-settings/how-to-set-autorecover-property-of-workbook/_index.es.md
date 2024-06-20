---
title: Cómo establecer la propiedad AutoRecover del Libro de trabajo
type: docs
weight: 220
url: /es/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Puedes utilizar Aspose.Cells para establecer la propiedad AutoRecover del libro de trabajo. El valor predeterminado de esta propiedad es **verdadero**. Cuando la estableces en **falso** en un libro de trabajo, Microsoft Excel deshabilita la recuperación automática (guardado automático) en ese archivo de Excel.

Aspose.Cells proporciona la propiedad [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) para activar o desactivar esta opción.

{{% /alert %}}

El siguiente código explica cómo usar la propiedad [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad, que es **verdadero**, luego lo establece en **falso** y guarda el libro. Luego lee nuevamente el libro y lee el valor de esta propiedad, que es **falso** en este momento.

## Código C# para establecer la propiedad AutoRecover del Libro de Trabajo

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Salida**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
