---
title: Search Data using Original Values
type: docs
weight: 540
url: /java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Sometimes the value of the data is hidden because it is formatted in some way. For example, suppose cell D4 has formula =Sum(A1:A2) and its value is 20 but it is formatted as ---, then the value 20 is hidden and cannot be found using Microsoft Excel find options. However, you can find it using Aspose.Cells using [LookInType.ORIGINAL_VALUES](https://apireference.aspose.com/java/cells/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
#### **Search Data using Original Values**
The following sample code illustrates the above point. It finds cell D4 which cannot be found using Microsoft Excel find options but Aspose.Cells can find it using [LookInType.ORIGINAL_VALUES](https://apireference.aspose.com/java/cells/com.aspose.cells/lookintype#ORIGINAL_VALUES). Please read the comments inside the code for more information.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
#### **Console Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
