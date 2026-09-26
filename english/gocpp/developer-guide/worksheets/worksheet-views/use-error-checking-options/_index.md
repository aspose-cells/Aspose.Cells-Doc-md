---
title: Use Error Checking Options with Golang via C++
linktitle: Use Error Checking Options
type: docs
weight: 140
url: /go-cpp/use-error-checking-options/
description: In this article, you will find sample code that will programmatically use error checking options of Excel worksheets e.g. Numbers stored as Text using Go API or Library.
keywords: store number as text in excel using Go, error check excel options Go
---

{{% alert color="primary" %}}

Microsoft Excel allows users to define error checking options and rules. Users often see error checks when creating formulas, a small triangle at the top right corner of a cell is highlighted when there's a problem with the cell. Excel provides information that helps users to correct common problems.

{{% /alert %}}

## **Types of Errors**

Errors that mean that the formula cannot return a result — such as dividing a number by zero — require immediate attention and an error value is displayed in the cell. Clicking on the green triangle shows an exclamation mark, clicking it opens a list of options.

The error can be resolved using the options, or be ignored. Ignoring an error means that the error will not appear in further error checks.

Aspose.Cells provides error checking option features. The [**ErrorCheckOption**](https://reference.aspose.com/cells/go-cpp/errorcheckoption/) class manages different types of error checks, for example, numbers stored as text, formula calculation errors, and validation errors. Use the [**ErrorCheckType**](https://reference.aspose.com/cells/go-cpp/errorchecktype/) enumeration to set the desired error checking.

## **Numbers Stored as Text**

Occasionally, numbers might be formatted and stored in cells as text. This can cause problems with calculations or produce confusing sort orders. Numbers that are formatted as text are left-aligned instead of right-aligned in the cell. If a formula that should perform a mathematical operation on cells doesn't return a value, check the alignment in the cells that the formula refers to – some or all of those cells might be numbers formatted as text.

You can use the error checking options to quickly convert numbers stored as text to real numbers. In Microsoft Excel 2003:

1. On the **Tools** menu, click **Options**.  
2. Select the Error Checking tab.  
   **Number stored as text** option is checked by default.  
3. Disable it.

The following sample code shows how to disable the numbers stored as text error checking option for a worksheet in the template XLS file using the Aspose.Cells APIs.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseErrorCheckingOptions.go" >}}
{{< app/cells/assistant language="go" >}}
