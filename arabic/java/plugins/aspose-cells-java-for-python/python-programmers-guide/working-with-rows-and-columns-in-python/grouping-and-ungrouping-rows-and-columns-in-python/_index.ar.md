---
title: تجميع وفك تجميع الصفوف والأعمدة في Python
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: تعرف على كيفية تجميع وفك تجميع الصفوف والأعمدة من خلال Aspose.Cells for Python عبر Java API.
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **إدارة التجميع والتفكيك للصفوف والأعمدة في Aspose.Cells for Python via Java**
###  **كيفية تجميع الصفوف والأعمدة في Python**
من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء أساليب groupRows وgroupColumns للمجموعة Cells. تأخذ كلتا الطريقتين المعلمات التالية:

- فهرس الصف/العمود الأول، الصف أو العمود الأول في المجموعة.
- فهرس الصف/العمود الأخير، آخر صف أو عمود في المجموعة.
- مخفي، وهو معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

**Python كود**

{{< highlight "python" >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
###  **كيفية فك تجميع الصفوف والأعمدة باستخدام Python**
قم بفك تجميع الصفوف أو الأعمدة المجمعة عن طريق استدعاء أساليب UngroupRows وUngroupColumns للمجموعة Cells. تأخذ كلتا الطريقتين نفس المعلمات:

- فهرس الصف أو العمود الأول، أول صف/عمود سيتم فك تجميعه.
- فهرس الصف أو العمود الأخير، آخر صف/عمود سيتم فك تجميعه.

**Python كود**

{{< highlight "python" >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
##  **تحميل كود التشغيل**
 تحميل**تجميع الصفوف والأعمدة وفك تجميعها (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
