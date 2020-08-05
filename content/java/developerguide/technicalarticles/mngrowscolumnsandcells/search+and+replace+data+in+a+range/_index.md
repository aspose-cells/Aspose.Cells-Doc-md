---
title : "Search and Replace Data in a Range" 
description : "" 
weight : 16451 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngrowscolumnsandcells/search+and+replace+data+in+a+range/
---

# Aspose.Cells for Java : Search and Replace Data in a Range


Sometimes, you need to search for and replace specific data in a range, ignoring any cell values outside the desired range. Aspose.Cells allows you to limit a search to a specific range. This article explains how.

Aspose.Cells provides the [FindOptions.setRange()](https://apireference.aspose.com/java/cells/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) method for specifying a range when searching for data.

Suppose you want to search for the string **"search"** and replace it with **"replace"** in the range **E3:H6**. In the screenshot below, the string "search" can be seen in several cells but we want to replace it only in a given range, here highlighted in yellow.

**Input file**  
![image](https://docs2.aspose.com/cells/java/attachments/5276684/5472883.png)

After the execution of the code, the output file looks like the below. All "search" strings within the range have been replaced with "replace".

**Output file**  
![image](https://docs2.aspose.com/cells/java/attachments/5276684/5472882.png)


