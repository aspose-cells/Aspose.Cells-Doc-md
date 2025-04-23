---
title: VBA projesine kitap başvurusu ekleyin
type: docs
weight: 10
url: /tr/java/add-a-library-reference-to-vba-project-in-workbook/
description: Aspose.Cells for Java API si aracılığıyla çalışma kitabına bir kitaplık referansı eklemeyi öğrenin.
keywords: Java da çalışma kitabına bir kitaplık referansı eklemeyi öğrenin, Java kullanarak çalışma kitabına bir kitaplık referansı ekleyin, Java da çalışma kitabına bir kitaplık referansı ayarlayın. 
---

{{% alert color="primary" %}}

Microsoft Excel'de, **Tools > References...**'a tıklayarak çalışma kitabına kitaplık referansı ekleyebilirsiniz. Bu, var olan referanslardan seçmenize veya kütüphanenize göz atmanıza yardımcı olacak olan aşağıdaki iletişim kutusunu açacaktır.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Ancak bazen, kütaplık referansını kod aracılığıyla eklemek veya kaydetmek gerekebilir. Bunun için Aspose.Cells'ın [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) yöntemini kullanabilirsiniz.

{{% /alert %}}

## **Çalışma kitabına bir kitaplık referansı eklemeyi öğrenin**

Aşağıdaki örnek kod, [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference-java.lang.String-java.lang.String-) yöntemini kullanarak çalışma kitabının VBA projesine iki kütüphane başvurusu ekler veya kaydeder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
{{< app/cells/assistant language="java" >}}
