---
title: Manage Shape Text Options with Golang via C++
linktitle: Manage Shape Text Options
type: docs
weight: 200
url: /go-cpp/managing-shape-text-options/
description: Learn how to manage shape text options programmatically using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

Aspose.Cells provides powerful features to manage shape text options in Excel files programmatically. This guide explains how to manipulate shape text properties such as alignment, orientation, and formatting using Aspose.Cells for Go via C++.

{{% /alert %}}

## **Managing Shape Text Options**

Aspose.Cells allows you to customize the text within shapes in Excel files. The [**Shape**](https://reference.aspose.com/cells/go-cpp/shape/) class provides methods and properties to manage text options such as alignment, orientation, and formatting.

### **Setting Text Alignment**
You can set the horizontal and vertical alignment of text within a shape using the [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/shape/gettexthorizontalalignment/) and [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/shape/gettextverticalalignment/) **methods**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TextOptions.go" >}}

### **Setting Text Orientation**
You can also set the orientation of the text within a shape using the **SetTextOrientationType** method with the [**TextOrientationType**](https://reference.aspose.com/cells/go-cpp/textorientationtype/) enumeration.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TextOptions-1.go" >}}

### **Formatting Text**
You can format the text within a shape using the [**Font**](https://reference.aspose.com/cells/go-cpp/font/) class. This allows you to set properties such as font size, color, and style.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TextOptions-2.go" >}}

## **Conclusion**
Aspose.Cells for Go via C++ provides a comprehensive set of tools to manage shape text options in Excel files. By using the [**Shape**](https://reference.aspose.com/cells/go-cpp/shape/) class, you can easily customize text alignment, orientation, and formatting to meet your specific requirements.
{{< app/cells/assistant language="go" >}}
