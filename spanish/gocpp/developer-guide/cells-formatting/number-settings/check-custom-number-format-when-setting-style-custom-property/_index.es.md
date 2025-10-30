---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom con Golang a través de C++
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo, que soporta verificar formatos de número personalizados al aplicar estilos. Este artículo mostrará cómo usar la biblioteca Aspose.Cells para verificar formatos de número personalizados y asegurar que el estilo sea correcto.
keywords: Aspose.Cells, bibliotecas C++, hojas de cálculo, estilos, formato de número personalizado, verificación, validación
type: docs
weight: 170
url: /es/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asignas un formato de número personalizado inválido a la propiedad [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/), Aspose.Cells no lanzará ninguna excepción. Pero si deseas que Aspose.Cells verifique si el formato de número personalizado asignado es válido o no, configura la propiedad [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) en **true**.

## **Comprobar formato de número personalizado al establecer la propiedad Personalizada de Estilo**

El siguiente código de ejemplo asigna un formato de número personalizado inválido a la propiedad [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/). Dado que ya configuramos la propiedad [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) en **true**, lanzará una excepción, por ejemplo, Formato de número inválido. Lee los comentarios dentro del código para más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
