---
title: Редактор электронных таблиц  Работа с функциями
type: docs
weight: 60
url: /ru/java/spreadsheet-editor-working-with-functions/
---

**Содержание**

- [Панель формул](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Вставить функцию](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Панель формул**
Панель формул - это текстовое поле сверху области листа. Она отображает формулу текущей ячейки, а также позволяет пользователю ее редактировать.

**Как это работает?**

Когда ячейка выбрана, панель формул синхронизируется с ячейкой, и формула отображается. Пользователю разрешено вносить изменения. Когда пользователь отредактирует и нажмет клавишу Enter, выполняется функция на JavaScript **saveFormulaBarContents**.
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Вставить функцию**
Чтобы вставить функцию или формулу:

1. Нажмите на ячейку, чтобы выбрать ее.
1. Нажмите кнопку **Вставить функцию** вверху.
1. Следуйте инструкциям в диалоговом окне **Вставить функцию**.
