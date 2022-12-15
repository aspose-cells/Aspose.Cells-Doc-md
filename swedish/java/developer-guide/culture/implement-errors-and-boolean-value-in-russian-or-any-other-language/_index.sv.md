---
title: Implementera fel och booleskt värde på ryska eller något annat språk
type: docs
weight: 30
url: /sv/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Möjliga användningsscenarier**
 Om du använder Microsoft Excel i ryska språket eller språket eller något annat språk, kommer det att visa fel och booleska värden enligt det språket eller språket. Du kan uppnå liknande beteende genom att använda Aspose.Cells[Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) metod eller egenskap. Du måste åsidosätta följande metoder för[Globaliseringsinställningar](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)klass.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implementera fel och booleskt värde på ryska eller något annat språk**
 Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Kontrollera exemplet på Excel-filen som används i den här koden och dess utdata-PDF. Skärmdumpen visar skillnaden mellan[Exempel på Excel-fil](48496697.xlsx) och den[Utdata PDF](48496696.pdf) för en referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
