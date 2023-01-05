---
title: Изменить тип цели ссылки HTML
type: docs
weight: 450
url: /ru/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells позволяет изменить тип цели ссылки HTML. HTML ссылка выглядит так:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как вы можете видеть, целевой атрибут в приведенной выше ссылке HTML — **_self**. Вы можете управлять этим целевым атрибутом с помощью свойства [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Это свойство принимает перечисление [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType), которое имеет следующие значения.

- [ПУСТОЙ](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [РОДИТЕЛЬ](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [СЕБЯ](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [ВЕРШИНА](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Изменить тип цели ссылки HTML**
 Следующий код иллюстрирует использование[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) имущество. Он изменяет тип цели ссылки на**пустой**. По умолчанию это**родитель** . Вы можете получить[исходный файл excel](5472932.xlsx) по этой ссылке, однако вы можете использовать любой файл Excel, содержащий внутри гиперссылку HTML, для запуска этого кода.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
