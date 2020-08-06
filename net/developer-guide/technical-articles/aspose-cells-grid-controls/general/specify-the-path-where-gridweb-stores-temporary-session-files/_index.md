---
title: Specify the path where GridWeb stores temporary session files
type: docs
weight: 50
url: /net/specify-the-path-where-gridweb-stores-temporary-session-files/
---

{{% alert color="primary" %}} 

When GridWeb session mode is ViewState, it stores its temporary session files inside the Application Base Directory. Sometimes, it is not OK to store temporary session files there because Application Base Directory might not have write permissions on it. In such cases, GridWeb throws such an exception

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

The solution to above problem is to give write access to Application Base Directory or change the GridWeb temporary session files path having write access using the GridWeb.SessionStorePath property. This path should be relative to Application Base Directory.

{{% /alert %}} 
## **Specify the path where GridWeb stores temporary session files**
The following sample code specifies the path where GridWeb stores temporary session files.



{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
