---
title: Delete Named Ranges
type: docs
weight: 90
url: /net/Delete-named-ranges/
description: You can learn how to remove defined names or named ranges from Excel or OpenOffice files with Aspose.Cells for .Net .
---

## **Introduction**
If there are too many defined names or named ranges in the Excel files, we have to clear some for they are not referred again.

## **Remove Named Range in MS Excel**

To remove a named range from Excel, you can follow these steps:
1. Open Microsoft Excel and open the workbook that contains the named range.
2. Go to the "Formulas" tab in the Excel ribbon.
3. Click on the "Name Manager" button in the "Defined Names" group. This will open the Name Manager dialog box.
4. In the Name Manager dialog box, select the named range you want to remove.
5. Click on the "Delete" button. Confirm the deletion when prompted.
6. Click on the "Close" button to close the Name Manager dialog box.
7. Save the workbook to retain the changes.


## **Deletes Named Range using Aspose.Cells for .Net **
With Aspose.Cells for .Net, you can remove named ranges or defined names by [text](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove)  or [index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) in the list.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Note: if the defined name is referred by formulas, it could not be removed . We only can remove formula of the defined name.

## **Removes Some Named Ranges**
When we remove a defined name, we have to check whether it is referred by all formulas in the file.
In order to improve peformance of removing named ranges,we can remove some together.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

## **Remove Duplicate Defined Names**
Some Excel fiels corrupt because some defined names are duplicate. So we can remove these duplicate names to repair the file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



