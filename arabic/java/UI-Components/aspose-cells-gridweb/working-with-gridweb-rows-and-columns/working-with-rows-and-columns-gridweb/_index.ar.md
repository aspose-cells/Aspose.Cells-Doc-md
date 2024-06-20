---
title: العمل مع الصفوف والأعمدة في GridWeb
type: docs
weight: 20
url: /ar/java/working-with-rows-and-columns-gridweb/
---

## **إدراج الصفوف والأعمدة**
يشرح هذا الموضوع كيفية إدراج صفوف وأعمدة جديدة في ورقة عمل باستخدام واجهة برمجة تطبيقات Aspose.Cells.GridWeb. يمكن إدراج الصفوف أو الأعمدة في أي موقع في ورقة العمل.
### **إدراج الصفوف**
لإدراج صف في أي موضع في ورقة العمل:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى النموذج الويب أو الصفحة.
1. الوصول إلى ورقة العمل التي تقوم بإضافة الصفوف إليها.
1. إدراج صف عن طريق تحديد فهرس الصف الذي سيتم إدراج الصف فيه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **إدراج الأعمدة**
لإدراج عمود في أي موضع في ورقة العمل:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. الوصول إلى ورقة العمل التي تقوم بإضافة الأعمدة إليها.
1. إدراج عمود عن طريق تحديد فهرس العمود الذي سيتم إدراج العمود فيه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

يمكنك أيضًا استخدام أساليب insertRows()/insertColumns() لإدراج صفوف/أعمدة متعددة في ورق العمل وفقًا لذلك.

{{% /alert %}} 
## **حذف الصفوف والأعمدة**
يوضح هذا الموضوع كيفية حذف الصفوف والأعمدة من ورقة العمل باستخدام واجهة برمجة التطبيقات Aspose.Cells.GridWeb. بمساعدة هذه الميزة ، يمكن للمطورين حذف الصفوف أو الأعمدة أثناء التشغيل.
### **حذف الصفوف**
لحذف صف من ورقة العمل الخاصة بك:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. الوصول إلى ورقة العمل التي تريد حذف الصفوف منها.
1. حذف صف من ورقة العمل عن طريق تحديد فهرس صفه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **حذف الأعمدة**
لحذف عمود من ورقة العمل الخاصة بك:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. الوصول إلى ورقة العمل التي تريد حذف الأعمدة منها.
1. حذف عمود من ورقة العمل عن طريق تحديد فهرس العمود الخاص به.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **تعيين ارتفاع الصف وعرض العمود**
في بعض الأحيان تكون قيم الخانات أوسع من الخانة التي تتواجد فيها أو تكون على عدة أسطر. هذه القيم لا تكون مرئية تماماً للمستخدمين ما لم يقوموا بتغيير ارتفاع الأسطر وعرض الأعمدة. تدعم Aspose.Cells.GridWeb تماماً ضبط ارتفاع الأسطر وعرض الأعمدة. يتناول هذا الموضوع هذه الميزات بالتفصيل بمساعدة الأمثلة.
### **العمل مع ارتفاعات الصفوف وأعراض الأعمدة**
#### **ضبط ارتفاع الصف**
لضبط ارتفاع صف:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج الويب أو الصفحة الخاصة بك.
1. الوصول إلى مجموعة GridCells في ورقة العمل.
1. ضبط ارتفاع جميع الخلايا في أي صف محدد.

{{% alert color="primary" %}} 

تقبل Aspose.Cells.GridWeb قياسات ارتفاع الصف وعرض العمود في نقاط، بوصة، بيكسل، إلخ.

{{% /alert %}} 

