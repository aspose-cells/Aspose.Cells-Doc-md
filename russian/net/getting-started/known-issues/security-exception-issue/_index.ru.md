﻿---
title: Проблема исключения безопасности
type: docs
weight: 30
url: /ru/net/security-exception-issue/
---
## **Проблема исключения безопасности**
Некоторые пользователи могут получить сообщение об ошибке «Исключение безопасности» при попытке использовать Aspose.Cells. Эта проблема обычно возникает в веб-приложении.
### **Объяснение**
 Aspose.Cells должен позвонить кому-то**GDI-интерфейсы Win32** предоставить некоторые важные функции. Если веб-сервер имеет строгий уровень доверия, может быть выдано это исключение безопасности.
### **Решение**
Попробуйте создать новый набор разрешений, чтобы предоставить разрешение безопасности Aspose.Cells.dll с включенным параметром «Разрешить вызовы неуправляемых сборок».
