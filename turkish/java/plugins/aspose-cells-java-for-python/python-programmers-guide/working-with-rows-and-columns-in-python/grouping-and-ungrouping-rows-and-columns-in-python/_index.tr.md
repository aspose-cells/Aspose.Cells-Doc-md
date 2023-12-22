---
title: Python'de Satırları ve Sütunları Gruplama ve Grubu Çözme
type: docs
weight: 40
url: /tr/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java API aracılığıyla Satırları ve Sütunları nasıl gruplandıracağınızı ve gruplarını çözeceğinizi öğrenin.
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **Aspose.Cells for Python via Java'de Satır ve Sütunların Grup ve Gruplandırma Yönetimi**
###  **Python'de Satırları ve Sütunları Gruplandırma**
Cells koleksiyonunun groupRows ve groupColumns yöntemlerini çağırarak satırları veya sütunları gruplandırmak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun dizini, gruptaki ilk satır veya sütun.
- Son satır/sütun dizini, gruptaki son satır veya sütun.
- Gizlidir, gruplandırma sonrasında satırların/sütunların gizlenip gizlenmeyeceğini belirten bir Boolean parametresidir.

**Python Kodu**

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
###  **Python'i kullanarak Satırların ve Sütunların Grubunu Çözme**
Cells koleksiyonunun UngroupRows ve UngroupColumns yöntemlerini çağırarak gruplandırılmış satırların veya sütunların grubunu çözün. Her iki yöntem de aynı parametreleri alır:

- İlk satır veya sütun dizini, gruplandırılacak ilk satır/sütun.
- Son satır veya sütun dizini, grubu çözülecek son satır/sütun.

**Python Kodu**

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
##  **Çalışan Kodu İndir**
 İndirmek**Satırları ve Sütunları Gruplama ve Grubu Çözme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
