---
title: Implementar errores y valor booleano en ruso o cualquier otro idioma con Golang a través de C++
linktitle: Implementar errores y valores booleanos
type: docs
weight: 40
url: /es/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aprenda cómo implementar errores y valores booleanos en ruso u otro idioma usando Aspose.Cells con Golang a través de C++
---

## **Escenarios de uso posibles**

Si usas Microsoft Excel en ruso u otro idioma, mostrará errores y valores booleanos según ese idioma. Puedes lograr un comportamiento similar usando Aspose.Cells con la propiedad [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/). Tendrás que sobrescribir los siguientes métodos de la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **Implementar Errores y Valor Booleano en Ruso u Otro Idioma**

El siguiente código de ejemplo ilustra cómo implementar Errores y Valor Booleano en Ruso u Otro Idioma. Por favor revise el [archivo de Excel de muestra](73990159.xlsx) usado en este código y su [PDF de salida](73990160.pdf). La captura de pantalla muestra la diferencia entre el archivo de Excel de muestra y el PDF de salida para referencia.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
