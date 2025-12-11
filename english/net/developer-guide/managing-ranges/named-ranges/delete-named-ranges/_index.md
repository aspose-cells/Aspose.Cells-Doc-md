---  
title: Delete Named Ranges  
type: docs  
weight: 90  
url: /net/Delete-named-ranges/  
description: You can learn how to remove defined names or named ranges from Excel or OpenOffice files with Aspose.Cells for .NET.  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**  
If there are too many defined names or named ranges in Excel files, we have to clear some because they are not referenced again.  

## **Remove Named Range in MS Excel**  

To remove a named range from Excel, you can follow these steps:  
1. Open Microsoft Excel and open the workbook that contains the named range.  
2. Go to the **Formulas** tab in the Excel ribbon.  
3. Click on the **Name Manager** button in the **Defined Names** group. This will open the Name Manager dialog box.  
4. In the Name Manager dialog box, select the named range you want to remove.  
5. Click on the **Delete** button. Confirm the deletion when prompted.  
6. Click on the **Close** button to close the Name Manager dialog box.  
7. Save the workbook to retain the changes.  


## **Delete Named Ranges using Aspose.Cells for .NET**  
With Aspose.Cells for .NET, you can remove named ranges or defined names by **text** or **index** in the list.  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}  

**Note:** If the defined name is referenced by formulas, it cannot be removed. You can only remove the formula of the defined name.  

## **Removing Some Named Ranges**  
When we remove a defined name, we have to check whether it is referenced by any formulas in the file.  
In order to improve performance of removing named ranges, we can remove several together.  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}  

## **Remove Duplicate Defined Names**  
Some Excel files become corrupt because some defined names are duplicated. So we can remove these duplicate names to repair the file.  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}  



{{< app/cells/assistant language="csharp" >}}
