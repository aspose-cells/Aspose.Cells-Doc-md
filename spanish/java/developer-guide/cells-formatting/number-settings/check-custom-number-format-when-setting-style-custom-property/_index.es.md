---
title: Compruebe el formato de número personalizado al configurar el estilo. Propiedad personalizada
type: docs
weight: 160
url: /es/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Posibles escenarios de uso**

 Si asigna un formato de número personalizado no válido a[**Estilo personalizado**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)property entonces Aspose.Cells no arrojará ninguna excepción. Pero si desea que Aspose.Cells verifique si el formato de número personalizado asignado es válido o no, configure el[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) propiedad a**verdadero**.

## **Compruebe el formato de número personalizado al establecer la propiedad Style.Custom**

 El siguiente código de ejemplo asigna un formato de número personalizado no válido a[**Estilo personalizado**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) propiedad. Como ya hemos establecido[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) propiedad a**verdadero** , por lo tanto, el API arrojará CellsException, por ejemplo*Formato de número no válido*.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
