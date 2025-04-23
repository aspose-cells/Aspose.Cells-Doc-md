---
title: Especificar Separadores de Números Decimales y de Grupo Personalizados para Libro de Trabajo
linktitle: Especificar Separadores de Números Decimales y de Grupo Personalizados para Libro de Trabajo
type: docs
weight: 110
url: /es/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cambiar los separadores decimales y de agrupación en números en Excel usando Aspose.Cells for Node.js via C++. 
keywords: especificar separador decimal personalizado en Excel Node.js vía C++, especificar separador de grupo personalizado en Excel Node.js vía C++, cambiar separador decimal y de grupo en Excel Node.js vía C++
---

{{% alert color="primary" %}}

En Microsoft Excel, puedes especificar los Separadores de Decimales y Miles Personalizados en lugar de usar Separadores de Sistema de las **Opciones Avanzadas de Excel** como se muestra en la captura de pantalla a continuación.

Aspose.Cells proporciona los métodos [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) y [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) para establecer los separadores personalizados para formatear/parsing de números.

{{% /alert %}}

## **Especificar Separadores Personalizados usando Microsoft Excel**

La siguiente captura de pantalla muestra las **Opciones Avanzadas de Excel** y destaca la sección para especificar los **Separadores Personalizados**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Especificando separadores personalizados usando Aspose.Cells for Node.js via C++**

El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados utilizando la API de Aspose.Cells. Especifica los Separadores de Decimal y Grupo Personalizados como punto y espacio, respectivamente.

### Código en Node.js para especificar separadores decimales y de grupo personalizados en números

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


