---
title: Включить поле ввода GridWeb
type: docs
weight: 110
url: /ru/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, поле ввода, панель формул
description: Эта статья представляет, как работать с панелью формул или полем ввода в GridWeb.
---

{{% alert color="primary" %}} 

Поле ввода GridWeb (в Excel называется панель формул) - это панель инструментов, которая отображается в верхней части элемента управления, и которую можно использовать для отображения или ввода значения или копирования данных/формулы для выделенной ячейки. Она также показывает имя ячейки, которую вы редактируете. После щелчка по рамке или при начале ввода данных или набора знака равенства (=) поле ввода будет активировано.

{{% /alert %}} 
## **Настройка поля ввода Aspose.Cells.GridWeb**
Элемент управления GridWeb предоставляет свойство ShowCellEditBox, которое разработчики могут установить в "True" для отображения панели инструментов. Значение по умолчанию этого атрибута - False. Когда его значение установлено в "True", поле ввода появится в верхней части элемента управления GridWeb.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Элемент управления GridWeb с полем ввода** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Пример**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
