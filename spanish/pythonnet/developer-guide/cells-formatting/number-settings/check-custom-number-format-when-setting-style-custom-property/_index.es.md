---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo, que soporta verificar formatos de números personalizados al aplicar estilos. Este artículo mostrará cómo usar la biblioteca Aspose.Cells para verificar formatos de números personalizados y asegurar que el estilo sea correcto.
keywords: Aspose.Cells, bibliotecas de Python, hojas de cálculo, estilos, formato de números personalizado, verificación, validación
type: docs
weight: 170
url: /es/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asigna un formato de número personalizado no válido a la propiedad [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom), entonces Aspose.Cells no lanzará ninguna excepción. Pero si desea que Aspose.Cells compruebe si el formato de número personalizado asignado es válido o no, entonces configure la propiedad [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) a **true**.

## **Comprobar formato de número personalizado al establecer la propiedad Personalizada de Estilo**

El siguiente código de muestra asigna un formato de número personalizado no válido a la propiedad [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Dado que ya hemos establecido la propiedad [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) a **true**, lanza una excepción, por ejemplo, Formato de número no válido. Por favor lea los comentarios dentro del código para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

