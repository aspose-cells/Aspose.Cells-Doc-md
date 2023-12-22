---
title: Проверка всего листа, а не только обновленных ячеек
type: docs
weight: 80
url: /ru/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
##  **Возможные сценарии использования**
По умолчанию GridWeb проверяет только обновленные ячейки и не проверяет весь лист. Однако, если вы хотите проверить весь рабочий лист на стороне клиента до того, как GridWeb отправит запрос на сервер, вам следует установить для переменной NeedValidateall внутри acwmain.js значение true.
##  **Проверка всего листа, а не только обновленных ячеек**
На следующем снимке экрана показана переменная NeedValidateall в acwmain.js. Установите для него значение true, и теперь GridWeb будет проверять весь ваш лист, а не только обновленные ячейки.

![задача: image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


