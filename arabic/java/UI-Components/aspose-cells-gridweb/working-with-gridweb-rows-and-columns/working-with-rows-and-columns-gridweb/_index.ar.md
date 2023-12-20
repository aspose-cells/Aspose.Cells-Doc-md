---
title: العمل مع GridWeb الصفوف والأعمدة
type: docs
weight: 20
url: /ar/java/working-with-rows-and-columns-gridweb/
---
## **إدراج صفوف وأعمدة**
يشرح هذا الموضوع كيفية إدراج صفوف وأعمدة جديدة في ورقة العمل باستخدام Aspose.Cells.GridWeb API. يمكن إدراج صفوف أو أعمدة في أي موضع بورقة العمل.
### **إدراج الصفوف**
لإدراج صف في أي موضع في ورقة العمل:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج أو صفحة ويب.
1. قم بالوصول إلى ورقة العمل التي تضيف صفوفًا إليها.
1. أدخل صفًا عن طريق تحديد فهرس الصف حيث سيتم إدراج الصف.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **إدراج الأعمدة**
لإدراج عمود في أي موضع في ورقة العمل:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج أو صفحة ويب.
1. قم بالوصول إلى ورقة العمل التي تضيف أعمدة إليها.
1. أدخل عمودًا عن طريق تحديد فهرس العمود حيث سيتم إدراج العمود.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

يمكنك أيضًا استخدام أساليب insertRows () / insertColumns () لإدراج صفوف / أعمدة متعددة في أوراق العمل وفقًا لذلك.

{{% /alert %}} 
## **حذف الصفوف والأعمدة**
يوضح هذا الموضوع كيفية حذف الصفوف والأعمدة من ورقة العمل باستخدام Aspose.Cells.GridWeb API. بمساعدة هذه الميزة ، يمكن للمطورين أخذ حذف صفوف أو أعمدة في وقت التشغيل.
### **حذف الصفوف**
لحذف صف من ورقة العمل الخاصة بك:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج أو صفحة ويب.
1. قم بالوصول إلى ورقة العمل التي تريد حذف الصفوف منها.
1. احذف صفًا من ورقة العمل عن طريق تحديد فهرس الصف الخاص به.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **حذف الأعمدة**
لحذف عمود من ورقة العمل الخاصة بك:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج أو صفحة ويب.
1. قم بالوصول إلى ورقة العمل التي تريد حذف الأعمدة منها.
1. احذف عمودًا من ورقة العمل عن طريق تحديد فهرس العمود الخاص به.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **ضبط ارتفاع الصف وعرض العمود**
في بعض الأحيان تكون قيم الخلية أعرض من الخلية الموجودة فيها أو تكون في عدة أسطر. هذه القيم ليست مرئية بالكامل للمستخدمين ما لم يغيروا ارتفاع وعرض الصفوف والأعمدة. Aspose.Cells.GridWeb يدعم بشكل كامل تحديد ارتفاع الصف وعرض العمود. يناقش هذا الموضوع هذه الميزات بالتفصيل بمساعدة الأمثلة.
### **العمل مع ارتفاع الصفوف وعرض العمود**
#### **ضبط ارتفاع الصف**
لتعيين ارتفاع الصف:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج / صفحة الويب الخاصة بك.
1. قم بالوصول إلى مجموعة GridCells الخاصة بورقة العمل.
1. عيّن ارتفاع جميع الخلايا في أي صف محدد.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb يقبل قياسات ارتفاع الصف وعرض العمود بالنقاط ، البوصات ، البكسل ، إلخ.

{{% /alert %}} 

**المخرجات: تم ضبط ارتفاع الصف الأول على 50 نقطة** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **ضبط عرض العمود**
لتعيين عرض العمود:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج / صفحة الويب الخاصة بك.
1. قم بالوصول إلى مجموعة GridCells الخاصة بورقة العمل.
1. قم بتعيين عرض جميع الخلايا في أي عمود محدد.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **تخصيص رؤوس الصفوف والأعمدة**
مثل Microsoft Excel ، Aspose.Cells. يستخدم موقع GridWeb أيضًا الرؤوس أو التسميات التوضيحية القياسية للصفوف (أرقام مثل 1 و 2 و 3 وما إلى ذلك) والأعمدة (أبجديًا مثل A و B و C وما إلى ذلك). Aspose.Cells.GridWeb يجعل من الممكن أيضًا تخصيص التسميات التوضيحية. يناقش هذا الموضوع تخصيص رؤوس الصفوف والأعمدة في وقت التشغيل باستخدام Aspose.Cells.GridWeb API.
### **تخصيص رأس الصف**
لتخصيص العنوان أو التسمية التوضيحية لصف:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج / صفحة ويب.
1. قم بالوصول إلى ورقة العمل في GridWorksheetCollection.
1. قم بتعيين التسمية التوضيحية لأي صف محدد.

