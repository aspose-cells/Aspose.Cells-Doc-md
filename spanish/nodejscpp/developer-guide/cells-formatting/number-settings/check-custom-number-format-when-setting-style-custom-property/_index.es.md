---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom
linktitle: Verificar formato de número personalizado al establecer la propiedad Style.Custom
description: Aspose.Cells es una biblioteca para Node.js para trabajar con archivos de hoja de cálculo, que soporta verificar formatos de número personalizados al aplicar estilos. Este artículo te mostrará cómo usar la biblioteca Aspose.Cells para comprobar formatos de número personalizados y asegurar que el estilo sea correcto.
keywords: Aspose.Cells, bibliotecas de Node.js, hojas de cálculo, estilos, formatos de número personalizados, verificación, validación
type: docs
weight: 170
url: /es/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asignas un formato de número personalizado inválido al método [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-), entonces Aspose.Cells for Node.js via C++ no lanzará ninguna excepción. Pero si quieres que Aspose.Cells verifique si el formato asignado es válido o no, configura el método [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) a **true**.

## **Verificar formato de número personalizado al establecer el método Style.setCustom(string)**

El siguiente código de ejemplo asigna un formato de número personalizado inválido al método [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-). Como ya configuramos el método [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) a **true**, lanza una excepción, por ejemplo Formato de número inválido. Revisa los comentarios en el código para más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
