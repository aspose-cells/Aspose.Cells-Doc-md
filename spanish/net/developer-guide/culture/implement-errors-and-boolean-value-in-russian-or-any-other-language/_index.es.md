---
title: Implementar errores y valor booleano en ruso o cualquier otro idioma
type: docs
weight: 40
url: /es/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Posibles escenarios de uso**

Si está utilizando Microsoft Excel en la configuración regional o el idioma ruso o cualquier otra configuración regional o idioma, mostrará errores y valores booleanos de acuerdo con esa configuración regional o idioma. Puede lograr un comportamiento similar usando Aspose.Cells usando el**[Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) propiedad. Tendrá que anular los siguientes métodos de[**Configuración de globalización**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)clase.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Implementar errores y valor booleano en ruso o cualquier otro idioma**

 El siguiente código de ejemplo ilustra cómo implementar errores y valores booleanos en ruso o en cualquier otro idioma. Por favor, checa el[Ejemplo de archivo de Excel](73990159.xlsx) utilizado en este código y su[Salida PDF](73990160.pdf)La captura de pantalla muestra la diferencia entre el archivo de muestra de Excel y la salida PDF como referencia.

![todo:imagen_alternativa_texto](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
