---
title: Добавление пользоватской серверной функции проверки
type: docs
weight: 110
url: /ru/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb, серверная проверка
description: Эта статья рассматривает работу с серверной валидацией в GridWeb.
---

## **Возможные сценарии использования**
Иногда вам может потребоваться реализовать проверку данных на сервере. Aspose.Cells.GridWeb позволяет добавлять собственную серверную проверку данных. Вам нужно указать диапазон ячеек или область. Вы также можете установить клиентские функции проверки для обратных вызовов с собственной серверной проверкой.
## **Добавить пользовательскую функцию проверки на стороне сервера**
Вам нужно установить класс проверки сервера, который реализует интерфейс **GridCustomServerValidation** с помощью атрибута **GridValidation.ServerValidation**. Вам также необходимо установить функцию проверки на стороне клиента (она должна быть написана на JavaScript на стороне клиента), эта функция обязательна для проверки данных на клиентском конце при обратном вызове. Вы можете установить строку сообщения об ошибке через свойства **GridValidation.ErrorMessage** и заголовок через свойства **GridValidation.ErrorTitle** для ваших нужд. Пожалуйста, ознакомьтесь с серией скриншотов, показывающих, как это работает (шаг за шагом) в данном сценарии после выполнения приведенного ниже примера кода. В примере вы не можете обновлять данные в ячейках B2:C3. Когда вы попытаетесь отредактировать эти ячейки на листе, вам будет предложено несколько сообщений об ошибках, и предыдущее значение будет восстановлено. Вы можете открыть окно консоли (в вашем браузере), чтобы печатать информацию/детали о ячейке для определенных событий. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
