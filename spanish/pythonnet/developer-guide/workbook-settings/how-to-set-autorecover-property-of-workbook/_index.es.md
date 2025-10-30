---
title: Cómo establecer la propiedad AutoRecover del Libro de trabajo
type: docs
weight: 220
url: /es/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para Python via .NET para configurar la propiedad AutoRecover del libro de trabajo. El valor predeterminado de esta propiedad es **true**. Cuando la estableces en **false** en un libro de trabajo, Microsoft Excel desactiva AutoRecover (Autosave) en ese archivo de Excel.

Aspose.Cells para Python via .NET proporciona la propiedad [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) para habilitar o deshabilitar esta opción.

{{% /alert %}}

El siguiente código explica cómo usar la propiedad [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) del libro. El código primero lee el valor predeterminado de esta propiedad, que es **true**, luego lo configura como **false** y guarda el libro. Luego vuelve a leer el libro y obtiene el valor de esta propiedad, que en ese momento es **false**.

## Código C# para establecer la propiedad AutoRecover del Libro de Trabajo

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Salida**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
