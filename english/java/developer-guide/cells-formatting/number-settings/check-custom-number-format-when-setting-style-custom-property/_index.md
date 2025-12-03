---
title: Check Custom Number Format when Setting Style.Custom Property
type: docs
weight: 160
url: /java/check-custom-number-format-when-setting-style-custom-property/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you assign invalid custom number format to [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style##setCustom-java.lang.String-) property then Aspose.Cells will not throw any exception. But if you want that Aspose.Cells should check if the assigned custom number format is valid or not then please set the [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#setCheckCustomNumberFormat-boolean-) property to **true**.

## **Check the Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#setCustom-java.lang.String-) property. Since we have already set [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#setCheckCustomNumberFormat-boolean-) property to **true**, therefore the API will throw  CellsException e.g. *Invalid number format*.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
{{< app/cells/assistant language="java" >}}
