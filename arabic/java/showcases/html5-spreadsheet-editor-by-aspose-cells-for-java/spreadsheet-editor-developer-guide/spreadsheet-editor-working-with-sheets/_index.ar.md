---
title: محرر جدول بيانات  العمل مع الأوراق
type: docs
weight: 20
url: /ar/java/spreadsheet-editor-working-with-sheets/
---

جدول المحتويات

- [إضافة وإزالة الأوراق؟](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [إعادة تسمية الأوراق](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [التبديل بين الأوراق](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **إضافة وإزالة الأوراق؟**
يسمح Microsoft Excel بوجود عدة أوراق في ملف واحد. يسمح محرر ويب لجداول البيانات HTML5 للمستخدم بإضافة وإزالة الأوراق. في علامة الأوراق لدينا قائمة منسدلة من الأوراق. تكون الورقة المحددة هي التي يتم فتحها بواسطة المحرر.

لإضافة ورقة جديدة:

1. التبديل إلى **علامة التبويب Sheets**.
1. انقر على زر **+** (زائد).

سيتم إضافة ورقة جديدة وسيتم تبديل المحرر إليها.

لإزالة الورقة المحددة حاليًا:

1. التبديل إلى **علامة التبويب Sheets**.
1. انقر على زر **-** (ناقص).

ستُزال الورقة المحددة حاليًا وسيتم تبديل المحرر إلى آخر محدد.

![todo:image_alt_text](4wgvmu8.png)

**كيف يعمل هذا؟**

عندما ينقر المستخدم على أزرار **+** (زائد) و **-** (ناقص)، يقوم فول الوجه الخلفي لـ JSF بيان الورقة **WorksheetView** بمعالجة الأحداث باستخدام **WorksheetView.onAddNewSheet** و **WorksheetView.onRemoveActiveSheet** الأساليب.
#### **WorksheetView.onAddNewSheet**
{{< highlight java >}}

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
{{< highlight java >}}

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

1. التبديل إلى **علامة التبويب Sheets**.
1. انقر على اسم الورقة في مربع النص لتحريره.
1. قم بتغيير اسم الورقة.
1. عند الانتهاء، اضغط مفتاح ENTER، أو انقر في أي مكان خارج المربع.

سيتم إعادة تسمية الورقة.

![todo:image_alt_text](4wgvmu8.png)

**كيف يعمل هذا؟**

عندما يتم تغيير قيمة مربع النص، يتم التعامل مع الحدث على الخادم باستخدام كائن خلفي JSF **WorksheetView** بواسطة الطريقة **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

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

1. التبديل إلى **علامة التبويب Sheets**.
1. حدد ورقة من القائمة المنسدلة.

سيقوم المحرر بالتبديل إلى الورقة المحددة.

![todo:image_alt_text](4wgvmu8.png)

**كيف يعمل هذا؟**

عندما يتم تغيير قيمة محدد القائمة المنسدلة، يتم التعامل مع الحدث على الخادم باستخدام كائن خلفي JSF **WorksheetView** بواسطة الطريقة **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

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
