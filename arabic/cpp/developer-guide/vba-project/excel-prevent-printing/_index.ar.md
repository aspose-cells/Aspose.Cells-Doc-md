---  
title: كيفية منع المستخدمين من طباعة ملف إكسل باستخدام C++  
linktitle: كيفية منع المستخدمين من طباعة ملف Excel  
type: docs  
weight: 600  
url: /ar/cpp/how-to-prevent-printing-excel/  
description: تعلم كيفية منع المستخدمين من طباعة إكسل عبر API Aspose.Cells for C++.  
keywords: طباعة excel، منع طباعة excel، كيفية منع المستخدمين من طباعة excel، excel منع الطباعة، منع طباعة دفتر العمل، منع المستخدمين من طباعة الدفتر الكامل بـ VBA.  
---  

## **سيناريوهات الاستخدام المحتملة**  
في عملنا اليومي، قد توجد معلومات هامة في ملف إكسل؛ ومن أجل حماية البيانات الداخلية من الانتشار، لن تسمح الشركة بطباعتها. ستوضح لك هذه الوثيقة كيفية منع الآخرين من طباعة ملفات إكسل.  

## **كيفية منع المستخدمين من طباعة الملف في برنامج MS-Excel**  
يمكنك تطبيق رمز VBA التالي لحماية ملفاتك المحددة من الطباعة.  
1. افتح جدول العمل الذي لا تسمح للآخرين بطباعته.  
1. حدد علامة التبويب "مطور" في شريط إكسل ثم انقر على زر "عرض الكود" في قسم "التحكمات". أو، يمكنك الضغط مع الاستمرار على مفاتيح ALT + F11 لفتح نافذة Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. ثم في مستكشف المشاريع الأيسر، انقر نقرًا مزدوجًا على ThisWorkbook لفتح الوحدة وإضافة بعض رموز VBA.  
<br>  
<img src="2.png" width=70% />  
1. ثم قم بحفظ وإغلاق هذا الكود، وعد إلى المصنف، وعند طباعة الملف النموذجي، لن يُسمح بالطباعة، وستظهر لك رسالة تحذيرية التالية:  
<br>  
<img src="3.png" width=70% />  

## **كيفية منع المستخدمين من طباعة ملف إكسل باستخدام Aspose.Cells for C++**  

توضح الشفرة النموذجية التالية كيفية منع المستخدمين من طباعة ملف إكسل:  

1. قم بتحميل [ملف العينة](sample.xlsx).  
1. الحصول على كائن VbaModuleCollection من خاصية VbaProject للمصنف.  
1. الحصول على كائن VbaModule عبر اسم "ThisWorkbook".  
1. ضبط خاصية الرموز لكائن VbaModule.  
1. حفظ ملف العينة إلى [تنسيق xlsm](out.xlsm).  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook from existing Excel file
    Workbook workbook(u"Sample.xlsx");

    // Access VBA project modules
    VbaModuleCollection modules = workbook.GetVbaProject().GetModules();

    // Set VBA code for 'ThisWorkbook' module
    modules.Get(u"ThisWorkbook").SetCodes(u"Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

    // Save the workbook as macro-enabled Excel file
    workbook.Save(u"out.xlsm");

    std::cout << "VBA code added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
