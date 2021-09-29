---
title: Implement Errors and Boolean Value in Russian or Any Other Language
type: docs
weight: 30
url: /java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Possible Usage Scenarios**
If you are using Microsoft Excel in Russian Locale or Language or any other Locale or Language, it will display Errors and Boolean values according to that Locale or Language. You can achieve similar behavior by using Aspose.Cells [Workbook.getSettings().setGlobalizationSettings()](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) method or property. You will have to override the following methods of [GlobalizationSettings](https://apireference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) class.

- [GlobalizationSettings.getErrorValueString()](https://apireference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://apireference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implement Errors and Boolean Value in Russian or Any Other Language**
The following sample code illustrates how to implement Errors and Boolean Value in Russian or Any Other Language. Please check the Sample Excel File used in this code and its Output PDF. The screenshot shows the difference between [Sample Excel File](48496697.xlsx) and the [Output PDF](48496696.pdf) for a reference.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
