---
title: Çalışma sayfasının Parola Korumalı Olup Olmadığını Algılama
type: docs
weight: 280
url: /tr/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Çalışma kitaplarını ve çalışma kitaplarını ayrı ayrı koruma olasılığı vardır. Örneğin, bir elektronik tablo, şifreyle korunan bir veya daha fazla çalışma sayfası içerebilir, ancak elektronik tablo kendisi korunmuş olabilir veya olmayabilir. Aspose.Cells API'leri, belirli bir çalışma sayfasının şifre korunup korunmadığını belirleme olanağı sağlar. Bu makale, Aspose.Cells for Java API'nin aynı şeyi başarmak için nasıl kullanıldığını göstermektedir.

{{% /alert %}}

## **Çalışma Sayfasının Şifre Korunup Korunmadığını Algılama**

Aspose.Cells for Java 8.7.0'nin **[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)** özelliği şimdi bir çalışma kitabının parola korumalı olup olmadığını algılamak için kullanılabilir. Boolean türü [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) alanı, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) parola korumalıysa **true** değerini döndürür, aksi halde **false** değerini döndürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
