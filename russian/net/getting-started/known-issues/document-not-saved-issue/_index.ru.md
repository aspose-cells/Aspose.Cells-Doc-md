---
title: Проблема с сохранением документа
type: docs
weight: 40
url: /ru/net/document-not-saved-issue/
---

## **Проблема**
У меня возникла странная проблема с электронной таблицей, которую я создал с помощью вашего контроля. Он открывается и редактируется в Excel нормально, но когда я пытаюсь выполнить сохранение или сохранить как, я получаю сообщение "Документ не сохранен".
### **Обзор проблемы**
Это ошибка в Excel: 

"Документ не сохранен" Сохранение файла, созданного из шаблона

Идентификатор статьи: 121942

Последний просмотр: 15 августа 2005 г.

Редакция: 1.3

Эта статья ранее публиковалась под Q121942
### **Симптом**
При попытке сохранить книгу Excel вы можете получить следующее сообщение об ошибке: **"Документ не сохранен"**
### **Причины**
Эта проблема может возникнуть, если выполнены следующие условия:

- Книга была создана из шаблона, содержащего встроенный объект.
- Вы вставили лист в свою книгу из шаблона.
- Шаблон содержит встроенный объект.
### **Решение**
Для сохранения вашей работы сначала необходимо удалить встроенные объекты из вашей книги.
