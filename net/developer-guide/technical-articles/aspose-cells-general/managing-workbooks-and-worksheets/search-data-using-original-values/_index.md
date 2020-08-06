---
title: Search Data using Original Values
type: docs
weight: 380
url: /net/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Sometimes the value of the data is hidden because it is formatted in some way. For example, suppose cell D4 has formula =Sum(A1:A2) and its value is 20 but it is formatted as ---, then the value 20 is hidden and cannot be found using Microsoft Excel find options. However, you can find it using Aspose.Cells using [LookInType.OriginalValues](https://apireference.aspose.com/net/cells/aspose.cells/lookintype)

{{% /alert %}} 

The following sample code illustrates the above point. It finds cell D4 which cannot be found using Microsoft Excel find options but Aspose.Cells can find it using [LookInType.OriginalValues](https://apireference.aspose.com/net/cells/aspose.cells/lookintype). Please read the comments inside the code for more information.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}
## **Console Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
