---
title: Populate Data First by Row then by Column
type: docs
weight: 10
url: /net/populate-data-first-by-row-then-by-column/
---

{{% alert color="primary" %}} 

Populating a spreadsheet with data first by row and then by column improves the overall performance.

{{% /alert %}} 

Putting data in the sequence A1, B1, A2, B2 is faster than A1, A2, B1, B2. If there are many cells in a worksheet and you follow the second sequence, that is, you're filling the data row by row, this tip can make the program much faster.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-PopulateDataEfficiently-PopulateDataFirstByRowThenColumns.cs" >}}
