---
title: محرر جداول البيانات - العمل مع الوظائف
type: docs
weight: 60
url: /ar/java/spreadsheet-editor-working-with-functions/
---
**جدول المحتويات**

- [شريط الصيغة](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - saveFormulaBarContents
- [أدخل وظيفة](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **شريط الصيغة**
شريط الصيغة هو مربع نص أعلى منطقة الورقة. يعرض صيغة الخلية الحالية وكذلك يسمح للمستخدم بتحريرها.

**كيف تعمل؟**

 عند تحديد خلية ، تتم مزامنة شريط الصيغة مع الخلية ويتم عرض الصيغة. يسمح للمستخدم بالتحرير. عندما يقوم المستخدم بالتحرير والضغط على مفتاح الإدخال ، وظيفة JavaScript**saveFormulaBarContents** يتم تنفيذ
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **أدخل وظيفة**
لإدراج دالة أو صيغة:

1. انقر فوق خلية لتحديدها.
1.  انقر**أدخل الوظيفة** زر في الأعلى.
1.  اتبع التعليمات الموجودة على**أدخل الوظيفة**الحوار.
