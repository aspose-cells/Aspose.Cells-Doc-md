---
title: HTML Bağlantısı Hedef Türünü Değiştirin
type: docs
weight: 450
url: /tr/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells, HTML bağlantı hedefi türünü değiştirmenize olanak tanır. HTML bağlantısı şöyle görünür:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Gördüğünüz gibi, yukarıdaki HTML bağlantısındaki hedef özniteliği **_self** şeklindedir. [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) özelliğini kullanarak bu hedef niteliğini kontrol edebilirsiniz. Bu özellik, aşağıdaki değerlere sahip [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) numaralandırmasını alır.

- [BOŞLUK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [EBEVEYN](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [KENDİNE](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TEPE](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **HTML Bağlantısı Hedef Türünü Değiştirin**
 Aşağıdaki kod kullanımını göstermektedir[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) Emlak. Bağlantı hedefi türünü şu şekilde değiştirir:**boşluk**. Varsayılan olarak,**ebeveyn** . alabilirsin[kaynak excel dosyası](5472932.xlsx) ancak bu bağlantıdan, bu kodu çalıştırmak için içinde HTML köprüsü bulunan herhangi bir excel dosyasını kullanabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
