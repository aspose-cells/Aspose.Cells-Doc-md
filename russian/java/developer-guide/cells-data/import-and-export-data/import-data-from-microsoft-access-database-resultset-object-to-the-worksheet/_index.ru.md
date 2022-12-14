---
title: Импорт данных из объекта ResultSet базы данных Microsoft на рабочий лист
type: docs
weight: 200
url: /ru/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Возможные сценарии использования**
Aspose.Cells может импортировать данные на рабочие листы из объекта ResultSet, который может быть создан из любой базы данных. Однако в этой статье специально создается объект ResultSet из базы данных Access Microsoft. Так как код одинаков для всех типов баз данных, то можно использовать его вообще.
## **UCanAccess — требуется для подключения к базе данных Access Microsoft**
 Пожалуйста, скачайте[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Он включает следующие файлы JAR. Добавьте их все в путь к классам.

- ucanaccess-4.0.1.jar
- Commons-lang-2.6.jar
- Commons-регистрация-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Для получения дополнительной помощи перейдите по этой ссылке Stack Overflow.

- [Ручное добавление JAR-файлов в ваш проект](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Образец Microsoft Файл базы данных Access 2016, используемый в образце кода**
В примере кода использовался следующий образец Microsoft Файл базы данных Access 2016. Вы можете использовать любой файл базы данных или создать свой собственный.

- [Студенты.accdb](48496712.accdb)

На следующем снимке экрана показан файл базы данных при открытии в Microsoft Access 2016.

![дело:изображение_альтернативный_текст](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Импортируйте данные из объекта ResultSet базы данных Microsoft на рабочий лист.**
 В следующем примере кода выполняется SQL-запрос из базы данных Access Microsoft и создается объект ResultSet. Затем он импортирует данные из объекта ResultSet в рабочий лист, используя[Рабочий лист.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) метод. В первый раз он использует индексы строк и столбцов, а затем использует имя ячейки для импорта данных на лист. Наконец, он сохраняет книгу как[Выходной файл Excel](48496713.xlsx). На снимке экрана показано влияние примера кода на выходной файл Excel для справки.

![дело:изображение_альтернативный_текст](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
