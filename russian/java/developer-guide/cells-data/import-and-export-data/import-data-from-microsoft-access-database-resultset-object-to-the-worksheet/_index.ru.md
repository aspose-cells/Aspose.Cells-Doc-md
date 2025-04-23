---
title: Импорт данных из объекта результатов Microsoft Access Database на лист
type: docs
weight: 200
url: /ru/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Возможные сценарии использования**
Aspose.Cells может импортировать данные на листы из объекта результатов, который может быть создан из любой базы данных. Однако этот статья специально создает объект результатов из базы данных Microsoft Access. Поскольку код такой же для всех типов баз данных, вы можете использовать его в общем.
## **UCanAccess - необходим для подключения к базе данных Microsoft Access**
Пожалуйста, загрузите [UCanAccess](http://ucanaccess.sourceforge.net/site.html). Он включает следующие файлы JAR. Добавьте их все в класспас.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Для получения дополнительной помощи, пожалуйста, посетите ссылку на Stack Overflow.

- [Вручную добавляя JAR-файлы в свой проект](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Образец файла базы данных Microsoft Access 2016, используемый внутри образца кода**
Внутри образца кода был использован следующий образец файла базы данных Microsoft Access 2016. Вы можете использовать любой файл базы данных или создать свой собственный.

- [Students.accdb](48496712.accdb)

На следующем скриншоте показан файл базы данных при открытии в Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Импорт данных из базы данных Microsoft Access в объект ResultSet в рабочем листе.**
Следующий пример кода выполняет SQL-запрос из базы данных Microsoft Access и создает объект ResultSet. Затем он импортирует данные из объекта ResultSet в рабочий лист с помощью метода [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet-java.sql.ResultSet-int-int-boolean-). В первый раз используются индексы строк и столбцов, затем используется имя ячейки для импорта данных в рабочий лист. В конце он сохраняет рабочую книгу как файл Excel [Output Excel File](48496713.xlsx). Скриншот демонстрирует эффект работы примера кода на результирующем Excel-файле для справки.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
