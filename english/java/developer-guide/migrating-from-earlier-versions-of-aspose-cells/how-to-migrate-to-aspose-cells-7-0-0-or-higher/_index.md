---
title: How to Migrate to Aspose.Cells 7.0.0 or Higher
type: docs
weight: 10
url: /java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In this article, we have shared the notable changes in the API that have been made in Aspose.Cells for Java 7.0.0 and onward versions as compared to the predecessor versions of Aspose.Cells for Java. This article will help users quickly migrate from the old API to the new API by understanding the changes made and carrying them out in their applications.

{{% /alert %}}

## **Notable Changes for the Existing Users**

Since the release of Aspose.Cells for Java v7.0.0, we have made some major **modifications** in the API and have added all the features that are present in Aspose.Cells for .NET to date. So, both Aspose.Cells for Java and .NET will be comparable now in terms of features and even in terms of method and property names.

Similar to the older approach, you can just import only one import statement in your application to access all the classes, interfaces, etc.

**Java**

{{< highlight java >}}
import com.aspose.cells.*;
{{< /highlight >}}

We have renamed certain API set to clean the API structure to match it to Aspose.Cells for .NET. We have added some collection classes and have replaced existing ones. For example, the **Worksheets** class has been replaced with **WorksheetCollection**. Similarly, the **Shapes** class has been replaced with **ShapeCollection**. However, the functionality of the classes has not been affected; rather, it has been enhanced.

If you wish to migrate to **the new API**, then you may need to carry out the following changes in your application to make things work on your end. The following list contains the changes made in classes and their respective methods as well.

## **Summary of the Changes in the API**

1) Collections in v2.5.4 or prior whose names **end** with 's' are renamed. In v7.0.0 or higher, the collections are named:
e.g., Shapes (Old) → ShapeCollection (New), Worksheets (Old) → WorksheetCollection (New), etc.

2) Getting an element from the collection has changed. For example, in v2.5.4 or prior we used to do it as `getXXX(int)`. In v7.0.0 or higher, now we do it as `get(int)`:
e.g., `Worksheets.getSheet(int)` (Old) → `WorksheetCollection.get(int)` (New), etc.

3) Getting the size (element count) of a collection has changed. In v2.5.4 or prior, we used to do it with `size()`. In v7.0.0 or higher, now we do it with `getCount()`:
e.g., `Worksheets.size()` (Old) → `WorksheetCollection.getCount()` (New), etc.

4) Boolean property getter methods in v2.5.4 or prior whose names start with 'is' have been changed. In v7.0.0, these now start with **get**:
e.g., `PageSetup.isBlackAndWhite()` (Old) → `PageSetup.getBlackAndWhite()` (New), etc.

{{< app/cells/assistant language="java" >}}
