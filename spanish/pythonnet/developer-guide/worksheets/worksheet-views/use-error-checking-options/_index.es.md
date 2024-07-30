---
title: Usar opciones de verificación de errores
type: docs
weight: 140
url: /es/python-net/use-error-checking-options/
description: En este artículo, encontrarás código de ejemplo que utilizará opciones de revisión de errores de las hojas de cálculo de Excel, como números almacenados como texto, utilizando la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Almacenar números como texto en Excel en Python, Cómo manejar opciones de revisión de errores en Excel en Python.
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios definir opciones y reglas de verificación de errores. Los usuarios a menudo ven verificaciones de errores al crear fórmulas, un pequeño triángulo en la esquina superior derecha de una celda resalta cuando hay un problema con una celda. Excel proporciona información que ayuda a los usuarios a corregir problemas comunes.

{{% /alert %}}

## **Tipos de Errores**

Errores que significan que la fórmula no puede devolver un resultado, como dividir un número por cero, requieren atención inmediata y se muestra un valor de error en la celda. Al hacer clic en el triángulo verde se muestra un signo de exclamación, al hacer clic en esto se abre una lista de opciones.

El error puede resolverse utilizando las opciones, o ignorarse. Ignorar un error significa que ese error no aparecerá en futuras verificaciones de errores.

Aspose.Cells para Python via .NET ofrece funciones de opciones de revisión de errores. La clase [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) gestiona diferentes tipos de revisiones de errores, como números almacenados como texto, errores de cálculo de fórmulas y errores de validación. Utiliza la enumeración [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) para establecer la revisión de errores deseada.

## **Números Almacenados como Texto**

Ocasionalmente, los números pueden formatearse y almacenarse en celdas como texto. Esto puede causar problemas con cálculos o producir órdenes de clasificación confusos. Los números formateados como texto están alineados a la izquierda en lugar de a la derecha en la celda. Si una fórmula que debería realizar una operación matemática en celdas no devuelve un valor, verifica la alineación en las celdas a las que hace referencia la fórmula; algunas o todas esas celdas pueden ser números formateados como texto.

Puedes usar las opciones de verificación de errores para convertir rápidamente los números almacenados como texto en números reales. En Microsoft Excel 2003:

1. En el menú **Herramientas**, haz clic en **Opciones**.
1. Selecciona la pestaña de Revisión de Errores. La opción **Número almacenado como texto** está marcada por defecto.
1. Desactívala.

El siguiente código de ejemplo muestra cómo deshabilitar la opción de revisión de errores de números almacenados como texto para una hoja de cálculo en el archivo XLS de la plantilla utilizando las APIs de Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
