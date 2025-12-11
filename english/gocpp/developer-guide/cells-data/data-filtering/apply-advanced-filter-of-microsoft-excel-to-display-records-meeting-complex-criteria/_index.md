---
title: Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria with Golang via C++
linktitle: Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria
type: docs
weight: 280
url: /go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Learn how to apply the advanced filter of Microsoft Excel to display records meeting complex criteria by using the Aspose.Cells for C++ API.
keywords: Apply Advanced Filter, Set Advanced Filter, Add Advanced Filter, Create Advanced Filter, How to add Advanced Filter to a range
---

## **Possible Usage Scenarios**

Microsoft Excel allows you to apply *Advanced Filter* on worksheet data to display records that meet complex criteria. You can apply Advanced Filter with Microsoft Excel via its *Data > Advanced* command as shown in this screenshot.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells also allows you to apply the Advanced Filter using the [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/) method. Like Microsoft Excel, it accepts the following parameters.

**isFilter**  
Indicates whether to filter the list in place.

**listRange**  
The list range.

**criteriaRange**  
The criteria range.

**copyTo**  
The range to which data will be copied.

**uniqueRecordOnly**  
Specifies whether to display or copy only unique rows.

## **Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria**

The following sample code applies the advanced filter to the [Sample Excel File](48496692.xlsx) and generates the [Output Excel File](48496691.xlsx). The screenshot shows both files for comparison. As you can see in the screenshot, the data has been filtered in the output Excel file according to complex criteria.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}