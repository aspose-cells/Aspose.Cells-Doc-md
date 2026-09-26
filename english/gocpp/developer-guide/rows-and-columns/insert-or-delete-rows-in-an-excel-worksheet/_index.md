---  
title: Insert or Delete Rows in an Excel Worksheet with Golang via C++  
linktitle: Insert or Delete Rows  
type: docs  
weight: 20  
url: /go-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: This article provides the C++ code to insert and delete rows in an Excel worksheet.  
keywords: c++ insert or delete rows in excel worksheet, c++ insert or delete rows in excel, c++ insert rows in excel, c++ delete rows in excel, insert or delete rows in excel worksheet with c++, insert or delete rows in excel with c++, insert rows in excel with c++, delete rows in excel with c++  
---  

{{% alert color="primary" %}}  

When creating a new worksheet, or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.  

{{% /alert %}}  

Aspose.Cells offers two methods for inserting and deleting rows: [**Cells.InsertRows**](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int_bool/) and [**Cells.DeleteRows**](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int/). These methods are optimized for performance and do the job very quickly.  

To insert or remove a number of rows, we recommend that you use the [**Cells.InsertRows**](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int_bool/) and [**Cells.DeleteRows**](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int/) methods instead of using the [**Cells.InsertRow**](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) or [**DeleteRow**](https://reference.aspose.com/cells/go-cpp/cells/deleterow_int/) methods in a loop.  

Aspose.Cells works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertOrDeleteRowsInAnExcelWorksheet.go" >}}  
{{< app/cells/assistant language="go" >}}
