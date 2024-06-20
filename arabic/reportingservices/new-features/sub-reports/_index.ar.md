---
title: التقارير الفرعية
type: docs
weight: 20
url: /ar/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

لقد قمنا بدعم تضمين تقرير فرعي في صف مجموعة الجدول. التنسيق هو:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **مثال**
**تقرير فرعي في جدول** 

![todo:image_alt_text](sub-reports_1.png)

في المثال، اسم التقرير الفرعي هو "تفاصيل أمر البيع". لديه معلمة واحدة، *رقم أمر البيع*. قيمة المعلمة هي *EmpSalesDetail.SalesOrderNumber.*
#### **قيود على استخدام التقارير الفرعية**
- يجب تصميم التقرير الفرعي باستخدام أداة Aspose.Cells.Reporting Services Designer.
- يمكن تضمين التقرير الفرعي فقط في صف مجموعة الجدول وصف المجموعة لا يمكن أن يحتوي على عناصر أخرى إلا التقرير الفرعي. غير مسموح تضمين تقرير فرعي في صفوف التفاصيل الخاصة بالجدول أو صفوف التذييل.
- حاليًا، لا يتم دعم تضمين مستوى أكثر من واحد. لا يمكن للتقرير الفرعي أن يحتوي على تقرير مضمن.
