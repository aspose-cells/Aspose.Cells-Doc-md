---  
title: كيفية إدارة التواريخ والأوقات
type: docs  
weight: 600  
url: /ar/nodejs-cpp/how-to-manage-dates-and-times/  
description: تعلم كيف تدير التواريخ والأوقات من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.  
keywords: كيفية إدارة التواريخ والأوقات، نظام التاريخ 1900، نظام التاريخ 1904، ضبط التواريخ والأوقات، الحصول على التواريخ والأوقات، إدارة التواريخ والأوقات، تخزين التواريخ والأوقات في إكسل، عرض التواريخ والأوقات في الخلايا.  
---  

## **كيفية تخزين التواريخ والأوقات في إكسل**  
يتم تخزين التواريخ والأوقات في الخلايا على أنها أرقام. وبالتالي، قيم الخلايا التي تحتوي على تواريخ وأوقات تكون من نوع رقمي. الرقم الذي يحدد تاريخًا ووقتًا يتكون من مكونات التاريخ (الجزء الصحيح) والوقت (الجزء الكسري). يُرجع خاصية Cell.DoubleValue هذا الرقم.  

## **كيفية عرض التواريخ والأوقات في Aspose.Cells**  
لعرض رقم كتاريخ ووقت، قم بتطبيق تنسيق التاريخ والوقت المطلوب على خلية عبر خاصية [Style.getNumber()](https://reference.aspose.com/cells/nodejs-cpp/style/#getNumber--) أو [Style.Custom]()، تُعيد خاصية CellValue.DateTimeValue كائن DateTime الذي يحدد التاريخ والوقت الذي يمثله الرقم الموجود في الخلية.  
<br>  
<image src="1.png" width="70%" />  

## **كيفية التبديل بين نظامي التواريخ في Aspose.Cells**  
تخزن برنامج MS-Excel التواريخ كأرقام تسمى قيم متسلسلة. قيمة متسلسلة هي عدد صحيح هو عدد الأيام المنقضية من اليوم الأول في نظام التاريخ. يدعم Excel الأنظمة التالية للقيم المتسلسلة للتواريخ:   

1. نظام التاريخ 1900. اليوم الأول هو 1 يناير 1900، وقيمته المتسلسلة هي 1. أما آخر يوم فهو 31 ديسمبر 9999، وقيمته المتسلسلة هي 2،958،465. يُستخدم هذا النظام في جدول العمل افتراضيًا.  
1. نظام التاريخ 1904. التاريخ الأول هو 1 يناير 1904، وقيمته التسلسلية 0. والتاريخ الأخير هو 31 ديسمبر 9999، وقيمته التسلسلية هي 2,957,003. لاستخدام هذا النظام في مصنف العمل، قم بضبط خاصية [WorkbookSettings.getDate1904()](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getDate1904--) على true.  

تُظهر هذا المثال أن القيم المتسلسلة المخزنة في نفس التاريخ في أنظمة تاريخ مختلفة هي مختلفة.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SwitchTwoDateSystems.js" >}}


النتيجة المخرجة:  
```  
A1 is Numeric Value: 45253  
use The 1904 date system====================  
A2 is Numeric Value: 43791  
```  

## **كيفية تعيين قيمة تاريخ ووقت في Aspose.Cells**  
يُعين هذا المثال قيمة DateTime في الخلية A1 و A2، يضبط تنسيق مخصص ل A1 وتنسيق رقمي ل A2، ثم يخرج أنواع القيمة.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-SetDateTimeValue.js" >}}


النتيجة المخرجة:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
```  

## **كيفية الحصول على قيمة تاريخ ووقت في Aspose.Cells**  
يُعين هذا المثال قيمة DateTime في الخلية A1 و A2، يضبط تنسيق مخصص ل A1 وتنسيق رقمي ل A2، يتحقق من أنواع القيمة في الخليتين، ثم يخرج قيمة DateTime وسلسلة مُنسَقة.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DatesAndTimes-GetDateTimeValue.js" >}}


النتيجة المخرجة:  
```  
A1 is Numeric Value: True  
Cell A1 contains a DateTime value.  
A1 DateTime Value: 11/23/2023 5:59:09 PM  
A1 DateTime String Value: 11-23-23 17:59:09  
A2 is Numeric Value: True  
Cell A2 contains a DateTime value.  
A2 DateTime Value: 11/23/2023 5:59:09 PM  
A2 DateTime String Value: 11/23/2023 17:59  
```  

