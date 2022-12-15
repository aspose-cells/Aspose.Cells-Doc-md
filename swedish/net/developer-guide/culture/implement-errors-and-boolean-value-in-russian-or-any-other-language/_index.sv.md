---
title: Implementera fel och booleskt värde på ryska eller något annat språk
type: docs
weight: 40
url: /sv/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Möjliga användningsscenarier**

Om du använder Microsoft Excel i ryska språket eller språket eller något annat språk, kommer det att visa fel och booleska värden enligt det språket eller språket. Du kan uppnå ett liknande beteende med Aspose.Cells genom att använda**[Arbetsbok.Inställningar.Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) egendom. Du måste åsidosätta följande metoder för[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Implementera fel och booleskt värde på ryska eller något annat språk**

 Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Vänligen kontrollera[Exempel på Excel-fil](73990159.xlsx) används i denna kod och dess[Utdata PDF](73990160.pdf)Skärmdumpen visar skillnaden mellan Exempel Excel-fil och utdata-PDF som referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
