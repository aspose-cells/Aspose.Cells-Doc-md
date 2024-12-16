---
title: Getting Started
type: docs
weight: 10
url: /go-cpp/getting-started/
description: How to install Aspose Cells for Go via C++ and create a Hello World application.
---

{{% alert color="primary" %}}

This page will show you how to install Aspose Cells for Go via C++ and create a Hello World application.

{{% /alert %}}

## **Installation**

### **Install Aspose Cells through GitHub**

The pkg.go.dev web is the easiest way to download and install Aspose.Cells for Go via C++.

1. Create a project for Go.
2. Import "github.com/aspose-cells/aspose.cells-go-cpp/v24" in your code.

[More step for details](/cells/go-cpp/installation/)

### **A demo for using Aspose.Cells for Go on Windows**

1. Download Aspose.Cells for Go via C++ from the following page:
[Download Aspose.Cells for Go via C++(Windows)](https://downloads.aspose.com/cells/go-cpp/)
2. Unzip the package and you will find a example which is on how to use Aspose.Cells for Go via C++.
3. Open the folder with Visual Studio Code or other IDEs.
4. main.go: this file shows how to code to test Aspose.Cells for Go via C++.

### **A demo for using Aspose.Cells for Go on Linux**

1. Download Aspose.Cells for Go from the following page:
[Download Aspose.Cells for Go(Linux)](https://downloads.aspose.com/cells/go/)
2. Unzip the package and you will find a example which is on how to use Aspose.Cells for Go for Linux.
3. Make sure you are in the path where example is located.
4. Run "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Run "cmake --build example/build"

## **Creating the Hello World Application**

The steps below creates the Hello World application using the Aspose.Cells API:

1. Create an instance of the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class.
1. If you have a license, then [apply it](/cells/go-cpp/licensing/).
   If you are using the evaluation version, skip the license related code lines.
1. Access any desired cell of a worksheet in the Excel file.
1. Insert the words "**Hello World!**" into a cell accessed.
1. Generate the modified Microsoft Excel file.

The implementation of the above steps is demonstrated in the examples below.

### **Code Sample: Creating a New Workbook**

The following example creates a new workbook from the scratch, inserts "**Hello World!**" into cell A1 on the first worksheet and saves the Excel file.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-go-Introduction-FirstApplication-1-new.go" >}}

### **Code Sample: Opening an Existing File**

The following example opens an existing Microsoft Excel template file, gets a cell and checks the value in the cell A1.

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
    lic, _ := NewLicense()
    lic.SetLicense_String(os.Getenv("LicensePath"))
    
    workbook, err1 := NewWorkbook_String("Book1.xlsx")
    if err1 != nil {
          println(err1)
    }
    worksheets, err2 := workbook.GetWorksheets()
    if err2 != nil {
        println(err2)
    }
    worksheet, err3 := worksheets.Get_Int(0)
    if err3 != nil {
        println(err3)
    }
    
    cells, err4 := worksheet.GetCells()
    if err4 != nil {
        println(err4)
    }
    
    cell, err5 := cells.Get_String("A1")
    if err5 != nil {
        println(err5)
    }
    print("Cell A1 value:")
    println(cell.GetStringValue())

    workbook.Save_String("Book1.pdf")
}

````
