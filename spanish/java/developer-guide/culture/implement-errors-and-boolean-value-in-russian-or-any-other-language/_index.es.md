---
title: Implementar errores y valor booleano en ruso o cualquier otro idioma
type: docs
weight: 30
url: /es/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Posibles escenarios de uso**
 Si está utilizando Microsoft Excel en la configuración regional o el idioma ruso o cualquier otra configuración regional o idioma, mostrará errores y valores booleanos de acuerdo con esa configuración regional o idioma. Puede lograr un comportamiento similar utilizando Aspose.Cells[Libro de trabajo.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) método o propiedad. Tendrá que anular los siguientes métodos de[Configuración de globalización](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)clase.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implementar errores y valor booleano en ruso o cualquier otro idioma**
 El siguiente código de ejemplo ilustra cómo implementar errores y valores booleanos en ruso o en cualquier otro idioma. Verifique el archivo Excel de muestra utilizado en este código y su PDF de salida. La captura de pantalla muestra la diferencia entre[Ejemplo de archivo de Excel](48496697.xlsx) y el[PDF de salida](48496696.pdf) para una referencia.

![todo:imagen_alternativa_texto](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
