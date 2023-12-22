---
title: Çalışma kitabındaki VBA projesine kitaplık referansı ekleme
type: docs
weight: 10
url: /tr/java/add-a-library-reference-to-vba-project-in-workbook/
description: Aspose.Cells for Java API numaralı telefondan çalışma kitabındaki VBA projesine nasıl kitaplık referansı ekleneceğini öğrenin.
keywords: How to Add a library reference to VBA project in workbook in Java, Insert a library reference to VBA project in workbook using Java, Java Set library reference to VBA project in workbook. 
---
{{% alert color="primary" %}}

 Microsoft Excel'de, VBA projesine bir kütüphane referansı ekleyebilirsiniz.**Araçlar > Referanslar...** manuel olarak. Mevcut referanslar arasından seçim yapmanıza veya kitaplığınıza kendiniz göz atmanıza yardımcı olacak aşağıdaki iletişim kutusunu açacaktır.

![yapılacak şey:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

Ancak bazen kitaplık referansını VBA projesine kod aracılığıyla eklemeniz veya kaydetmeniz gerekir. Aspose.Cells'i kullanarak yapabilirsiniz[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) yöntem.

{{% /alert %}}

##  **Çalışma kitabındaki VBA projesine kütüphane referansı nasıl eklenir**

 Aşağıdaki örnek kod, kullanarak çalışma kitabının VBA projesine iki kitaplık başvurusu ekler veya kaydeder.[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
