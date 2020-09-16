---
title: How to Migrate to Aspose.Cells 7.0.0 or Higher
type: docs
weight: 10
url: /java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

In this article, we have shared the notable changes in the API that have been carried in Aspose.Cells for Java 7.0.0 and onward versions as compared to the predecessor versions of Aspose.Cells for Java. This article will help the users to quickly migrate from Old API to new API by understanding the changes made and carrying them out in their applications.

{{% /alert %}}

## **Notable Changes for the Existing Users**

Since the release of Aspose.Cells for Java v7.0.0, we have made some major modification in the API and have added all those features that are present in Aspose.Cells for .NET to date. So, both Aspose.Cells for Java and .NET will be comparable now in terms of features and even in terms of methods and properties names.

Similar to the older approach, you can just import only one import statement in your application to fetch all the classes, interfaces etc.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

We have renamed certain API’s set to clean the API structure to match it with Aspose.Cells for .NET. We have added some collection classes now and have replaced them with existing collection classes. Like Worksheets class has been replaced with **WorksheetCollection**. Similarly, Shapes class has been replaced with **ShapeCollection**. However, the functionality of the classes has not been affected rather enhanced.

If you wish to migrate to new API then you may need to carry out the following changes in your application to make things working on your end. The following list contains the changes made in classes and their respective methods as well.

## **Summary of the Changes in the API**

1) Collections in v2.5.4 or prior whose names ending with 's' are renamed. In v7.0.0 or higher, the Collections are named as:
e.g., Shapes (Old) -> ShapeCollection (New), Worksheets (Old) -> WorksheetCollection (New), ...,etc.

2) Getting element from the Collection is changed. For example, in v2.5.4 or prior we used to do it as getXXX(int), in v7.0.0 or higher, now we do it as get(int):
e.g., Worksheets.getSheet(int) (Old) -> WorksheetCollection.get(int) (New), ...etc.

3) Getting size(element count) of one Collection is changed. In v2.5.4 or prior, we used to do it with size(), in v7.0.0 or higher, now we do it with getCount():
Worksheets.size() (Old) -> WorksheetCollection.getCount() (New), ...,etc.

4) Boolean properties' getter methods in v2.5.4 or prior whose names starting with 'is' are changed. In v7.0.0 these are started with "get":
e.g., PageSetup.isBlackAndWhite() (Old) -> PageSetup.getBlackAndWhite() (New), ...,etc.
