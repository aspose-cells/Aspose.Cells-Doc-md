---
title: Печать GridWeb
type: docs
weight: 90
url: /ru/net/print-gridweb/
---
{{% alert color="primary" %}} 

Бывают случаи, когда разработчикам необходимо распечатать содержимое GridWeb с веб-страницы без сохранения результата в виде файла электронной таблицы Microsoft Excel. Элемент управления Aspose.Cells.GridWeb поддерживает эту функцию через функцию на стороне клиента.

{{% /alert %}} 
## **Печать GridWeb**
Чтобы распечатать содержимое, Aspose.Cells.GridWeb for .NET предоставил клиентскую функцию GridWeb.Print, которую можно использовать в вызове JavaScript, как показано ниже.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-PrintGridWeb-PrintGridWebJS.aspx" >}}



После того, как функция JavaScript установлена, ее можно активировать при любом событии по выбору. Пожалуйста, проверьте следующий фрагмент ASP.NET, который использует определенную выше функцию JavaScript для события нажатия кнопки.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-PrintGridWeb-PrintGridWeb.aspx" >}}
