---  
title: Check Version Number  
type: docs  
weight: 80  
url: /net/check-version-number/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}

Wondering which version of Aspose.Cells you are using? We publish new versions of Aspose.Cells, both to introduce new features and to fix issues, on a regular basis. The version number consists of a major version number, a minor version number, and a hotfix version number. Each number must be an integer from 0 upwards. The format is as follows:

major.minor.hotfix

When we release a new build of Aspose.Cells, we update the version number.

This article explains how to check which version of Aspose.Cells is installed on the system manually and using the Aspose.Cells API.

{{% /alert %}}

## **Check Version Number Manually**

To find out which version of Aspose.Cells you are using manually:

1. Right‑click the Aspose.Cells.dll file and select **Properties**.  
2. Click the **Version** (or **Details**) tab to check the version number.

## **Check Version Number Using the Aspose.Cells API**

To find out which version of Aspose.Cells you are using through the API, use the CellsHelper class’s **GetVersion** static method to get Aspose.Cells’ version number.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}  
{{< app/cells/assistant language="csharp" >}}
