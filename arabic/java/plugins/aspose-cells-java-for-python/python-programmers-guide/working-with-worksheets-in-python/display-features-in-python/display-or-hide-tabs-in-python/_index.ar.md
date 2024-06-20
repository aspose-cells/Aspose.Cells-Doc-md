---
title: عرض أو إخفاء علامات التبويب في Python
type: docs
weight: 30
url: /ar/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - عرض إخفاء علامات التبويب**
### **إخفاء علامات التبويب**
لإخفاء علامات التبويب باستخدام **Aspose.Cells جافا لـ Ruby**، اتصل بوحدة **displayhidetabs**.

**كود Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **جعل علامات التبويب مرئية**
اجعل علامات التبويب مرئية بواسطة الطبقة المحورية مع طريقة *setSheetTabBarHidden(false)* من فئة *Workbook*.

**كود Python**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **مرحبًا بالعالم (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
