---
title: Cómo configurar la propiedad Autorrecuperación de Workbook
type: docs
weight: 220
url: /es/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 Puede usar Aspose.Cells para establecer la propiedad Autorrecuperación del libro de trabajo. El valor predeterminado de esta propiedad es**verdadero** . cuando lo configuras**falso** en un libro de trabajo, Microsoft Excel deshabilita la Autorrecuperación (Autoguardado) en ese archivo de Excel.

 Aspose.Cells proporciona[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) propiedad para habilitar o deshabilitar esta opción.

{{% /alert %}}

 El siguiente código explica cómo usar[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) propiedad del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad que es**verdadero** , entonces lo establece como**falso** y guarda el libro de trabajo. Luego lee el libro de trabajo nuevamente y lee el valor de esta propiedad que es**falso** en este momento.

## C# código para establecer la propiedad Autorrecuperación de Workbook

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Producción**

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
