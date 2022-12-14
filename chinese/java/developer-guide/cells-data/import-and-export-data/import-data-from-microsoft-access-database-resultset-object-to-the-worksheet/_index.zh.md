---
title: 将数据从 Microsoft Access 数据库结果集对象导入到工作表
type: docs
weight: 200
url: /zh/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **可能的使用场景**
Aspose.Cells 可以将数据从可以从任何数据库创建的 ResultSet 对象导入工作表。但是，本文专门从 Microsoft Access 数据库创建了一个 ResultSet 对象。由于代码对于所有类型的数据库都是相同的，因此您可以通用地使用它。
## **UCanAccess - 需要连接到 Microsoft Access 数据库**
请下载[优能通](http://ucanaccess.sourceforge.net/site.html).它包括以下 JAR 文件。将它们全部添加到类路径中。

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

如需更多帮助，请访问此 Stack Overflow 链接。

- [手动将 JAR 添加到您的项目](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **样本 Microsoft 样本代码中使用的 Access 2016 数据库文件**
示例代码中使用了以下示例 Microsoft Access 2016 数据库文件。您可以使用任何数据库文件或创建自己的数据库文件。

- [学生.accdb](48496712.accdb)

以下屏幕截图显示了在 Microsoft Access 2016 中打开时的数据库文件。

![待办事项：图片_替代_文本](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **将数据从 Microsoft Access 数据库结果集对象导入工作表。**
以下示例代码从 Microsoft Access 数据库执行 SQL 查询并创建一个 ResultSet 对象。然后它使用 ResultSet 对象将数据导入工作表[工作表.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)） 方法。第一次，它使用行和列索引，然后使用单元格名称将数据导入工作表。最后，它将工作簿另存为[输出 Excel 文件](48496713.xlsx).截图展示了示例代码对输出Excel文件的效果，供参考。

![待办事项：图片_替代_文本](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
