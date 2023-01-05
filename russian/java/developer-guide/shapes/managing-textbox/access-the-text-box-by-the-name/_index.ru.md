---
title: Доступ к текстовому полю по имени
type: docs
weight: 580
url: /ru/java/access-the-text-box-by-the-name/
---
{{% alert color="primary" %}} 

 Раньше доступ к текстовым полям осуществлялся по индексу из[Рабочий лист.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) коллекция, но теперь вы также можете получить доступ к текстовому полю по имени из этой коллекции. Это удобный и быстрый способ получить доступ к текстовому полю, если вы уже знаете его имя.

{{% /alert %}} 
## **Доступ к текстовому полю по имени**
Следующий пример кода сначала создает текстовое поле и присваивает ему некоторый текст и имя. Затем в следующих строках мы обращаемся к тому же текстовому полю по его имени и печатаем его текст.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **Консольный вывод**
Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

 This is MyTextBox

{{< /highlight >}}
