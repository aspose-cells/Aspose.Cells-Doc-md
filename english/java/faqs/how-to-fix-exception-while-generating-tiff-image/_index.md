---
title: How to fix Exception while generating TIFF image
type: docs
weight: 60
url: /java/how-to-fix-exception-while-generating-tiff-image/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

TIFF images are supported natively by Java from Java 9. However, TIFF images are not supported by Java 8 and older. For TIFF support in old Java environments, Aspose.Cells for Java depends on the Java Advanced Imaging (JAI) package from Oracle. Exception will occur if JAI package is not avaliable:
```java
NoClassDefFoundError: com/sun/media/imageio/plugins/tiff/TIFFImageWriter
```
Or more clear exception in newer Aspose.Cells for Java:
```java
Exception: Please add Java Advanced Imaging (JAI) references to generate TIFF image for Java 8 and older!

```

## Solution
1. Please install JAI for Java 8 and older: [How to intall JAI](https://docs.aspose.com/cells/java/installation/#to-tiff-images-by-java-8-and-older)
2. Upgrade to Java 9 and above.


{{< app/cells/assistant language="java" >}}
