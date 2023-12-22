---
title: العمل مع الصفوف والأعمدة GridWeb
type: docs
weight: 20
url: /ar/java/working-with-rows-and-columns-gridweb/
---
##  **إدراج الصفوف والأعمدة**
يشرح هذا الموضوع كيفية إدراج صفوف وأعمدة جديدة في ورقة العمل باستخدام Aspose.Cells.GridWeb API. يمكن إدراج الصفوف أو الأعمدة في أي موضع في ورقة العمل.
###  **إدراج الصفوف**
لإدراج صف في أي موضع في ورقة العمل:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج الويب أو الصفحة.
1. قم بالوصول إلى ورقة العمل التي تقوم بإضافة صفوف إليها.
1. قم بإدراج صف عن طريق تحديد فهرس الصف الذي سيتم إدراج الصف فيه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
###  **إدراج الأعمدة**
لإدراج عمود في أي موضع في ورقة العمل:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. قم بالوصول إلى ورقة العمل التي تقوم بإضافة أعمدة إليها.
1. قم بإدراج عمود عن طريق تحديد فهرس العمود الذي سيتم إدراج العمود فيه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

يمكنك أيضًا استخدام أساليب InsertRows()/insertColumns() لإدراج صفوف/أعمدة متعددة في أوراق العمل وفقًا لذلك.

{{% /alert %}} 
##  **حذف الصفوف والأعمدة**
يوضح هذا الموضوع كيفية حذف الصفوف والأعمدة من ورقة العمل باستخدام Aspose.Cells.GridWeb API. وبمساعدة هذه الميزة، يمكن للمطورين حذف الصفوف أو الأعمدة في وقت التشغيل.
###  **حذف الصفوف**
لحذف صف من ورقة العمل الخاصة بك:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. قم بالوصول إلى ورقة العمل التي تريد حذف الصفوف منها.
1. حذف صف من ورقة العمل عن طريق تحديد فهرس الصف الخاص به.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
###  **حذف الأعمدة**
لحذف عمود من ورقة العمل الخاصة بك:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج ويب أو صفحة.
1. قم بالوصول إلى ورقة العمل التي تريد حذف الأعمدة منها.
1. حذف عمود من ورقة العمل عن طريق تحديد فهرس العمود الخاص به.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
##  **تحديد ارتفاع الصف وعرض العمود**
في بعض الأحيان تكون قيم الخلايا أوسع من الخلية الموجودة فيها أو الموجودة على عدة أسطر. لا تكون هذه القيم مرئية بشكل كامل للمستخدمين إلا إذا قاموا بتغيير ارتفاع الصفوف والأعمدة وعرضها. Aspose.Cells.GridWeb يدعم بشكل كامل تحديد ارتفاعات الصف وعرض العمود. يناقش هذا الموضوع هذه الميزات بالتفصيل بمساعدة الأمثلة.
###  **العمل مع ارتفاعات الصف وعرض العمود**
####  **تحديد ارتفاع الصف**
لتعيين ارتفاع الصف:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج/صفحة الويب الخاصة بك.
1. قم بالوصول إلى مجموعة GridCells الخاصة بورقة العمل.
1. قم بتعيين ارتفاع جميع الخلايا في أي صف محدد.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb يقبل قياسات ارتفاع الصف وعرض العمود بالنقاط والبوصة والبكسل وما إلى ذلك.

{{% /alert %}} 

**الإخراج: تم ضبط ارتفاع الصف الأول على 50 نقطة** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
####  **تحديد عرض العمود**
لتعيين عرض العمود:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج/صفحة الويب الخاصة بك.
1. قم بالوصول إلى مجموعة GridCells الخاصة بورقة العمل.
1. قم بتعيين عرض جميع الخلايا في أي عمود محدد.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
##  **تخصيص رؤوس الصفوف والأعمدة**
مثل Microsoft Excel، Aspose.Cells. يستخدم GridWeb أيضًا الرؤوس القياسية أو التسميات التوضيحية للصفوف (أرقام مثل 1 و2 و3 وما إلى ذلك) والأعمدة (أبجدية مثل A وB وC وما إلى ذلك). Aspose.Cells.GridWeb يجعل من الممكن أيضًا تخصيص التسميات التوضيحية. يناقش هذا الموضوع تخصيص رؤوس الصفوف والأعمدة في وقت التشغيل باستخدام Aspose.Cells.GridWeb API.
###  **تخصيص رأس الصف**
لتخصيص الرأس أو التسمية التوضيحية للصف:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج/صفحة ويب.
1. الوصول إلى ورقة العمل في GridWorksheetCollection.
1. قم بتعيين التسمية التوضيحية لأي صف محدد.

