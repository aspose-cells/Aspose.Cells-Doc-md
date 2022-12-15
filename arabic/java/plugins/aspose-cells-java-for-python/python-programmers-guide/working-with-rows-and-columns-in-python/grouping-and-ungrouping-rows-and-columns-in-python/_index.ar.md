---
title: تجميع وإلغاء تجميع الصفوف والأعمدة في Python
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns-in-python/
---
## **Aspose.Cells - إدارة المجموعة للصفوف والأعمدة**
### **تجميع الصفوف والأعمدة**
من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء التابعين groupRows و groupColumns للمجموعة Cells. تأخذ كلتا الطريقتين المعلمات التالية:

- أول صف / فهرس العمود ، أول صف أو عمود في المجموعة.
- فهرس الصف / العمود الأخير ، الصف أو العمود الأخير في المجموعة.
- مخفي ، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف / الأعمدة بعد التجميع أم لا.

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
### **فك تجميع الصفوف والأعمدة**
قم بفك تجميع الصفوف أو الأعمدة المجمعة عن طريق استدعاء أساليب UngroupRows و UngroupColumns للمجموعة Cells. تأخذ كلتا الطريقتين نفس المعلمات:

- الصف الأول أو فهرس العمود ، الصف / العمود الأول المراد فك تجميعه.
- فهرس الصف أو العمود الأخير ، الصف / العمود الأخير المراد فك تجميعه.

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
## **تحميل كود الجري**
 تحميل**تجميع وفك تجميع الصفوف والأعمدة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
