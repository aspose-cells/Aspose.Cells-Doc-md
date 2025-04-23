---
title: Проблема HTTPS SSL
type: docs
weight: 20
url: /ru/net/https-ssl-issue/
---

## **Проблема HTTPS/SSL**
Некоторые пользователи сообщали, что у них возникают проблемы при загрузке Excel-файлов, созданных с помощью Aspose.Cells. Когда открывается диалог сохранения, имя файла содержит имя страницы aspx вместо имени файла Excel, а тип файла остается пустым.
### **Объяснение**
Мы изменили заголовки HTTP-ответов, чтобы решить проблему с HTTP-сжатием. Это может вызвать проблему при отправке файлов в браузер клиента через HTTPS/SSL.
### **Решение**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
