---
title: Check Version Number
type: docs
weight: 80
url: /python-java/check-version-number/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Wonder which version of Aspose.Cells you are using? We publish new versions of Aspose.Cells, both to introduce new features and to fix issues, on a regular basis. The version number consists of major version number, minor version number, and hotfix version number. Each number must be an integer from 0 up. The format is as follows:

major.minor.hotfix

When we release a new build of Aspose.Cells, we update the version number.

This article explains how to check which version of Aspose.Cells is installed on the system manually and using the Aspose.Cells API.

{{% /alert %}}

## **Check Version Number Manually**

To find out which version of Aspose.Cells you are using manually:

1. Right-click the Aspose.Cells.dll file and select **Properties**.
1. Click the Version (or Details) tab to check the version number.

## **Check Version Number Using the Aspose.Cells API**

To find out which version of Aspose.Cells you are using through the API, use the [CellsHelper](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper) class GetVersion static method to get Aspose.Cell's version number.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}
