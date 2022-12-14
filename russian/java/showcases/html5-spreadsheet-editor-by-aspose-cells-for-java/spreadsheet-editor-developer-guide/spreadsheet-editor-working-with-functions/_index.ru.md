---
title: Редактор электронных таблиц — работа с функциями
type: docs
weight: 60
url: /ru/java/spreadsheet-editor-working-with-functions/
---
**Оглавление**

- [Панель формул](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - сохранитьFormulaBarContents
- [Вставить функцию](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Панель формул**
Строка формул — это текстовое поле над областью листа. Он отображает формулу текущей ячейки, а также позволяет пользователю редактировать ее.

**Как это работает?**

 Когда ячейка выбрана, панель формул синхронизируется с ячейкой, и формула отображается. Пользователю разрешено редактировать. Когда пользователь редактирует и нажимает клавишу ввода, функция JavaScript**сохранитьFormulaBarContents** казнен
#### **сохранитьFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Вставить функцию**
Чтобы вставить функцию или формулу:

1. Щелкните ячейку, чтобы выбрать ее.
1.  Нажмите**Вставить функцию** кнопка сверху.
1.  Следуйте инструкциям на**Вставить функцию**диалог.
