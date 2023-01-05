---
title: Проблема HTTPS SSL
type: docs
weight: 20
url: /ru/net/https-ssl-issue/
---
## **Проблема HTTPS/SSL**
Некоторые пользователи сообщили, что у них возникли проблемы с загрузкой файлов Excel, созданных с помощью Aspose.Cells. Когда открывается диалоговое окно сохранения, имя файла содержит имя страницы aspx вместо файла excel, а тип файла пуст.
### **Объяснение**
Мы изменили заголовки ответа HTTP, чтобы решить проблему со сжатием HTTP. Это может вызвать проблемы при отправке файлов в клиентский браузер через HTTPS/SSL.
### **Решение**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
