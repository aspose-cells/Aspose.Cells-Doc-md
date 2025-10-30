---
title: Implementera fel och boolean värden på ryska eller annat språk med Golang via C++
linktitle: Implementera Fel och Boolean Värde
type: docs
weight: 40
url: /sv/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Lär dig hur du implementerar fel och boolean värden på ryska eller annat språk med Aspose.Cells med Golang via C++.
---

## **Möjliga användningsscenario**

Om du använder Microsoft Excel på rysk lokalitet eller språk eller något annat, kommer den att visa fel och booleanvärden enligt den lokalen eller språket. Du kan åstadkomma liknande beteende med Aspose.Cells genom att använda [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/) egenskapen. Du måste åsidosätta följande metoder i [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **Implementera fel och booleska värden på ryska eller något annat språk**

Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Kontrollera den [Exempel Excel-filen](73990159.xlsx) som används i denna kod och dess [Utdata-PDF](73990160.pdf). Skärmbilden visar skillnaden mellan Exempel Excel-filen och Utdata-PDF för referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
