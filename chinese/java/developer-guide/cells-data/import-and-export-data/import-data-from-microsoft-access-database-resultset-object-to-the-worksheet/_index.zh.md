---
title: 从Microsoft Access数据库ResultSet对象导入数据到工作表
type: docs
weight: 200
url: /zh/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **可能的使用场景**
Aspose.Cells可以从ResultSet对象导入数据到工作表，该对象可以从任何数据库创建。然而，该文章特别从Microsoft Access数据库创建了一个ResultSet对象。由于代码适用于所有类型的数据库，因此您可以通用使用。
## **UCanAccess - 连接到Microsoft Access数据库所需**
请下载[UCanAccess](http://ucanaccess.sourceforge.net/site.html)。其中包括以下JAR文件。将它们全部添加到类路径中。

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

如需更多帮助，请访问此Stack Overflow链接。

- [手动将JAR文件添加到您的项目中](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **用于标本代码中的Sample Microsoft Access 2016数据库文件**
下面的示例Microsoft Access 2016数据库文件在示例代码中使用。您可以使用任何数据库文件或创建您自己的。

- [Students.accdb](48496712.accdb)

下面的截图显示了在Microsoft Access 2016中打开的数据库文件。

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **从Microsoft Access数据库ResultSet对象导入数据到工作表。**
以下示例代码从Microsoft Access数据库执行SQL查询，并创建ResultSet对象。然后，它使用[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/zh-CN/java/com.aspose.cells/cells#importResultSet-java.sql.ResultSet-int-int-boolean-)方法将数据从ResultSet导入到工作表中。第一次使用行和列索引导入，之后使用单元格名称导入数据。最后，将工作簿保存为[输出Excel文件](48496713.xlsx)。截图显示了示例代码对输出Excel文件的效果，供参考。

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
