---
title: Выполнение клиентской функции на изменение страницы GridWeb
type: docs
weight: 70
url: /ru/java/execute-client-side-function-on-gridweb-page-change/
---

## **Возможные сценарии использования**
Иногда вам нужно выполнить вашу клиентскую функцию при изменении страницы GridWeb. Aspose.Cells.GridWeb предоставляет свойство OnPageChangeClientFunction для этой цели. Пожалуйста, установите это свойство с клиентской функцией, которую вы хотите выполнить.
## **Выполнение клиентской функции на изменение страницы GridWeb**
Следующий код на Java объясняет, как использовать свойство GridWebBean.setOnPageChangeClientFunction(). Он устанавливает это свойство с клиентской функцией с именем MyOnPageChange. Обратите внимание, что это свойство действительно только в том случае, если вы включили постраничную навигацию, то есть GridWebBean.setEnablePaging(true). Теперь, каждый раз при изменении страницы GridWeb будет вызывать клиентскую функцию MyOnPageChange, которая выводит **текущий индекс страницы** в **консоль**, как показано на этом скриншоте.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **Образец кода**
Это код клиентской функции MyOnPageChange, который будет выполнен из-за этой строки, то есть Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

Следующий код объясняет, как включить постраничную навигацию и установить свойство OnPageChangeClientFunction.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
