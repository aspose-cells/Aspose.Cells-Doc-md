---
title: Sort Data
type: docs
weight: 90
url: /net/sort-data/
---

{{% alert color="primary" %}}

This article is designed to provide developers with a detailed understanding of how to sort data in a worksheet.

Data sorting is a handy and versatile feature of Microsoft Excel. Generally, sorting is performed on a list, which is defined as a contiguous group of data where the data is displayed in columns. Aspose.Cells allows you to sort worksheet data alphabetically or numerically. It sorts data in the same way as Microsoft Excel does.

You might work with Office Automation for data sorting but Office Automation has its drawbacks. There are several reasons and issues involved: security, stability, scalability/speed, price, and features. In short, there are many reasons to look for a different solution, with the top one being that Microsoft themselves strongly recommends against Office Automation from software solutions.

In this article, we create a console application in Visual Studio.NET, and sort data with a few simple lines of code using the **Aspose.Cells API**.

{{% /alert %}}

## **Using Aspose.Cells to Sort Data in a Worksheet**

1. Create a Microsoft Excel file with different data sets or contents.
1. Download and install Aspose.Cells:
   1. [Download](https://downloads.aspose.com/cells/net) Aspose.Cells for .NET.
1. Install it on your development computer.

{{% alert color="primary" %}}

All [Aspose](https://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.

{{% /alert %}}

1. Create a project:
   1. Start Visual Studio .NET.
   1. Create a new console application.
1. Add a reference to Aspose.Cells in your project:
   1. Add a reference to …\Program Files\Aspose\ Aspose.Cells for .NET \Bin\Net1.0\Aspose.Cells.dll
1. Sort the data in the worksheet:
   1. Add code to the project.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SortData-1.cs" >}}
