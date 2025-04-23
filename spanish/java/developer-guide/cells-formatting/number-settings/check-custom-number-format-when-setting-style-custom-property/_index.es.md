---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom
type: docs
weight: 160
url: /es/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asigna un formato de número personalizado no válido a la propiedad [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom), Aspose.Cells no lanzará ninguna excepción. Pero si desea que Aspose.Cells verifique si el formato de número personalizado asignado es válido o no, establezca la propiedad [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) en **true**.

## **Verificar el formato de número personalizado al establecer la propiedad Style.Custom**

El siguiente código de muestra asigna un formato de número personalizado no válido a la propiedad [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Dado que ya hemos establecido la propiedad [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) en **true**, por lo tanto, la API lanzará CellsException por ejemplo *Formato de número no válido*.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
{{< app/cells/assistant language="java" >}}
