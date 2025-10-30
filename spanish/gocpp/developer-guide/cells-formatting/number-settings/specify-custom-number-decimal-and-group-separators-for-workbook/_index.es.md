---
title: Especificar separadores decimales y de grupo de números personalizados para libro de trabajo con Golang a través de C++
linktitle: Especificar separadores personalizados de decimales y agrupación
type: docs
weight: 110
url: /es/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cambiar el separador decimal y de grupo en números en MS Excel y con Golang a través de C++ usando la API de Aspose.Cells for C++.
keywords: especificar separador decimal personalizado en excel, especificar separador decimal personalizado en excel c++, especificar separador de grupo personalizado en excel, especificar separador de grupo personalizado en excel c++, especificar separador decimal y de grupo personalizados en excel, especificar separador decimal y de grupo en excel c++, cambiar separador decimal en excel, cambiar separador de grupo en excel, cambiar separador decimal en excel c++, cambiar separador de grupo en excel c++
---

{{% alert color="primary" %}}

En Microsoft Excel, puedes especificar los Separadores de Decimales y Miles Personalizados en lugar de usar Separadores de Sistema de las **Opciones Avanzadas de Excel** como se muestra en la captura de pantalla a continuación.

Aspose.Cells proporciona las propiedades [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) y [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) para establecer los separadores personalizados para el formato/análisis de números.

{{% /alert %}}

## **Especificar Separadores Personalizados usando Microsoft Excel**

La siguiente captura de pantalla muestra las **Opciones Avanzadas de Excel** y destaca la sección para especificar los **Separadores Personalizados**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Especificar Separadores Personalizados usando Aspose.Cells**

El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados utilizando la API de Aspose.Cells. Especifica los Separadores de Decimal y Grupo Personalizados como punto y espacio, respectivamente.

### Código en C++ para especificar separadores personalizados de decimal y grupo

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
