---
title: Доступ к текстовому полю по имени
type: docs
weight: 580
url: /ru/java/access-the-text-box-by-the-name/
---

{{% alert color="primary" %}} 

Ранее, текстовые поля обращались по индексу из коллекции [Workheet.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes), а теперь вы также можете получить доступ к текстовому полю по имени из этой коллекции. Это удобный и быстрый способ получить доступ к вашему текстовому полю, если вы уже знаете его имя.

{{% /alert %}} 
## **Доступ к текстовому полю по имени**
Приведенный ниже образец кода сначала создает текстовое поле и назначает ему некоторый текст и имя. Затем в следующих строках мы получаем доступ к тому же текстовому полю по его имени и печатаем его текст.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **Вывод в консоль**
Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

 This is MyTextBox

{{< /highlight >}}
