---
title: Compruebe el formato de número personalizado al configurar el estilo. Propiedad personalizada
type: docs
weight: 170
url: /es/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Posibles escenarios de uso**

 Si asigna un formato de número personalizado no válido a[**Estilo personalizado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)property, entonces Aspose.Cells no arrojará ninguna excepción. Pero si desea que Aspose.Cells verifique si el formato de número personalizado asignado es válido o no, configure el[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propiedad a**verdadero**.

## **Compruebe el formato de número personalizado al establecer la propiedad Style.Custom**

 El siguiente código de ejemplo asigna un formato de número personalizado no válido a[**Estilo personalizado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propiedad. Desde entonces, ya hemos establecido[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propiedad a**verdadero**, por lo tanto, arroja una excepción, por ejemplo, formato de número no válido. Lea los comentarios dentro del código para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
