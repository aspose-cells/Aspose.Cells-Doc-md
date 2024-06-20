---
title: Implementar Errores y Valor Booleano en Ruso u Otro Idioma
type: docs
weight: 30
url: /es/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Escenarios de uso posibles**
Si está utilizando Microsoft Excel en la configuración regional o idioma ruso u otro idioma, mostrará Errores y Valores Booleanos según esa configuración regional o idioma. Puede lograr un comportamiento similar utilizando el método o propiedad [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) de Aspose.Cells. Deberá sobrescribir los siguientes métodos de la clase [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implementar Errores y Valor Booleano en Ruso u Otro Idioma**
El siguiente código de muestra ilustra cómo implementar Errores y Valor Booleano en Ruso u Otro Idioma. Por favor, revise el Archivo de Excel de muestra utilizado en este código y su PDF de salida. La captura de pantalla muestra la diferencia entre el [Archivo de Excel de muestra](48496697.xlsx) y el [PDF de salida](48496696.pdf) como referencia.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
