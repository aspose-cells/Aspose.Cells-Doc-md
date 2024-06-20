---
title: Проверка всего рабочего листа, а не только обновленных ячеек
type: docs
weight: 140
url: /ru/net/aspose-cells-gridweb/validate-entire-worksheet-instead-of-only-the-updated-cells/
keywords: GridWeb,validate,js,client
description: Эта статья рассказывает, как валидировать клиентскую js функцию в GridWeb.
---

## **Возможные сценарии использования**
По умолчанию GridWeb валидирует только обновленные ячейки и не валидирует весь рабочий лист. Однако, если вы хотите валидировать весь рабочий лист на стороне клиента перед отправкой запроса от GridWeb на сервер, то вы должны установить переменную needValidateall внутри acwmain.js в true.
## **Проверить весь рабочий лист, а не только обновленные ячейки**
На следующем скриншоте отображается переменная needValidateall в acwmain.js. Пожалуйста, установите ее в true, и теперь GridWeb будет валидировать весь ваш рабочий лист, а не только обновленные ячейки.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)
