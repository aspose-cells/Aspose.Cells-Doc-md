---
title: Implementera fel och booleska värden på ryska eller något annat språk
type: docs
weight: 40
url: /sv/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Möjliga användningsscenario**

Om du använder Microsoft Excel på ryskt språk eller något annat språk eller plats visar det fel och booleska värden enligt det språket eller platsen. Du kan uppnå en liknande funktion med Aspose.Cells genom att använda [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) egenskapen. Du måste åsidosätta följande metoder i [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klass.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Implementera fel och booleska värden på ryska eller något annat språk**

Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Kontrollera den [Exempel Excel-filen](73990159.xlsx) som används i denna kod och dess [Utdata-PDF](73990160.pdf). Skärmbilden visar skillnaden mellan Exempel Excel-filen och Utdata-PDF för referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
