---
title: Проблема с сводной таблицей
type: docs
weight: 50
url: /ru/net/pivot-table-issue/
---

## **Симптом**
"Я пытался открыть сгенерированный файл Excel с помощью кнопки "Открыть" в IE. Excel был создан с помощью чтения шаблона Excel. При нажатии кнопки Открыть он открывается, но в то же время появляется сообщение об ошибке "Не удается открыть исходный файл сводной таблицы.....".

Но когда я сохраняю сгенерированный файл Excel с помощью кнопки "Сохранить" и открываю его из файла по сохраненному пути, он открывается правильно, без ошибок."
### **Решение**
Aspose.Cells устанавливает формат данных сводной таблицы и заставляет MS Excel создавать отчет о сводной таблице и другие задачи расчета на основе источника данных при открытии книги в MS Excel. Поэтому следует использовать **SaveType.OpenInBrowser**, а не **SaveType.OpenInExcel**. Одна из многих причин заключается в том, что при использовании опции OpenInExcel при сохранении сгенерированного файла в MS Excel во время выполнения с помощью кнопки "Открыть" из окна загрузки, MS Excel не может проанализировать данные книги для создания отчета о сводной таблице. Это вызвано проблемой с именем файла, это происходит в IE, так как оно добавляет что-то вроде "[1]" для того, чтобы сделать его как "имяФайла" + "[1]" + ".xls" к исходному имени и, таким образом, это не имеет никакого отношения к Aspose.Cells. (т.е. всегда добавляет "[1]" для того, чтобы сделать "имяФайла" + "[1]" + ".xls" и не похоже на имяФайла.xls). Другими словами, если файл содержит сводную таблицу, его нельзя открыть, используя опцию SaveType OpenInExcel, и это будет применяться как для того, если вы создаете файл с нуля, так и для использования любого шаблонного файла для исходных данных для создания отчета о сводной таблице. Поэтому следует использовать опцию SaveType OpenInBrowser, если в файле есть данные сводной таблицы для создания отчета о сводной таблице.

Вам следует изменить свой код и обновить на SaveType.OpenInBrowser, если вы используете метод Workbook.Save()

Или отредактируйте свой код, чтобы использовать "inline", если вы используете опцию "attachment" в своем коде. Например.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
