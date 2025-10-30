---
title: Cómo establecer la propiedad AutoRecuperar del libro de trabajo con Golang vía C++
linktitle: Cómo establecer la propiedad AutoRecover del Libro de trabajo
type: docs
weight: 220
url: /es/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Aprende cómo habilitar o deshabilitar la propiedad AutoRecover de un libro de trabajo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para establecer la propiedad AutoRecover de un libro de trabajo. El valor predeterminado de esta propiedad es **true**. Cuando lo configuras a **false** en un libro de trabajo, Microsoft Excel deshabilita AutoRecover (Autosave) en ese archivo de Excel.

Aspose.Cells proporciona la propiedad [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) para habilitar o deshabilitar esta opción.

{{% /alert %}}

El siguiente código explica cómo usar la propiedad [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad, que es **true**, luego lo establece en **false** y guarda el libro de trabajo. Luego lee el libro de trabajo nuevamente y obtiene el valor de esta propiedad, que en ese momento es **false**.

## Código C++ para establecer la propiedad AutoRecover del Libro de trabajo

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Salida**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
