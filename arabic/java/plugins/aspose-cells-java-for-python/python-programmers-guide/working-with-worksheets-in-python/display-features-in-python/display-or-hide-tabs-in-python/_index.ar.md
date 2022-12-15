---
title: عرض أو إخفاء علامات التبويب في Python
type: docs
weight: 30
url: /ar/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - عرض إخفاء علامات التبويب**
### **علامات التبويب الاختباء**
 لإخفاء علامات التبويب باستخدام ملفات**Aspose.Cells Java لروبي** ، مكالمة**عرض** وحدة.

**Python كود**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **جعل علامات التبويب مرئية**
اجعل علامات التبويب مرئية باستخدام أسلوب setSheetTabBarHidden (false) لفئة المصنف.

**Python كود**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**Hello World (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
