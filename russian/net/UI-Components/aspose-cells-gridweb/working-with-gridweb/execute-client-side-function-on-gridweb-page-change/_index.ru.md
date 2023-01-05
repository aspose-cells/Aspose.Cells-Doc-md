---
title: Выполнение функции на стороне клиента при изменении страницы GridWeb
type: docs
weight: 140
url: /ru/net/execute-client-side-function-on-gridweb-page-change/
---
## **Возможные сценарии использования**
Иногда вам нужно выполнить функцию на стороне клиента при изменении страницы GridWeb. Aspose.Cells.GridWeb предоставляет для этой цели свойство OnPageChangeClientFunction. Пожалуйста, установите это свойство с функцией на стороне клиента, которую вы хотите выполнить.
## **Выполнение функции на стороне клиента при изменении страницы GridWeb**
Следующая разметка aspx объясняет, как использовать свойство OnPageChangeClientFunction. Он устанавливает свойство с помощью клиентской функции с именем MyOnPageChange. Обратите внимание, что это свойство действительно только в том случае, если вы включили пейджинг, т.е. EnablePaging="true". Теперь всякий раз, когда вы изменяете страницу GridWeb, она будет вызывать функцию на стороне клиента MyOnPageChange, которая печатает**индекс текущей страницы** на**приставка** как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](execute-client-side-function-on-gridweb-page-change_1.png)
## **Образец кода**
Это код клиентской функции MyOnPageChange, которая будет выполняться из-за установки свойства OnPageChangeClientFunction = "MyOnPageChange" в GridWeb. Это полная разметка страницы aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
