---
title: عرض أو إخفاء خطوط الشبكة في Python
type: docs
weight: 10
url: /ar/java/display-or-hide-gridlines-in-python/
---
## **Aspose.Cells - عرض اخفاء خطوط الشبكة**
### **إخفاء خطوط الشبكة**
 لإخفاء ورقة العمل باستخدام**Aspose.Cells Java لروبي** ، مكالمة**displayhidegridlines** وحدة.

**Python كود**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **جعل خطوط الشبكة مرئية**
لجعل خطوط الشبكة مرئية ، استخدم طريقة setGridlinesVisible (true) لفئة ورقة العمل.

**Python كود**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**DisplayHideGridlines (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
