--- 
title: How to Check Frozen State without Excel with Golang via C++ 
linktitle: Frozen State 
type: docs 
weight: 190 
url: /go-cpp/how-to-check-frozen-state-of-excel-worksheet 
description: In this article, you will learn how to check the frozen state of an Excel worksheet programmatically using C++ with the Aspose.Cells API. 
--- 

## **Introduction** 

In this article, we will learn how to check the frozen state of an Excel worksheet programmatically. We can simply determine whether the worksheet is frozen or split in MS Excel. But is there a way to determine whether it is frozen or split using C++? We can accomplish this with Aspose.Cells for Go via C++. 

## **Are Window Panes Frozen?** 
With Aspose.Cells for Go via C++, we can check whether the window is frozen and how many rows and columns are locked. 

Please use the [**GetPaneState()**](https://reference.aspose.com/cells/go-cpp/worksheet/getpanestate/) property to check the state of window panes and to get locked rows and columns with the [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/go-cpp/worksheet/getfreezedpanes/) method. 
1. Construct a Workbook to open the file.  
2. Check whether the worksheet is frozen.  
3. Get the locked rows and columns.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FrozenState.go" >}} 

{{< app/cells/assistant language="go" >}}