**تم تخصيص رؤوس الصف 1 و 2** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
###  **تخصيص رأس العمود**
لتخصيص رأس العمود أو التسمية التوضيحية له:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج/صفحة ويب.
1. الوصول إلى ورقة العمل في GridWorksheetCollection.
1. قم بتعيين التسمية التوضيحية لأي عمود محدد.

**تم تخصيص رؤوس العمود 1 و2** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
##  **تجميد وإلغاء تجميد الصفوف والأعمدة**
يشرح هذا الموضوع كيفية تجميد الصفوف والأعمدة وإلغاء تجميدها. يسمح تجميد الأعمدة أو الصفوف للمستخدمين بإبقاء عناوين الأعمدة أو عناوين الصفوف مرئية أثناء التمرير إلى أجزاء أخرى من ورقة العمل. تعتبر هذه الميزة مفيدة للغاية عند العمل مع أوراق العمل التي تحتوي على كميات كبيرة من البيانات. عندما يقوم المستخدمون بالتمرير، يتم تمرير البيانات فقط لأسفل وتظل العناوين في مكانها، مما يجعل قراءة التاريخ أسهل. ميزة تجميد الأجزاء مدعومة فقط في Internet Explorer 6.0 أو أعلى.
###  **تجميد الصفوف والأعمدة**
لتجميد عدد محدد من الصفوف والأعمدة:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج/صفحة ويب.
1. الوصول إلى ورقة عمل.
1. تجميد عدد من الصفوف والأعمدة.

{{% alert color="primary" %}} 

 من الممكن أيضًا تجميد عدد محدد من الصفوف والأعمدة باستخدام الواجهة. انقر بزر الماوس الأيمن فوق الخلية التي تريد تجميد الصفوف والأعمدة فيها، ثم حددها**تجميد** من القائمة.

{{% /alert %}} 

**الصفوف والأعمدة في حالة تجميد** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
###  **إلغاء تجميد الصفوف والأعمدة**
لإلغاء تجميد الصفوف والأعمدة:

1. أضف عنصر التحكم Aspose.Cells.GridWeb إلى نموذج/صفحة ويب.
1. الوصول إلى ورقة عمل.
1. إلغاء تجميد الصفوف والأعمدة.

**ورقة عمل بعد فك التجميد** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
##  **حماية الصفوف والأعمدة**
يناقش هذا الموضوع بعض الأساليب لحماية الخلايا الموجودة في الصفوف والأعمدة من أي نوع من الإجراءات التي يقوم بها المستخدمون النهائيون. يمكن للمطورين تنفيذ هذه الحماية باستخدام تقنيتين: عن طريق جعل الخلايا في الصفوف والأعمدة للقراءة فقط، أو عن طريق تقييد خيارات قائمة سياق GridWeb.
###  **تقييد خيارات قائمة السياق**
يوفر GridWeb قائمة سياق يمكن للمستخدمين النهائيين استخدامها لتنفيذ العمليات على عنصر التحكم. توفر القائمة العديد من الخيارات لمعالجة الخلايا والصفوف والأعمدة.

**استكمال الخيارات السياقية** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

من الممكن تقييد أي نوع من العمليات من جانب العميل على الصفوف والأعمدة عن طريق تقييد الخيارات المتاحة في قائمة السياق. يمكن القيام بذلك عن طريق تعيين سمات EnableClientColumnOperations وEnableClientRowOperations لعنصر التحكم GridWeb إلى false. من الممكن أيضًا تقييد المستخدمين من تجميد الصفوف والأعمدة عن طريق تعيين سمة EnableClientFreeze لعنصر التحكم GridWeb إلى false.

**قائمة السياق بعد تقييد خيارات الصفوف والأعمدة** 

![ما يجب القيام به:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
