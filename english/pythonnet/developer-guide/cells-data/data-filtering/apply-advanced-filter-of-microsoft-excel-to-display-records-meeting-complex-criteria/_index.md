---
title: Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria
type: docs
weight: 280
url: /python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Learn how to apply advanced filter of microsoft excel to display records meeting complex criteria by using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Apply Advanced Filter, Python Set Advanced Filter, Python Add Advanced Filter, Python Create Advanced Filter, How to add Advanced Filter to a range using Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to apply *Advanced Filter* on worksheet data to display records that meet complex criteria. You can apply Advanced Filter with Microsoft Excel via its *Data > Advanced* command as shown in this screenshot.

![todo:image_alt_text](1.png)

Aspose.Cells for Python via .NET also allows you to apply the Advanced Filter using the [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool) method. Just like Microsoft Excel, it accepts the following parameters.

**isFilter**

Indicates whether filtering the list in place.

**listRange**

The list range.

**criteriaRange**

The criteria range.

**copyTo**

The range where copying data to.

**uniqueRecordOnly**

Only displaying or copying unique rows.

## **Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria**

The following sample code applies the advanced filter on the [Sample Excel File](48496692.xlsx) and generates the [Output Excel File](48496691.xlsx). The screenshot shows both files for comparison. As you can see inside the screenshot, data has been filtered inside the output Excel file according to complex criteria.

![todo:image_alt_text](2.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
{{< app/cells/assistant language="python-net" >}}
