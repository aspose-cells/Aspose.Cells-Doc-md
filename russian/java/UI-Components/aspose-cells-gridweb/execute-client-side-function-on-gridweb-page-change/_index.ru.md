---
title: Выполнение функции на стороне клиента при изменении страницы GridWeb
type: docs
weight: 70
url: /ru/java/execute-client-side-function-on-gridweb-page-change/
---
##  **Возможные сценарии использования**
Иногда вам нужно выполнить функцию на стороне клиента при изменении страницы GridWeb. Для этой цели Aspose.Cells.GridWeb предоставляет свойство OnPageChangeClientFunction. Установите это свойство с функцией на стороне клиента, которую вы хотите выполнить.
##  **Выполнение функции на стороне клиента при изменении страницы GridWeb**
 Следующий код Java объясняет, как использовать свойство GridWebBean.setOnPageChangeClientFunction(). Он устанавливает свойство с помощью клиентской функции MyOnPageChange. Обратите внимание: это свойство действительно только в том случае, если вы включили разбиение по страницам, т. е. GridWebBean.setEnablePaging(true). Теперь всякий раз, когда вы меняете страницу GridWeb, она вызывает клиентскую функцию MyOnPageChange, которая печатает**индекс текущей страницы** на**консоль** как показано на этом скриншоте.

![задача: image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
##  **Образец кода**
Это код клиентской функции MyOnPageChange, которая будет выполнена из-за этой строки, т.е. Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

В следующем коде объясняется, как включить разбиение по страницам и установить свойство OnPageChangeClientFunction.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
