---  
title: البحث عن البيانات أو البحث
type: docs  
weight: 50  
url: /ar/nodejs-cpp/find-or-search-data/  
description: تعلم كيفية العثور أو البحث عن خلايا تحتوي على بيانات محددة عبر واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.  
keywords: العثور على بيانات Node.js بواسطة C++، البحث عن بيانات Node.js بواسطة C++، العثور على خلايا تحتوي على صيغة Node.js بواسطة C++، البحث عن خلايا تحتوي على صيغة Node.js بواسطة C++، البحث عن بيانات أو صيغ باستخدام FindOptions في Node.js بواسطة C++، البحث عن بيانات أو صيغ باستخدام FindOptions في Node.js بواسطة C++، العثور على خلايا تحتوي على سلسلة معينة من القيمة أو الرقم Node.js بواسطة C++، البحث عن خلايا تحتوي على بيانات معينة  
---  

{{% alert color="primary" %}}  
يسمح Microsoft Excel للمستخدمين بالعثور على خلايا في ورقة العمل تحتوي على بيانات محددة.  
{{% /alert %}}  

## **العثور على الخلايا التي تحتوي على بيانات محددة**  

### **استخدام Microsoft Excel**  

يسمح Microsoft Excel للمستخدمين بالعثور على خلايا في ورقة العمل تحتوي على بيانات محددة. إذا قمت باختيار **تحرير** من قائمة **بحث** في Microsoft Excel، سترى مربع حوار يمكنك تحديد قيمة البحث فيها.  

هنا، نبحث عن القيمة "البرتقال". تسمح Aspose.Cells أيضًا للمطورين بالعثور على الخلايا في ورقة العمل التي تحتوي على القيم المحددة.  

### ** باستخدام Aspose.Cells for Node.js via C++**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) العديد من الطرق للعثور على خلايا تحتوي على بيانات تم تحديدها من قبل المستخدم، ومن بين هذه الطرق نوقش بشكل أكثر تفصيلًا أدناه.  

{{% alert color="primary" %}}  
تعيد جميع طرق البحث مراجع الخلايا التي تحتوي على البيانات المحددة.  
{{% /alert %}}  

## **العثور على الخلايا التي تحتوي على صيغة**  

يمكن للمطورين العثور على صيغة محددة في ورقة العمل من خلال استدعاء مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) وطريقة [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) الخاصة بها. عادةً، تقبل طريقة [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) ثلاثة معلمات:  

- **الكائن:** الكائن الذي تبحث عنه. يجب أن يكون النوع int أو double أو DateTime أو string أو bool.  
- **الخلية السابقة:** الخلية السابقة بنفس الكائن. يمكن تعيين هذا المعامل إلى null إذا كنت تبحث من البداية.  
- **FindOptions:** خيارات للبحث عن الكائن المطلوب.  

تستخدم الأمثلة أدناه بيانات ورقة العمل لممارسة طرق البحث:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **العثور على البيانات أو الصيغ باستخدام FindOptions**  

من الممكن العثور على القيم المحددة باستخدام طريقة [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) من مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) مع عدة [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). عادةً، تقبل طريقة [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) المعلمات التالية:  

- **قيمة البحث**, البيانات أو القيمة التي يتم البحث عنها.  
- **الخلية السابقة**, آخر خلية احتوت على نفس القيمة. يمكن تعيين هذه المعلمة إلى قيمة null عند البحث من البداية.  
- **خيارات البحث**, خيارات البحث.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **العثور على الخلايا التي تحتوي على قيمة سلسلة أو رقم محدد**  

من الممكن العثور على قيم نصية محددة من خلال استدعاء نفس طريقة [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) الموجودة في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) مع عدة [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

حدد خصائص [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) و [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-). يوضح رمز المثال التالي كيفية استخدام هذه الخصائص للعثور على خلايا تحتوي على عدد مختلف من النصوص في **البداية** أو في **المنتصف** أو في **النهاية** لنص الخلية.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **مواضيع متقدمة**  
- [العثور على الخلايا ذات النمط المحدد](/cells/ar/nodejs-cpp/find-cells-with-specific-style/)  
- [العثور عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة](/cells/ar/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/nodejs-cpp/search-data-using-original-values/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
