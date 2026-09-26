---
title: Setting Margins with Golang via C++
linktitle: Setting Margins
type: docs
weight: 20
url: /go-cpp/setting-margins/
description: Learn how to set the margins of an Excel worksheet using C++. This guide covers setting page margins, centering content, and configuring header and footer margins programmatically with Aspose.Cells for Go via C++.
keywords: set excel worksheet margin to center c++, set worksheet header and footer margin c++
---

{{% alert color="primary" %}}

Aspose.Cells fully supports Microsoft Excel's page setup options. Developers may need to configure page setup settings for worksheets to control the printing process. This topic discusses how to use Aspose.Cells to configure page margins.

{{% /alert %}}

## **Setting Margins**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains the [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class.

The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) property used to set the page setup options for a worksheet. The [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) property is an object of the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class that enables developers to set different page layout options for a printed worksheet. The [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class provides various properties and methods used to set page‑setup options.

### **Page Margins**

Set page margins (left, right, top, bottom) using the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class members. A few of the methods are listed below which are used to specify page margins:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/go-cpp/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getbottommargin/)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingMargins.go" >}}

### **Center on Page**

It is possible to center content on a page horizontally and vertically. For this, there are useful members of the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class, **SetCenterHorizontally()** and **SetCenterVertically()**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingMargins-1.go" >}}

### **Header and Footer Margins**

Set header and footer margins with the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class members such as **SetHeaderMargin()** and **SetFooterMargin()**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingMargins-2.go" >}}
{{< app/cells/assistant language="go" >}}
