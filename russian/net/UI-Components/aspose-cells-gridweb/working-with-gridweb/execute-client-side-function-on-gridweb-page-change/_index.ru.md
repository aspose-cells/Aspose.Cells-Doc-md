---
title: Выполнение клиентской функции на изменение страницы GridWeb
type: docs
weight: 140
url: /ru/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: Эта статья представляет, как работать с клиентской js функцией в GridWeb.
---

## **Возможные сценарии использования**
Иногда вам нужно выполнить вашу клиентскую функцию при изменении страницы GridWeb. Aspose.Cells.GridWeb предоставляет свойство OnPageChangeClientFunction для этой цели. Пожалуйста, установите это свойство с клиентской функцией, которую вы хотите выполнить.
## **Выполнение клиентской функции на изменение страницы GridWeb**
Нижеприведенная разметка aspx объясняет, как использовать свойство OnPageChangeClientFunction. Она устанавливает свойство с клиентской функцией под названием MyOnPageChange. Обратите внимание, это свойство действительно только в том случае, если вы включили постраничное отображение, т.е. EnablePaging="true". Теперь, при изменении страницы GridWeb, она будет вызывать клиентскую функцию MyOnPageChange, которая выводит **текущий индекс страницы** в **консоль**, как показано на этом скриншоте.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Образец кода**
Это код клиентской функции MyOnPageChange, который будет выполнен из-за установки свойства OnPageChangeClientFunction ="MyOnPageChange" в GridWeb. Это полная разметка aspx-страницы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
