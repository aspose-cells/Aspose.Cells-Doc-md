---
title: Получение данных подключения к SQL
type: docs
weight: 20
url: /ru/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells может помочь вам извлечь данные о соединении с SQL. Это включает любые данные, необходимые для подключения к серверу SQL, например, **URL сервера**, **имя пользователя**, **имя таблицы**, **полный SQL запрос**, **тип запроса**, **расположение таблицы** и **имя именованного диапазона**, связанного с ним.

{{% /alert %}} 

В Microsoft Excel подключитесь к базе данных, выполнив следующее:

1. Нажмите меню **Данные** и выберите **Из других источников**, а затем **Из SQL Server**.
1. Затем выберите **Данные**, а затем **Подключения**.
1. Используйте мастер подключений для подключения к базе данных и создания запроса к базе данных.

**Показ варианта соединения с SQL в Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells предоставляет метод Workbook.getDataConnections() для извлечения внешних соединений. Он возвращает коллекцию объектов ExternalConnection в книге.

Если объект ExternalConnection содержит данные соединения с SQL, его можно привести к типу DBConnection, и его свойства можно использовать для извлечения команды базы данных, типа команды, описания соединения, информации о соединении, учетных данных и т. д.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






