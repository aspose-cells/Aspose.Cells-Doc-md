---
title: Изменение размера GridWeb и его панели заголовка
type: docs
weight: 30
url: /ru/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[Добавить GridWeb в веб-форму](/cells/ru/net/add-gridweb-to-web-form/), обсуждалось изменение размера элемента управления Aspose.Cells.GridWeb с помощью WYSIWYG. В этой статье объясняется, как сделать то же самое, но во время выполнения с помощью элемента управления Aspose.Cells.GridWeb API. Также объясняется, как изменить размер строк заголовков элемента управления Aspose.Cells.GridWeb, чтобы их данные было легче читать.

{{% /alert %}} 
## **Изменение ширины и высоты Aspose.Cells.GridWeb**
Изменение ширины и высоты элемента управления Aspose.Cells.GridWeb — простая, но важная функция. Элемент управления Aspose.Cells.GridWeb представлен классом GridWeb в API. Чтобы изменить ширину и высоту элемента управления GridWeb, просто используйте его свойства ширины и высоты.

{{% alert color="primary" %}} 

Ширина и высота элемента управления могут быть определены в пикселях или точках.

{{% /alert %}} 

Вывод следующего фрагмента кода показан ниже.

**Изменена ширина и высота элемента управления GridWeb.** 

![дело:изображение_альтернативный_текст](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Изменение ширины и высоты панели заголовка**
Aspose.Cells. Элемент управления GridWeb содержит две следующие строки заголовка:

- Верхняя панель заголовка, эта панель заголовка представляет столбцы как A, B, C, D и т. д.
- Левая панель заголовка, эта панель заголовка представляет строки как 1, 2, 3, 4 и т. д.

Обе эти строки заголовка показаны ниже.

**Заголовки** 

![дело:изображение_альтернативный_текст](resize-gridweb-and-its-header-bar_2.png)

Измените высоту верхней панели заголовка и ширину левой панели заголовка, используя свойства HeaderBarHeight и HeaderBarWidth элемента управления GridWeb соответственно. На рисунке ниже показан вывод следующего примера кода.

**Изменена ширина и высота панели заголовка** 

![дело:изображение_альтернативный_текст](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