**الناتج: تم ضبط ارتفاع الصف الأول إلى 50 نقطة** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **ضبط عرض العمود**
لضبط عرض عمود:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج الويب أو الصفحة الخاصة بك.
1. الوصول إلى مجموعة GridCells في ورقة العمل.
1. تعيين عرض جميع الخلايا في أي عمود محدد.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **تخصيص رؤوس الأسطر والأعمدة**
مثل Microsoft Excel، يستخدم Aspose.Cells.GridWeb أيضًا رؤوس أو عناوين قياسية للصفوف (أرقام مثل 1، 2، 3 وهكذا) والأعمدة (أبجدية مثل A، B، C وهكذا). يجعل Aspose.Cells.GridWeb أيضاً من الممكن تخصيص العناوين. يتناول هذا الموضوع تخصيص رؤوس الأسطر والأعمدة في وقت التشغيل باستخدام واجهة برمجة تطبيقات Aspose.Cells.GridWeb.
### **تخصيص رأس الصف**
لتخصيص رأس أو تسمية صف:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى صفحة ويب/ النموذج.
1. قم بالوصول إلى ورقة العمل في مجموعة GridWorksheetCollection.
1. قم بتعيين التسمية لأي صف محدد.

تم تخصيص رؤوس الصفين 1 و 2 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **تخصيص رأس العمود**
لتخصيص الرأس أو التسمية لعمود:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى صفحة ويب/ النموذج.
1. قم بالوصول إلى ورقة العمل في مجموعة GridWorksheetCollection.
1. قم بتعيين التسمية لأي عمود محدد.

تم تخصيص رؤوس العمودين 1 و 2 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **تجميد وفك تجميد الصفوف والأعمدة**
يشرح هذا الموضوع كيفية تجميد وإلغاء تجميد الصفوف والأعمدة. يسمح تجميد الأعمدة أو الصفوف للمستخدمين بالاحتفاظ بعناوين الأعمدة أو عناوين الصفوف مرئية أثناء التمرير إلى أجزاء أخرى من ورقة العمل. هذه الميزة مفيدة للغاية عند العمل مع ورق العمل الذي يحتوي على مجلدات كبيرة من البيانات. عندما يقوم المستخدمون بالتمرير، يتم التمرير فقط للبيانات، وتبقى العناوين في مكانها، مما يجعل البيانات أسهل في القراءة. ميزة تجميد الأجزاء معتمدة فقط في Internet Explorer 6.0 أو أعلى.
### **تجميد الصفوف والأعمدة**
لتجميد عدد معين من الصفوف والأعمدة:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى صفحة ويب/ النموذج.
1. الوصول إلى ورقة العمل.
1. تجميد عدد من الصفوف والأعمدة.

{{% alert color="primary" %}} 

من الممكن أيضًا تجميد عدد معين من الصفوف والأعمدة باستخدام الواجهة. انقر بزر الماوس الأيمن في الخلية التي تريد تجميد الصفوف والأعمدة بها وحدد **تجميد** من القائمة.

{{% /alert %}} 

الصفوف والأعمدة في حالة مجمدة 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **إلغاء تجميد الصفوف والأعمدة**
لإلغاء تجميد الصفوف والأعمدة:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى صفحة ويب/ النموذج.
1. الوصول إلى ورقة العمل.
1. إلغاء تجميد الصفوف والأعمدة.

**ورقة العمل بعد إلغاء التجميد** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **حماية الصفوف والأعمدة**
يناقش هذا الموضوع بعض التقنيات لحماية الخلايا في الصفوف والأعمدة من أي نوع من الإجراءات التي يقوم بها المستخدمون النهائيون. يمكن للمطورين تنفيذ هذه الحماية باستخدام تقنيتين: عن طريق جعل الخلايا في الصفوف والأعمدة للقراءة فقط، أو عن طريق تقييد خيارات قائمة السياق في GridWeb.
### **تقييد خيارات القائمة السياقية**
يوفر GridWeb قائمة سياق يمكن للمستخدمين النهائيين استخدامها لأداء العمليات على العنصر التحكم. توفر القائمة العديد من الخيارات للتلاعب بالخلايا والصفوف والأعمدة.

**خيارات سياقية كاملة** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

من الممكن تقييد أي نوع من العمليات على الجانب العميلي على الصفوف والأعمدة عن طريق تقييد الخيارات المتاحة في قائمة السياق. يمكن القيام بذلك عن طريق ضبط سمات EnableClientColumnOperations و EnableClientRowOperations لعنصر التحكم GridWeb على false. كما يمكن تقييد المستخدمين من تجميد الصفوف والأعمدة عن طريق ضبط سمة EnableClientFreeze لعنصر التحكم GridWeb على false.

**قائمة سياقية بعد تقييد خيارات الصف والعمود** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