**تم تخصيص رؤوس الصف 1 و 2** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **تخصيص رأس العمود**
لتخصيص رأس العمود أو التسمية التوضيحية له:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج / صفحة ويب.
1. قم بالوصول إلى ورقة العمل في GridWorksheetCollection.
1. قم بتعيين التسمية التوضيحية لأي عمود محدد.

**تم تخصيص رؤوس العمود 1 و 2** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **تجميد وإلغاء تجميد الصفوف والأعمدة**
يشرح هذا الموضوع كيفية تجميد وإلغاء تجميد الصفوف والأعمدة. يتيح تجميد الأعمدة أو الصفوف للمستخدمين الاحتفاظ بعناوين الأعمدة أو عناوين الصفوف مرئية أثناء قيامهم بالتمرير إلى أجزاء أخرى من ورقة العمل. هذه الميزة مفيدة للغاية عند التعامل مع أوراق العمل التي تحتوي على كميات كبيرة من البيانات. عندما يقوم المستخدمون بالتمرير يتم تمرير البيانات فقط لأسفل وتظل العناوين في مكانها ، مما يسهل قراءة التاريخ. ميزة تجميد الأجزاء مدعومة فقط في Internet Explorer 6.0 أو إصدار أحدث.
### **تجميد الصفوف والأعمدة**
لتجميد عدد معين من الصفوف والأعمدة:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج / صفحة ويب.
1. قم بالوصول إلى ورقة العمل.
1. قم بتجميد عدد من الصفوف والأعمدة.

{{% alert color="primary" %}} 

 من الممكن أيضًا تجميد عدد محدد من الصفوف والأعمدة باستخدام الواجهة. انقر بزر الماوس الأيمن فوق الخلية حيث تريد تجميد الصفوف والأعمدة وتحديدها**تجميد** من القائمة.

{{% /alert %}} 

**الصفوف والأعمدة في حالة التجميد** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **إلغاء تجميد الصفوف والأعمدة**
لإلغاء تجميد الصفوف والأعمدة:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج / صفحة ويب.
1. قم بالوصول إلى ورقة العمل.
1. إلغاء تجميد الصفوف والأعمدة.

**ورقة عمل بعد فك التجميد** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **حماية الصفوف والأعمدة**
يناقش هذا الموضوع بعض الأساليب لحماية الخلايا في الصفوف والأعمدة من أي نوع من الإجراءات التي يقوم بها المستخدمون النهائيون. يمكن للمطورين تنفيذ هذه الحماية باستخدام تقنيتين: عن طريق جعل الخلايا في الصفوف والأعمدة للقراءة فقط ، أو عن طريق تقييد خيارات قائمة سياق GridWeb.
### **تقييد خيارات قائمة السياق**
يوفر GridWeb قائمة سياق يمكن للمستخدمين النهائيين استخدامها لأداء العمليات على عنصر التحكم. توفر القائمة العديد من الخيارات لمعالجة الخلايا والصفوف والأعمدة.

**خيارات سياقية كاملة** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_6.png)

من الممكن تقييد أي نوع من العمليات من جانب العميل في الصفوف والأعمدة من خلال تقييد الخيارات المتاحة في قائمة السياق. يمكن القيام بذلك عن طريق تعيين خصائص EnableClientColumnOperations و EnableClientRowOperations لعنصر التحكم GridWeb إلى false. من الممكن أيضًا تقييد المستخدمين من تجميد الصفوف والأعمدة عن طريق تعيين سمة EnableClientFreeze للتحكم في GridWeb إلى false.

**قائمة السياق بعد تقييد خيارات الصفوف والعمود** 

![ما يجب القيام به: image_بديل_نص](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
