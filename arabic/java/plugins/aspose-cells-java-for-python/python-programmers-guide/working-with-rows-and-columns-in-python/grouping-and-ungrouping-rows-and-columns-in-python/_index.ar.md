---
title: تجميع وفك تجميع الصفوف والأعمدة في Python
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: تعلم كيفية تجميع وفك تجميع الصفوف والأعمدة من خلال Aspose.Cells لـ Python عبر واجهة Java.
keywords: كيفية تجميع وفك تجميع الصفوف والأعمدة في Python عبر Java، تجميع الصفوف والأعمدة باستخدام Python عبر Java، تجميع وفك تجميع الصفوف والأعمدة بواسطة Python عبر Java. 
---

## **إدارة تجميع وفك تجميع الصفوف والأعمدة في Aspose.Cells لـ Python via Java**
### **كيفية تجميع الصفوف والأعمدة في Python**
يمكن تجميع الصفوف أو الأعمدة عن طريق استدعاء أساليب groupRows و groupColumns في مجموعة Cells. تأخذ كلا الطريقتين المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

**كود Python**

{{< highlight python >}}

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
### **كيفية فك تجميع الصفوف والأعمدة باستخدام Python**
إلغاء تجميع الصفوف أو الأعمدة المجمعة عن طريق استدعاء أساليب UngroupRows و UngroupColumns لمجموعة Cells. تأخذ كلا الطريقتين نفس المعلمات:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

**كود Python**

{{< highlight python >}}

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
## **تحميل رمز التشغيل**
تحميل **تجميع وفك تجميع الصفوف والأعمدة (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
