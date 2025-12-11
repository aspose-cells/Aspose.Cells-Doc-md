---  
title: Find out if VBA Project is Protected with Golang via C++  
linktitle: Find out if VBA Project is Protected  
type: docs  
weight: 20  
url: /go-cpp/find-out-if-vba-project-is-protected/  
description: Check if the VBA project of an Excel file is protected using Aspose.Cells with Golang via C++.  
---  

## **Find out if a VBA Project Is Protected in C++**

You can determine whether the VBA (Visual Basic for Applications) project of your Excel file is protected using Aspose.Cells via the [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) property.

## **Sample Code**

The following sample code creates a workbook and then checks if its VBA project is protected or not. It then protects the VBA project and checks again whether the VBA project is protected. Please see its console output for reference. Before protection, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) returns **false**, but after protection, it returns **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}

## **Console Output**

This is the console output of the above sample code for reference.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}