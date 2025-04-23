---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo, que admite la verificación de formatos de número personalizados al aplicar estilos. Este artículo le mostrará cómo utilizar la biblioteca Aspose.Cells para verificar formatos de número personalizados y asegurarse de que el estilo sea correcto.
keywords: Aspose.Cells, bibliotecas NET, hojas de cálculo, estilos, formato de números personalizado, comprobación, validación
type: docs
weight: 170
url: /es/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asigna un formato de número personalizado no válido a la propiedad [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom), entonces Aspose.Cells no lanzará ninguna excepción. Pero si desea que Aspose.Cells compruebe si el formato de número personalizado asignado es válido o no, entonces configure la propiedad [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) a **true**.

## **Comprobar formato de número personalizado al establecer la propiedad Personalizada de Estilo**

El siguiente código de muestra asigna un formato de número personalizado no válido a la propiedad [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). Dado que ya hemos establecido la propiedad [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) a **true**, lanza una excepción, por ejemplo, Formato de número no válido. Por favor lea los comentarios dentro del código para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
{{< app/cells/assistant language="csharp" >}}
