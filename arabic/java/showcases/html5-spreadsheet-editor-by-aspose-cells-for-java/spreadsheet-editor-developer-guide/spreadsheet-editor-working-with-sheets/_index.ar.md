---
title: محرر جداول البيانات - العمل مع الأوراق
type: docs
weight: 20
url: /ar/java/spreadsheet-editor-working-with-sheets/
---
**جدول المحتويات**

- [إضافة أوراق وإزالتها؟](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [إعادة تسمية الأوراق](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [التبديل بين الأوراق](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **إضافة أوراق وإزالتها؟**
Microsoft يسمح Excel بأوراق متعددة في ملف واحد. يسمح محرر جداول بيانات HTML5 للمستخدم بإضافة الأوراق وإزالتها. في علامة التبويب "جداول البيانات" ، لدينا قائمة منسدلة بالأوراق. الورقة المحددة هي الورقة التي يفتحها المحرر.

لإضافة ورقة جديدة:

1.  التبديل إلى**علامة التبويب "جداول البيانات"**.
1. انقر فوق زر ** + ** (زائد).

ستتم إضافة ورقة جديدة وسيتحول المحرر إليها.

لإزالة الورقة المحددة حاليًا:

1.  التبديل إلى**علامة التبويب "جداول البيانات"**.
1. انقر فوق زر ** - ** (ناقص).

ستتم إزالة الورقة المحددة حاليًا وسيتحول المحرر إلى آخر ورقة تم تحديدها.

![ما يجب القيام به: image_بديل_نص](4wgvmu8.png)

**كيف تعمل؟**

 عندما ينقر المستخدم على** + ** (زائد) و**-** تم النقر فوق الزر (ناقص) ، وحدة برامج JSF الخلفية**WorksheetView** يتعامل مع الأحداث باستخدام**WorksheetView.onAddNewSheet** و**WorksheetView.onRemoveActiveSheet **.
#### **WorksheetView.onAddNewSheet**
{{< highlight "java" >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight "java" >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **إعادة تسمية الأوراق**
لإعادة تسمية ورقة:

1.  التبديل إلى**علامة التبويب "جداول البيانات"**.
1. انقر فوق اسم الورقة في مربع النص لتحريره.
1. قم بتغيير اسم الورقة.
1. عند الانتهاء ، اضغط على مفتاح ENTER ، أو انقر في أي مكان خارج المربع.

ستتم إعادة تسمية الورقة.

![ما يجب القيام به: image_بديل_نص](4wgvmu8.png)

**كيف تعمل؟**

 عندما يتم تغيير قيمة مربع النص ، يتم التعامل مع الحدث على الخادم بواسطة وحدة برامج الواجهة الخلفية JSF**WorksheetView** باستخدام الطريقة**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **التبديل بين الأوراق**
للتبديل إلى ورقة أخرى:

1.  التبديل إلى**علامة التبويب "جداول البيانات"**.
1. حدد ورقة من القائمة المنسدلة.

سوف يتحول المحرر إلى الورقة المحددة.

![ما يجب القيام به: image_بديل_نص](4wgvmu8.png)

**كيف تعمل؟**

 عندما يتم تغيير قيمة محدد القائمة المنسدلة ، تتم معالجة الحدث على الخادم بواسطة وحدة برامج الواجهة الخلفية JSF**WorksheetView** باستخدام الطريقة**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
