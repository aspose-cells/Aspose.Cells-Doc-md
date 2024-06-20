---
title: Python da Satır ve Sütunları Gruplama ve Gruplamadan Çıkarma
type: docs
weight: 40
url: /tr/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Aspose.Cells for Python Via Java API sı aracılığıyla Satır ve Sütunları Gruplama ve Gruplamadan Çıkarmayı Öğrenin.
keywords: Python Via Java ile Satır ve Sütunları Gruplama ve Gruplamadan Çıkarma, Python Via Java Kullanarak Satır ve Sütunları Gruplama, Python Via Java da Satır ve Sütunları Gruplama. 
---

## **Python'da Aspose.Cells ile Satır ve Sütun Gruplama ve Gruplamayı Yönetme via Java**
### **Python'da Satırları ve Sütunları Gruplama**
Cells koleksiyonunun groupRows ve groupColumns yöntemlerini çağırarak satırları veya sütunları gruplamak mümkündür. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır/sütun indeksi, grup içindeki ilk satır veya sütun.
- Son satır/sütun indeksi, grup içindeki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.

**Python Kodu**

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
### **Python Kullanarak Satırları ve Sütunları Gruplandırma**
Cells koleksiyonunun UngroupRows ve UngroupColumns yöntemlerini çağırarak gruplanmış satırları veya sütunları çıkarabilirsiniz. Her iki yöntem de aşağıdaki parametreleri alır:

- İlk satır veya sütun dizini, ayrılmak istenen ilk satır/sütun.
- Son satır veya sütun dizini, ayrılmak istenen son satır/sütun.

**Python Kodu**

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
## **Çalışan Kodu İndir**
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Grup ve Grupsuz Sıraları ve Sütunları İndirin (Aspose.Cells)**:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
