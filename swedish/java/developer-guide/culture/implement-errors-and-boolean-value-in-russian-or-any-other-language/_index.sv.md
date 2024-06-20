---
title: Implementera fel och booleska värden på ryska eller något annat språk
type: docs
weight: 30
url: /sv/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Möjliga användningsscenario**
Om du använder Microsoft Excel på rysk lokal eller språk eller någon annan lokal eller språk, kommer den att visa fel och booleska värden enligt den lokalen eller språket. Du kan uppnå liknande beteende genom att använda metoden eller egenskapen [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) i Aspose.Cells. Du måste åsidosätta följande metoder i klassen [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implementera fel och booleska värden på ryska eller något annat språk**
Följande exempelkod visar hur man implementerar fel och booleska värden på ryska eller något annat språk. Vänligen kontrollera den provexcelfil som används i denna kod och dess utdatapdf. Skärmbilden visar skillnaden mellan [provexcelfil](48496697.xlsx) och [utdatapdf](48496696.pdf) för referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
