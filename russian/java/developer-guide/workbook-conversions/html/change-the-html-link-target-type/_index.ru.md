---
title: Изменить тип HTML ссылки
type: docs
weight: 450
url: /ru/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

Aspose.Cells позволяет вам изменять тип цели HTML-ссылки. HTML-ссылка выглядит следующим образом:

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видите, атрибут target в приведенной выше HTML-ссылке имеет значение **_self**. Вы можете контролировать этот атрибут target, используя свойство [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Это свойство принимает перечисление [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType), в котором есть следующие значения.

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Изменить тип HTML ссылки**
Приведенный ниже код демонстрирует использование свойства [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Он изменяет тип цели ссылки на **blank**. По умолчанию это **родитель**. Вы можете получить [исходный файл Excel](5472932.xlsx) по этой ссылке, однако вы можете использовать любой файл Excel, содержащий гиперссылку HTML, чтобы выполнить этот код.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
