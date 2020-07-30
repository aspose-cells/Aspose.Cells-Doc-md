---
title : "Manipulate Named Range in a Workbook" 
description : "" 
weight : 12034 
toc : false
type: docs
url: /cpp/developerguide/data/manipulate+named+range+in+a+workbook/
---

# Aspose.Cells for C++ : Manipulate Named Range in a Workbook


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Manipulate Named Range in a Workbook](#manipulate-named-range-in-a-workbook)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Aspose.Cells supports the manipulation of existing named ranges. All the existing named ranges can be accessed from [IWorkbook.GetIWorksheets().GetINames()](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_worksheet_collection/#aa9e7bc07917a152a2c0de161cca133fa) collection. Once, you access the named range, you can change its various methods e.g. [GetFullText](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#a5b450ef193365dec035c58280fbe9563) and [GetRefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36).

## Manipulate Named Range in a Workbook

The following sample code reads the first named-range inside the [source excel file](https://docs2.aspose.com/cells/cpp/attachments/22970927/23167008.xlsx) and prints its [FullText](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#a5b450ef193365dec035c58280fbe9563) and [RefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36) properties on the console. After that, it modifies [RefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36) property and saves the [output excel file](https://docs2.aspose.com/cells/cpp/attachments/22970927/23167009.xlsx).

## Sample Code

## Console Output

The following console output prints the values of [FullText](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#a5b450ef193365dec035c58280fbe9563) and [RefersTo](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_name/#afdb10a12d8d395ae81de231f017eba36) members of the existing *Named Range* in the above code.

{{< code lang="cs" >}}
Full Text: TestRange
Refers To: =Sheet1!$D$3:$G$6
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/cpp/images/icons/bullet_blue.gif) [outputManipulateNamedRangeInWorkbook.xlsx](https://docs2.aspose.com/cells/cpp/attachments/22970927/23167009.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/cpp/images/icons/bullet_blue.gif) [sampleManipulateNamedRangeInWorkbook.xlsx](https://docs2.aspose.com/cells/cpp/attachments/22970927/23167008.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

