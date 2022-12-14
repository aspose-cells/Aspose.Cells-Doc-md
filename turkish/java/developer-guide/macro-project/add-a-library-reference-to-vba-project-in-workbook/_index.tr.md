---
title: Çalışma kitabında VBA projesine bir kitaplık başvurusu ekleyin
type: docs
weight: 10
url: /tr/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 Microsoft Excel'de, VBA projesine bir kitaplık başvurusu ekleyebilirsiniz.**Araçlar > Referanslar...** manuel olarak. Mevcut referanslar arasından seçim yapmanıza veya kitaplığınıza kendiniz göz atmanıza yardımcı olacak aşağıdaki iletişim kutusunu açacaktır.

![yapılacaklar:resim_alternatif_Metin](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Ancak bazen, kod aracılığıyla VBA projesine kitaplık referansı eklemeniz veya kaydetmeniz gerekir. Aspose.Cells ile yapabilirsiniz.[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) yöntem.

{{% /alert %}}

## **Çalışma kitabında VBA projesine bir kitaplık başvurusu ekleyin**

 Aşağıdaki örnek kod, kullanarak çalışma kitabının VBA projesine iki kitaplık başvurusu ekler veya kaydeder.[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
