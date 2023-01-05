---
title: Выполнение функции на стороне клиента при изменении страницы GridWeb
type: docs
weight: 70
url: /ru/java/execute-client-side-function-on-gridweb-page-change/
---
## **Возможные сценарии использования**
Иногда вам нужно выполнить функцию на стороне клиента при изменении страницы GridWeb. Aspose.Cells.GridWeb предоставляет для этой цели свойство OnPageChangeClientFunction. Пожалуйста, установите это свойство с функцией на стороне клиента, которую вы хотите выполнить.
## **Выполнение функции на стороне клиента при изменении страницы GridWeb**
Следующий код Java объясняет, как использовать свойство GridWebBean.setOnPageChangeClientFunction(). Он устанавливает свойство с помощью клиентской функции с именем MyOnPageChange. Обратите внимание, что это свойство допустимо только в том случае, если вы включили разбиение по страницам, т. е. GridWebBean.setEnablePaging(true). Теперь всякий раз, когда вы изменяете страницу GridWeb, она будет вызывать функцию на стороне клиента MyOnPageChange, которая печатает**индекс текущей страницы** на**приставка** как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](execute-client-side-function-on-gridweb-page-change_1.png)
## **Образец кода**
Это код клиентской функции MyOnPageChange, которая будет выполняться из-за этой строки, т.е. Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

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
