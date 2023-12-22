---
title: Verifique el formato de número personalizado al configurar el estilo. Propiedad personalizada
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo, que admite la verificación de formatos de números personalizados al diseñar. Este artículo le mostrará cómo utilizar la biblioteca Aspose.Cells para verificar formatos de números personalizados y asegurarse de que el estilo sea correcto.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /es/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Posibles escenarios de uso**

 Si asigna un formato de número personalizado no válido a[**Estilo.Personalizado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propiedad, entonces Aspose.Cells no generará ninguna excepción. Pero si desea que Aspose.Cells verifique si el formato de número personalizado asignado es válido o no, configure el[**Libro de trabajo.Configuración.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propiedad a *verdadero**.

##  **Verifique el formato de número personalizado al configurar la propiedad Style.Custom**

 El siguiente código de muestra asigna un formato de número personalizado no válido a[**Estilo.Personalizado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propiedad. Desde entonces, ya hemos configurado[**Libro de trabajo.Configuración.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propiedad a *true**, por lo tanto arroja una excepción, por ejemplo, formato de número no válido. Lea los comentarios dentro del código para obtener más ayuda.

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
