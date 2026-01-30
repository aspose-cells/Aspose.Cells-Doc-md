---
title: Detect if Worksheet is Password Protected with Go
linktitle: Detect if Worksheet is Password Protected
type: docs
weight: 360
url: /gocpp/detect-if-worksheet-is-password-protected/
description: Learn how to detect if a worksheet is password protected using Aspose.Cells for Go.
ai_search_scope: cells_go
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password‑protected; however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect if a given worksheet is password protected or not. This article demonstrates the usage of the Aspose.Cells for Go API to achieve the same.

{{% /alert %}}

Aspose.Cells for Go exposes the [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/go/aspose.cells/protection/isprotectedwithpassword/) property to detect if a worksheet is password protected or not. The Boolean‑type [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/go/aspose.cells/protection/isprotectedwithpassword/) property returns **true** if a [**Worksheet**](https://reference.aspose.com/cells/go/aspose.cells/worksheet/) is password‑protected and **false** if not.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectIfWorksheetIsPasswordProtected.go" >}}

{{< app/cells/assistant language="go" >}}