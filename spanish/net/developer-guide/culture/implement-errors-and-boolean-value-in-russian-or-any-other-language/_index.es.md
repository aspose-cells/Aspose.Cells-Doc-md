---
title: Implementar Errores y Valor Booleano en Ruso u Otro Idioma
type: docs
weight: 40
url: /es/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Escenarios de uso posibles**

Si está usando Microsoft Excel en un entorno de idioma ruso o de cualquier otro idioma, mostrará Errores y valores Booleanos de acuerdo con ese idioma. Puede lograr un comportamiento similar usando Aspose.Cells mediante el uso de la propiedad [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Deberá anular los siguientes métodos de la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Implementar Errores y Valor Booleano en Ruso u Otro Idioma**

El siguiente código de ejemplo ilustra cómo implementar Errores y Valor Booleano en Ruso u Otro Idioma. Por favor revise el [archivo de Excel de muestra](73990159.xlsx) usado en este código y su [PDF de salida](73990160.pdf). La captura de pantalla muestra la diferencia entre el archivo de Excel de muestra y el PDF de salida para referencia.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
{{< app/cells/assistant language="csharp" >}}
