---
title: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 450
url: /tr/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells size HTML bağlantı hedef türünü değiştirme olanağı sağlar. HTML bağlantısı şuna benzer:

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self** olarak görünüyor. Bu hedef özniteliğini [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) özelliğini kullanarak kontrol edebilirsiniz. Bu özellik [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) numarasını alır ve aşağıdaki değerlere sahiptir.

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **HTML Bağlantı Hedef Türünü Değiştirme**
Aşağıdaki kod, [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) özelliğinin kullanımını gösterir. Bu kod bağlantı hedef türünü **blank** olarak değiştirir. Varsayılan olarak, hedef türü **parent**'tır. Bu kodu çalıştırmak için [kaynak excel dosyasını](5472932.xlsx) kullanabilirsiniz, ancak içindeki HTML bağlantısı olan herhangi bir excel dosyasını kullanabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
{{< app/cells/assistant language="java" >}}
