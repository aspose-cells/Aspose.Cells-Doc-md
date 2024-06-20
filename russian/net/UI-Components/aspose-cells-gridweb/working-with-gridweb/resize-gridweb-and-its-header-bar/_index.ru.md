---
title: Изменение размера GridWeb и его заголовочной панели
type: docs
weight: 30
url: /ru/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb, изменить размер
description: В этой статье описано, как изменить размер в GridWeb.
---

{{% alert color="primary" %}} 

[Добавление GridWeb в веб-форму](/cells/ru/net/aspose-cells-gridweb/add-gridweb-to-web-form/), обсуждается изменение размера элемента управления Aspose.Cells.GridWeb с использованием WYSIWYG. В этой статье объясняется, как сделать то же самое, но во время выполнения с использованием API Aspose.Cells.GridWeb. Также объясняется, как изменить размер заголовочных панелей элемента управления Aspose.Cells.GridWeb, чтобы их данные было проще читать.

{{% /alert %}} 
## **Изменение ширины и высоты Aspose.Cells.GridWeb**
Изменение ширины и высоты элемента управления Aspose.Cells.GridWeb - это простая, но важная функция. Элемент управления Aspose.Cells.GridWeb представляется классом GridWeb в API. Для изменения ширины и высоты элемента управления GridWeb просто используйте его свойства ширины и высоты.

{{% alert color="primary" %}} 

Ширина и высота элемента управления могут быть определены в пикселях или пунктах.

{{% /alert %}} 

Результатом следующего фрагмента кода является показанное ниже.

**Измененная ширина и высота элемента управления GridWeb** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Изменение ширины и высоты заголовочной панели**
Элемент управления Aspose.Cells.GridWeb содержит две заголовочные панели следующим образом:

- Верхняя заголовочная панель, эта заголовочная панель представляет столбцы как A, B, C, D и т. д.
- Левая заголовочная панель, эта заголовочная панель представляет строки как 1, 2, 3, 4 и т. д.

Обе эти заголовочные панели показаны ниже.

**Заголовочные панели** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

Измените высоту верхней панели заголовка и ширину левой панели заголовка с помощью свойств HeaderBarHeight и HeaderBarWidth управления GridWeb соответственно. Ниже приведен вывод примера кода, который следует за ним.

**Измененная ширина и высота панели заголовка** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
