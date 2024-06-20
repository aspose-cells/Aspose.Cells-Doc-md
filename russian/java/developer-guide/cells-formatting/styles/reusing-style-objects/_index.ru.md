---
title: Повторное использование объектов стиля
type: docs
weight: 60
url: /ru/java/reusing-style-objects/
---

{{% alert color="primary" %}}

Повторное использование объектов стиля может сэкономить память и ускорить выполнение программы.

{{% /alert %}}

Чтобы применить форматирование к большому диапазону ячеек на листе:

1. Создайте объект стиля.
1. Укажите атрибуты.
1. Примените стиль к ячейкам в диапазоне.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Тот же процесс, о котором говорилось выше, также может быть выполнен следующим образом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

Поскольку методы [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) и [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) используют гораздо меньше памяти и эффективны, старое свойство *Cell.getStyle()*, которое потребляло много ненужной памяти, было удалено с выпуском *Aspose.Cells 7.1.0*.

{{% /alert %}}
