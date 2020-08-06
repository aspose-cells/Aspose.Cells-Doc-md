---
title: Populate Data First by Row then by Column
type: docs
weight: 10
url: /java/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}} 

Populating a spreadsheet with data first by row and then by column improves the overall performance.

{{% /alert %}} 
### **Example**
Putting data in the sequence A1, B1, A2, B2 is faster than A1, A2, B1, B2. If there are many cells in a worksheet and you follow the second sequence, that is, you're filling the data row by row, this tip can make the program much faster.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-PopulateDatabyRowthenColumn-PopulateDatabyRowthenColumn.java" >}}
