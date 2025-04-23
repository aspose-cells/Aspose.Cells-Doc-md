---
title: Укажите, совместим ли сводная таблица с Excel2003 при обновлении сводной таблицы
type: docs
weight: 80
url: /ru/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ предоставляет свойство [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-), которое позволяет указать, совместима ли сводная таблица с Excel 2003 при обновлении. Если значение истинное, строка должна содержать не более 255 символов, иначе она будет усечена. Если **ложное**, ограничения по длине не применяются. Значение по умолчанию — **истина**.

{{% /alert %}}

## **Укажите, совместима ли сводная таблица с Excel2003 при обновлении сводной таблицы**

В следующем примере кода объясняется использование свойства [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-). Оригинальная строка имеет длину 383 символа. Но когда свойство [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) установлено **true** и обновляется сводная таблица, данные ячейки B5 сводной таблицы усекаются и становятся длиной 255 символов. Однако, когда свойство [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) установлено **false** и сводная таблица снова обновляется, данные ячейки B5 сводной таблицы не усекаются и остаются длиной 383 символа. Пожалуйста, прочтите комментарии внутри кода для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

