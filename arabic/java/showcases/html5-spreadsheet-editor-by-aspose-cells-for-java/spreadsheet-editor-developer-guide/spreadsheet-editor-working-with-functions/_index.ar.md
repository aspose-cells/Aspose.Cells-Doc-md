---
title: محرر الجداول  العمل مع الوظائف
type: docs
weight: 60
url: /ar/java/spreadsheet-editor-working-with-functions/
---

جدول المحتويات

- [شريط الصيغ](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [إدراج وظيفة](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **شريط الصيغ**
شريط الصيغ هو مربع نص أعلى من منطقة الورقة. يعرض الصيغة للخلية الحالية ويسمح للمستخدم بتحريرها أيضًا.

**كيف يعمل هذا؟**

عند تحديد خلية، يتم مزامنة شريط الصيغ مع الخلية ويتم عرض الصيغة. يُسمح للمستخدم بالتحرير. عند قيام المستخدم بالتحرير والضغط على مفتاح الإدخال، يتم تنفيذ دالة جافا سكريبت **saveFormulaBarContents**
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **إدراج وظيفة**
لإدراج وظيفة أو صيغة:

1. انقر فوق الخلية لتحديدها.
1. انقر على زر **إدراج وظيفة** في الأعلى.
1. اتبع التعليمات في حوار **إدراج وظيفة**.
{{< app/cells/assistant language="java" >}}
