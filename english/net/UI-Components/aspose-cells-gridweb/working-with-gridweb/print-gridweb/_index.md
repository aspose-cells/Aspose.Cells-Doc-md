---
title: Print GridWeb
type: docs
weight: 90
url: /net/print-gridweb/
---

{{% alert color="primary" %}} 

There are times when developers need to print the GridWeb contents from a web page without saving the result as Microsoft Excel spreadsheet file. The Aspose.Cells.GridWeb control supports this feature via client side function.

{{% /alert %}} 
## **Printing GridWeb**
In order to print the contents, the Aspose.Cells.GridWeb for .NET has exposed the GridWeb.Print client-side function which can be used in a JavaScript call as demonstrated below.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-PrintGridWeb-PrintGridWebJS.aspx" >}}



Once the JavaScript function is in place, it can be triggered on any event of choice. Please check the following ASP.NET snippet which uses the above defined JavaScript function on a button click event.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-PrintGridWeb-PrintGridWeb.aspx" >}}
